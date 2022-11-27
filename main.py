import funkce_hledac as hledac
"""
Máme hledače pokladů, který hledá právě jeden ukrytý poklad ve čtverci o hraně width polí. Hledač začíná na pozici [0,0]
(vlevo nahoře) a v každém kroku se pohne jedním ze 4 směrů se stejnou pravděpodobností.
Pokud by měl vyjít ze čtverce, zůstává stát (a jeho neúspěšný krok se započítá).

Napište funkci, která pro zadanou šířku width zjistí, zdali v steps krocích hledač najde poklad.

Následně napište funkci, která provede předchozí funkci pro zadaný parametr count krát a vypíše, jaká je pravděpodobnost nalezení pokladu.

Poklad na začátku umístěte na náhodnou pozici.
"""








print(hledac.najde_poklad(10,50,True))

