filmovi = [{"Naziv" : "Film1", "PozKomentari" : 5, "NegKomentari" :6}, {"Naziv" : "Film2", "PozKomentari" : 2, "NegKomentari" :18}, {"Naziv" : "Film3", "PozKomentari" : 12, "NegKomentari" : 4}]
def film_najbolji(filmovi):
    najBr = 0
    najFilm = ""
    for film in filmovi:
        if film["PozKomentari"] > najBr:
            najBr = film["PozKomentari"]
            najFilm = film["Naziv"]
    print(f"Najbolji film je {najFilm} i njegov broj pozitivnih kometara je {najBr}")
    return

def PocinjeSa (filmovi,pocetak):
    for film in filmovi:
        if film["Naziv"].startswith(pocetak):
            print(film["Naziv"])
    return

pocetak = input("Unesite pocetak naziva koji zelite")

print(PocinjeSa(filmovi,pocetak))





