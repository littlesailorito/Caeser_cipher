from main import letters_G,letters_S
shift=input("Give the shift to rotate: ")
string= input("Give the string to encrypt: ")
result= []
vals=0
flag=False
for char in string:
    if ord(char) < 97:
        for key,value in letters_G.items():
            if key == char:
                flag= False
                vals+=((value+3)%26)
        for key,value in letters_G.items():
            if value==vals and flag==False:
                result.append(key)
                vals=0
                flag= True
                break
    elif ord(char)>=97:
        for key,value in letters_S.items():
            if key == char:
                flag= False
                vals+=((value+3)%26)
        for key,value in letters_S.items():
            if value==vals and flag==False:
                result.append(key)
                vals=0
                flag= True
                break
                
    if char==" ":
        result.append(" ")

print("".join(result))