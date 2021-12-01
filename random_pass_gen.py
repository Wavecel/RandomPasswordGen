import random as r
import array as A
MAX_len = 12
a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
b = ["A","B","C","D","E","F","G","H","I","J",'K',"L",'M',"N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
c=["%","@","!","$","*","#","+","-","|","^"]
d= ["1","2","3","4","5","6","7","8","9","0"]
allset= a+b+c+d
r_a = r.choice(a)
r_b = r.choice(b)
r_c = r.choice(c)
r_d = r.choice(d)

passw= r_a+r_b+r_c+r_d

for x in range(MAX_len-4):
    passw = passw + r.choice(allset)
    passw_l = A.array("u",passw)
    r.shuffle(passw_l)
f_pass=""

for x in passw_l:
    f_pass=f_pass+x
print(f_pass)

