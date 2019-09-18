id_001 = "rizkyfahryandi"
pass_001 = "fahry123"
id_002 = "neroazaziel"
pass_002 = "nero123"
id_011 = "tara"
pass_011 = "tara123"
id_012 = "tasyi"
pass_012 = "tasyi12345"

def pilihan():
	login=int(input("Silahkan Pilih : "))
	if login == 1:
		pemilik()
	elif login == 2:
		kasir()
	else:
		print("Tidak Ditemukan")
		pilihan()

def pemilik():
	username=input("Username : ")
	password=input("Password : ")
	if username==id_001 and password==pass_001:
		print("WELCOME")
	elif username==id_002 and password==pass_002:
		print("WELCOME")
	else:
		print("Username atau Password salah")
		pemilik()

def kasir():
	username=input("Username : ")
	password=input("Password : ")
	if username==id_011 and password==pass_011:
		print("WELCOME")
	elif username==id_012 and password==pass_012:
		print("WELCOME")
	else:
		print("Username atau Password salah")
		kasir()

print("Login sebagai : \n", "1. Pemilik\n", "2. Kasir")
pilihan()