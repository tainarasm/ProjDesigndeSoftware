def maior(lista):
    i=1
    while i<len(lista):
        if lista[i-1]>lista[i]:
           maior=lista[i-1]
        i=i+1
return maior
