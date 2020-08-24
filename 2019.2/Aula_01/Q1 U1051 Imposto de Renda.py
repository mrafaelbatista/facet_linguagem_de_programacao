salario = float(input("Digite o seu salário: "))
if salario <= 2000.00 :
    print("Você é isento do Imposto de Renda")
elif salario >= 2000.01 and salario <= 3000.00 :
    imposto = salario - 2000.00
    imposto = imposto * (8/100)
    print("Imposto a ser pago é " + str(imposto))
elif salario >= 3000.01 and salario <= 4500.00:
    # Isento
    imposto = salario - 2000 # Isento
    imposto = imposto - 1000 # 8%
    # Imposto = 8% + 18%
    imposto = 80.0 + (imposto * 0.18)
    print("Imposto a ser pago é " + str(imposto))
elif salario > 4500.00 :
    # Isento
    imposto = salario - 2000 # Isento
    imposto = imposto - 1000 # 8%
    imposto = imposto - 1500 # 18%
    # Imposto = 8% + 18% + 28%
    imposto = 80.0 + 270.0 + (imposto * 0.28)
    print("Imposto a ser pago é {0:.2f}".format(imposto, 2))
