from data import letters_G,letters_S
def Decryption():
    shift : int= int(input("Give the shift to derotate: "))
    string : str= input("Give the string to decrypt: ")
    result : list= []
    vals: int= 0
    flag : bool= False
    for char in string:
        if ord(char) < 97:
            for key,value in letters_G.items():
                if key == char:
                    flag= False
                    vals+=((value-shift)%26)
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
                    vals+=((value-shift)%26)
            for key,value in letters_S.items():
                if value==vals and flag==False:
                    result.append(key)
                    vals=0
                    flag= True
                    break
                    
        if char==" ":
            result.append(" ")
    return "".join(result)

