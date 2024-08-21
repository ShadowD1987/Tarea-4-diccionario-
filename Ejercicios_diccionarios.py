# desarrola un algoritmo en python que imprima de manera ascendente los valores de un diccionario

def valores_ascendentes_diccionario(dicc):
    

    valores = sorted(dicc.values())


    print("Los valores en forma ascendente son:", valores)



valores_ascendentes_diccionario({
    "u" : 1000,
    "v" : 10,
    "x" : 200,
    "y" : 250
    
})

#desarrolla un algoritmo que verifique si todas las claves:valor de un diccioanrio se encuentra en otro diccionario

def claves_valor(dic1, dic2):
    
    for c, v in dic1.items():
        
        if c not in dic2 or dic2[c] != v:
            
            return "Las claves : valor de los diccionarios NO son iguales"
        
    return "Las claves : valor de los diccionarios son iguales"
        
     

print(claves_valor({
    
    "a" : 1,
    "b" : 2,
    "c" : 3
    
},{
    
    "a" : 1,
    "b" : 2,
    "c" : 3
    
}))

#desarrollar una funciín que reciba dos diccionarios como parámetros y los mezcle: si hay una clave repetida, se debe asignar el valor del primer diccioanrio.

def mezcla_diccionarios(dic1, dic2):
    
    a = dic1
    
    for c, v in dic2.items():
        
        if c not in a:
            
            a[c] = v
    
    return a



print(mezcla_diccionarios({
    
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4
},{
    "e" : 5,
    "f" : 6,
    "g" : 7,
    "d" : 8
}))
        
    
# desarrollar un programa que dada una lista de personas, imprima los nombres y apellidos de las personas que están en un rango de edad

def rango_edad(persona, min, max):
    
    for i in persona:
        
        if min <= i["edad"] <= max:
            
            print(i)
            
            
   
lista = [ 
{"nombre" : "Raúl","apellido" : "Rojas","edad" : 35},
{"nombre" : "Marta","apellido" : "Rosas","edad" : 87},
{"nombre" : "Paul","apellido" : "Walker","edad" : 40},
{"nombre" : "Dilan","apellido" : "Diaz","edad" : 19}]

         
rango_edad(lista,10,40)
    