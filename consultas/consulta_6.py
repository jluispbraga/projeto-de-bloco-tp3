# Função 6 - Listar o funcionário com o salário médio mais alto
def listar_funcionario_com_maior_salario_medio(salarios_df, funcionarios_df):
    media_salarios = salarios_df.groupby('funcionario_id')['salario'].mean().reset_index()
    salario_maximo = media_salarios['salario'].max()
    funcionario_id = media_salarios.loc[media_salarios['salario'] == salario_maximo, 'funcionario_id'].values[0]
    funcionario = funcionarios_df[funcionarios_df['id'] == funcionario_id]
    print(funcionario)
