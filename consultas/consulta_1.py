import pandas as pd


# Consulta 1 - Listar individualmente as tabelas em ordem crescente
def listar_tabelas(conn):
    tabelas = ['Funcionarios', 'Cargos', 'Departamentos', 'HistoricoSalarios', 'Dependentes']
    for tabela in tabelas:
        query = f'SELECT * FROM {tabela} ORDER BY id ASC'
        df = pd.read_sql_query(query, conn)
        print(f"\nTabela: {tabela}")
        print(df)
