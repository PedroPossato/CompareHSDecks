import urllib
import requests

response = requests.get(raw_input("\nInsira link, por favor: ")).text.split("\n")

listaDeNomes = []
listaDeValores = []
conta = 0
count = 0

for r in response:
    if "Dust Cost:" in r:
        count += 1
    if '<span class="card-name">' in r:
        nome = r.split('span class="card-name">')[1].split("</span")[0]
        valor = int (r.split('span class="card-count">')[1].split('</span>')[0])
        if nome not in listaDeNomes:
            conta+=1
            listaDeNomes.append(nome)
            listaDeValores.append(valor)
        else:
            listaDeValores[listaDeNomes.index(nome)] += valor

for j in range(conta):
    print listaDeNomes[j],'-',(listaDeValores[j]/(count*1.0))

print ""
