import pathlib, os, time
from mods.colors import SourceColorList

colors = SourceColorList()
cwd = os.getcwd().replace("\\", "/")
installersdir = cwd+"/res/installers/"

#####################################################
# NPCAP                                             #
#####################################################

def checkpcap():
    if not pathlib.Path("C:/Program Files/Npcap/NPFInstall.exe").exists():

        print(f"{colors.RED}[!] No npcap Installation Found.{colors.RESET}")
        time.sleep(1.5)
        print(f"{colors.GREEN}[+] Installing from embedded installer...{colors.RESET}")
        time.sleep(1.5)
        
        os.system(installersdir+"npcap.exe")

    else: 
        print(f"{colors.GREEN}[*] Found valid installation of npcap.{colors.RESET}")