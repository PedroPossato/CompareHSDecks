import urllib
import sys

def getPage(url):
    try:
        return urllib.urlopen(url).readlines()
    except:
        print "Erro ao abrir o url"

link = raw_input("\nInsira link, por favor: ")
response = getPage(link)
listaDeNomes = []
listaDeValores = int
listaDeValores = []
conta = 0
count = 0

for i in range(len(response)):
    if "Dust Cost:" in response[i]:
        count+=1
    if '<span class="card-name">' in response[i]:
        nome = response[i].split('span class="card-name">')[1].split("</span")[0]
        valor = int (response[i].split('span class="card-count">')[1].split('</span>')[0])
        if nome not in listaDeNomes:
            conta+=1
            listaDeNomes.append(nome)
            listaDeValores.append(valor)
        else:
            listaDeValores[listaDeNomes.index(nome)] += valor

print ""

for j in range(conta):
    print listaDeNomes[j],'-',(listaDeValores[j]/(count*1.0))
