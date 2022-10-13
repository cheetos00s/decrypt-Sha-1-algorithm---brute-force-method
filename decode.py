from urllib.request import urlopen
import hashlib
import time

contraseña = "de68a951c1586debd9031e55c96f667072382937"

list_contraseña = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8')
st = time.time()
for x in list_contraseña.split('\n'):
    
    hashPrueba = hashlib.sha1(bytes(x, 'utf-8')).hexdigest()
    print(hashPrueba, x)

    if(contraseña == hashPrueba):
        print("la contraseña es:  ",str(x))
        et = time.time()
        print('Execution time: ',(et - st)," seconds")
        quit()
