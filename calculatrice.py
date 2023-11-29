def calculatrice():
    historique = []

    while True:
        try:
            nombre1 = float(input("Entrez le premier nombre : "))
            operation = input("Entrez l'opération (+, -, *, /) : ")
            nombre2 = float(input("Entrez le deuxième nombre : "))

            if operation == '+':
                resultat = nombre1 + nombre2
            elif operation == '-':
                resultat = nombre1 - nombre2
            elif operation == '*':
                resultat = nombre1 * nombre2
            elif operation == '/':
                if nombre2 == 0:
                    print("Erreur : Division par zéro impossible")
                    continue
                resultat = nombre1 / nombre2
            else:
                print("Opération non valide")
                continue

            print(f"Résultat : {resultat}")
            historique.append((nombre1, operation, nombre2, resultat))

            print("\nHistorique des opérations :")
            for i, operation in enumerate(historique, 1):
                print(f"{i}. {operation[0]} {operation[1]} {operation[2]} = {operation[3]}")

            effacer = input("Voulez-vous effacer l'historique ? (Oui/Non) : ")
            if effacer.lower() == 'oui':
                historique = []       

            continuer = input("Voulez-vous effectuer un autre calcule ? (Oui/Non) : ")
            if continuer.lower() != 'oui':
                break

        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    calculatrice()
