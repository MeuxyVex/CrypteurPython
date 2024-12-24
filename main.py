#!/usr/bin/python3
########################################################################################################
##########################################################################################################
#Verifcation de pip                                 
import subprocess
import sys
import importlib                                                                       
def verifierpip():
    try:
        import pip
    except ImportError:
        print("Pip n'est pas encore installer, \nLancement de l'installation...")
        try:
            subprocess.check_call([sys.executable, "-m", "ensurepip", "--upgrade"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
            print("Installer avec succès !")
            input("Appuyez sur Entrée pour continuer...")
            subprocess.Popen([sys.executable] + sys.argv)
            sys.exit()
        except subprocess.CalledProcessError:
            print("Echec de l'installation, nouvelle tentative...")
        import urllib.request
        import os
        url = "https://bootstrap.pypa.io/get-pip.py"
        get_pip = "get-pip.py"
        urllib.request.urlretrieve(url, get_pip)
        subprocess.check_call([sys.executable, get_pip])
        os.remove(get_pip)
        print("Installation réussi")
        input("Appuyez sur Entrée pour continuer...")
        subprocess.Popen([sys.executable] + sys.argv)
        sys.exit()
    else:
        print("PIP ✔️")
if __name__ == "__main__":
    verifierpip()

##########################################################################################################
##########################################################################################################
#Verification des packages 
def verifiepackage():
    installed = []
    packages = ["colorama", "pyfiglet", "pygame"]
    for package in packages:
        try:
            importlib.import_module(package)
            installed.append(package)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", package])
            print(package, "Installés avec succès")
            installed.append(package)
    if len(installed) == len(packages):
        print("Colorama✔️, pyfiglet✔️, pygame✔️ ")

if __name__ == "__main__":
    verifiepackage()

##########################################################################################################
##########################################################################################################
#Musique
from modules import play
play("modules/m1.wav")
##########################################################################################################
##########################################################################################################
#Main cryptage
import colorama
import pyfiglet
texte1 = pyfiglet.figlet_format("Crypteur magique")
print(colorama.Fore.MAGENTA + texte1 + colorama.Style.RESET_ALL)
while True:
    print(colorama.Fore.MAGENTA + "Choisisez votre méthode de cryptage")
    choix = input("╔(1) Code Cesar \n║\n╠═(2) RSA\n║\n╠═(3) **Pas disponible**\n║\n╚════> " + colorama.Style.RESET_ALL)
    if choix == "1":
        choix2 = input("Crypteur ou decrypteur > ").lower()
        if choix2 == "crypteur":
            from modules import cesar
            cesar()
        elif choix2 == "decrypteur":
            from modules import decryptagecesar
            decryptagecesar()
        else:
            print("Reverifiez votre entrée.")


    elif choix == "2":
        choix2 = input("Crypteur ou decrypteur > ").lower()
        if choix2 == "crypteur":
            chin = input("Generation de clées ? Y/N ").lower()
            if chin == "y":
                from modules import rsaeclé
                rsaeclé()
            elif chin == "n":
                from modules import rsacryptage
                rsacryptage()
        elif choix2 == "decrypteur":
            from modules import rsadecryptage
            rsadecryptage()
        else:
            print("Reverifiez votre entrée.")


    elif choix =="3": 
       print(colorama.Fore.WHITE + "**Méthode de cryptage en cours de devloppement**" + colorama.Style.RESET_ALL)  
       print( "Technique de cryptage dev =", colorama.Fore.GREEN + "1" + colorama.Style.RESET_ALL, "Technique de cryptage nondev = ", colorama.Fore.RED + "2"" et ""3" + colorama.Style.RESET_ALL)
    
    else:
        print("Revrifiez votre entrée")
##########################################################################################################
##########################################################################################################





        





    






