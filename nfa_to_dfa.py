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
    for element in lista_nodos:
        print(element)
    return lista_nodos

def obtener_transicion(combinacion, simbolo):
    global todos_nodos
    #Un solo estado
    if(len(combinacion) == 1):
        for transicion in todos_nodos:
            if(transicion[0]==simbolo and transicion[1]==combinacion[0]):
                print("estado transicion con ", simbolo, "= ", transicion[2])


    else:
        lista_nodos = [];
        lista_transiciones = []
        for estado in combinacion:
            for transicion in todos_nodos:
                if(transicion[0]==simbolo and estado==transicion[1]):
                    lista_transiciones.append(transicion[2])

        print("estado transicion con ", simbolo, "= ", lista_transiciones)

    return



#Variables globales
todos_nodos = []
estados_transicion = []

def main():
    global todos_nodos
    archivo_NFA = open(input());
    automatas = archivo_NFA.read().split("\n")
    #Procesamiento de cada NFA
    for nfa in automatas:
        ultima_linea = False
        conjunto_nodos = set([])
        conjunto_simbolos = set([])
        valores = nfa
        while not ultima_linea:
            if valores[-1] == "}":
                ultima_linea = True
                valores = valores[:-1]

            valores = valores[1:]
            todos_nodos = obtener_nodos(valores)
            print(todos_nodos, "¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
            for nodo in todos_nodos:
                #Agrega los nodos y los simbolos del conjunto
                conjunto_simbolos.add(nodo[0])
                conjunto_nodos.add(nodo[1])
                conjunto_nodos.add(nodo[2])

            print("Conjuntos", end="")
            simbolos = list(conjunto_simbolos)
            for simbolo in simbolos:
                print("\t"*(len(conjunto_nodos)//2), end="")
                print(simbolo, end="")
            combinaciones = list(powerset(conjunto_nodos))
            for combinacion in combinaciones:
                print(combinacion)
                for simbolo in conjunto_simbolos:
                    obtener_transicion(combinacion, simbolo)
        

main()