mangten = ["toan", "an", "quy", "tam", "an", "linh", "an"]
#thay ten an bang ten chien
for vitri, ten in enumerate(mangten):
    if ten == "an":
        mangten[vitri]= "chien"
        

print(mangten)

