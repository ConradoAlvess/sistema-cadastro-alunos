alunos = []

def cadastroAlunos ():
    nome = input("Digite o nome do aluno: ")
    ano = input("Digite a serie do aluno: ")
    senha = input("Digite a senha do aluno: ")
    

    for u in alunos:
        if u["nome"] == nome:
            print("Aluno já existe")
            return

    alunos.append({"nome": nome, "ano": ano, "senha": senha, "notas": []})
    print("Cadastro do aluno realizado com sucesso!")

def login():
    nome = input("Digite o nome do aluno: ")
    senha = input("Digite a senha do aluno: ")

    for u in alunos:
        if u["nome"] == nome and u["senha"] == senha:
            print(f"Login do aluno {nome} realizado com sucesso!")
            return True
        
    print("Login invalído! Verefique nome e a senha.")
    return False

def menu_logado():
    while True:
        print("\n1 - Ver alunos")
        print("\n2 - Calcular nota")
        print("\n3 - Sair")

        op = input("Escolha: ")

        if op == "1":
            if len(alunos) == 0:
                print("Nenhum aluno cadastrado.")
            else:
                for u in alunos:
                    print(f"Nome: {u['nome']} | Ano/Série: {u['ano']} | Notas: {u['notas']}")
        
        elif op == "2":
            nome_aluno = input("Digite o nome do aluno: ")

            aluno_encontrado = None
            for u in alunos:
                if u["nome"] == nome_aluno:
                    aluno_encontrado = u
                    break

            if aluno_encontrado is None:
                print("Aluno não encontrado.")
            else:
                nota1 = float(input("Digite a primeira nota do aluno: "))
                nota2 = float(input("Digite a segunda nota do aluno: "))
                nota3 = float(input("Digite a terceira nota do aluno: "))
                aluno_encontrado["notas"] = [nota1, nota2, nota3]
                
                total = (nota1 + nota2 + nota3)/3
                
                print(f"Média do aluno: {total:.2f}")

                if total >= 6:
                    print(f"Aluno {aluno_encontrado['nome']} aprovado!")
                else:
                    print(f"Aluno {aluno_encontrado['nome']} reprovado!")
        
        elif op == "3":
            break
        else:
            print("Opção invalida")

def sistema():
    while True:
        print("\n1 - Cadastrar")
        print("\n2 - Login")
        print("\n3 - Sair")

        op = input("Escolha: ")

        if op == "1":
            cadastroAlunos()
        elif op == "2":
          if  login():
                menu_logado()
        elif op == "3":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção invalida!")

sistema()
