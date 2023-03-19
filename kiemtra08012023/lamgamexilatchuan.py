#cho mang chua cac qua, "Q"n bai
quanbaiHieu = ["10","5" ,"6"]
quanbaiCau = ["10","2","3","A","A"]

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
                if bai == "10" or bai ==  "A" or bai ==  "J" or bai ==  "K" or bai ==  "Q" :
                    tongdiem=tongdiem+10
            return tongdiem
            
        case 4:
            for bai in toanboquanbai:
                if bai == "A":
                    tongdiem = tongdiem +1
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
                if bai == "10" or bai ==  "J" or bai ==  "K" or bai ==  "Q" : 
                    tongdiem=tongdiem+10

            return tongdiem
            
        case 5:
            for bai in toanboquanbai:
                if bai == "A":
                    tongdiem = tongdiem 
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
                if bai == "10" or bai ==  "J" or bai ==  "K" or bai ==  "Q" : 
                    tongdiem=tongdiem+10

            if(tongdiem < 22):
                return 51
            else:
                return 22 
            
#ai cao diem hon thi in ra
diemcuaHieu = tinhdiemtoanboquanbai(quanbaiHieu)
diemcuacau = tinhdiemtoanboquanbai(quanbaiCau)
print("diem cua Hieu la", diemcuaHieu)
print("diem cua Cau la", diemcuacau)



# neu cau woac
if (diemcuacau > 21 and diemcuacau < 50):
    if(diemcuaHieu >21 and diemcuaHieu < 50 ):
        print ( " hoa")
    else:
        print ( "con thang cau")
else:
    if (diemcuaHieu > 21 and diemcuaHieu < 50) :
        print( " cau thang con")
    else:
        if diemcuaHieu > diemcuacau :
            print ( "con thang cau")
        elif diemcuaHieu < diemcuacau :
            print (" con thua cau") 
        else:
            print ("hoa")
# hoa
# khi diem bang nhau, hoac 2 ong woac het
# if (diemcuaHieu == diemcuacau) or (diemcuacau >21 and diemcuaHieu >21 and diemcuacau < 50  and diemcuaHieu <50  ) :
    # print("hoa") 
# cau thang
# diemcau > diemhieu va cau khong woac
# else:
    # if (diemcuacau > diemcuaHieu) and (diemcuacau  < 22 or diemcuacau>50) or (diemcuacau < diemcuaHieu) and (diemcuaHieu  > 22 or diemcuaHieu<50) :
        # print("cau thang con and hieu thua")

# hieu thang
    # if (diemcuaHieu > diemcuacau) and (diemcuaHieu  < 22 or diemcuaHieu>50) or (diemcuaHieu < diemcuacau) and (diemcuacau > 22 or diemcuacau<50):
        # print("con thang cau va cau thua")



# quy dinh
# xi vang 53
# xi lat 52
# ngu linh 51
# woac thi lon hon 21 va nho hon 50
# woac thi la 22,23,24,....50 => ko woac=25
# 

# xet diem cua cau
# 1. neu cau woac:
    # xet diem cua con
    # neu con woac thi 2 ong hoa
    # con ko woac thi con thang

#. 2 cau ko woac
    # xet diem cua con
    # neu con woac => con thua
    # neu con ko woac => so diem => ai con hon thi nguoi do thang hoac hoa

