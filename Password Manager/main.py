from cryptography.fernet import Fernet

'''''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


def view():
    with open('password.txt', 'r') as f: 
        for line in f.readlines():
            data = line.rstrip() #Erase spaces
            user, passw = data.split("|")
            print("User: ", user, "| Password: ", fer.decrypt(passw.encode()).decode())
def new():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f: #w = write (Erase the txt)  r = reads file only
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


Master_pwd = input("What is the master password: ")
key = load_key() + Master_pwd.encode()
fer = Fernet(key)

while True:
    Option = input("Add new password or view existing one? (view, new, q to quit): ").lower()
    if Option == "view":
        view()
    elif Option == "new":
        new()
    elif Option == "q":
        break
    else:
        print("Choose a correct option next time")