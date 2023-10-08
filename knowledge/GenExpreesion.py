lista_S = [1, 2, 3, 4, 5]

def zmien():
    nowa_lista = []
    for x in lista_S:
        nowa_lista.append(x*2)
    return nowa_lista

nowa_lista2 = [x * 2 for x in lista_S] # wyrazenie listowne
nowa_lista3 = (x * 2 for x in lista_S) # wyrazenie generatora

print(nowa_lista2)
print(nowa_lista3) # objekt genexpr
print(next(nowa_lista3))
print(next(nowa_lista3)) # jak mozna next to mozna i fora
for x in nowa_lista3: # nie idzie od nowa listy tylko tam gdzie "next" skonczylo !!!
    print(x)