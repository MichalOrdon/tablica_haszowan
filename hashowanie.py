def wykonaj_hash(index, tablica_glowna, ilosc_kolizji=0):
    hashowanie = (index + ilosc_kolizji) % (len(tablica_glowna))
    if ilosc_kolizji == len(tablica_glowna):
        return None
    if tablica_glowna[hashowanie] is None:
        return hashowanie
    else:
        return wykonaj_hash(index, tablica_glowna, ilosc_kolizji + 1)


def na_ASCII(klucz_nazwisko):
    nazwisko_ASCII = klucz_nazwisko.encode()
    kodHash = sum(nazwisko_ASCII) * 100
    return kodHash


wejscie = open('nazwiska.txt', 'r')
dane_z_pliku = wejscie.read().splitlines()
wejscie.close()

tablica_glowna = [None for index in range(len(dane_z_pliku))]

for linijka in dane_z_pliku:
    hash = na_ASCII(linijka)
    print(hash)
    index_linii = wykonaj_hash(hash, tablica_glowna)
    if index_linii is not None:
        tablica_glowna[index_linii] = linijka
