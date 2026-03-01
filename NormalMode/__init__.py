import json
import ColorPrint
import random

def GenerateRandomPass(generatedPasswords:list,details:dict):
# Setup data
    fn = details["FirstName"]
    sn = details["Surname"]
    dob = details["DateOfBirth"].split("/") # [DD, MM, YYYY]
    
    # Handle lists by picking one random element
    alias = random.choice(details["Online Aliases"]) if details["Online Aliases"] else fn
    pet = random.choice(details["Pet Names"]) if details["Pet Names"] else "Pet"

    dice = random.randint(2, 6) # Starting from 3 since 1-2 are covered by defaults

    if dice == 2:
        f_name = details["FirtName"]
        s_name = details["Surname"]
        schar = random.choice(["!", "@", "#", "$", "_",""," "])
        generatedPasswords.append(f"{f_name}{schar}{s_name}\n")
    elif dice == 3:
        # Pattern: Online Alias + Birth Year (e.g., WXYZ2008)
        generatedPasswords.append(f"{alias}{dob[2]}\n")

    elif dice == 4:
        # Pattern: Pet Name + Special Character + Day (e.g., XYZ@08)
        char = random.choice(["!", "@", "#", "$", "_",""," "])
        generatedPasswords.append(f"{pet}{char}{dob[0]}\n")

    elif dice == 5:
        # Pattern: Family Combo (e.g., IJKL_MNOP)
        f_name = details["Father's Name"]
        m_name = details["Mother's Name"]
        schar = random.choice(["!", "@", "#", "$", "_",""," "])
        generatedPasswords.append(f"{f_name}{schar}{m_name}\n")

    elif dice == 6:
        # Pattern: Address snippet + Year
        # Takes 'Street' from '123, Street, City'
        addr = details["Address"].split(",")
        street = addr[1].strip() if len(addr) > 1 else "Home"
        generatedPasswords.append(f"{street}{dob[2]}\n")


def PasswordGen(IsAppend,num_password):
    f_detail = open("config/Normal.json",'r')


    if IsAppend:
        f_pass = open("output/output.txt",'a')
    else:
        f_pass = open("output/output.txt",'w')

    details = json.load(f_detail)
    split_DOB = details["DateOfBirth"].split("/")

            
    # Default Passowrd combinations
    if not IsAppend:
        generatedPasswords = [(details["FirstName"].capitalize() + details["Surname"].capitalize() + '\n'),
                            (details["FirstName"].lower() + details["Surname"].lower() + '\n'),
                            (details["FirstName"].capitalize() + details["Surname"].capitalize() + split_DOB[0] +'\n'),
                            (details["FirstName"].lower() + details["Surname"].lower()+split_DOB[0] + '\n')]
    else:
        generatedPasswords = []
    
    if num_password <= 3:
        ColorPrint.LogWarning("Number of passwords requested is less than or equal to default combinations. Generating default combinations only.")
        f_pass.writelines(generatedPasswords)
        ColorPrint.LogSuccess("Password generation complete")
        f_pass.close()
        f_detail.close()
        return

    
    #More combination of passwords
    GenerateRandomPass(generatedPasswords,details)
    unique_set = set(generatedPasswords)

    # Keep generating until we hit the target number
    while len(unique_set) < num_password:
        temp_list = []
        GenerateRandomPass(temp_list, details)
        # .update adds the new password only if it's not already there
        unique_set.update(temp_list)

    # Convert back to a list to write to the file
    final_passwords = list(unique_set)
    f_pass.writelines(final_passwords)

    f_pass.writelines(generatedPasswords)
    generatedPasswords.clear()
    ColorPrint.LogSuccess("Passwords Generation complete")
    f_pass.close()
    f_detail.close()


def Generate(num_password):
    PasswordGen(False,num_password)
    
def Append(num_password):
    PasswordGen(True,num_password)






