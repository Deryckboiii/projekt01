#harmadik alkalom

def szam_bekeres(legnagyobb_szam):
    szam = input("Kérek egy számot:")
    if szam.isdigit():
        szam = int(szam)
        if szam == 0:
            print("Nem ismerem a nullát")
        elif szam > legnagyobb_szam:
            print("Túl nagy számot adtál meg")
        else:
            print("Most már tudok számmal dolgozni")
    else:
        print("Nem számot adtál meg!")
    return szam

def szamologep():
    muvelet = input("MIlyen műveletet akar végrehajtani? (+,-,*,/):")
    egyik_szam = szam_bekeres(10)
    masik_szam = szam_bekeres(100)
    if muvelet == "+":
        eredmeny = egyik_szam + masik_szam
    elif muvelet == "-":
        eredmeny = egyik_szam - masik_szam
    elif muvelet == "*":
        eredmeny = egyik_szam * masik_szam
    else:
        eredmeny = egyik_szam / masik_szam

    print(f"eredmeny: {egyik_szam} {muvelet} {masik_szam} = {eredmeny}")

def veletlenszeru():
    import random
    szam = random.randint(0, max)
    return szam

#program indítása
if __name__ == "__main__":
    szamologep()
