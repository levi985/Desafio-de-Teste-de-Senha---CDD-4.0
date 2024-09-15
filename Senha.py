senha = int(input("Digite uma senha"))
print("================================")
csenha = int(input("Confirme sua senha"))
print("================================")
while senha != csenha:
    csenha = int(input("A senhas são diferentes. Confirme sua senha"))
    print("================================")
else:
    print("Senha definida com sucesso. Lembre-se dela!")
print("================================")
cont = 0
while cont <= 3:
    senhan = int(input("Digite sua senha"))
    if senhan == senha:
        print("Acesso liberado!")
        break
    else:
        print("Senha incorreta")
    cont += 1
if cont == 3:
    print("bloqueio de segurança")
