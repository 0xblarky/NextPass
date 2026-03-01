# import ColorPrint as cprint
from google import genai
from dotenv import load_dotenv
import os
import json
import ColorPrint as cprint
import random
import time

def GeneratePassword(isAppend:bool):
    #Initial Setup
    load_dotenv("./.env")
    Tjson = open("./config/AI.json")
    details:dict = json.load(Tjson)

    if len(details.keys()) < 3:
        cprint.LogError("Insufficient Details given. There should be more than or equal to 3 details. Reverting to the menu....")
        time.sleep(2)
        return

    if len(os.getenv("API_KEY")) == 0:
        cprint.LogError("No API KEY detected. Please add your API KEY in API_KEY field in a .env file")
        time.sleep(2)
        return
    
        

    #Setup gemini
    client = genai.Client(api_key=os.getenv("API_KEY"))

    num_passwords = input("How many passowrds would you like to generate? :- ")

    if int(num_passwords) <= 0:
        cprint.LogError("Invalid Input\nReturning to the menu...")
        return
        
        

    response = client.models.generate_content(
        model="gemini-2.5-flash",contents=f"""
    Act as an automated password format generator. I will provide a list of keys representing a target's details. Your job is to create short notations for these keys and then generate probable password formats using them.

    Input Keys:
    {', '.join(details.keys())}

    Global Modifiers to include in formats:
    [S] = Special Character (e.g., @, !, #) [Add any special character of your choice]
    [N] = Random Number (e.g., 1, 12, 123) [Add any number of your choice]

    Output Structure & Constraints (STRICT):
    You must output EXACTLY two lines of text. Do not include introductory text, explanations, markdown formatting, code blocks, or bullet points.

    Line 1 (The Mapping): Output your generated 2-3 letter uppercase bracketed notation and the original key, separated by a colon. Separate each pair with a comma and a space. (e.g., [FN]:first_name, [BY]:birth_year)

    Line 2 (The Formats): Output {num_passwords} logical password format combinations using the notations from Line 1 and the Global Modifiers. Separate each format with a comma and a space. (e.g., [FN][BY], [FN][S][N], [N][FN][BY][S]).

    Generate the output now.
        """
        

    )

    # file.write(response.text)
    # file.close()
    #take the result and format it(Add user details)




    #Split the lines and clean up the lists immediately
    sliced_response = response.text.strip().split("\n")

    #Use list comprehension to strip whitespace from every item
    notations = [n.strip() for n in sliced_response[0].split(",")]
    formats = [f.strip() for f in sliced_response[1].split(",")]

    #Convert notations into a clean dictionary for easy lookup
    #This turns "['[FN]:FirstName', '[SN]:Surname']" into {"[FN]": "FirstName", "[SN]": "Surname"}
    notation_dict = {}
    for n in notations:
        parts = n.split(":")
        if len(parts) == 2:
            notation_dict[parts[0].strip()] = parts[1].strip()

    final_results = []

    #Iterate through formats and apply all replacements to a temporary string
    for fmt in formats:
        current_format = fmt # Hold the current format (e.g., "[FN][DOB][S][N]")
        
        for not_key, not_val in notation_dict.items():
            if not_key in current_format:
                # Look up the actual value from your 'details' dictionary using 'not_val'
                #Todo: Check if the value is a list or a single value
                detail = details.get(not_val, "")
                actual_detail = ""
                if type(detail) == str or type(detail) == int:
                    actual_detail = actual_detail + str(detail)
                elif type(detail) == list:
                    i = random.randint(0,len(detail)-1)
                    actual_detail = actual_detail + detail[i]
                


                # Update the temporary string with the new detail
                current_format = current_format.replace(not_key, actual_detail)

                if '[S]' in current_format:
                    char = random.choice(['!', '@','#', '$' ,'%' ,'^' ,'&' ,'*'])
                    current_format = current_format.replace('[S]',char)
                elif '[N]' in current_format:
                    num = random.randint(0,1000)
                    current_format = current_format.replace('[N]',str(num))
                    
                    
                
        #After checking ALL notations, append the fully updated string
        final_results.append(current_format+'\n')
    cprint.LogSuccess("Passwords generated succesfully!")


    if isAppend == False:
        file = open("./Output/AIoutput.txt",'w')
        file.writelines(final_results)
    else:
        file = open("./Output/AIoutput.txt",'a')
        file.writelines(final_results)


    choice = input("Would you like to generate more passwords? (y/N) :- ")
    
    if choice.lower() == 'y':
        GeneratePassword(True)
    elif choice == '' or choice.lower() == 'n':
        cprint.LogSuccess("Returning to the menu....")
        return
    else:
        cprint.LogError("Invalid Input, Returning to the menu....")


