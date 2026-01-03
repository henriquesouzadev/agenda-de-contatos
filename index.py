import msvcrt
import os

contatos = []

opcoes = [
  "1. Adicionar contato",
  "2. Lista de contatos",
  "3. Remover contato",
  "4. Marcar/desmarcar contato como favorito",
  "5. Editar contato",
  "6. Lista de contatos favoritos",
  "7. Sair"
]

indice = 0

def limpar_console():
  os.system('cls')

def menu():
  limpar_console()

  print("\nMenu do gerenciador de tarefas: ")
  
  for i, opcao in enumerate(opcoes):
    if i == indice:
      print(f"\033[32m> {opcao}\033[0m")
    else:
      print(f"  {opcao}")

def aguardar_enter():
  print("\nPressione Enter para continuar...")

  while True:
    tecla = msvcrt.getch()
    if tecla == b'\r':
      break

def adicionar_contato():
  nome = input("\nDigite o nome do contato: ")
  telefone = input("\nDigite o telefone do contato: ")
  email = input("\nDigite o e-mail do contato: ")
  favorito = input("\nDeseja salvar o contato como favorito? (s/n): ").lower()

  if favorito not in ('s', 'n'):
      print("Opção inválida.")
      aguardar_enter()
  else: 
    favoritoValor = True if favorito == 's' else False

    contatos.append({
      'nome': nome,
      'telefone': telefone,
      'email': email,
      'favorito': favoritoValor,
    })
  
def mostrar_contatos():
  limpar_console()

  print("\n/==== Agenda de contatos ====/")
  
  if not contatos:
    print("Nenhum contato na agenda")
  else:
    print(f"{'ID': <4} {'Nome': <20} {'Telefone': <20} {'E-mail': <30} {'Favorito': <10}") 
    for i, contato in enumerate(contatos, start=1):
      print(f"{i: <4} {contato['nome']: <20} {contato['telefone']: <20} {contato['email']: <30} {'Sim' if contato['favorito'] else 'Não' : <10}") 

  aguardar_enter()

def contatos_favoritos():
  limpar_console()

  favoritos = [contato for contato in contatos if contato['favorito']]

  if not favoritos:
    print("Nenhum favorito encontrado")
  else:
    print("\n/==== Contatos favoritos ====/")

    print(f"{'ID': <4} {'Nome': <20} {'Telefone': <20} {'E-mail': <30}") 
    for i, contato in enumerate(favoritos):
      print(f"{i: <4} {contato['nome']: <20} {contato['telefone']: <20} {contato['email']: <30}")
    
  aguardar_enter()

def deletar_contato():
  indice_contato = int(input("\nDigite o ID do contato que deseja remover: "))
  if indice_contato < 1 or indice_contato > len(contatos):
    print("Contato não encontrado.")
  else:
    contato_removido = contatos.pop(indice_contato - 1)
    print(f"Contato {contato_removido['nome']} removido com sucesso.")

def trocar_favorito():
  indice_contato = int(input("\nDigite o ID do contato que deseja adicionar aos favoritos: "))
  if indice_contato < 1 or indice_contato > len(contatos):
    print("Contato não encontrado.")
  else:
    favorito = input("Deseja marcar/desmarcar como favorito? (s/n): ").lower()
    if favorito not in ('s', 'n'):
      print("Opção inválida.")
      aguardar_enter()
    else: 
      contatos[indice_contato -1]['favorito'] = True if favorito == 's' else False
      print("\nContato atualizado com sucesso!")
  
def editar_contato():
  indice_contato = int(input(f"\nDigite o ID do contato que deseja editar: "))
  contato = contatos[indice_contato -1]

  if indice_contato < 1 or indice_contato > len(contatos):
    print("Contato não encontrada")
  else: 
    nome = input("\nDigite o nome do contato: ")
    telefone = input("\nDigite o telefone do contato: ")
    email = input("\nDigite o e-mail do contato: ")
    favorito = input("\nDeseja salvar o contato como favorito? (s/n): ").lower()

    if nome:
      contato['nome'] = nome
    
    if telefone:
      contato['telefone'] = telefone

    if email:
      contato['email'] = email
    
    if favorito:
      contato['favorito'] = True if favorito == 's' else False

    print("\nContato atualizado com sucesso!")

while True:
  menu()
  tecla = msvcrt.getch()

  if tecla == b'\xe0':
    tecla = msvcrt.getch()

    if tecla == b'H':
      indice = (indice - 1) % len(opcoes)
    elif tecla == b'P':
      indice = (indice + 1) % len(opcoes)
  
  elif tecla == b'\r':
      opcao = indice + 1

      if opcao is not None:
        if opcao == 1:
          adicionar_contato()
        if opcao == 2:
          mostrar_contatos()
        if opcao == 3:
          deletar_contato()
        if opcao == 4:
          trocar_favorito()
        if opcao == 5:
          editar_contato()
        if opcao == 6:
          contatos_favoritos()
        if opcao == 7:
          print("Fechando o programa...")
          break

    