import math

def l_persegi(sisi):
    luas = sisi*sisi
    keliling = sisi*sisi*sisi*sisi
    print(f"Luas Persegi {sisi} * {sisi} = {luas}")
    print(f"keliling persegi adalah {keliling}")

def persegi_panjang (panjang, lebar):
        luas = panjang * lebar
        print("hasil luas persegi panjang dari", panjang, "x", lebar, "=", luas)

def l_segitiga(alas , tinggi):
    luas = 1/2 * alas * tinggi
    print(f"Luas segitiga adalah 1/2 * 1{alas} * {tinggi} = {luas}")

def belahketupat(d1,d2):
     luasBelah = 1/2 * d1 * d2
     print(f"Luas belah ketupat {1/2} * {d1} * {d2} = {luasBelah}")

def layanglayang(d1, d2):
     luaslayang = 1/2 * d1 * d2
     print(f"Luas layang layang {1/2} * {d1} * {d2} = {luaslayang}")

def balok(panjang, lebar, tinggi):
     luasbalok =  2 * (panjang*lebar) + (panjang*tinggi) + (lebar*tinggi)
     print(f"Luas balok adalah {luasbalok}")

def l_kubus(sisi):
     luaskubus = 6 * (sisi*sisi)
     print(f"luas kubus adalah {luaskubus}")

def luastabung(jari2, tinggi):
     luastabung = 2 * 22/7 * (jari2 + tinggi)
     print(f"Luas tabung adalah {luastabung}")

def prismasegitiga(alas, keliling, tinggi):
     luasprisma = (2 * alas) + (keliling * tinggi)
     print(f"Luas prisma segitiga adalah {luasprisma}")

def limassegiempat(sisi, limassegitigak):
     luaslimas = (sisi*sisi) + (4*limassegitigak)
     print(f"Luas limas segi empat adalah {luaslimas}")
     