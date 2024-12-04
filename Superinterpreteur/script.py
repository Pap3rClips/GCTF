print("Bienvenue dans le Superinterpreteur !")
print("Lancement du programme ...")

import pwn
import re

host = "guardiactf.live"
port = 12350
conn = pwn.remote(host, port)

# résolution des liste de compréhension

while True:
    data = conn.recvuntil(b"?").decode()
    print("resultat : ", data)
    match = re.findall(r"(\[.*?\])", data)
    output = match[1]
    result = eval(output)
    conn.sendline(bytes(str(result), "utf-8"))
    if "[48/50]" in data:
        break
    

conn.close()
print("Fermeture du programme")