from usuario import Usuario

user1 = Usuario("Messias", "Batista", 33,\
    "Masculino", "12345678978")
print(user1.descrever_usuario())

user2 = Usuario("Flávia", "Daniel", 91,\
    "não declarado", "7894561312" )
print(user2.descrever_usuario())

user3 = Usuario("Fagner", "PCC", 52, "Masc", "74523159745")
print(user3.descrever_usuario())