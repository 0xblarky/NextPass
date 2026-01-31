import NormalMode
import ColorPrint



ColorPrint.PrintBanner()

print("The Advance Password Dictionary Generator")
print("Created by: github.com/Blu-PY\n\n")

print("A tool used to produce a password list from the details of target.\n\n")


print("""Instructuctions:
      1. The user can choose 2 modes of generation of password dicitonary.
      2. Normal Mode will use the code only to generate the passwords.
      3. AI Assisted mode will generate the passwords with the help of code and available AI options.
      4. The user must have their own API Key to use AI assisted mode.
      5. The details of the target must be entered in the TargetDetails.json file.
      6. DO NOT DELETE THE OUTPUT FOLDER.\n\n""")





choice_text="""\n---------------------------------------------------\nChoose your mode to start generating:
1. Normal (Default)
2. AI Assisted (API KEY NEEDED)
0. Quit\n---------------------------------------------------
Option: """



mode = None
quit = False

while not quit:
    mode_choice = input(choice_text)
    try:
        if mode_choice not in ['0','1','2']:
            raise ValueError
        if mode_choice == '0':
            print("\nThank you for using the tool!\nExiting...")
            quit = True
        elif mode_choice == '1':
            ColorPrint.LogSuccess("Normal Mode Selected")
            pass_number = int(input("How many password would you like to generate? (Limit:- if less than 4, Defaults to 4)\n-> "))
            NormalMode.Generate(int(pass_number))
            choice = input("Want to generate more passwords? (y/n) ")
            if choice == "y":
                pass_number = int(input("How many password would you like to generate?\n-> "))
                NormalMode.Append(int(pass_number))
            elif choice == "n":
                continue
        elif mode_choice == '2':
            ColorPrint.LogSuccess("AI assisted Mode Selected")
    except ValueError:
        ColorPrint.LogWarning("Enter Valid Option!")
