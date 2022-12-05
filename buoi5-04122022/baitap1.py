#cho mang ten
mangten = ["toan", "thanh", "quy", "tam", "chi", "linh", "thanh"]
sotenthanh=0
#tim xem trong lop co may ban ten thanh ?
for ten in (mangten): 
    if ten == "thanh": 
        sotenthanh = sotenthanh + 1
print("so ban ten thanh la", sotenthanh)        
