from encrypter import Encryption
from decrypter import Decryption



if __name__ == "__main__":

   

    quit : int= 1
    choose : int= 0
    while quit:
        choose=input("Choose:\n1)Encrypt\n2)Decrypt\n3)Exit\n")
        if int(choose)==1:
            print(f"The result of the encryption is {Encryption()}")
        if int(choose)==2:
            print(f"The result of the decryption is {Decryption()}")
        if int(choose)==3:
            break

