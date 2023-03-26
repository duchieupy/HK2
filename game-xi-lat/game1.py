import random

#cho mang chua cac qua, "Q"n bai
quanbaiHieu = []
quanbaiCau = []

# chay ham ngau nhien => lay duoc so ngau nhien
soluongquanbairandomHieu = random.randint(2, 5)
soluongquanbairandomCau = random.randint(2, 5)


for i in range(soluongquanbairandomHieu):
    conbaiRandom = str(random.randint (2,10))
    quanbaiHieu.append(conbaiRandom) 


print("quan bai của hieu", quanbaiHieu)
for i in range(soluongquanbairandomCau):
    conbaiRandom = str(random.randint(2,10))
    quanbaiCau.append(conbaiRandom)

print(" quan bai cua cau", quanbaiCau)

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



























