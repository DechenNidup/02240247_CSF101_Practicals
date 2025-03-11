my_friend_array=["Dog", 2, 2.1, True, None]
myfirstarraylength= len(my_friend_array)
my_friend_array.append("cute")
mysecondarraylength=len(my_friend_array)
print(myfirstarraylength-mysecondarraylength)


family=["Dad", "Mom","Sis", "Bro"]
arraylength=len(family)
family.append("Me") 

family=["Dad", "Mom","Sis", "Bro"]
family.append("Me") 
print(family)
arraylength=len(family)
for index in range(arraylength):
    print(family[index])
    
index=0
while index<arraylength:
    print(family[index])
    index=index + 1
