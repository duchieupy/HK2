mangdiem = [1,2,1,2,3,8,9,7,8,10, 4]
#thay the cac diem thap(duoi 5) thanh diem 5
#mangten[1] = "tan"
for vitri, diem in enumerate(mangdiem):
    if diem<5 :
        print("in diem nho hon 5", mangdiem[vitri])
        mangdiem[vitri]= 5

print(mangdiem)
   
