#cho mang chua cac quan bai
quanbaiHieu = ["A","Q"]
quanbaiCau = ["A","K"]

#tinh diem tat ca quan bai cua nguoi choi tra ve diem
def tinhdiemtoanboquanbai(toanboquanbai):
    soluongquanbai = len(toanboquanbai)

    match soluongquanbai:
        case 2:
            #xi vang
            if toanboquanbai == ["A","A"]:
                return 53
            #xi lat
            if (toanboquanbai == ["A","J"] ) or (toanboquanbai == ["A","K"] )or (toanboquanbai == ["A","Q"]) or (toanboquanbai == ["A","10"]):
                return 52
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


# hoa
# khi diem bang nhau, hoac 2 ong woac het
if (diemcuaHieu == diemcuacau) or (diemcuacau  and diemcuaHieu >21 and diemcuacau  and diemcuaHieu <50  ) :
    print("hoa") 
# cau thang
# diemcau > diemhieu va cau khong woac
else:
    if (diemcuacau > diemcuaHieu) and (diemcuacau  < 22 or diemcuacau>50):
        print("cau thang con")

# hieu thang
    if (diemcuaHieu > diemcuacau) and (diemcuaHieu  < 22 or diemcuaHieu>50):
        print("con thang cau")



# quy dinh
# xi vang 53
# xi lat 52
# ngu linh 51
# woac thi lon hon 21 va nho hon 50
# woac thi la 22,23,24,....50 => ko woac=25
# 
