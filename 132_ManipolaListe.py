studenti = ["Arianna","Bruno","Dario","Elena","Mario","Teresa"]

andrea = "Andrea"
gabriel = "Gabriel"
studenti.append(andrea)
studenti.append(gabriel)

studenti.insert(3, "Riccardo")

studenti.remove(studenti[1])

studenti.remove("Teresa")

for pos, nomi in enumerate(studenti):
    print("Studente", pos+1, ":", nomi)