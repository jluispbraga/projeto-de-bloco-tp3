import pandas as pd


# Consulta 8 - Listar o analista com o salário mais alto, entre 5000 e 9000
def listar_analista_com_salario_alto(salarios_df, funcionarios_df, cargos_df):
    analistas = funcionarios_df[funcionarios_df['cargo_id'].isin(cargos_df[cargos_df['nome'] == 'Analista']['id'])]
    salarios_analistas = salarios_df[salarios_df['funcionario_id'].isin(analistas['id'])]
    salarios_filtro = salarios_analistas[
        (salarios_analistas['salario'] >= 5000) & (salarios_analistas['salario'] <= 9000)]
    salario_maximo = salarios_filtro['salario'].max()
    analista_alto_salario = salarios_filtro[salarios_filtro['salario'] == salario_maximo].merge(funcionarios_df,
                                                                                                left_on='funcionario_id',
                                                                                                right_on='id')
    print(analista_alto_salario)

