frase = input("Ingresa una frase: ") 
vocal_a = 0 
vocal_e =0
vocal_i =0
vocal_o=0
vocal_u=0


for frase in "aeiouAEIOU":
    if "aeiouAEIOU" in frase:
        if vocal_a == "a" or "A":
            vocal_a +=1
        elif vocal_e == "e" or "E":
            vocal_e +=1
        elif vocal_i == "i" or "I":
            vocal_i +=1
        elif vocal_o == "o" or "O":
            vocal_o +=1
        elif vocal_u == "u" or "U":
            vocal_u +=1

print("La frase tiene", vocal_a, "vocales a.")
print("La frase tiene", vocal_e, "vocales e.")
print("La frase tiene", vocal_i, "vocales i.")
print("La frase tiene", vocal_o, "vocales o.")
print("La frase tiene", vocal_u, "vocales u.")