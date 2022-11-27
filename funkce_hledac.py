import  random

def inicializace_mapy(sirka):
    """
    Vykresluje mapu s pozicema hráče a pokladu

    """
    moje_mapa = []
    # načtení listu do čtverce
    for i in range(0,sirka):
        moje_mapa.append(list('■' * int(sirka)))

    return  moje_mapa

def  zaneseni_objektu(mapa,souradnice_hrace, souradnice_pokladu):
    """
    zakreslí do mapy souřadnice hráče a pokladu
    """
    moje_mapa = mapa.copy()
    moje_mapa[souradnice_hrace[0]][souradnice_hrace[1]] = '○'
    moje_mapa[souradnice_pokladu[0]][souradnice_pokladu[1]] = "x"
    for radek in moje_mapa:
        print(' '.join(radek))
    print('-----')


#     funkce pohyb do 4 smeru na zaklade nah cisla


def souradnice_pokladu(velikost):
    """
    vrátí náhodné souřadnice x,y ve čverci o zadané velikosti
    """
    x = 0
    y = 0
    while x + y == 0:
        x = random.randint(0, velikost -1)
        y = random.randint(0, velikost - 1)
    return (x,y)



def udelej_krok(velikost, souradnice_hrace):
    """
    Na základě náhodného čísla udělá náhodný pohyb o 1 krok pokud je to mžné a vrátí souřadnice
    """
    nahodny_smer = random.randint(1,4)
    # funkce kde se upravují pozice pokud je upravená pozice v rangi
    def krok_nahoru():
        if souradnice_hrace[0] - 1 >= 0:
            souradnice_hrace[0] -= 1
        return [souradnice_hrace[0],souradnice_hrace[1]]

    def krok_vpravo():
        if souradnice_hrace[1] + 1 < velikost:
            souradnice_hrace[1] += 1
        return [souradnice_hrace[0],souradnice_hrace[1]]

    def krok_dolu():
        if souradnice_hrace[0] + 1 < velikost:
            souradnice_hrace[0] += 1
        return [souradnice_hrace[0],souradnice_hrace[1]]

    def krok_vlevo():
        if souradnice_hrace[1] - 1 >= 0:
            souradnice_hrace[1] -= 1
        return [souradnice_hrace[0],souradnice_hrace[1]]

    # podmínky náh čísla a vracení funkce
    if nahodny_smer == 1:
        return krok_nahoru()
    elif nahodny_smer ==2:
        return  krok_vpravo()
    elif nahodny_smer == 3:
        return krok_dolu()
    elif nahodny_smer == 4:
        return  krok_vlevo()

def najde_poklad(velikost, limit_kroku, kreslit = False):
    """
    Při zadané velikosti mapy a limitu kroků vrátí da li se našel poklad
    """
    kroky = 0
    trefa = False
    pozice_hrace = [0,0]
    pozice_pokladu = souradnice_pokladu(velikost)
    # dokud si nevyčerpla kroky nebo nenašel poklad tak dělej
    while limit_kroku != kroky and trefa == False:
        kroky += 1
        pozice_hrace = udelej_krok(velikost,pozice_hrace)
        trefa = pozice_pokladu == tuple(pozice_hrace)
        if kreslit:
            zaneseni_objektu(inicializace_mapy(velikost),pozice_hrace,pozice_pokladu)

    return trefa


