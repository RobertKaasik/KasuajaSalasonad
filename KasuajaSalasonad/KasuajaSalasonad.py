from funktsioonid import *
users=["Robert"]
passwords=["12345"]

while True:
    print("Registreerimine-1,-\nAvtoriseerimine-2,\nVäljä-3")
    v=int(input())
    if v==1:
        print("Registreerimine")#пишим логин и пароль
        while 1:
            log=input("kasutajatunnus:")
            if log not in users:
                print("Tunnu soobib")
                break
            else:
                print("See nimi juba on olemas listis")
        v=input("Arvuti-A voi ise-I loob parool")
        if v.upper()=="A":
            pas=passautomat()
        elif v.upper()=="I":
            while 1:
                pas=input("Sisesta oma parool")
                tulemus=paskontroll(passwords)
                if tulemus==True:
                    users.append(log)
                    passwords.append(pas)
                    break
        else:
            print("Parool ei soobib")
    elif v==2:
        print("Avtoriseerimine")
        log=input("Kasutajatunnus:")
        if passwords.index(pas)==users.index(user):
            print("Tere tulemast")

    elif v==3:
        print("Väljä")
        break
    else:
        print("On vaja valida 1,2 või 3")