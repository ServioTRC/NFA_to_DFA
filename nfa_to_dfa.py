"""

2ndo Proyecto Matematicas Computacionales
Transformación NFA a DFA

Servio Tulio Reyes Castillo A01371719
Jorge Alexis Rubio Sumano   A01372074

"""

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

def obtener_transicion(combinacion, simbolo):
    #Se obtine el estado de transicion de la combinación de paramtero, con el simbolo indicado
    global todos_nodos
    lista_transiciones = []
    if(len(combinacion) == 1):
        for transicion in todos_nodos:
            if(transicion[0]==simbolo and transicion[1]==combinacion[0]):
                #print("estado transicion con ", simbolo, "= ", transicion[2])
                lista_transiciones.append(transicion[2])

    else:
        for estado in combinacion:
            for transicion in todos_nodos:
                if(transicion[0]==simbolo and estado==transicion[1]):
                    if(not(transicion[2] in lista_transiciones)):
                        lista_transiciones.append(transicion[2])

        #print("estado transicion con ", simbolo, "= ", lista_transiciones)
    res = ""
    for val in lista_transiciones:
        res += val
    return res



#Variables globales
todos_nodos = []
estados_transicion = "{"

def main():
    global todos_nodos, estados_transicion
    try:
        input_file_name = input("Enter the file name to use as NFA input: ")
        output_file_name = "salida.txt"
        archivo_NFA = open(input_file_name)
        automatas = archivo_NFA.read().split("\n")
        #Procesamiento de cada NFA
        for nfa in automatas:
            ultima_linea = False
            conjunto_nodos = set([])
            conjunto_simbolos = set([])
            valores = nfa
            if valores == "":
                ultima_linea = True
            while not ultima_linea:
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

                '''print("Conjuntos", end="")
                simbolos = list(conjunto_simbolos)
                for simbolo in simbolos:
                    print("\t"*(len(conjunto_nodos)//2), end="")
                    print(simbolo, end="")'''
                combinaciones = list(powerset(conjunto_nodos))

                #Genera todos los estados de transicion
                for combinacion in combinaciones:
                    #print(combinacion)
                    #Por cada elemento del alfabeto
                    for simbolo in conjunto_simbolos:
                        estados_transicion += "(" + str(simbolo) + ","
                        #Da formato al conjunto {q0,q1,...,qn}
                        for estado in combinacion:
                            estados_transicion += estado + ""
                        if len(obtener_transicion(combinacion,simbolo)) == 0:
                            estados_transicion += ",), \n"
                        else:
                            estados_transicion += "," + str(obtener_transicion(combinacion,simbolo)) + "),\n"
                estados_transicion = estados_transicion[:-2]
                estados_transicion += "}"
                #print("\nDFA: ", estados_transicion)
                archivo_DFA = open(output_file_name, "w")
                archivo_DFA.write(estados_transicion)
                archivo_DFA.close()
    except Exception:
        print("Error opening the file")
        exit(-1)

main()