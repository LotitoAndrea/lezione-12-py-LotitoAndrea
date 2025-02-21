studenti = []
studentiClasse = ["Andrea","Riccardo","Gabriel","Hostina","Scramuzza"]
for i in range(5):
    studente = input("Inserisci il nome dello studente: ")
    if studente in studentiClasse:
        if studente not in studenti:
            studenti.append(studente)
        else:
            print(studente, "è già stato inserito")
    else:
        print(studente, "non è uno studente di questa classe")
print(studenti)