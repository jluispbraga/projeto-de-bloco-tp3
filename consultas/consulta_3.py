import pandas as pd


# Função 3 - Listar funcionários que tiveram aumento salarial nos últimos 3 meses
def listar_funcionarios_com_aumento(conn):
    query = '''
    SELECT h1.funcionario_id, f.nome
    FROM HistoricoSalarios h1
    JOIN Funcionarios f ON f.id = h1.funcionario_id
    WHERE h1.mes IN (
            (SELECT MAX(mes) FROM HistoricoSalarios) - 2,
            (SELECT MAX(mes) FROM HistoricoSalarios) - 1,
            (SELECT MAX(mes) FROM HistoricoSalarios)
        )
    GROUP BY h1.funcionario_id
    ORDER BY f.nome;
    '''
    df = pd.read_sql_query(query, conn)
    print(df)
