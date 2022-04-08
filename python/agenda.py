'''Faça um algoritmo que mostre o seguinte menu:
1 - LISTAR (nomes e telefones)
2 - BUSCAR (mostrar telefone a partir do nome)
3 - ADICIONAR  (adicionar nome e telefone)
4 - ALTERAR (buscar um nome e alterar telefone)
5 - LISTAR TODOS OS CADASTRADOS (lista todos os nomes cadastrado)
6 - SAIR (ao escolhe essa função sai do programa)
O programa deve rodar num loop sempre que mostrar algo ele retorna ao menu.
Dica: esse programa usa tudo que aprendemos até agora (Estrutura de decisão, estrutura de repetição, dicionário)
Anexar documento contendo o código com a extensão py ou txt!'''

lista = [{'nome':'alice','telefone':'40028922'},
         {'nome':'ana','telefone':'43428922'},
         {'nome':'alex','telefone':'40028182'}]

while True:
    print("1 - LISTAR (nomes e telefones)")
    print("2 - BUSCAR (mostrar telefone a partir do nome)")
    print("3 - ADICIONAR  (adicionar nome e telefone)") # c
    print("4 - ALTERAR (buscar um nome e alterar telefone)")
    print("5 - LISTAR TODOS OS CADASTRADOS (lista todos os nomes cadastrado)")#c
    print("6 - SAIR (ao escolhe essa função sai do programa)")

    opcao = int(input("digite uma opção de 1 a 6 :  "))

    if opcao == 1:
        print("listar")
        if len(lista) > 0:
            for i, contato in enumerate(lista):
                print("contato {}:".format(i+1))
                print(f"nome: {contato['nome']}")
                print(f"telefone: {contato['telefone']}")


    elif opcao == 2:
        print("buscar")
        nome = input("nome: ")
        for contato in lista:
            if contato['nome'] == nome:
                print(f"nome: {contato['nome']}")
                print(f"telefone: {contato['telefone']}")
            else:
              print("nao existe esse contato")

    elif opcao == 3:
        print("adicionar")
        nome = input("nome : ")
        telefone = input("telefone :  ")
        contato = {"nome":nome,"telefone":telefone}
        lista.append(contato)
        print("cadastro realizado")


    elif opcao == 4:
        print("alterar")
        nome = input("nome: ")
        for contato in lista:
            if contato['nome'] == nome:
                print(f"telefone: {contato['telefone']}")
                contato['telefone'] = int(input("novo telefone:  "))
            else:
                print("nao existe esse contato")


    elif opcao == 5:
            print("\n listar tds contatos:")
            for contato in lista:
                print(f"nome: {contato['nome']}")
                print(f"telefone: {contato['telefone']}")


    elif opcao == 6:
            break
    else:
     print("opção invalida")


