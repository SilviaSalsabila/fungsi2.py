def luaspersegipanjang(panjang,lebar):
    return panjang*lebar

def kelilingpersegipanjang(panjang,lebar):
    return 2* (panjang+lebar)

panjang=int(input("masukan panjang lebar persegi: "))
lebar=int(input("masukan lebar persegi: "))

hasil_luas= luaspersegipanjang(panjang,lebar)
hasil_keliling=kelilingpersegipanjang(panjang,lebar)
print("hasil luas:",hasil_luas)
print("hasil keliling:",hasil_keliling)
