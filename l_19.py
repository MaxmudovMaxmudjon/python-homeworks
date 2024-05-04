def eng_katta(son1,son2,son3):
    return max(son1,son2,son3)
print(eng_katta(10,-5,7))


def katta_harf(matnlar):
    yangi_matnlar = []
    for matn in matnlar:
        yangi_matnlar.append(matn[0].upper()+matn[1:])
    return yangi_matnlar
royxat = ["salom","Maxmudjon","nima gap","bugun"]
print(katta_harf(royxat))


def juft_sonlar(sonlar):
    juft_s = []
    for son in sonlar:
        if son % 2 == 0:
            juft_s.append(son)
    return juft_s
royxat = [1,2,3,4,5,6,7,8,9,10]
print(juft_sonlar(royxat))
