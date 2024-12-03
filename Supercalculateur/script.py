# importation des outils nécessaires
import pwn
import re

# défintion de la fonction de résolution d'équation
def solve_equation(data):
    # définition du pattern et du match
    # 93 + 38
    match = re.search(r"(\d+)\s+([+\-*/])\s+(\d+)", data)
    if match:
        a = int(match.group(1))
        b = int(match.group(3))
        operateur = match.group(2)
        print("a : ", a)
        print("b : ", b)
        print("operateur : ", operateur)

        if operateur=="+":
            return a + b
        elif operateur=="-":
            return a - b
        elif operateur=="*":
            return a * b
        elif operateur=="/":
            return a / b
        else:
            print("opérateur inconnue", operateur)
    else:
        print("Aucune équation valide trouvé :(")
        print(data)
        end = True
    # condition de lancement de l'algo
        

# définition des variables de configuration de la connexion au serveur distant
host = "guardiactf.live"
port = 12347

# initialisation de la connexion au serveur distant
conn = pwn.remote(host, port)

# récupération de la donnée et envoie dans la fonction de résolution
while True:
    data = conn.recvuntil(b"?").decode()
    print(data)
    conn.sendline(str(solve_equation(data)))
    response = conn.recvline().decode()
    print(response)
    if "[200/200]" in data:
        print("fin !!!")
        break

while True:
    data = conn.recv(1024).decode()
    print(data)
    if len(data) < 1024:
        break

# fermeture de la connexion au serveur distant
conn.close()