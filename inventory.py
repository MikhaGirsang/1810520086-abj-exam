file = open("db-inventory.txt", "a")
while True :
    inputConfirm = input("Input data inventory baru (ya/tidak)?")
    print('*'*30)
    if inputConfirm == "ya":
        devices = input("Nama Perangkat : ")
        location = input("Lokasi : ")
        file.write("Nama Perangkat : " + devices + ", Lokasi : " 
        + location + "\n")
        print('-'*30)
    elif inputConfirm == "tidak":
        break
    else:
        print("Masukan \"ya\" atau \"tidak\" \n")
file.close()

file = open("db-inventory.txt", "r")
isifile = []
for item in file:
    item = item.strip()
    isifile.append(item)
file.close()

for item in isifile:
    print(item)