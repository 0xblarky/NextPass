from colorama import Fore, Style

next_banner = """ 
 _______                   __   
 \\      \\   ____ ___  ____/  |_ 
 /   |   \\_/ __ \\\\  \\/  /\\   __\\
/    |    \\  ___/ >    <  |  |  
\\____|__  /\\___  >__/\\_ \\ |__|  
        \\/     \\/      \\/       """


pass_banner = """
__________                       
\\______   \\_____    ______ ______
 |     ___/\\__  \\  /  ___//  ___/
 |    |     / __ \\_\\___ \\ \\___ \\ 
 |____|    (____  /____  >____  >
                \\/     \\/     \\/ """


def PrintBanner():
 
    next_lines = next_banner.splitlines()
    pass_lines = pass_banner.splitlines()
    max_len = max(len(next_lines), len(pass_lines))

    # pad shorter banner with empty lines
    next_lines += [""] * (max_len - len(next_lines))
    pass_lines += [""] * (max_len - len(pass_lines))

    for left, right in zip(next_lines, pass_lines):
        print(Fore.CYAN + left.ljust(1) + Style.RESET_ALL + right)
        
        
def LogError(msg):
    print(Fore.RED + "\n[ERROR] " + '\n' + msg + Style.RESET_ALL)

def LogSuccess(msg):
    print(Fore.GREEN + "\n[SUCCESS] " + '\n'+ msg + Style.RESET_ALL)
    
    
def LogWarning(msg):
    print(Fore.YELLOW + "\n[WARNING] " + '\n'+ msg + Style.RESET_ALL)