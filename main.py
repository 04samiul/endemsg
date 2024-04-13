def run():
    import os 
    os.system("pip install cryptography")
    from cryptography.fernet import Fernet

    message= input("\n\n\nEnter Your massage: ")
    msg= message.lower()
    key= Fernet.generate_key()

    fernet = Fernet(key)

    en_msg= fernet.encrypt(msg.encode())
    de_msg= fernet.decrypt(en_msg).decode()

    def en() :
        print("Encryption message is: \n\n",en_msg,"\n\n")

    def de():
        print("dcryption message is: \n\n",de_msg,"\n\n")

    print("Select Method")
    print("[1] for Encryption")
    print("[2] for Decryption")
    method = input("Enter method: ")

    if method == "1" :
        print("Encrypting the message......")
        en()
    elif method == "2" :
        print("Decrypting the message......")
        de()
    else:
        print("Wrong method selected. Try again.......")

user_name= input("Username: ")
user_pass= input("Password: ")
names={"samiul":"##pp@@", "samiul.islam":"islamabad+ddos", "random":"random"}
if user_name in names and names[user_name] == user_pass:
    print("Access granted.....")
    run()
else:
    print("Username and password dosen't match, You must be a fool....")