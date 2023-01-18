mangdiemhocsinh = [ 5,8,7,9,10,4,2,1,3,4,2,3,3,3,]
#dem xem mang nay co bao nhieu diem chan
sodiemchan = 0 
sodiemle = 0
for diem in mangdiemhocsinh :
    if diem % 2 == 0:     
        sodiemchan=sodiemchan + 1
    else:
        sodiemle = sodiemle + 1
print("so diem le",  sodiemle)        
print("so diem chan",sodiemchan)


    
        
        
       
       