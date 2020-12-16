password='2002'
x=input()
if (x == password):
    print("Acesso Permitido")
else:
    print("Senha Invalida")
    while (x != password):
        x = input()
        if (x == password):
            print("Acesso Permitido")
        else:
            print("Senha Invalida")