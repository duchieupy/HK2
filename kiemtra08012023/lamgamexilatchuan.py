#cho mang chua cac quan bai
quanbaiHieu = ["A","A"]
quanbaiCau = ["A","A"]

#tinh diem tat ca quan bai cua nguoi choi tra ve diem
def tinhdiemtoanboquanbai(toanboquanbai):
    soluongquanbai = len(toanboquanbai)

    match soluongquanbai:
        case 2:
            #xi vang
            if toanboquanbai == ["A","A"]:
                return 9999
            #xi lat
            
            #binh thuong
                return "sap win"
        case 3:
            return 3
        case 4:
            return 4
        case 5:
            return 5

#ai cao diem hon thi in ra
diemcuaHieu = tinhdiemtoanboquanbai(quanbaiHieu)
diemcuacau = tinhdiemtoanboquanbai(quanbaiCau)
print("diem cua Hieu la", diemcuaHieu)
print("diem cua Cau la", diemcuacau)

if diemcuaHieu == diemcuacau:
    print("hoa")