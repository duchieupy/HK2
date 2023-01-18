#cho mang chua cac quan bai
quanbai = ["2","10","A"]
tongdiem = 0

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


for bai in quanbai: 
    diemcuatungquanbai = tinhdiemquanbai(bai)
    print("diem cua tung quan bai", diemcuatungquanbai)
    tongdiem=tongdiem+diemcuatungquanbai

print ( " tong diem quan bai cua hieu la" , tongdiem)