mangdiemhocsinh = [1,3,6,10,9,8,4,5,7]

#tim so lon nhat trong mang

tongsophantu =0

#moi lan chay qua thi phantu cong them 1
for chay in mangdiemhocsinh :  
    tongsophantu=tongsophantu+1

solonnhat = mangdiemhocsinh[0]
vitrisolonnhat = 0

for vitri in range(tongsophantu):
    if solonnhat < mangdiemhocsinh[vitri]:
        solonnhat = mangdiemhocsinh[vitri]
        vitrisolonnhat = vitri
                                                                                
print("so lon nhat", solonnhat)
print("vi tri so lon nhat", vitrisolonnhat)
