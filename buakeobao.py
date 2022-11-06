from random import randint

print("chọn búa,kéo,bao:")

ngườichoi = input()
máy = randint(4,6)

if máy == 4:
    máy = "búa"
if máy == 5:
    máy = "kéo"
if máy == 6 :
    máy = "bao"

print("bạn chọn:" + ngườichoi)
print("máy chọn:" + máy)

if máy == ngườichoi:
    print("hòa")
else:
    if ngườichoi== "kéo":
        if máy == "búa":
            print("bạn đã thua")
        else:
            print("bạn đã thắng")

    elif ngườichoi == "búa":
        if máy ==  "kéo":
            print("bạn đã thua")
        else:
            print("bạn đã thắng")
    elif ngườichoi == "bao":
        if máy == "kéo":
            print("bạn đã thua")
        else:
            print("bạn đã thắng")
    else:
        print("nhập tào lao sai rồi")


