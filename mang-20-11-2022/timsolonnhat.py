mangdiemhocsinh = [1,3,6,10, 9, 8, 4, 2, 7]

#tim so lon nhat trong mang

#y tuong
#chay qua no
#so sanh voi lai 1 so trung gian
#so trung gian
#cho thang dau tien la so lon nhat
#chay qua tung thang
#neu thang do lon hon thi gan cho so lon nhat la thang do
solonnhat = mangdiemhocsinh[0]
for chay in mangdiemhocsinh:
    if solonnhat < chay:
        solonnhat = chay
        
print("so lon nhat", solonnhat)
