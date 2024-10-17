import csv
import os
import pandas as pd

'''
    Dados que serão usados
'''
funcionarios = [
    {'id': 1, 'nome': 'João Silva', 'cargo_id': 1, 'departamento_id': 1},
    {'id': 2, 'nome': 'Ana Santos', 'cargo_id': 2, 'departamento_id': 1},
    {'id': 3, 'nome': 'Pedro Costa', 'cargo_id': 3, 'departamento_id': 2},
    {'id': 4, 'nome': 'Lucas Pereira', 'cargo_id': 2, 'departamento_id': 3},
    {'id': 5, 'nome': 'Mariana Souza', 'cargo_id': 4, 'departamento_id': 4},
    {'id': 6, 'nome': 'Fernanda Lima', 'cargo_id': 1, 'departamento_id': 2},
    {'id': 7, 'nome': 'Carlos Dias', 'cargo_id': 5, 'departamento_id': 3},
    {'id': 8, 'nome': 'Juliana Andrade', 'cargo_id': 3, 'departamento_id': 5},
    {'id': 9, 'nome': 'Fábio Castro', 'cargo_id': 4, 'departamento_id': 4},
    {'id': 10, 'nome': 'Beatriz Alves', 'cargo_id': 5, 'departamento_id': 5},
    {'id': 11, 'nome': 'Rafael Alves', 'cargo_id': 2, 'departamento_id': 2},
    {'id': 12, 'nome': 'Camila Rocha', 'cargo_id': 1, 'departamento_id': 5},
    {'id': 13, 'nome': 'Eduardo Mello', 'cargo_id': 2, 'departamento_id': 1},
    {'id': 14, 'nome': 'Patrícia Moreira', 'cargo_id': 1, 'departamento_id': 3},
    {'id': 15, 'nome': 'Tiago Lopes', 'cargo_id': 3, 'departamento_id': 4},
    {'id': 16, 'nome': 'Roberta Martins', 'cargo_id': 4, 'departamento_id': 1},
    {'id': 17, 'nome': 'Fernando Nunes', 'cargo_id': 5, 'departamento_id': 2},
    {'id': 18, 'nome': 'Larissa Barros', 'cargo_id': 1, 'departamento_id': 4},
    {'id': 19, 'nome': 'Vinícius Azevedo', 'cargo_id': 2, 'departamento_id': 5},
    {'id': 20, 'nome': 'Aline Fernandes', 'cargo_id': 3, 'departamento_id': 3},
]

cargos = [
    {'id': 1, 'nome': 'Estagiário'},
    {'id': 2, 'nome': 'Analista'},
    {'id': 3, 'nome': 'Gerente'},
    {'id': 4, 'nome': 'Diretor'},
    {'id': 5, 'nome': 'Técnico'},
]

departamentos = [
    {'id': 1, 'nome': 'Recursos Humanos'},
    {'id': 2, 'nome': 'Tecnologia'},
    {'id': 3, 'nome': 'Financeiro'},
    {'id': 4, 'nome': 'Marketing'},
    {'id': 5, 'nome': 'Vendas'},
]

historico_salarios = [
    {'id': 1, 'funcionario_id': 1, 'mes': 1, 'ano': 2024, 'salario': 1500},
    {'id': 2, 'funcionario_id': 2, 'mes': 6, 'ano': 2024, 'salario': 5000},
    {'id': 3, 'funcionario_id': 3, 'mes': 3, 'ano': 2024, 'salario': 7000},
    {'id': 4, 'funcionario_id': 4, 'mes': 7, 'ano': 2024, 'salario': 6000},
    {'id': 5, 'funcionario_id': 5, 'mes': 12, 'ano': 2024, 'salario': 9000},
    {'id': 6, 'funcionario_id': 11, 'mes': 2, 'ano': 2024, 'salario': 5200},
    {'id': 7, 'funcionario_id': 12, 'mes': 4, 'ano': 2024, 'salario': 1300},
    {'id': 8, 'funcionario_id': 13, 'mes': 5, 'ano': 2024, 'salario': 5100},
    {'id': 9, 'funcionario_id': 14, 'mes': 3, 'ano': 2024, 'salario': 1400},
    {'id': 10, 'funcionario_id': 15, 'mes': 6, 'ano': 2024, 'salario': 7500},
    {'id': 11, 'funcionario_id': 16, 'mes': 8, 'ano': 2024, 'salario': 9200},
    {'id': 12, 'funcionario_id': 17, 'mes': 2, 'ano': 2024, 'salario': 4500},
    {'id': 13, 'funcionario_id': 18, 'mes': 3, 'ano': 2024, 'salario': 1550},
    {'id': 14, 'funcionario_id': 19, 'mes': 1, 'ano': 2024, 'salario': 5300},
    {'id': 15, 'funcionario_id': 20, 'mes': 11, 'ano': 2024, 'salario': 7200},
    {'id': 16, 'funcionario_id': 4, 'mes': 8, 'ano': 2024, 'salario': 6200},
    {'id': 17, 'funcionario_id': 4, 'mes': 9, 'ano': 2024, 'salario': 6300},
    {'id': 18, 'funcionario_id': 4, 'mes': 10, 'ano': 2024, 'salario': 6400},
    {'id': 19, 'funcionario_id': 2, 'mes': 8, 'ano': 2024, 'salario': 5100},
    {'id': 20, 'funcionario_id': 2, 'mes': 9, 'ano': 2024, 'salario': 5200},
    {'id': 21, 'funcionario_id': 2, 'mes': 10, 'ano': 2024, 'salario': 5300},
]


dependentes = [
    {'id': 1, 'funcionario_id': 1, 'nome': 'Maria Silva', 'idade': 5, 'genero': 'Feminino'},
    {'id': 2, 'funcionario_id': 1, 'nome': 'Lucas Silva', 'idade': 3, 'genero': 'Masculino'},
    {'id': 3, 'funcionario_id': 2, 'nome': 'Pedro Santos', 'idade': 7, 'genero': 'Masculino'},
    {'id': 4, 'funcionario_id': 4, 'nome': 'Ana Santos', 'idade': 4, 'genero': 'Feminino'},
    {'id': 5, 'funcionario_id': 4, 'nome': 'Carla Costa', 'idade': 6, 'genero': 'Feminino'},
    {'id': 6, 'funcionario_id': 11, 'nome': 'Fernanda Alves', 'idade': 3, 'genero': 'Feminino'},
    {'id': 7, 'funcionario_id': 11, 'nome': 'Julia Alves', 'idade': 5, 'genero': 'Feminino'},
    {'id': 8, 'funcionario_id': 12, 'nome': 'Gabriel Rocha', 'idade': 2, 'genero': 'Masculino'},
    {'id': 9, 'funcionario_id': 13, 'nome': 'Sofia Mello', 'idade': 6, 'genero': 'Feminino'},
    {'id': 10, 'funcionario_id': 13, 'nome': 'Laura Mello', 'idade': 4, 'genero': 'Feminino'},
    {'id': 11, 'funcionario_id': 14, 'nome': 'Paulo Moreira', 'idade': 8, 'genero': 'Masculino'},
    {'id': 12, 'funcionario_id': 15, 'nome': 'Alice Lopes', 'idade': 5, 'genero': 'Feminino'},
    {'id': 13, 'funcionario_id': 17, 'nome': 'Caio Nunes', 'idade': 6, 'genero': 'Masculino'},
    {'id': 14, 'funcionario_id': 18, 'nome': 'Marina Barros', 'idade': 2, 'genero': 'Feminino'},
    {'id': 15, 'funcionario_id': 19, 'nome': 'Lucas Azevedo', 'idade': 3, 'genero': 'Masculino'},
]
'''
    Fim dos dados usados
'''


# Funcao para crias as tabelas
def create_tables(conn):
    cursor = conn.cursor()

    '''
        Inicio da criação das tabelas
    '''
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Funcionarios (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        cargo_id INTEGER,
        departamento_id INTEGER,
        FOREIGN KEY(cargo_id) REFERENCES Cargos(id),
        FOREIGN KEY(departamento_id) REFERENCES Departamentos(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cargos (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Departamentos (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS HistoricoSalarios (
        id INTEGER PRIMARY KEY,
        funcionario_id INTEGER,
        mes INTEGER,
        ano INTEGER,
        salario REAL,
        FOREIGN KEY(funcionario_id) REFERENCES Funcionarios(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Dependentes (
        id INTEGER PRIMARY KEY,
        funcionario_id INTEGER,
        nome TEXT NOT NULL,
        idade INTEGER,
        genero TEXT NOT NULL,
        FOREIGN KEY(funcionario_id) REFERENCES Funcionarios(id)
    )
    ''')

    conn.commit()

    '''
        Fim da criação das tabela
    '''


# Função para criar o csv
def create_csv(nome_arquivo, dados, campos):
    '''
    :param nome_arquivo:
    :param dados:
    :param campos:
    :return: criar um csv com os dados do arquivo
    '''
    os.makedirs('src', exist_ok=True)
    caminho_arquivo = os.path.join('src', nome_arquivo)
    with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=campos)
        writer.writeheader()
        writer.writerows(dados)


# Função para criar o csv
def run_create_datas():
    create_csv('funcionarios.csv', funcionarios, ['id', 'nome', 'cargo_id', 'departamento_id'])
    create_csv('cargos.csv', cargos, ['id', 'nome'])
    create_csv('departamentos.csv', departamentos, ['id', 'nome'])
    create_csv('historico_salarios.csv', historico_salarios, ['id', 'funcionario_id', 'mes', 'ano', 'salario'])
    create_csv('dependentes.csv', dependentes, ['id', 'funcionario_id', 'nome', 'idade', 'genero'])


# Função para importar para o banco de dados
def import_csv_to_bd(nome_tabela, caminho_csv, conn):
    '''
    :param nome_tabela:
    :param caminho_csv:
    :return: converter o csv para sql e preencher o banco de dados
    '''
    caminho_arquivo = os.path.join('src', caminho_csv)
    df = pd.read_csv(caminho_arquivo, sep=',', encoding='utf-8')
    df.to_sql(nome_tabela, conn, if_exists='replace', index=False)


# Função para criar tabelas-criacao do banco de dados
def run_create_tables(conn):
    import_csv_to_bd('Funcionarios', 'funcionarios.csv', conn)
    import_csv_to_bd('Cargos', 'cargos.csv', conn)
    import_csv_to_bd('Departamentos', 'departamentos.csv', conn)
    import_csv_to_bd('HistoricoSalarios', 'historico_salarios.csv', conn)
    import_csv_to_bd('Dependentes', 'dependentes.csv', conn)


def run(conn):
    create_tables(conn)
    run_create_datas()
    run_create_tables(conn)
