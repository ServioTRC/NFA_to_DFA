from itertools import chain, combinations

def powerset(iterable):
    #Genera todos los subconjuntos
    xs = list(iterable)
    return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1))

def obtener_nodos(valores):
    #Obtiene los nodos del string ingresado
    lista_nodos = []
    cuenta_inicio = 0
    cuenta_final = 0
    for i in range(len(valores)):
        if valores[i] == "(":
            cuenta_inicio = i+1
        elif valores[i] == ")":
            cuenta_final = i
            lista = []
            temporal = valores[cuenta_inicio:cuenta_final]
            temporal = temporal.split(",")
            lista.append(temporal[0])
            lista.append(temporal[1])
            lista.append(temporal[2])
            lista_nodos.append(lista)
    return lista_nodos

def main():
    ultima_linea = False
    todos_nodos = []
    conjunto_nodos = set([])
    conjunto_simbolos = set([])
    while not ultima_linea:
        valores = input()
        if valores[-1] == "}":
            ultima_linea = True
            valores = valores[:-1]

        valores = valores[1:]
        todos_nodos = obtener_nodos(valores)
        for nodo in todos_nodos:
            #Agrega los nodos y los simbolos del conjunto
            conjunto_simbolos.add(nodo[0])
            conjunto_nodos.add(nodo[1])
            conjunto_nodos.add(nodo[2])

        combinaciones = list(powerset(conjunto_nodos))
        print("Conjuntos", end="")
        simbolos = list(conjunto_simbolos)
        for simbolo in simbolos:
            print("\t"*(len(conjunto_nodos)//2), end="")
            print(simbolo, end="")
        print()
        for combinacion in combinaciones:
            print(combinacion)
        

main()