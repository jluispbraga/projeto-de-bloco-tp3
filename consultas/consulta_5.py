import pandas as pd


# Consulta 5 - Listar qual estagiário possui filho
def listar_estagiario_com_filho(conn):
    query = '''
    SELECT f.nome AS estagiario, dep.nome AS dependente
    FROM Funcionarios f
    JOIN Dependentes dep ON f.id = dep.funcionario_id
    JOIN Cargos c ON f.cargo_id = c.id
    WHERE c.nome = 'Estagiário'
    '''
    df = pd.read_sql_query(query, conn)
    print(df)
