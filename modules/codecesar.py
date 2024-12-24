
def cesar():
    phrase = input("Entrez votre phrase à crypter > ")
    numero = int(input("Entrer un numero qui sera votre clé de cryptage > "))

    if numero % 26 == 0:
        numb = numero + 1

    else:
        numb = numero

    phraseunicode = []

    for char in phrase:
        nouveau_char = chr(ord(char) + numb % 26)
        phraseunicode.append(nouveau_char)

    phrase_final = "".join(phraseunicode)

    print (phrase_final)
    print ("Clé de décryptage = ", numb % 26)

def decryptagecesar():
    Entree = input("Texte à decrypter > ")
    entreecode = int(input("Clé de cryptage "))

    phraseunicode = []

    for char in Entree:
        nouveau_char = chr(ord(char) - entreecode)
        phraseunicode.append(nouveau_char)

    phrase_final = "".join(phraseunicode)
    print(phrase_final)






