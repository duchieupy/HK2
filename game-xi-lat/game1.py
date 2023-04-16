import random

#cho mang chua cac qua, "Q"n bai
quanbaiHieu = []
quanbaiCau  = []

tiencau=100
tienHieu=100
datcoc=20

# yeu cau
# ai thang thi cong len 20
# thua thi tru 20
# hoa thi ko ai bi tru tien va cong tien

# chay ham ngau nhien => lay duoc so ngau nhien
soluongquanbairandomHieu = random.randint(2, 5)
soluongquanbairandomCau  = random.randint(2, 5)

# tao ramdom quan bai cua Hieu
# random.randint (2,10) ranndom 1 so tu 2 toi 10
for i in range(soluongquanbairandomHieu):
    conbaiso = random.randint(1,13)
    if(conbaiso==1):
        conbaiRandom = 'A'
    elif(conbaiso== 11):
        conbaiRandom = 'J'
    elif (conbaiso == 12):
        conbaiRandom = 'Q'
    elif (conbaiso == 13):
        conbaiRandom = 'K'
    else:
        conbaiRandom = str(conbaiso)
    
    quanbaiHieu.append(conbaiRandom) 

print("quan bai của hieu", quanbaiHieu)

# tao random quan bai cua Cau
for i in range(soluongquanbairandomCau):
    # random.randint(1,13)1=>A 2 3 4 5 6 7 8 9 10 11 => J 12=>Q 13=>K
    conbaiso = random.randint(1,13)

    if(conbaiso==1):
        conbaiRandom = 'A'
    elif(conbaiso== 11):
        conbaiRandom = 'J'
    elif (conbaiso == 12):
        conbaiRandom = 'Q'
    elif (conbaiso == 13):
        conbaiRandom = 'K'
    else:
        conbaiRandom = str(conbaiso)

    quanbaiCau.append(conbaiRandom)


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
            if (toanboquanbai == ["A","J"]) or (toanboquanbai == ["A","K"] )or (toanboquanbai == ["A","Q"]) or (toanboquanbai == ["A","10"]):
                return 52
            # if (toanboquanbai == ["J","A"]) or (toanboquanbai == ["K","A"] )or (toanboquanbai == ["Q","A"]) or (toanboquanbai == ["10","A"]):
                # return 52
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
                return 51 # NGU lINH
            else:
                return 22 # woac
            
#ai cao diem hon thi in ra
diemcuaHieu = tinhdiemtoanboquanbai(quanbaiHieu)
diemcuacau = tinhdiemtoanboquanbai(quanbaiCau)
print("diem cua Hieu la", diemcuaHieu)
print("diem cua Cau la", diemcuacau)


# neu cau woac
if (diemcuacau > 21 and diemcuacau < 50):
    if(diemcuaHieu >21 and diemcuaHieu < 50 ):
        print(" tiền cậu là ", tiencau)
        print("tiền hiếu là ", tienHieu)
        print ( "hoa")
    else:
        tiencau = tiencau - datcoc
        tienHieu= tienHieu + datcoc
        print(" tien cau la ",tiencau)
        print(" tien cua hieu là", tienHieu)
        print ( "con thang cau")

else:
    if (diemcuaHieu > 21 and diemcuaHieu < 50) :
        tiencau = tiencau + datcoc
        tienHieu = tienHieu - datcoc
        print("tien cau là",tiencau)
        print (" tiền hieu là",tienHieu)
        print( "cau thang con",)

    else:
        if diemcuaHieu > diemcuacau :
            tiencau = tiencau - datcoc
            tienHieu = tienHieu+ datcoc
            print("tien cau là",tiencau)
            print (" tiền hieu là",tienHieu)
            print ( "con thang cau")
        elif diemcuaHieu < diemcuacau :
            tiencau = tiencau + datcoc
            tienHieu = tienHieu -  datcoc
            print (" con thua cau") 

        else:
            print(" tiền cậu là ", tiencau)
            print("tiền hiếu là ", tienHieu)
            print ("hoa")



























