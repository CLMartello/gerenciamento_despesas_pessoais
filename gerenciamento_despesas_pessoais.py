#criacao das contas iniciais do sistema e do banco de contas geral
conta0 = ["c6", 1, 23457, 0]
conta1 = ["Caixa", 1234, 11119872, 0]
banco_contas = [conta0, conta1]

#precisa reconhecer o modo data, pra isso vou importar
from datetime import date, time, datetime, timedelta

#criacao das transacoes = [data, tipo (receita ou despesa), categoria (salario, alimentacao, transporte, lazer, outros), descricao (livre), valor (float)]
#tipo = receita 1 e despesa 2
#categoria = salario 1, alimentacao 2, transporte 3, lazer 4 e outros 5
#descricao e string livre
#valor e float
#transacões da conta 0
t0 = [date(2023, 1, 1), 1, 1, "salario janeiro", float(3500.00)]
t1 = [date(2023, 1, 2), 2, 2, "mercado janeiro", float(557.20)]
t2 = [date(2023, 2, 23), 2, 3, "onibus estagio", float(5.43)]
t3 = [date(2023, 3, 11), 1, 5, "mesada da vovo", float(120.00)]
t4 = [date(2023, 3, 12), 2, 4, "cinema", float(54.00)]
t5 = [date(2023, 3, 12), 2, 2, "pipoca do cinema", float(22.00)]
t6 = [date(2023, 3, 28), 2, 5, "blusinha", float(99.99)]
t7 = [date(2023, 4, 7), 2, 3, "uber pass", float(25.99)]
t8 = [date(2023, 5, 13), 1, 5, "dinheiro da vovo", float(72.00)]
t9 = [date(2023, 6, 3), 2, 2, "chiclete", float(0.98)]

#transacções da conta 1
t10 = [date(2023, 1, 1), 1, 1, "salario janeiro", float(15000.00)]
t11 = [date(2023, 2, 2), 2, 2, "mercado", float(3546.94)]
t12 = [date(2023, 2, 6), 2, 4, "hotel", float(1499.00)]
t13 = [date(2023, 3, 17), 1, 5, "emprestimo pro tio", float(4999.99)]
t14 = [date(2023, 3, 19), 2, 3, "helicoptero", float(2010.00)]
t15 = [date(2023, 4, 22), 1, 1, "salario abril", float(15000.00)]
t16 = [date(2023, 5, 22), 2, 4, "maldivas", float(16473.44)]
t17 = [date(2023, 5, 31), 2, 2, "jantar", float(19.99)]
t18 = [date(2023, 6, 1), 1, 1, "salario junho", float(15000.00)]
t19 = [date(2023, 6, 5), 2, 2, "jantar", float(1578.00)]

#lista com todas as transações disponíveis, transacoes da conta 0 na lista 0 e transacoes da conta 1 na lista 1
banco_t = [[t0, t1, t2, t3, t4, t5, t6, t7, t8, t9], [t10, t11, t12, t13, t14, t15, t16, t17, t18, t19]]
              
#função inicial exibindo as opções de operações de maneira enumerada, pedindo ao usuario que escolha qual operação gostara de realizar
def inicio():
    print("Olá! As seguintes operações estão disponíveis:\n1.Cadastrar conta\n2.Remover conta\n3.Mesclar contas\n4.Extrato da conta\n5.Incluir transação\n6.Editar a última transação\n7.Transferir fundos\n8.Resumo das contas\n9.Resumo de receitas e despesas do mês\n10.Saldo geral dos últimos 6 meses\n11.Despesas separadas por categorias\n12.Sair do menu")
    a = input("Escolha o número da operação que você gostaria de realizar:")
    if teste_int(a) == True:
        a = int(a)
        return a


#funcao de menu que puxa as outras funções para executar cada uma das operações
def menu():
    a = inicio()
    if teste_int(a) == False or a == None:
        return chamada_menu()
    if a == 1:
        cadastrar()
    if a == 2:
        remover()
    if a == 3:
        mesclar()
    if a == 4:
        extrato()
    if a == 5:
        incluir_transacao()
    if a == 6:
        editar_transacao()
    if a == 7:
        transferir_fundos()
    if a == 8:
        resumo_contas()
    if a == 9:
        receitas_despesas()
    if a == 10:
        saldo_semestre()
    if a == 11:
        categorias()
    if a == 12:
        print("Obrigada por usar o sistema de gerenciamento de despesas pessoais.")
        return
    if 1 > a or a > 12:
        print("Essa não é uma opção disponível. Escolha uma opção válida.")
        return chamada_menu()

#funcao para exibir as contas de maneira ordenada para poder usar a selecao delas depois
def mostrar_contas():
    index = 0
    if banco_contas == []:
        print("Você não possui nenhuma conta cadastrada.")
        return chamada_menu()
    for conta in banco_contas:
        print(index, "Banco:", conta[0], "\tAgência: %04d" % conta[1], "\tConta: %010d" % conta[2], "\tSaldo: %.2f" % saldo_conta(index))
        index += 1


#funcao para mostra as transacoes dentro de listas
def mostrar_transacoes(lista):
    for t in lista:
        if t[1] == 1 and t[2] == 1:
            print("Data:", t[0].strftime("%d/%m/%Y"), "\tTipo: Receita", "\tCategoria: Salário", "\tDescrição:", t[3], "\tValor: %.2f" % t[4])
        if t[1] == 1 and t[2] == 5:
            print("Data:", t[0].strftime("%d/%m/%Y"), "\tTipo: Receita", "\tCategoria: Outros", "\tDescrição:", t[3], "\tValor: %.2f" % t[4])
        if t[1] == 2 and t[2] == 2:
            print("Data:", t[0].strftime("%d/%m/%Y"), "\tTipo: Despesa", "\tCategoria: Alimentação", "\tDescrição:", t[3], "\tValor: %.2f" % t[4])         
        if t[1] == 2 and t[2] == 3:
            print("Data:", t[0].strftime("%d/%m/%Y"), "\tTipo: Despesa", "\tCategoria: Transporte", "\tDescrição:", t[3], "\tValor: %.2f" % t[4])         
        if t[1] == 2 and t[2] == 4:
            print("Data:", t[0].strftime("%d/%m/%Y"), "\tTipo: Despesa", "\tCategoria: Lazer", "\tDescrição:", t[3], "\tValor: %.2f" % t[4])         
        if t[1] == 2 and t[2]== 5:
            print("Data:", t[0].strftime("%d/%m/%Y"), "\tTipo: Despesa", "\tCategoria: Outros", "\tDescrição:", t[3], "\tValor: %.2f" % t[4])         


#funcao para mostrar uma transacao isolada
def mostrar_trans_unica(t):
    if t[1] == 1 and t[2] == 1:
            print("Data:", t[0].strftime("%d/%m/%Y"), "\tTipo: Receita", "\tCategoria: Salário", "\tDescrição:", t[3], "\tValor: %.2f" % t[4], end = "")
    if t[1] == 1 and t[2] == 5:
            print("Data:", t[0].strftime("%d/%m/%Y"), "\tTipo: Receita", "\tCategoria: Outros", "\tDescrição:", t[3], "\tValor: %.2f" % t[4], end = "")
    if t[1] == 2 and t[2] == 2:
            print("Data:", t[0].strftime("%d/%m/%Y"), "\tTipo: Despesa", "\tCategoria: Alimentação", "\tDescrição:", t[3], "\tValor: %.2f" % t[4], end = "")         
    if t[1] == 2 and t[2] == 3:
            print("Data:", t[0].strftime("%d/%m/%Y"), "\tTipo: Despesa", "\tCategoria: Transporte", "\tDescrição:", t[3], "\tValor: %.2f" % t[4], end = "")         
    if t[1] == 2 and t[2] == 4:
            print("Data:", t[0].strftime("%d/%m/%Y"), "\tTipo: Despesa", "\tCategoria: Lazer", "\tDescrição:", t[3], "\tValor: %.2f" % t[4], end = "")         
    if t[1] == 2 and t[2]== 5:
            print("Data:", t[0].strftime("%d/%m/%Y"), "\tTipo: Despesa", "\tCategoria: Outros", "\tDescrição:", t[3], "\tValor: %.2f" % t[4], end = "")  


#função extra para escolher uma opção de conta dentre as disponíveis
def conta():
    print("Abaixo estão as contas cadastradas:")
    mostrar_contas()
    x = len(banco_contas)
    a = input("Digite o número da conta na qual você deseja realizar a operação:")
    if teste_int(a) == False:
        return
    a = int(a)
    for n in range(x):
        if n == a:
            return a
    if n != a:
        print("Essa não é uma opção válida. Operação cancelada.")
        return chamada_menu()

def chamada_menu():
    input("Aperte qualquer tecla para continuar:\n")
    menu()

#FUNCIONALIDADE 1 - CADASTRAR CONTA
#função para cadastrar nova conta, precisando prover nome do banco e numeros da agencia e da conta
def cadastrar():
    print("Você irá cadastrar uma nova conta, tenha em mãos o nome do banco e os números da agência e da conta bancária.")
    banco = input("Insira o nome do banco da nova conta:")
    if type(banco) != str or banco == '':
        print("Essa não é uma opção válida. Operação cancelada.")
        return chamada_menu()
    agencia = input("Insira o número da agência:")
    if teste_int(agencia) == False:
        return chamada_menu()
    agencia = int(agencia)
    if agencia > 10000:
        print("O número da agência deve ser composta de no máximo quatro dígitos. Operação cancelada.")
        return chamada_menu()
    conta = input("Insira o número da conta:")
    if teste_int(conta) == False:
        return chamada_menu()
    conta = int(conta)
    if conta > 10000000000:
        print("O número da agência deve ser composta de no máximo dez dígitos. Operação cancelada.")
        return chamada_menu()
    saldo = 0
    conta_nova = [banco, agencia, conta, saldo]
    banco_contas.append(conta_nova)
    banco_t.append([])
    print("Sua nova conta foi cadastrada:\n", "Banco:", conta_nova[0], "\tAgência: %04d" % conta_nova[1], "\tConta: %010d" % conta_nova[2], "\tSaldo: %.2f" % saldo)
    return chamada_menu()


#FUNCIONALIDADE 1 - REMOVER CONTA
#função para remover uma conta que existe no banco de contas
def remover():
    print("Você irá remover uma conta.")
    a = conta()
    if a == None:
        return chamada_menu()
    print("Tem certeza que deseja remover a conta", a, "? Todos os dados serão excluídos.")
    b = input("Digite '1' para confirmar e '2' para cancelar a operação.")
    if teste_int(b) == False:
        return chamada_menu()
    if b == None:
        print("Essa não é uma opção válida. Operação cancelada.")
        return chamada_menu()
    a = int(a)
    b = int(b)
    if b == 1:
        del banco_contas[a]
        del banco_t[a]
        print("A conta", a, "e suas transações foram removidas.")
        print("Você possui as seguintes contas:")
        mostrar_contas()   
    if b == 2:
        print("Operação de remoção da conta", a, "cancelada.")
        print("Você possui as seguintes contas:")
        mostrar_contas()
    if b != 1 and b != 2:
        print("Você deve escolher uma opção válida. Operação cancelada.")
        return chamada_menu()
    return chamada_menu()
 

#FUNCIONALIDADE 1 - MESCLAR CONTAS
#função para unificar as transações de duas contas e ordenar essas transações por data
def mesclar():
    print("Você deseja mesclar duas contas.")
    a = conta()
    if teste_int(a) == False:
        return chamada_menu()
    b = conta()
    if teste_int(b) == False:
        return chamada_menu()
    if a == b:
        print("Você deve escolher duas contas diferentes. Operação cancelada.")
        return chamada_menu()
    mesclar_t = []
    a = int(a)
    b = int(b)
    mesclar_t = banco_t[a]+banco_t[b]
    mesclar_t.sort()
    print("Parabéns! Você mesclou as contas", a, "e", b, "com sucesso. Abaixo estão todas as transações das contas mescladas.")
    mostrar_transacoes(mesclar_t)
    return chamada_menu()


#função extra para testar se o valor adicionado corresponde ao tipo exigido - float para valor da transação
def teste_float(valor):
    if valor is None:
        print("Essa não é uma opção válida. Operação cancelada.")
        return False
    try:
        float(valor)
        return True
    except:
        print("Essa não é uma opção válida. Operação cancelada.")
        return False


#função extra para testar se a opção de entrada corresponde ao tipo exigido - número inteiro para opções de escolha de conta, escolha de tipo de transação e escolha de categoria de transação
def teste_int(entrada):
    if entrada is None:
        print("Essa não é uma opção válida. Operação cancelada.")
        return False
    try:
        int(entrada)
        return True
    except:
        print("Essa não é uma opção válida. Operação cancelada.")
        return False


#funcao extra para verificar a entrada de data
def data():
    x = input("Digite o ano da sua transação usando 4 dígitos:")
    if teste_int(x) == False:
        print("Está não é uma opção válida. Operação cancelada.")
        return chamada_menu()
    x = int(x)
    if x < 1823 or x > 2123:
        print("O ano precisa ser um número entre 1823 e 2123")
        return chamada_menu()
    y = input("Digite o mês da sua transação:")
    if teste_int(y) == False:
        print("Está não é uma opção válida. Operação cancelada.")
        return chamada_menu()
    y = int(y)
    if y > 12 or y < 1:
        print("O mês precisa ser um número entre 1 e 12.")
        return chamada_menu()
    z = input("Digite o dia da sua transação:")
    if teste_int(z) == False:
        print("Está não é uma opção válida. Operação cancelada.")
        return chamada_menu()
    z = int(z)
    if z > 31 or z < 1:
        print("O dia precisa ser um número entre 1 e 31.")
        return chamada_menu()
    b = date(x, y, z)
    return b
            

#função extra para escolher o tipo de transação, receita ou despesa 
def tipo():
    a = input("Digite 1 se está for uma transação é de receita e 2 se for uma transação de despesa:")
    if teste_int(a) == False:
        return chamada_menu()
    a = int(a)
    if a != 1 and a != 2:
        print("Esta não é uma opção válida. Operação cancelada.")
        return chamada_menu()
    return a


#função extra para escolher a categoria da transação, com opções exclusivas se for tipo receita ou se for tipo despesa
def categoria(x):
    if x == 1:
        a = input("Escolha uma categoria para sua transação de receita:\n1-Salário\\n5-Outros\n")
        if teste_int(a) == False or a == None:
            return chamada_menu()
        a = int(a)
        if a != 1 and a != 5:
            print("Esta não é uma opção válida. Operação cancelada.")
            return chamada_menu()
        return a
    if x == 2:
        a = input("Escolha uma categoria para sua transação de despesa:\n2-Alimentação\n3-Transporte\n4-Lazer\n5-Outros\n")     
        if teste_int(a) == False or a == None:
            return chamada_menu()
        a = int(a)
        if a < 2 or a > 5:
            print("Esta não é uma opção válida. Operação cancelada.")
            return chamada_menu()
        return a            


#função extra para escolher o valor da transação
def valor():
    a = input("Adicione um valor para sua transação.")
    if teste_float(a) == False or a == None:
        return chamada_menu()
    a = float(a)
    if a < 0:
        return chamada_menu()
    return a

def extrato():
    valor = 0
    print("Você deseja saber o extrato de uma conta.")
    a = conta()
    if teste_int(a) == False or a == None:
        return chamada_menu()
    a = int(a)
    t_conta = banco_t[a]
    if t_conta == []:
        print("Essa conta não possui transações.")
        return chamada_menu()
    for t in t_conta:
        if t[1] == 1:
            valor = valor + t[4]
            mostrar_trans_unica(t)
            print("\tSaldo: %.2f" % valor)
        if t[1] == 2:
            valor = valor - t[4]
            mostrar_trans_unica(t)
            print("\tSaldo: %.2f" % valor)
    return chamada_menu()
    

#FUNCIONALIDADE 2 - INCLUIR TRANSAÇÃO
#função para incluir uma transação em alguma conta escolhida
def incluir_transacao():
    nova_t = []
    print("Você deseja incluir uma transação.")
    a = conta()
    if teste_int(a) == False or a == None:
        return chamada_menu()
    b = tipo()
    if teste_int(b) == False or b == None:
        return chamada_menu()
    c = categoria(b)
    if teste_int(c) == False or c == None:
        return chamada_menu()
    d = input("Escreve brevemente uma descrição para sua transação:")
    if d == "":
        print("Essa não é uma opção válida. Operação cancelada.")
        return chamada_menu()
    e = valor()
    if teste_float(e) == False or e == None:
        return chamada_menu()
    nova_t = [date.today(), b, c, d, e]
    t_conta = banco_t.pop(a)
    t_conta.append(nova_t)
    t_conta.sort()
    banco_t.insert(a, t_conta)
    print("Nova transação adicionada:")
    mostrar_trans_unica(nova_t)
    return chamada_menu()


#função extra especifica para editar a transação
def editar(x, a, b):
    ultima_t = []
    t_conta = banco_t.pop(x)
    t_conta.sort()
    ultima_t = t_conta.pop(-1)
    del ultima_t[a]
    ultima_t.insert(a, b)
    print("Você alterou a sua última transação.")
    mostrar_trans_unica(ultima_t)
    t_conta.append(ultima_t)
    banco_t.insert(x, t_conta)


#FUNCIONALIDADE 2 - EDITAR A ÚLTIMA TRANSAÇÃO
#função para escolher o que editar na última transação
def editar_transacao():
    t_conta = []
    x = conta()
    if teste_int(x) == False or x == None:
        return chamada_menu()
    x = int(x)
    t_conta = banco_t[x]
    if t_conta == []:
        print("Essa conta não possui transações.")
        return chamada_menu()
    t_conta.sort()
    print("Você deseja editar a última transação adicionada. A transação é a seguinte:")
    mostrar_trans_unica(t_conta[-1])
    print("\nVocê pode editar os seguintes itens:\n0-Data\n1-Tipo de transação\n2-Categoria da transação\n3-Descrição da transação\n4-Valor da transação")
    a = input("Digite o número corresponte ao dado que você deseja editar:")
    if teste_int(a) == False or a == None:
        return chamada_menu()
    a = int(a)
    if a == 0:
        b = data()
        editar(x, a, b)
    if a == 1:
        b = tipo()
        editar(x, a, b)
        if b == 1:
            print("Você precisa alterar também a categoria.")
            c = categoria(1)
            editar(x, 2, c)
        if b == 2:
            print("Você precisa alterar também a categoria.")
            c = categoria(2)
            editar(x, 2, c)
    if a == 2:
        b = categoria(t_conta[-1][1])
        editar(x, a, b)
    if a == 3:
        b = input("Escreve brevemente uma nova descrição para sua transação:")
        editar(x, a, b)
    if a == 4:
        b = valor()
        editar(x, a, b)
    return chamada_menu()
    

#funcao extra para adição de uma transação pelo sistema
def auto_transacao(a, b, c, d, e):
    nova_t = [date.today(), b, c, d, e]
    t_conta = banco_t.pop(a)
    t_conta.append(nova_t)
    t_conta.sort()
    banco_t.insert(a, t_conta)
    mostrar_trans_unica(nova_t)


#FUNCIONALIDADE 2 - TRANSFERÊNCIA DE FUNDOS
#função para transferir fundos de uma conta para a outra
def transferir_fundos():
    print("Você irá transferir fundos de uma conta para outra.")
    a = conta()
    if teste_int(a) == False or a == None:
        return chamada_menu()
    a = int(a)
    b = conta()
    if teste_int(b) == False or b == None:
        return chamada_menu()
    b = int(b)
    if b == a:
        print("Você precisa escolher uma conta diferente para transferir fundos. Operação cancelada.")
        return chamada_menu()
    c = valor()
    if teste_float(c) == False or c == None:
        return chamada_menu()
    c = float(c)
    if saldo_conta(a) >= c:
        print("Sua transferência foi realizada com sucesso")
        print("Transação de saque:")
        auto_transacao(a, 2, 5, "saque", c)
        print("\nTransação de depósito:")
        auto_transacao(b, 1, 5, "depósito", c)
        print("\nSuas contas possuem os seguintes saldos:")
        mostrar_contas()
    else:
        print("O valor escolhido é superior ao limite da conta.")
    return chamada_menu()


#funcao extra para calcular saldo das contas
def saldo_conta(x):
    t_conta = banco_t[x]
    valor = 0
    if t_conta == []:
        return 0
    for t in t_conta:
        if t[1] == 1:
            valor += t[4]
        if t[1] == 2:
            valor -= t[4]        
    return valor


#FUNCONALIDADE 3 - RESUMO DAS CONTAS
#funcao para mostrar o resumo das contas com o saldo ao lado e saldo total
def resumo_contas():
    a = len(banco_contas)
    valor = 0
    saldo_total = 0
    for x in range(a):
        t_conta = banco_t[x]
        for t in t_conta:
            if t[1] == 1:
                valor += t[4]
            if t[1] == 2:
                valor -= t[4]
        print("A conta", banco_contas[x][0], "possui saldo de %.2f" % valor)
        saldo_total += valor
        valor = 0
    print("Seu saldo total é de %.2f" % saldo_total)
    return chamada_menu()

#FUNCIONALIDADE 3 - RECEITAS E DESPESAS DO MÊS ATUAL
#funcao para mostrar as receitas e despesas do mes atual
def receitas_despesas():
    a = len(banco_contas)
    banco_t_geral = []
    t_mes_atual = []
    r = 0
    d = 0
    for x in range(a):
        banco_t_geral += banco_t[x]
    for t in banco_t_geral:
        if "{}".format(t[0].month) == "{}".format(date.today().month):
            t_mes_atual.append(t)
    for t in t_mes_atual:
        if t[1] == 1:
            r += t[4]
        if t[1] == 2:
            d += t[4]
    print("A receita do mês atual foi de %.2f" % r, "reais. E a despesa do mês atual foi de %.2f" % d, "reais.")
    return chamada_menu()


#FUNCIONALIDADE 2 - SALDO DOS ÚLTIMOS 6 MESES
#funcao que calcula o saldo dos últimos 6 meses e demonstra mes a mes
def saldo_semestre():
    a = len(banco_contas)
    banco_t_geral = []
    valor = 0
    meses = []
    mes1 = int("{}".format(date.today().month))
    mes2 = (date.today() - timedelta(30))
    mes2 = int("{}".format(mes2.month))
    mes3 = (date.today() - timedelta(60))
    mes3 = int("{}".format(mes3.month))
    mes4 = (date.today() - timedelta(90))
    mes4 = int("{}".format(mes4.month))
    mes5 = (date.today() - timedelta(120))
    mes5 = int("{}".format(mes5.month))
    mes6 = (date.today() - timedelta(150))
    mes6 = int("{}".format(mes6.month))
    meses = [mes1, mes2, mes3, mes4, mes5, mes6]
    for x in range(a):
        banco_t_geral += banco_t[x]
    for n in meses:
        for t in banco_t_geral:
            if int("{}".format(t[0].month)) == n:
                if t[1] == 1:
                    valor += t[4]
                if t[1] == 2:
                    valor -= t[4]
        print("O saldo do mês", n, "é de %.2f" % valor, "reais.")
    return chamada_menu()


#FUNCIONALIDADE 3 - SEPARAÇÃO DAS DESPESAS PELAS CATEGORIAS
#funcao que separa todas as despesas por categorias
def categorias():
    despesas = []
    alimentacao = []
    transporte = []
    lazer = []
    outros = []
    alim = 0
    trans = 0
    laz = 0
    out = 0
    a = len(banco_contas)
    banco_t_geral = []
    for x in range(a):
        banco_t_geral += banco_t[x]    
    for t in banco_t_geral:
        if t[1] == 2:
            despesas.append(t)
    for d in despesas:
        if d[2] == 2:
            alim += d[4]
        if d[2] == 3:
            trans += d[4]
        if d[2] == 4:
            laz += d[4]
        if d[2] == 5:
            out += d[4]
    print("Suas despesas por categorias estão discriminadas abaixo.\nAlimentação:", alim,"reais.\nTransporte:", trans,"reais.\nLazer:", laz,"reais.\nOutros:", out,"reais.")
    return chamada_menu()

menu()
