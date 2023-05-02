# On insère notre alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWYYZABCDEFGHIJKLMNOPQRSTUVWYYZ"

# On invite l'utilisateur à saisir son message
message_a_crypter = input("Veuillez saisir votre message :")

# On transforme notre message en majuscules
message_a_crypter = message_a_crypter.upper()

# On demande à l'utilisateur de saisir une clé de chiffrement
cle_decalage = int(input("Veuillez saisir un nombre compris entre 1 et 25 en guise de clé :"))

# On crée une variable destinée à accueillir notre futur message cryptée
message_crypte = ""

# On veut récupérer chaque caractere du message à crypter
for caractere in message_a_crypter:
    num_position = alphabet.find(caractere)
    nouvelle_position = num_position + cle_decalage

    if caractere in alphabet:
        message_crypte = message_crypte + alphabet[nouvelle_position]
    else:
        message_crypte = message_crypte + caractere

print("Votre message",message_a_crypter,"a été crypté de la façon suivante : \n",message_crypte)

