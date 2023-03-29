from installer import checkpcap, os, time
from pyfiglet import figlet_format
from mods.colors import SourceColorList
import requests, subprocess
from threading import Thread
import psutil

def check_process_running(process_name):
    """
    Check if any process is running with the given name.
    """
    for process in psutil.process_iter():
        try:
            if process.name().lower() == process_name.lower():
                process.kill()
                
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass



def startAD():
    subprocess.call([bindir + "AD.exe"])



colors = SourceColorList()
banner = figlet_format("SCAMSuite")
checked_internet = False
update_id = "AOMC-900323"
bindir = os.getcwd() + "/res/bin/"


def main():
    os.system("cls")
    print(f"{colors.MAGENTA}{banner}{colors.RESET}")
    
    time.sleep(1.5)
    print(f"{colors.YELLOW}[-] Checking for dependencies.{colors.RESET}")
    time.sleep(0.5)
    checkpcap()
    time.sleep(0.5)
    print(f"{colors.GREEN}[+] All the dependencies should be installed.{colors.RESET}")
    time.sleep(1.5)
    print(f"{colors.YELLOW}[-] Checking for main server response (For updates).")
    time.sleep(1.5)

    try:
        r = requests.get("https://raw.githubusercontent.com/yungestdev/ScamSuiteMeta/main/version.md")

        if r.status_code == 200:
            print(f"{colors.GREEN}[+] Server is up")
            checked_internet = True
        else:
            print(f"{colors.RED}[!] Server is up, but it replied with an error.{colors.RED}")
    except:
        print(f"{colors.RED}[!] Could not initialize web request, check for internet connection.{colors.RESET}")

    time.sleep(0.5)

    if checked_internet:
        print(f"{colors.YELLOW}[-] Getting last update ID...{colors.RESET}")
        time.sleep(1)

        if r.text.split()[0] != update_id:
            print(f"{colors.YELLOW}[^] There is an update available, consider updating please.{colors.RESET}")
        else: print(f"{colors.GREEN}[+] Everything is up to date, thank you for choosing SCAMSuite!{colors.RESET}")
    
    print(f"{colors.GREEN}[+] Ready to go, press Enter to start{colors.RESET}")
    input("")
    os.system("cls")
    print(f"{colors.MAGENTA}{banner}{colors.RESET}")
    
    while True:

        command = input("Enter command > ")

        if command == "help":

            print("""
help - Invokes the list of commands
wshark - Launches wireshark
adesk - Launches AnyDesk
    ONLY TO DO THE REVERSE CONNECTION - do NEVER USE THIS to make them connect

quit - Closes the program

""")

        elif command == "wshark":
            check_process_running("wireshark.exe")
            subprocess.call([bindir + "wshark/wireshark.exe"])

        elif command == "adesk":
            check_process_running("AD.exe")
            t1 = Thread(target=startAD, daemon=True)
            t1.start()



        elif command == "quit": 
            exit()

if __name__ == "__main__":
    try: 
        main()
    except KeyboardInterrupt:
        print("\nGoodBye")