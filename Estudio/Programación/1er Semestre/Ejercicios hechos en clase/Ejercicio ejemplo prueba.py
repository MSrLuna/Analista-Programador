def textos(txt1, txt2):
    espacio = " "
    punto = "."
    concatenado = txt1 + espacio + txt2 + punto
    return concatenado

texto1 = input("Primer texto:  | ")
texto2 = input("Segundo texto: | ")

texto_completo = textos(texto1, texto2)

print(texto_completo)