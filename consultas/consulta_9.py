# Consulta 9 - Listar qual departamento possui o maior número de dependentes
def listar_departamento_mais_dependentes(funcionarios_df, dependentes_df, departamentos_df):
    dependentes_count = dependentes_df.merge(funcionarios_df, left_on='funcionario_id', right_on='id')
    dependentes_por_departamento = dependentes_count.groupby('departamento_id').size().reset_index(name='qtd_dependentes')
    departamentos_count = dependentes_por_departamento.merge(departamentos_df, left_on='departamento_id', right_on='id')
    max_dependentes = departamentos_count['qtd_dependentes'].max()
    departamento_maior = departamentos_count[departamentos_count['qtd_dependentes'] == max_dependentes]
    print(departamento_maior[['nome', 'qtd_dependentes']])
