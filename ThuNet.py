import hashlib
import requests

def do_login():
    uname = input("Please input your user name:\n")
    password = input("Please input your password:\n")
    hashcd_md5 = hashlib.md5()
    hashcd_md5.update(password.encode())
    tr_password = hashcd_md5.hexdigest()
    tr_password = '{MD5_HEX}' + tr_password
    content = {'action': 'login',
               'username': uname,
               'password': tr_password,
               'ac_id': 1
               }
    r = requests.post('http://net.tsinghua.edu.cn/do_login.php', data = content)
    print(r.text)

def do_logout():
    content = {'action': 'logout'}
    r = requests.post('http://net.tsinghua.edu.cn/do_login.php', data = content)
    print(r.text)

if __name__ == '__main__':
    option = input("What do you want? login/logout\n")
    if option == 'login':
        do_login()
    elif option == 'logout':
        do_logout()
    else:
        print("wrong option, please type 'login' or 'logout'")