tenhocsinh = ["hieu", "bao", "duy"]
#chay khong can biet vi tri
for ten in tenhocsinh:
  print(ten)

#chay voi vi tri
for i in range(len(tenhocsinh)):
    print(tenhocsinh[i])
    print("vi tri", i)
    
    
#ham khong nhan khong tra
def inten():
    print("ten toi la Hieu")
    
#ham nhan khong tra
def inten(ten):
    print("ten toi la", ten)

#ham tra
def tratuoi():
    return 20

#ham nhan va tra
def tinhtong(a, b):
    return a+b

#lay gia tri tra ve tu ham
tong = tinhtong(2,5)
print("tong la ", tong)