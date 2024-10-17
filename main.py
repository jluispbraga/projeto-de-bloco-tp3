import sqlite3

from consultas import *
from create_tables_and_csv import *

diretorio = 'src'
os.makedirs(diretorio, exist_ok=True)
conn = sqlite3.connect(os.path.join(diretorio, 'empresa.db'))

# Buildar o banco de dados e os arquivos CSV
run(conn)


def executar_consulta(consulta, conn):
    funcionarios_df = pd.read_csv('src/funcionarios.csv')
    historico_salarios_df = pd.read_csv('src/historico_salarios.csv')
    dependentes_df = pd.read_csv('src/dependentes.csv')
    departamentos_df = pd.read_csv('src/departamentos.csv')
    cargos_df = pd.read_csv('src/cargos.csv')

    consultas = {
        1: consulta_1.listar_tabelas,
        2: consulta_2.listar_funcionarios_com_detalhes,
        3: consulta_3.listar_funcionarios_com_aumento,
        4: consulta_4.listar_media_idade_filhos,
        5: consulta_5.listar_estagiario_com_filho,
        6: consulta_6.listar_funcionario_com_maior_salario_medio,
        7: consulta_7.listar_analista_pai_duas_meninas,
        8: consulta_8.listar_analista_com_salario_alto,
        9: consulta_9.listar_departamento_mais_dependentes,
        10: consulta_10.listar_media_salario_por_departamento
    }
    consultas_com_parametros = {
        6: {'salarios_df': historico_salarios_df, 'funcionarios_df': funcionarios_df},
        7: {'funcionarios_df': funcionarios_df, 'dependentes_df': dependentes_df, 'cargos_df': cargos_df},
        8: {'salarios_df': historico_salarios_df, 'funcionarios_df': funcionarios_df, 'cargos_df': cargos_df},
        9: {'funcionarios_df': funcionarios_df, 'dependentes_df': dependentes_df, 'departamentos_df': departamentos_df},
        10: {'salarios_df': historico_salarios_df, 'funcionarios_df': funcionarios_df, 'departamentos_df': departamentos_df}
    }

    if consulta in consultas:
        if consulta in consultas_com_parametros:
            consultas[consulta](**consultas_com_parametros[consulta])
        else:
            consultas[consulta](conn)
    else:
        print('Consulta inexistente, favor digitar um número válido')


def options():
    print('1 - Listagem das tabelas em ordem crescente')
    print('2 - Listagem dos funcionarios com cargos, departamentos e dependentes')
    print('3 - Listagem dos funcionários que tiveram aumento salarial nos últimos 3 meses')
    print('4 - Listagem das média de idade dos filhos dos funcionários por departamento')
    print('5 - Listagem de qual estagiário possui filho')
    print('6 - Listagem do funcionário com o salário médio mais alto')
    print('7 - Listagem do analista que é pai de 2 meninas')
    print('8 - Listagem do analista com o salário mais alto, entre 5000 e 9000')
    print('9 - Listagem de qual departamento possui o maior número de dependentes')
    print('10 - Listagem da média de salário por departamento em ordem decrescente')
    return int(input('Digite o número da consulta: '))


print('Conectado com banco de dados!')
print('Bem-vindo ao programa!')

while True:
    try:
        print('Qual consulta você quer fazer?')
        consulta = int(options())
        executar_consulta(consulta, conn)
    except ValueError:
        print('Entrada inválida! Por favor, digite um número válido.')

    continuar = input('Deseja realizar outra consulta? (sim/não) ').strip().lower()
    if continuar in ['n', 'nao', 'não']:
        print('Saindo do sistema...')
        break
