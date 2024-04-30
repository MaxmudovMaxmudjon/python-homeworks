with open('pi.txt') as file:
    malumot = file.read()
    print(malumot)


with open('pi.txt') as file:
    pi = file.read()
bdate = '55724825'
if bdate in pi:
    print(f"{bdate} shu son bor")
else:
    print("uchramaydi")

text = '3.14159'
number = float(text)
with open('pi.pickle','wb') as file:
    pickle.dump(number,file)



