import random
#создам функцию
def passautomat()->str:
	#пароль создает машина
	str0=".,:;!_*-+()/#¤%&"
	str1 = '0123456789'
	str2 = 'qwertyuiopasdfghjklzxcvbnm'
	str3 = str2.upper()
	#print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
	str4 = str0+str1+str2+str3
	#print(str4)
	ls = list(str4)
	#	print(ls)
	random.shuffle(ls)
	print(ls)
	psword = "".join([random.choice(ls) for x in range(12)])
	return psword

def paskontroll(pasword: str)->bool:
	ls=list(psword)
	for e in ls:
		if e.isdigit(): d=True
		if e.isalpha(): a=True
		if e.isupper(): u=True
		if e.islower(): l=True
		if e in list(".,;:!_-*+()/#%&"): s=True
	if d==True and a==True and u==True and l==True and s==True:
		t=True
	else:
		t=False
	return t