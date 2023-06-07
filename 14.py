mayores = 0
menores = 0
femeninas = 0
masculinos = 0

for i in range(1,16):
    print("Persona", i ,"de 15:")
    genero = input("Digite M para masculino o F para femenino--> ")
    genero = genero.lower()
    if genero == "m":
        masculinos += 1
    elif genero == "f":
        femeninas += 1
    
    edad = int(input("Digite su edad--> "))
    if edad >= 18:
        mayores += 1
    else:
        menores += 1

print("masculinos:", masculinos, "\nfemeninos:", femeninas, "\nmayores:", mayores, "\nmenores:", menores)
    
