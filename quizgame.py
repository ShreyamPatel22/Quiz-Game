# this is a module that will allow you to encrypt text
from cryptography.fernet import Fernet 

'''
#define a key, it will take a string of text  and turn it into a random text that you cant get without knowing the key
##key + password + text to encrypt = random text
##random text + key + password = text to encrypt
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file
    file.close()
    return key
#e
master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key) 


#create a function
def view():
    #use r to read to exisiting file and not create one
    with open('password.txt', 'r') as f:
        #for loop to read all the lines
        for line in f.readlines():
            #rstrip strips off the carriage return from our line
            data = line.rstrip()
            # .split will seperate username from password. 
            # .split will look for "|" and return the list without the pipe charaters 
            user, passw = data.split("|")
            print("User:", user, ", Password:", fer.decrypt(passw.encode()).decode())

#use with to close the file. 'a' allows to add something the end of an exisitng file and create a new file if that doesn't exist

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")
    with open('password.txt', 'a') as f:
        f.write(name + "|" + (fer.encrypt(pwd.encode()).decode() + "\n"))
                
        

while True:
    mode = input("Would you like to add a new password or view exisiting ones (view, add), press q to quit? ").lower()
   
    if mode ==  "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
    