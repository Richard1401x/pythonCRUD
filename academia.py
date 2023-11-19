import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='302302',
    database='academiaturmab',
)

cursor = conexao.cursor()


print("Menu de Opções\n "
"Digite 1 para ALUNOS\n "
"Digite 2 para PERSONAL\n "
"Digite 3 para FUNCIONARIOS\n"
" Digite 4 para MODALIDADES")
opcao = input("Qual a opção: ")

if opcao == '1': #ALUNOS
      print(" 1 - Cadastra\n 2 - Atualizar\n 3 - Consultar\n 4 - Deletar")
      resposta = input("Digite: ")

      if resposta == '1': #CADASTRO DE ALUNO
            nome = input("Digite o Nome: ")
            telefone = input("Telefone:  ")
            end = input("Endereço: ")
            cpf = input("CPF: ")
            email = input("Email: ")

            comando = f'INSERT INTO alunos (nome, telefone, end, cpf,  email) VALUES ("{nome}", {telefone}, "{end}", {cpf}, "{email}")'

            cursor.execute(comando)
            conexao.commit()  # editar banco de dados
            print("CADASTRO REALIZADO COM SUCESSO!!!")
      if resposta == '2': #ATUALIZAR DADOS DO ALUNO
            print("VOCÊ DESEJA ATUALIZAR")
            print(" 1 - Atualizar Nome\n 2 - Atualizar Telefone\n 3 - Atualizar Endereço\n 4 - Atualizar Email\n 5 - Atualizar CPF")
            resposta1 = input("O que deseja atualizar: ")
            if resposta1 == '1': #ATUALIZAR NOME
                  nome = input("Digite o nome que deseja atualizar: ")
                  atualizar = input("Digite o novo nome: ")
                  comando = f'UPDATE alunos SET nome = "{atualizar}" WHERE nome = "{nome}"'
                  cursor.execute(comando)
                  conexao.commit()  # editar banco de dados
                  print("NOME ATUALIZADO")
            if resposta1 == '2': #ATUALIZAR TELEFONE
                  telefone = input("Digite o antigo número que deseja atualizar: ")
                  atualizar = input("Digite o novo numero: ")
                  comando = f'UPDATE alunos SET telefone = "{atualizar}" WHERE telefone = "{telefone}"'
                  cursor.execute(comando)
                  conexao.commit()  # editar banco de dados
                  print("TELEFONE ATUALIZADO")
            if resposta1 == '3':# ATUALIZAR ENDEREÇO
                  endereco = input("Digite o antigo endreço que deseja atualizar: ")
                  atualizar = input("Digite o novo endereço: ")
                  comando = f'UPDATE alunos SET end = "{atualizar}" WHERE end = "{endereco}"'
                  cursor.execute(comando)
                  conexao.commit()  # editar banco de dados
                  print("ENDEREÇO ATUALIZADO")
            if resposta1 == '4': #ATUALIZAR EMAIL
                  email = input("Digite o antigo E-mail que deseja atualizar: ")
                  atualizar = input("Digite o novo E-mail: ")
                  comando = f'UPDATE alunos SET email = "{atualizar}" WHERE email = "{email}"'
                  cursor.execute(comando)
                  conexao.commit()  # editar banco de dados
                  print("E-MAIL ATUALIZADO")
            if resposta1 == '5': #ATUALIZAR O CPF
                  cpf = input("Digite o antigo CPF que deseja atualizar: ")
                  atualizar = input("Digite o novo CPF: ")
                  comando = f'UPDATE alunos SET cpf = "{atualizar}" WHERE cpf = "{cpf}"'
                  cursor.execute(comando)
                  conexao.commit()  # editar banco de dados
                  print("CPF ATUALIZADO")
                  cursor.close()
                  conexao.close()

      if resposta == '3': #Conculta o banco de dados
            comando = f'SELECT*FROM alunos'
            cursor.execute(comando)
            resultado = cursor.fetchall()  # ler o banco de dados
            print(resultado)

      if resposta == '4': #Exclui informação do banco de dados
            matricula = input("Digite aqui a matrícula do aluno que deseja excluir: ")
            comando = f'DELETE FROM alunos WHERE matricula = "{matricula}"'
            cursor.execute(comando)
            conexao.commit()  # editar banco de dados

if opcao == '2': #PERSONAL TRAINER
      print(" 1 - Cadastra\n 2 - Atualizar\n 3 - Consultar\n 4 - Deletar")
      resposta2 = input("Digite: ")

      if resposta2 == '1': #CADASTRO DE PERSONAL
            cref = input("Digite seu CREF: ")
            cpf = input("CPF: ")
            nome = input("Digite o Nome: ")
            telefone = input("Telefone:  ")
            email = input("Email: ")

            comando = f'INSERT INTO personal (cref, cpf, nome, telefone, email) VALUES ({cref}, {cpf}, "{nome}", {telefone}, "{email}")'

            cursor.execute(comando)
            conexao.commit()  # editar banco de dados
            print("CADASTRO REALIZADO COM SUCESSO!!!")
      if resposta2 == '2': #ATUALIZAR CADASTRO PERSONAL
            print("VOCÊ DESEJA ATUALIZAR")
            print(" 1 - Atualizar CREF\n 2 - Atualizar CPF\n 3 - Atualizar Nome\n 4 - Atualizar Telefone\n 5 - Atualizar E-mail")
            escolha = input("Digite: ")
            if escolha == '1': #ATUALIZAR CREF
                  cref = input("Digite o CREF que deseja atualizar: ")
                  atualizar = input("Digite o novo CREF: ")
                  comando = f'UPDATE personal SET cref = "{atualizar}" WHERE cref = "{cref}"'
                  cursor.execute(comando)
                  conexao.commit()  # editar banco de dados
                  print("CREF ATUALIZADO")
            if escolha == '2': #ATUALIZAR CPF
                  cpf = input("Digite o CPF que deseja atualizar: ")
                  atualizar = input("Digite o novo CPF: ")
                  comando = f'UPDATE personal SET cpf = "{atualizar}" WHERE cpf = "{cpf}"'
                  cursor.execute(comando)
                  conexao.commit()  # editar banco de dados
                  print("CPF ATUALIZADO")
            if escolha == '3': #ATUALIZAR NOME
                  nome = input("Digite o Nome que deseja atualizar: ")
                  atualizar = input("Digite o novo Nome: ")
                  comando = f'UPDATE personal SET nome = "{atualizar}" WHERE nome = "{nome}"'
                  cursor.execute(comando)
                  conexao.commit()  # editar banco de dados
                  print("NOME ATUALIZADO")
            if escolha == '4': #ATUALIZAR TELEFONE
                  telefone = input("Digite o Telefone que deseja atualizar: ")
                  atualizar = input("Digite o novo Telefone: ")
                  comando = f'UPDATE personal SET telefone = "{atualizar}" WHERE telefone = "{telefone}"'
                  cursor.execute(comando)
                  conexao.commit()  # editar banco de dados
                  print("TELEFONE ATUALIZADO")
            if escolha == '5': #ATUALIZAR E-MAIL
                  email = input("Digite o E-mail que deseja atualizar: ")
                  atualizar = input("Digite o novo E-mail3: ")
                  comando = f'UPDATE personal SET email = "{atualizar}" WHERE email = "{email}"'
                  cursor.execute(comando)
                  conexao.commit()  # editar banco de dados
                  print("E-MAIL ATUALIZADO")
      if resposta2 == '3': #CONSULTAR CADASTRO PERSONAL
            comando = f'SELECT*FROM PERSONAL'
            cursor.execute(comando)
            resultado = cursor.fetchall()  # ler o banco de dados
            print(resultado)

      if resposta2 == '4': #DELETAR CADASTRO
            cref = input("Digite aqui a CREF do PERNSONAL que deseja excluir: ")
            comando = f'DELETE FROM personal WHERE cref = "{cref}"'
            cursor.execute(comando)
            conexao.commit()  # editar banco de dados

if opcao == '3': #FUNCIONARIOS
      print(" 1 - Cadastra\n 2 - Atualizar\n 3 - Consultar\n 4 - Deletar")
      resposta3 = input("Digite: ")

      if resposta3 == '1': #CADASTRO DE FUNCIONARIOS
            cpf = input("Digite seu CPF: ")
            nome = input("Nome: ")
            email = input("Digite seu E-mail: ")
            end = input("Endereço:  ")
            telefone = input("Telefone: ")
            funcao = input("Função de trabalho: ")

            comando = f'INSERT INTO funcionarios (cpf, nome, email, end, telefone, funcao) VALUES ({cpf}, "{nome}", "{email}", "{end}", {telefone}, "{funcao}")'

            cursor.execute(comando)
            conexao.commit()  # editar banco de dados
            print("CADASTRO REALIZADO COM SUCESSO!!!")
      if resposta3 == '2':  # ATUALIZAR CADASTRO FUNCIONARIOS
            print("VOCÊ DESEJA ATUALIZAR")
            print(" 1 - Atualizar CPF\n 2 - Atualizar Nome\n 3 - Atualizar E-mail\n 4 - Atualizar Endereço\n 5 - Atualizar Telefone\n 6 - Função de Trabalho")
            escolha = input("Digite: ")
            if escolha == '1':  # ATUALIZAR CPF
                  cpf = input("Digite o cpf que deseja atualizar: ")
                  atualizar = input("Digite o novo CPF: ")
                  comando = f'UPDATE funcionarios SET cpf = "{atualizar}" WHERE cpf = "{cpf}"'
                  cursor.execute(comando)
                  conexao.commit()  # editar banco de dados
                  print("CPF ATUALIZADO")
            if escolha == '2':  # ATUALIZAR NOME
                  nome = input("Digite o NOME que deseja atualizar: ")
                  atualizar = input("Digite o novo NOME: ")
                  comando = f'UPDATE funcionarios SET nome = "{atualizar}" WHERE nome = "{nome}"'
                  cursor.execute(comando)
                  conexao.commit()  # editar banco de dados
                  print("NOME ATUALIZADO")
            if escolha == '3':  # ATUALIZAR EMAIL
                  email = input("Digite o E-mail que deseja atualizar: ")
                  atualizar = input("Digite o novo E-mail: ")
                  comando = f'UPDATE funcionarios SET email = "{atualizar}" WHERE email = "{email}"'
                  cursor.execute(comando)
                  conexao.commit()  # editar banco de dados
                  print("E-MAIL ATUALIZADO")
            if escolha == '4':  # ATUALIZAR ENDEREÇO
                  endereco = input("Digite o Endereço que deseja atualizar: ")
                  atualizar = input("Digite o novo Endereço: ")
                  comando = f'UPDATE funcionarios SET end = "{atualizar}" WHERE end = "{endereco}"'
                  cursor.execute(comando)
                  conexao.commit()  # editar banco de dados
                  print("ENDEREÇO ATUALIZADO")
            if escolha == '5':  # ATUALIZAR TELEFONE
                  telefone = input("Digite o Telefone que deseja atualizar: ")
                  atualizar = input("Digite o novo Telefone: ")
                  comando = f'UPDATE funcionarios SET telefone = "{atualizar}" WHERE telefone = "{telefone}"'
                  cursor.execute(comando)
                  conexao.commit()  # editar banco de dados
                  print("TELEFONE ATUALIZADO")
            if escolha == '6':  # ATUALIZAR FUNÇÃO
                  funcao = input("Digite a Função que deseja atualizar: ")
                  atualizar = input("Digite a nova Função: ")
                  comando = f'UPDATE funcionarios SET funcao = "{atualizar}" WHERE funcao = "{funcao}"'
                  cursor.execute(comando)
                  conexao.commit()  # editar banco de dados
                  print("FUNÇÃO ATUALIZADO")
      if resposta3 == '3': #CONSULTAR CADASTRO DE FUNCIONARIOS
            comando = f'SELECT*FROM funcionarios'
            cursor.execute(comando)
            resultado = cursor.fetchall()  # ler o banco de dados
            print(resultado)
      if resposta3 == '4': #DELETAR CADASTRO
            cpf = input("Digite aqui a CPF do FUNCIONARIO que deseja excluir: ")
            comando = f'DELETE FROM funcionarios WHERE cpf = "{cpf}"'
            cursor.execute(comando)
            conexao.commit()  # editar banco de dados
if opcao == '4': #MODALIDADES
      print(" 1 - Cadastra\n 2 - Atualizar\n 3 - Consultar\n 4 - Deletar")
      resposta4 = input("Digite: ")

      if resposta4 == '1': #CADASTRO DE MODALIDADE
            nome = input("Nome da Modalidade que Deseja Cadastrar: ")
            duracao = input("Duração de Tempo: ")

            comando = f'INSERT INTO modalidades (nome, duracao) VALUES ("{nome}","{duracao}")'

            cursor.execute(comando)
            conexao.commit()  # editar banco de dados
            print("CADASTRO REALIZADO COM SUCESSO!!!")
      if resposta4 == '2':  # ATUALIZAR CADASTRO MODALIDADES
            print("VOCÊ DESEJA ATUALIZAR")
            print(" 1 - Atualizar Nome\n 2 - Atualizar Duração")
            escolha = input("Digite: ")
            if escolha == '1':  # ATUALIZAR NOME
                  nome = input("Digite o Nome que deseja atualizar: ")
                  atualizar = input("Digite o novo Nome: ")
                  comando = f'UPDATE modalidades SET nome = "{atualizar}" WHERE nome = "{nome}"'
                  cursor.execute(comando)
                  conexao.commit()  # editar banco de dados
                  print("NOME ATUALIZADO")
            if escolha == '2':  # ATUALIZAR DURAÇÃO
                  duracao = input("Digite o Duração que deseja atualizar: ")
                  atualizar = input("Digite a nova Duração: ")
                  comando = f'UPDATE modalidades SET duracao = "{atualizar}" WHERE duracao = "{duracao}"'
                  cursor.execute(comando)
                  conexao.commit()  # editar banco de dados
                  print("DURAÇÃO ATUALIZADA")

      if resposta4 == '3': #CONSULTAR CADASTRO DE FUNCIONARIOS
            comando = f'SELECT*FROM modalidades'
            cursor.execute(comando)
            resultado = cursor.fetchall()  # ler o banco de dados
            print(resultado)
      if resposta4 == '4': #DELETAR CADASTRO
            nome = input("Digite aqui o Nome da Modalidade que deseja excluir: ")
            comando = f'DELETE FROM modalidades WHERE nome = "{nome}"'
            cursor.execute(comando)
            conexao.commit()  # editar banco de dados

cursor.close()
conexao.close()