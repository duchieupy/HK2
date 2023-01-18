#cho mang chua cac quan bai
quanbaiHieu = ["J","10","A"]
quanbaiCau = ["J","4","2"]
tongdiemhieu = 0
tongdiemcau = 0
tongquanbaihieu = 0
tongquanbaicau = 0
def tinhdiemquanbai(quanbai):
    match quanbai:
        case "2":
            return 2
        case "3":
            return 3
        case "4":
            return 4
        case "5":
            return 5
        case "6":
            return 6
        case "7":
            return 7
        case "8":
            return 8
        case "9":
            return 9
        case "10" | "J"| "Q"| "K"| "A":
            return 10


for bai in quanbaiHieu:
    tongquanbaihieu = tongquanbaihieu + 1
    if  tongquanbaihieu > 3 :
        bai == "A"
        tongdiemhieu = tongdiemhieu + 1
        diemcuatungquanbai = tinhdiemquanbai(bai)
        tongdiemhieu=tongdiemhieu+diemcuatungquanbai

print ( " tong diem quan bai cua hieu la" , tongdiemhieu)

for bai in quanbaiCau:
    tongquanbaicau = tongquanbaicau + 1
    if tongquanbaicau > 3  and bai == "A":
        tongdiemcau = tongdiemcau + 1
    diemcuatungquanbai = tinhdiemquanbai(bai)
    tongdiemcau=tongdiemcau+diemcuatungquanbai

print ( " tong diem quan bai cua cau la" , tongdiemcau)

# Tim xem ai thang?
if tongdiemhieu == tongdiemcau and tongdiemhieu >= 22 or tongdiemcau >=22 :
    print(" hoa ")
else:
    if tongdiemhieu > tongdiemcau and tongdiemhieu <= 22 :
        print ("hieu thang cau ")
    elif tongdiemhieu > tongdiemcau and tongdiemhieu >= 22:
        print("cau thang hieu")
    elif tongdiemcau > tongdiemhieu and tongdiemcau <= 22 :
        print ("cau thang hieu ")
    elif tongdiemcau > tongdiemhieu and tongdiemcau >= 22:
        print("hieu thang cau")
  
