# -*- coding: utf8 -*-
import sqlite3

class BancoDados:
    def __init__(self, database):
        # Inicialização da conexão com o banco de dados
        self.conexao = sqlite3.connect(database)
        # Criação de um cursor para executar comandos SQL
        self.cursor = self.conexao.cursor()
        
        # Verifica se as tabelas já existem no banco de dados
        if not self.verificar_tabelas():
            # Se as tabelas não existirem, cria as tabelas
            self.criarTabela()

    def __del__(self):
        # Método para fechar a conexão quando o objeto for destruído
        self.conexao.close()

    def verificar_tabelas(self):
        # Método para verificar se as tabelas já existem no banco de dados
        # Consulta para verificar a existência das tabelas
        sql = "SELECT name FROM sqlite_master WHERE type='table'"
        # Executa a consulta
        self.cursor.execute(sql)
        # Obtém o resultado da consulta
        tabelas = self.cursor.fetchall()
        # Verifica se as tabelas necessárias existem
        tabelas_necessarias = {'lsClientes', 'lsFornecedores', 'lsUsuario', 'lsLoja', 'lsProdutos'}
        return set([tabela[0] for tabela in tabelas]) == tabelas_necessarias

    def __del__(self):
        # Método para fechar a conexão quando o objeto for destruído
        self.conexao.close()

    def cadastro(self, tabela, args):
        # Método para inserir novos registros na tabela
        colunas = ', '.join(args.keys())
        valores = tuple(args.values())
        placeholders = ', '.join(['?'] * len(args))
        # Construção do comando SQL para inserção
        sql = f"INSERT INTO {tabela} ({colunas}) VALUES ({placeholders})"
        # Execução do comando SQL
        self.cursor.execute(sql, valores)
        # Commit para confirmar a transação no banco de dados
        self.conexao.commit()

    def leitura(self, tabela):
        # Método para recuperar todos os registros de uma tabela
        sql = f"SELECT * FROM {tabela}"
        # Execução do comando SQL
        self.cursor.execute(sql)
        # Retorno dos resultados
        return self.cursor.fetchall()

    def atualizacao(self, tabela, args, condicao):
        # Método para atualizar registros na tabela
        set_clause = ', '.join([f"{coluna} = ?" for coluna in args.keys()])
        valores = tuple(args.values())
        # Construção do comando SQL para atualização
        sql = f"UPDATE {tabela} SET {set_clause} WHERE {condicao}"
        # Execução do comando SQL
        self.cursor.execute(sql, valores)
        # Commit para confirmar a transação no banco de dados
        self.conexao.commit()

    def delecao(self, tabela, condicao):
        # Método para deletar registros da tabela
        sql = f"DELETE FROM {tabela} WHERE {condicao}"
        # Execução do comando SQL
        self.cursor.execute(sql)
        # Commit para confirmar a transação no banco de dados
        self.conexao.commit()
        
    def criarTabela(self):
        self.cursor.execute("CREATE TABLE lsClientes (nome TEXT," 
                            + "email TEXT PRIMARY KEY, notasFiscais TEXT)")
        self.cursor.execute("CREATE TABLE lsFornecedores (cnpj TEXT PRIMARY KEY,"
                            + " nome TEXT, email TEXT, produtodos TEXT, "
                            +"prasos TEXT, notasFiscais TEXT)")
        self.cursor.execute("CREATE TABLE lsUsuario (nome TEXT, cpf TEXT PRIMARY KEY,"
                            + " email TEXT, senha TEXT, estoque TEXT, "
                            + "investimentos TEXT, faturamento TEXT, custos TEXT,"
                            + " relatorios TEXT)")
        self.cursor.execute("CREATE TABLE lsLoja (nome TEXT, cpf TEXT PRIMARY KEY, "
                            + "cnpj TEXT, estoque TEXT, notasFiscais TEXT, "
                            + "relatorios TEXT)")
        self.cursor.execute("CREATE TABLE lsProdutos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, "
                            + "preco REAL, descricao TEXT, img TEXT, "
                            + "codigodbarras TEXT, lote TEXT, praso TEXT, "
                            + "obs TEXT)")
        print("Tabela Criada")

"""# Exemplo de uso:
# Criação de uma instância do objeto BancoDados
bd = BancoDados(database='cocadaboa.db')

# Exemplo de cadastro
args_cadastro = {'nome': 'João', 'email': 'joao@email.com'}
bd.cadastro('lsClientes', args_cadastro)

# Exemplo de leitura
dados = bd.leitura('lsClientes')
print(dados)

# Exemplo de atualização
args_atualizacao = {'email': 'novo_email@email.com'}
bd.atualizacao('lsClientes', args_atualizacao, 'nome = "João"')

# Exemplo de deleção
bd.delecao('lsClientes', 'nome = "João"')
"""
