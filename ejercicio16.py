print("-------------------------------------------------------")
print("ejercicio16 determina la salida")
print("-------------------------------------------------------")

# entradas
A = (input("ingrese A: "))
B = (input("ingrese B: "))
C = (input("ingrese C: "))

# proceso
print("-------------------------------------------------------")
if A > B:
    if A > C:
        if B > C:
            print(A, B, C)
        else:
            print(A, C, B)
    else:
        print(C, A, B)
else:
        if B > C:
            if A > C:
                print(B, A, C)
            else:
                print(B, C, A)
        else:
            print(B, C, A)
