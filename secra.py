from style.banner import display_banner
from src.cpe_search import search_cpe
from src.cve_search import search_cve
from colorama import Style , Fore
from src.Scanner import scan_cpe
import sys

def display1_vulnrabilities(cpes=None) -> str:

    for idx, cpew in enumerate(cpes, start=1):
        print(f"{idx}.{cpew.cpeName}{Style.RESET_ALL}")

    try:
        print ("=" * 60)
        choice = int(input(f"{Fore.YELLOW}\nSelect Number To Scan (Or Select 0 to Exit): {Style.RESET_ALL}"))
        if choice == 0:
            return False , None
        if 1 <= choice <= len(cpes):
            selected_cpe =  cpes[choice - 1].cpeName
            print("=" * 60)
            print (f"{selected_cpe}")
            print("=" * 60)
    except (ValueError, IndexError):
        print(" Command Error !")
        return display1_vulnrabilities(cpes)

    cves = search_cve(selected_cpe)
    if not cves:
        print(f"{Fore.RED}[-] Not Found Vulnrability.{Style.RESET_ALL}")
        return

def cve_run(cpes):

    global selected_cpe
    for idx, cpew in enumerate(cpes, start=1):
        print(f"{idx}. {cpew} ")

    try:
        print ("=" * 60)
        choice = int(input("\nSelect Number To Scan (Or Select 0 to Exit): "))
        if choice == 0:
            return False , None
        if 1 <= choice <= len(cpes):
            selected_cpe =  cpes[choice - 1]
            print("=" * 60)
            print (f"{selected_cpe}")
            print("=" * 60)
    except (ValueError, IndexError):
        print(" Command Error !")
        return cve_run(cpes)

    cve = search_cve(selected_cpe)
    if cve:
       return

def main():
    

    while True:
        display_banner()
        print  (     f"\n{Fore.WHITE}{Style.DIM}"        "1. Search Vulnrabiltice " f"                 (example scan device if you enter os and version)")
        print (    f"{Fore.WHITE}{Style.DIM}"          "2. Search Vulnrabilitice For IP         " ,   "(example scan device if you enter IP)"   )
        choice = input("\nEnter your Choice: ").strip()

        if choice == "1":
            print("=" * 60)
            os_name = input("Enter name of the OS (example: Microsoft Windows, Linux): ").lower()
            version = input("Enter Version (example: 10 , 2.4.3): ").lower()
            
            while True:
                print("")
                print("=" * 60)
                print ("Searching CPEs... ")
                print ("=" * 60)
                cpes = search_cpe(os_name, version)
                    
                if not cpes:
                       print(f"{Fore.RED}Not Found CPEs:{Style.RESET_ALL}")
                       choice2 = input("Click 1 To Back and 2 to Exit: ").strip()
                       if choice2 == '1':
                          return main()
                       elif choice2 == '2':
                            print("Good Bye :)")
                            return None
                     
                continue_searching = display1_vulnrabilities(cpes)
                if not continue_searching:
                   break

            action = input(f"\n{Fore.WHITE}{Style.DIM} Enter 'back' to go back or exit to quite: ")
            if action == 'exit':
               print("Exiting the tool...")
               sys.exit(0)

            elif action != 'back':
               print(f"{Fore.WHITE}{Style.DIM}Invalid input, please enter 'back' or 'exit' to quit: ").strip().lower()
               continue
        
        elif choice == "2":
             ip = input("\nEnter IP: ").strip()
             print("=" * 60)
             print (f"[+] Scanning : {ip}")
             print("=" * 60)
             cpes = scan_cpe(ip)
             print("=" * 60)
             print (cpes)
             print("=" * 60)
             print("Please Wait...")
             if not cpes:
                 print(f"{Fore.RED}Sorry Not Found CPEs{Style.RESET_ALL}")
                 choice1 = input(f"{Fore.WHITE}{Style.DIM}type back and choose number one to check the service versions: " ).strip()
                 if choice1 == 'back':
                    return main()
                 else:
                     return None
             cve = search_cve(cpes)
             if not cve:
                print("[-] Not Found Vulnrability")
                return
             print("found cve")

if __name__ == "__main__":
    main()
