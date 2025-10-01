import NormalMode


splash_text=""" _______                   __ __________                       
 ╲      ╲   ____ ___  ____╱  │╲______   ╲_____    ______ ______
 ╱   │   ╲_╱ __ ╲╲  ╲╱  ╱╲   __╲     ___╱╲__  ╲  ╱  ___╱╱  ___╱
╱    │    ╲  ___╱ >    <  │  │ │    │     ╱ __ ╲_╲___ ╲ ╲___ ╲ 
╲____│__  ╱╲___  >__╱╲_ ╲ │__│ │____│    (____  ╱____  >____  >
        ╲╱     ╲╱      ╲╱                     ╲╱     ╲╱     ╲╱ 
\t\t\t\tVersion: 1.0.0                                                           
                                                               """
                                                               
print(splash_text)

print("The Advance Password Dictionary Generator")
print("Created by: github.com/Blu-PY\n\n")

print("A tool used to produce a password list from the details of target.\n\n")


print("""Instructuctions:
      1. The user can choose 2 modes of generation of password dicitonary.
      2. Normal Mode will use the code only to generate the passwords.
      3. AI Assisted mode will generate the passwords with the help of code and available AI options.
      4. The user must have their own API Key to use AI assisted mode.
      5. The details of the target must be entered in the details.json file.
      6. DO NOT DELETE THE OUTPUT FOLDER.\n\n""")


choice_text="""\n---------------------------------------------------\nChoose your mode to start generating:
1. Normal (Default)
2. AI Assisted (API KEY NEEDED)
0. Quit\n---------------------------------------------------
Option: """



mode = None
quit = False

while not quit:
    mode_choice = int(input(choice_text))
    try:
        if mode_choice == 0:
            print("\nThank you for using the tool!\nExiting...")
            quit = True
        elif mode_choice == 1:
            print("Normal Mode Selected")
            pass_number = int(input("How many password would you like to generate?\n-> "))
            mode = NormalMode.NormalMode()
            mode.Generate(pass_number)
            choice = input("Want to generate more passwords? (y/n) ")
            if choice == "y":
                pass_number = int(input("How many password would you like to generate?\n-> "))
                mode.Append(pass_number)
            elif choice == "n":
                continue
        elif mode_choice == 2:
            print("AI assisted Mode Selected")

    except ValueError:
        print("Enter Valid Option!")
