mangdiemhocsinhlop7a2 = [1,2,3,8,9,7,8,10]

songuoikhongduochsgioi = 0
#kiem tra xem lop ngay co phai toan hoc sinh gioi hay khong?
#biet hoc sinh gioi la co diem lon hon hoac bang 8
for diem in mangdiemhocsinhlop7a2:
    if diem <8 :
        songuoikhongduochsgioi= songuoikhongduochsgioi + 1
    
if songuoikhongduochsgioi > 1 :
    print(" lop do khong duoc hs gioi")
    