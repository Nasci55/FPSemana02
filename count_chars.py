phr= input()

x = phr.split(" ")
tam = {}
for palavras in x:
    tam[palavras] = len(palavras)
print(tam)