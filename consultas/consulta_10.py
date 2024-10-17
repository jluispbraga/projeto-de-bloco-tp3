# Função 10 - Listar a média de salário por departamento em ordem decrescente
def listar_media_salario_por_departamento(salarios_df, funcionarios_df, departamentos_df):
    media_salario = salarios_df.merge(funcionarios_df, left_on='funcionario_id', right_on='id')
    media_por_departamento = media_salario.groupby('departamento_id')['salario'].mean().reset_index(
        name='media_salario')
    media_departamentos = media_por_departamento.merge(departamentos_df, left_on='departamento_id', right_on='id')
    media_departamentos = media_departamentos.sort_values(by='media_salario', ascending=False)
    print(media_departamentos[['nome', 'media_salario']])
