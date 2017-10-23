'''
Jorge Alexis Rubio Sumano A01372074
Servio Tulio Reyes Castillo A01371719

Program which transforms a transformation from a NFA to a DFA

'''

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
    todos_nodos = []
    conjunto_nodos = set([])
    conjunto_simbolos = set([])

    #Creacion de archivos
    input_file_name = input("Enter the file name to use as NFA input: ")
    output_file_name = input("Enter the file name to save the DFA output: ")
    valores = ""
    file = open(input_file_name, "r")   
    for line in file.readlines():
        valores += line;
    file.close()

    file = open(output_file_name, "w")

    valores = valores[1:-1]
    todos_nodos = obtener_nodos(valores)
    for nodo in todos_nodos:
        #Agrega los nodos y los simbolos del conjunto
        conjunto_simbolos.add(nodo[0])
        conjunto_nodos.add(nodo[1])
        conjunto_nodos.add(nodo[2])

    combinaciones = list(powerset(conjunto_nodos))
    #print("Conjuntos", end="")
    file.write("Conjuntos")
    simbolos = list(conjunto_simbolos)
    for simbolo in simbolos:
        #print("\t"*(len(conjunto_nodos)//2+1), end="")
        #print(simbolo, end="")
        file.write("\t"*(len(conjunto_nodos)//2+1))
        file.write(simbolo)
    #print()
    file.write("\n")
    for combinacion in combinaciones:
        #print(str(combinacion)+("\t"*((len(conjunto_nodos)//2+1)-(len(combinacion)//2)+1)), end='')
        file.write(str(combinacion)+("\t"*((len(conjunto_nodos)//2+1)-(len(combinacion)//2)+1)))
        for simbolo in simbolos:
            conjunto_parcial = set([])
            for nodo in todos_nodos:
                if nodo[0] == simbolo and nodo[1] in combinacion:
                    conjunto_parcial.add(nodo[2])
            if len(conjunto_parcial) == 0:
                #print("{}", end='')
                file.write("{}")
            else:
                #print(conjunto_parcial, end='')
                file.write(str(conjunto_parcial))
            #print("\t"*((len(conjunto_nodos)//2+1)-(len(conjunto_parcial)//2)), end='')
            file.write("\t"*((len(conjunto_nodos)//2+1)-(len(conjunto_parcial)//2)))
        #print()
        file.write("\n")
    file.close()

main()