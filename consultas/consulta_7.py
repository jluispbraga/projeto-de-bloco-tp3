# Consulta 7 - Listar o analista que é pai de 2 meninas
def listar_analista_pai_duas_meninas(funcionarios_df, dependentes_df, cargos_df):
    analistas = funcionarios_df[funcionarios_df['cargo_id'].isin(cargos_df[cargos_df['nome'] == 'Analista']['id'])]
    analistas_dependentes = analistas.merge(dependentes_df, left_on='id', right_on='funcionario_id')
    num_meninas = analistas_dependentes[analistas_dependentes['genero'] == 'Feminino'].groupby('funcionario_id').size()
    analistas_com_duas_meninas = num_meninas[num_meninas == 2].reset_index()
    result = analistas[analistas['id'].isin(analistas_com_duas_meninas['funcionario_id'])]
    print(result)
