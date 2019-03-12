answer = False
Tries = 3


while (answer  == False) & (Tries >  0) :
    aquestion = input("De quel groupe faisait parti Kurt Cobain?")
    if question == "Nirvana" :
        print("Bravo, c’est la bonne réponse")
        answer  = True
    else :
        print("Dommage, ce n’est pas la bonne réponse")
        Tries -= 1
        print("Il vous reste " + str(Tries) + " réponses")

answer  = False
while (answer  == False) & (Tries >  0) :
    question = input("A quel age est il mort?")
    if question == "27" :
        print("Bravo, c’est la bonne réponse")
        answer  = True
    else :
        print("Dommage, ce n’est pas la bonne réponse")
        Tries -= 1
        print("Il vous reste " + str(Tries) + " réponses")


answer  = False
while (answer  == False) & (Tries >  0) :
    question = input("De quel instrument jouait-il?")
    if question == "Guitare" :
        print("Bravo, c’est la bonne réponse, Vous avez répondu a toutes les questions! GG")
        answer  = True
    else :
        print("Dommage, ce n’est pas la bonne réponse")
        Tries -= 1
        print("Il vous reste " + str(Tries) + " réponses")

if answer == False :
    print("Dommage tu as perdu le jeu")	