mangdiemhocsinh = [5,8,7,9,10, 1,3 ,4,2,1,7,4,5,8,10,7,8,6,4,2,9,4,7,10]

#kha la lon hoac bang 6 va duoi 8
#gioi la lọn hon hoạc bang 8
#tb la doui 6 tren 4
#yeu la duoi 4

#thay giao hieu tinh coi:
#co bao nhieu hoc sinh kha
#bao nhieu hoc sinh gioi
#bao nhieu hoc sinh TB
#bao nhieu hoc sinh yeu

sohsgioi=0
sohskha=0
sohstb=0
sohsyeu=0

for diem in mangdiemhocsinh :
    if diem >= 8 :
        sohsgioi = sohsgioi + 1
    if diem < 8 and diem >= 6 :
        sohskha = sohskha+ 1 
    if diem < 6 and diem > 4 :
        sohstb = sohstb+ 1 
    if diem <= 4  :
        sohsyeu = sohsyeu+ 1 
    
print(" so hoc sinh gioi", sohsgioi)
print(" so hoc sinh kha", sohskha)
print(" so hoc sinh tb ", sohstb)
print(" so hoc sinh yeu", sohsyeu)
  


    
        
        
       
       