# Projet Questionnaire V2.1 avec utilisation de dictionnaires
def recuperer_questionnaire():
    with open("questionnaire.txt", "r") as file:
        lignes = file.readlines()

        for i in range(len(lignes)):
            question = {f"titre{i + 1}": "", f"choix{i + 1}": (), f"bonne_reponse{i + 1}": ""}
            ligne = lignes[i].split("/")
            question[f"titre{i + 1}"] = ligne[0]
            question[f"choix{i + 1}"] = ligne[1].split(" ")
            question[f"bonne_reponse{i + 1}"] = ligne[2].strip()
            questionnaire[f"question{i + 1}"] = question


def poser_question(titre, choix):

    print("QUESTION: ", titre)

    for i in range(len(choix)):
        print(f" {i+1}-", choix[i])


def demander_reponse(min, max):
    reponse_str = input(f"Entrez votre reponse (entre {min} et {max}) : ")

    try:
        reponse_int = int(reponse_str)

        if min<= reponse_int <= max:
            return reponse_int

        print(f"ERREUR : Veuillez entrer un chiffre entre {min} et {max}")
    except:
        print("ERREUR : Veuillez entrez un chiffre")


def lancer_questionnaire(questionnaire):

    score = 0

    for i in range(len(questionnaire)):

        question = questionnaire[f"question{i+1}"]
        titre = question[f"titre{i+1}"]
        choix = question[f"choix{i+1}"]
        bonne_reponse = question[f"bonne_reponse{i+1}"]

        poser_question(titre, choix)
        reponse = demander_reponse(1, len(choix))

        if choix[reponse-1] == bonne_reponse:
            score += 1
            print("Bonne reponse")
        else:
            print("Mauvaise reponse")

    print(f"Score finale: {score} / {len(questionnaire)}")

#--------------------QUESTIONNAIRE-----------------------
questionnaire = {}
recuperer_questionnaire()
lancer_questionnaire(questionnaire)
