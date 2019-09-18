from q3_user import User

user1 = User("Osvaldo", "Rafael")
user1.primeiro_nome = "Rafael"
user1.sobrenome = "Andrade"
user1.sexo = "muito, avoroçado"
print(user1.saudacao())
print(user1.descrever_usuario())