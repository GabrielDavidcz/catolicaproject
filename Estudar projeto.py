from Functions import *
cadastro = importar_usuarios()
naopode = '!#$%¨&*()-_+=[]'
autenticado = False
usuario_logado = None
caronas = []
count = len(cadastro) + 1

while True:
    print('----------------             BABLACAR         -------------')
    print('----------------  [1] Cadastrar Novo Usuario  -------------')
    print('----------------  [2]         Login           -------------')
    print('----------------  [3]          Sair           -------------')
    op = input('Digite uma das opções acima: ')
    if op in ['1', '2', '3']:
        op = int(op)
    else:
        print("Por favor, digite apenas 1, 2 ou 3.")
    if op == 1:
        cadastrar_usuarios(naopode, cadastro, count)
        count += 1
    elif op == 2:
        usuario_logado = fazer_login(cadastro)
        if usuario_logado:
            autenticado = True
            while True:
                print('\n------------------- Menu de Caronas -------------------')
                if usuario_logado['tipo'].upper() == 'M':
                    print('[1] Cadastrar Carona')
                    print('[2] Ver Caronas Disponíveis')
                    print('[3] Buscar Carona')
                    print('[4] Reservar Vaga em Carona')
                    print('[5] Voltar')
                    print('[6] Cancelar cadastro de carona')
                    print('[7] Mostrar Detalhes de Carona')
                    print('[8] Mostrar Caronas Cadastradas')
                    print('[9] Trocar senha da conta')
                    print('[10] Trocar email da conta')
                    print('[11] Relatório de Totalizadores')
                else:
                    print('[1] Ver Caronas Disponíveis')
                    print('[2] Buscar Carona')
                    print('[3] Reservar Vaga em Carona')
                    print('[4] Voltar')
                    print('[5] Cancelar reserva')
                    print('[6] Mostrar Detalhes de Carona')
                    print('[7] Trocar senha da conta')
                    print('[8] Trocar email da conta')
                op_menu = int(input('Escolha uma opção: '))
                if usuario_logado['tipo'].upper() == 'M':
                    if op_menu == 1:
                        print(f'Cadastro de carona ---- {usuario_logado["nome"]} ----')
                        origem = input('Digite o local de origem: ').strip()
                        destino = input('Digite o destino: ').strip()
                        data = input('Digite a data da carona (ex: DD/MM/AAAA): ').strip()
                        horario = input('Digite o horário da carona (ex: HH:MM): ').strip()
                        vagas = int(input('Digite a quantidade de vagas: ').strip())
                        valor_vaga = float(input('Digite o valor por vaga: ').strip())
                        carona = {
                            'motorista': usuario_logado['nome'],
                            'email_motorista': usuario_logado['email'],
                            'origem': origem,
                            'destino': destino,
                            'data': data,
                            'horario': horario,
                            'vagas': vagas,
                            'valor_vaga': valor_vaga,
                            'reservas': []
                        }
                        caronas.append(carona)
                        print('Carona cadastrada com sucesso!')
                    elif op_menu == 2:
                        carona_disponiveis(caronas)
                    elif op_menu == 3:
                        print('------  MENU DE BUSCA  ------')
                        busca_origem = input('Digite a origem desejada: ').lower()
                        busca_destino = input('Digite o destino desejado: ').lower()
                        caronas_disponiveis = []
                        for c in caronas:
                            if c['vagas'] > 0:
                                caronas_disponiveis.append(c)
                        encontrou = False
                        for carona in caronas_disponiveis:
                            if carona['origem'].lower() == busca_origem and carona['destino'].lower() == busca_destino:
                                print("\n--- Carona Encontrada ---")
                                print(f"Motorista: {carona['motorista']}")
                                print(f"Origem: {carona['origem']}")
                                print(f"Destino: {carona['destino']}")
                                print(f"Data: {carona['data']}")
                                print(f"Horário: {carona['horario']}")
                                print(f"Vagas disponíveis: {carona['vagas']}")
                                print(f"Valor por vaga: R$ {carona['valor_vaga']:.2f}")
                                encontrou = True
                        if not encontrou:
                            print('Nenhuma carona encontrada.')
                    elif op_menu == 4:
                        print('------ Reservar Vaga em Carona ------')
                        email_motorista = input('Digite o e-mail do motorista: ').strip().lower()
                        data_carona = input('Digite a data da carona (ex: DD/MM/AAAA): ').strip()
                        carona_encontrada = reservar_carona(email_motorista, data_carona, caronas, usuario_logado)
                        if carona_encontrada:
                            print('Reseva feita com sucesso!')
                    elif op_menu == 5:
                        print('Voltando ao menu principal...')
                        break
                    elif op_menu == 6:
                        cancelar_cadastro(caronas, usuario_logado)
                    elif op_menu == 7:
                        print('------ Detalhes da Carona ------')
                        email_motorista = input('Digite o e-mail do motorista: ').strip().lower()
                        data_carona = input('Digite a data da carona (DD/MM/AAAA): ').strip()
                        carona_encontrada = detalhes_da_carona(email_motorista, data_carona, caronas)
                    elif op_menu == 8:
                        print('------ Mostrar Caronas Cadastradas ------')
                        caronas_disponiveis1 = []
                        for c in caronas:
                            if c['vagas'] > 0:
                                caronas_disponiveis1.append(c)
                        if len(caronas_disponiveis1) == 0:
                            print('Nenhuma carona disponível no momento.')
                        else:
                            for carona in caronas_disponiveis1:
                                print("\n--- Carona ---")
                                print(f"Motorista: {carona['motorista']}")
                                print(f"Origem: {carona['origem']}")
                                print(f"Destino: {carona['destino']}")
                                print(f"Data: {carona['data']}")
                                print(f"Horário: {carona['horario']}")
                                print(f"Vagas disponíveis: {carona['vagas']}")
                                print(f"Valor por vaga: R$ {carona['valor_vaga']:.2f}")
                                print(f"Passageiros: {carona['reservas']}")
                    elif op_menu == 9:
                        print('------ Alterar Senha ------')
                        senha_atual = input('Digite sua senha atual: ').strip()
                        if usuario_logado['senha'] == senha_atual:
                            nova_senha = input('Digite a nova senha: ').strip()
                            usuario_logado['senha'] = nova_senha
                            print("Senha alterada com sucesso!")
                        else:
                            print("Senha atual incorreta.")
                    elif op_menu == 10:
                        print('------ Alterar Email ------')
                        email_atual = input('Digite seu e-mail atual: ').strip().lower()
                        if usuario_logado['email'] == email_atual:
                            novo_email = input('Digite o novo email: ').strip().lower()
                            usuario_logado['email'] = novo_email
                            print("E-mail alterado com sucesso!")
                        else:
                            print("E-mail atual incorreto. Tente novamente.")
                    elif op_menu == 11:
                        relatorio_totalizador(caronas, usuario_logado)

                else:  
                    if op_menu == 1:
                        carona_disponiveis(caronas)
                    elif op_menu == 2:
                        print('------  MENU DE BUSCA  ------')
                        busca_origem = input('Digite a origem desejada: ').lower()
                        busca_destino = input('Digite o destino desejado: ').lower()
                        caronas_disponiveis = []
                        for c in caronas:
                            if c['vagas'] > 0:
                                caronas_disponiveis.append(c)
                        encontrou = False
                        for carona in caronas_disponiveis:
                            if carona['origem'].lower() == busca_origem and carona['destino'].lower() == busca_destino:
                                print("\n--- Carona Encontrada ---")
                                print(f"Motorista: {carona['motorista']}")
                                print(f"Origem: {carona['origem']}")
                                print(f"Destino: {carona['destino']}")
                                print(f"Data: {carona['data']}")
                                print(f"Horário: {carona['horario']}")
                                print(f"Vagas disponíveis: {carona['vagas']}")
                                print(f"Valor por vaga: R$ {carona['valor_vaga']:.2f}")
                                encontrou = True
                        if not encontrou:
                            print('Nenhuma carona encontrada.')
                    elif op_menu == 3:
                        print('------ Reservar Vaga em Carona ------')
                        email_motorista = input('Digite o e-mail do motorista: ').strip().lower()
                        data_carona = input('Digite a data da carona (ex: DD/MM/AAAA): ').strip()
                        carona_encontrada = reservar_carona(email_motorista, data_carona, caronas, usuario_logado)
                        if carona_encontrada:
                            print('Reseva feita com sucesso!')
                    elif op_menu == 4:
                        print('Voltando ao menu principal...')
                        break
                    elif op_menu == 5:
                        print('------ Cancelar Reserva ------')
                        email = input('E-mail do motorista: ').lower()
                        data = input('Data da carona (DD/MM/AAAA): ')
                        confirmacao = input('Tem certeza que deseja cancelar esta reserva? (S/N): ').upper()
                        if confirmacao == 'S':
                            reserva_encontrada = False
                            for carona in caronas:
                                if carona['email_motorista'] == email and carona['data'] == data and usuario_logado['nome'] in carona['reservas']:
                                    reserva_encontrada = True
                                    carona['reservas'].remove(usuario_logado['nome'])
                                    carona['vagas'] += 1
                                    print('Reserva cancelada com sucesso!')
                                    break
                            if not reserva_encontrada:
                                print('Reserva não encontrada.')
                        else:
                            print('Operação cancelada pelo usuário.')
                    elif op_menu == 6:
                        print('------ Detalhes da Carona ------')
                        email_motorista = input('Digite o e-mail do motorista: ').strip().lower()
                        data_carona = input('Digite a data da carona (DD/MM/AAAA): ').strip()
                        carona_encontrada = detalhes_da_carona(email_motorista, data_carona, caronas)
                    elif op_menu == 7:
                        print('------ Alterar Senha ------')
                        senha_atual = input('Digite sua senha atual: ').strip()
                        if usuario_logado['senha'] == senha_atual:
                            nova_senha = input('Digite a nova senha: ').strip()
                            usuario_logado['senha'] = nova_senha
                            print("Senha alterada com sucesso!")
                        else:
                            print("Senha atual incorreta.")
                    elif op_menu == 8:
                        print('------ Alterar Email ------')
                        email_atual = input('Digite sua senha atual: ').strip()
                        if usuario_logado['email'] == email_atual:
                            novo_email = input('Digite o novo email: ').strip()
                            usuario_logado['email'] = novo_email
                            print("email alterado com sucesso!")
                        else:
                            print("email atual incorreto.")

    elif op == 3:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")



















