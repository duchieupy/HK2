#cho mang chua cac quan bai
quanbaiHieu = ["J","A"]
quanbaiCau = ["J","K","2"]
tongdiemhieu = 0
tongdiemcau = 0

def tinhdiemquanbai(quanbai, soluongquanbai):
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
        case "10" | "J"| "Q"| "K":
            return 10
        case "A":
            if(soluongquanbai>3):
                return 1
            else:
                return 10

soluongquanbai = len(quanbaiHieu)
for bai in quanbaiHieu:
    diemcuatungquanbai = tinhdiemquanbai(bai, soluongquanbai)
    tongdiemhieu=tongdiemhieu+diemcuatungquanbai

print ( " tong diem quan bai cua hieu la" , tongdiemhieu)

soluongquanbaiCau = len(quanbaiCau)
for bai in quanbaiCau:
    diemcuatungquanbai = tinhdiemquanbai(bai, soluongquanbaiCau)
    tongdiemcau=tongdiemcau+diemcuatungquanbai

print ( " tong diem quan bai cua cau la" , tongdiemcau)

# Tim xem ai thang?
if tongdiemhieu == tongdiemcau or tongdiemhieu >= 22 and tongdiemcau >=22 :
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
  
