import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='302302',
    database='academiaturmab',
)

cursor = conexao.cursor()

#CRUD


#INSERIR

nome = input("Digite o Nome: ")
telefone = input("Telefone:  ")
end = input("Endereço: ")
cpf = input("CPF: ")
email = input("Email: ")

comando = f'INSERT INTO alunos (nome, telefone, end, cpf,  email) VALUES ("{nome}", {telefone}, "{end}", {cpf}, "{email}")'

cursor.execute(comando)
conexao.commit() #editar banco de dados


#CONSULTAR

comando = f'SELECT*FROM alunos'
cursor.execute(comando)
resultado = cursor.fetchall() #ler o banco de dados
print(resultado)

#DELETAR
matricula = "8888"
comando = f'DELETE FROM alunos WHERE matricula = "{matricula}"'
cursor.execute(comando)
conexao.commit() #editar banco de dados


#ATUALIZAR

nome = "jose"
email = "rafateste@gmail.com"
comando = f'UPDATE alunos SET email = "{email}"  WHERE nome = "{nome}"'
cursor.execute(comando)
conexao.commit() #editar banco de dados

cursor.close()
conexao.close()