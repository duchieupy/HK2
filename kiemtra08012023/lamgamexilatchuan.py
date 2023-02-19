#cho mang chua cac quan bai
quanbaiHieu = ["8","9"]
quanbaiCau = ["3","K"]

#tinh diem tat ca quan bai cua nguoi choi tra ve diem
def tinhdiemtoanboquanbai(toanboquanbai):
    soluongquanbai = len(toanboquanbai)
    tongdiem=0
    match soluongquanbai:
        case 2:
            #xi vang
            if toanboquanbai == ["A","A"]:
                return 53
            #xi lat
            if (toanboquanbai == ["A","J"] ) or (toanboquanbai == ["A","K"] )or (toanboquanbai == ["A","Q"]) or (toanboquanbai == ["A","10"]):
                return 52
            #binh thuong
            else:
                for bai in toanboquanbai:
                    if bai == "2":
                        tongdiem=tongdiem+2
                    if bai == "3":
                        tongdiem=tongdiem+3
                    if bai == "4":
                        tongdiem=tongdiem+4
                    if bai == "5":
                        tongdiem=tongdiem+5
                    if bai == "6":
                        tongdiem=tongdiem+6
                    if bai == "7":
                        tongdiem=tongdiem+7
                    if bai == "8":
                        tongdiem=tongdiem+8
                    if bai == "9":
                        tongdiem=tongdiem+9
                    if bai == "10" or bai == "J" or bai == "Q" or bai == "K" or bai == "A":
                        tongdiem=tongdiem+10

                return tongdiem
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
