nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a primeira nota: "))
nota3 = float(input("Digite a primeira nota: "))

nota_final = (nota1 + nota2 + nota3)

if nota_final >= 21:
    print("Aluno Aprovado")
elif nota_final >=9:
    print ("Aluno em Recuperação")
else:
    print ("Aluno reprovado")

