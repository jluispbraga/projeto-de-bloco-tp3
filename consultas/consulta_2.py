import pandas as pd


# Consulta 2 - Listar funcionários, cargos, departamentos e dependentes
def listar_funcionarios_com_detalhes(conn):
    query = '''
    SELECT f.nome AS funcionario, c.nome AS cargo, d.nome AS departamento, dep.nome AS dependente
    FROM Funcionarios f
    LEFT JOIN Cargos c ON f.cargo_id = c.id
    LEFT JOIN Departamentos d ON f.departamento_id = d.id
    LEFT JOIN Dependentes dep ON f.id = dep.funcionario_id
    ORDER BY f.nome ASC
    '''
    df = pd.read_sql_query(query, conn)
    print(df)
