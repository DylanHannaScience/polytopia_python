def vegallapot(n):
    """
    Ellenőrzi, hogy a játék végállapot-e.
    Ha valamelyik játékos összes városát és egységét elvesztette, akkor vége a játéknak.
    """
    return n["player1_cities"] == 0 or n["player2_cities"] == 0


def hasznossag(n):
    """
    Hasznossági függvény: értékeli az állapotot.
    - Pozitív érték: előnyben van az első játékos.
    - Negatív érték: előnyben van a második játékos.
    """
    return (n["player1_cities"] * 10 + n["player1_units"] * 2) - (n["player2_cities"] * 10 + n["player2_units"] * 2)


def neighbors_of_n(n):
    """
    Generálja az összes lehetséges következő állapotot az aktuális játékos számára.
    - Egy játékos mozgathatja az egységeit, támadhat, vagy új egységeket képezhet.
    - Itt egyszerűsített lépéseket modellezünk.
    """
    allapotok = []

    # Pl. az első játékos új egységeket képezhet vagy mozgathat
    if n["current_player"] == 1:
        if n["player1_cities"] > 0:  # Ha van városa, képezhet egységet
            uj_allapot = n.copy()
            uj_allapot["player1_units"] += 1
            uj_allapot["current_player"] = 2
            allapotok.append(uj_allapot)

        if n["player2_units"] > 0:  # Ha van ellenséges egység, támadhat
            uj_allapot = n.copy()
            uj_allapot["player2_units"] -= 1
            uj_allapot["current_player"] = 2
            allapotok.append(uj_allapot)

    # Második játékos hasonló akciókat végezhet
    else:
        if n["player2_cities"] > 0:
            uj_allapot = n.copy()
            uj_allapot["player2_units"] += 1
            uj_allapot["current_player"] = 1
            allapotok.append(uj_allapot)

        if n["player1_units"] > 0:
            uj_allapot = n.copy()
            uj_allapot["player1_units"] -= 1
            uj_allapot["current_player"] = 1
            allapotok.append(uj_allapot)

    return allapotok

INF = float('inf')

def minmax(n):
    def max_value(n):
        if vegallapot(n):
            return hasznossag(n)

        max = -INF
        for a in neighbors_of_n:
            max = max(max, min_value(a))
        return max

    def min_value(n):
        if vegallapot(n):
            return hasznossag(n)

        min = +INF
        for a in neighbors_of_n:
            min = min(min, max_value(a))

        return min

    return min_value(n), max_value(n)
