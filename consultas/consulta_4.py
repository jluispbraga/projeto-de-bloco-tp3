import pandas as pd


# Consulta 4 - Listar a média de idade dos filhos dos funcionários por departamento
def listar_media_idade_filhos(conn):
    query = '''
    SELECT d.nome AS departamento, ROUND(AVG(dep.idade), 2) AS media_idade_filhos
    FROM Dependentes dep
    JOIN Funcionarios f ON dep.funcionario_id = f.id
    JOIN Departamentos d ON f.departamento_id = d.id
    GROUP BY d.nome
    ORDER BY media_idade_filhos
    '''
    df = pd.read_sql_query(query, conn)
    print(df)
