from cryptography.fernet import Fernet
def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key
master_pwd  = input('type you master password: ')
key =  load_key() + master_pwd.encode()
fer = Fernet(key)

# def writeKey():
#     key = Fernet.generate_key()
#     with open('key.key', 'wb') as key_file:
#         key_file.write(key)
    
# writeKey()


def view():
   with open('password.txt', 'r') as f:
       for line in f.readlines():
           data = line.rstrip()
           user,passw = data.split('|')
           print('username is:', user, ", password is:", fer.decrypt(passw.encode()).decode())

def add():
    username = input('account name: ')
    pwd = input('password: ')

    with open('password.txt', 'a') as f:
        f.write(username+ '|'+ fer.encrypt(pwd.encode()).decode() + '\n')
    

while True:
    mode = input('would you like to add new password or view existing? (add/view), type Q to quit ').lower()
    if mode == 'q':
        break
    if mode == 'add':
       add()
    elif mode== 'view':
        view()
    else: 
        print('please type a valid mode')
        continue