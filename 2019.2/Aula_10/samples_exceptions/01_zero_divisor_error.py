# #Verifique o erro gerado
# print(50/0)

#Tente agora assim
# try:
#     print(50/0)
# except ZeroDivisionError:
#     print("Você não pode dividir por zero")


#Bloco else

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

msg = "Número A: %d \n" \
      "Número B: %d" %(num1, num2)
print(msg)

try:
    resposta = num1 / num2
except ZeroDivisionError:
    print("Você não pode dividir por zero")
else:
    print(resposta)