import pandas as pd
import utils
from DataLabeler import DataLabeler

dataLabeler = DataLabeler()

PATH_DATABASE = '/home/franciele/Projetos/rotulacao-dados/src/data/data_base.csv'
PATH_MUNICIPIO = '/home/franciele/Projetos/rotulacao-dados/src/data/{}.csv'
PATH_LABELED = '/home/franciele/Projetos/rotulacao-dados/src/data_labeled/{}.csv'


df = pd.read_csv(PATH_DATABASE)
list_municipios = df.municipio.unique()

for municipio in list_municipios:
    if (municipio == 'SALVADOR'):
        print(municipio)
        utils.clean_log(municipio)
        log = utils.create_log(municipio)

        df_municipio = pd.read_csv(PATH_MUNICIPIO.format(municipio))
        dataLabeler.mark_database(df_municipio)

        groups = dataLabeler.find_groups(list(df_municipio['label']), log)
        
        column_final_label = dataLabeler.get_column_label(len(list(df_municipio['label'])), groups)
        
        df_municipio['final_label'] = column_final_label 
        
        df_municipio = df_municipio.drop(columns=['Unnamed: 0', 'id', 'municipio', 'label'])
        print(df_municipio.head())
        df_municipio.to_csv(PATH_LABELED.format(municipio))

        data_labeled = pd.read_csv(PATH_LABELED.format(municipio))
        print(data_labeled.head())
        utils.clean_figure(municipio)


        # data = [
        #     ['01/01/2019', '3', 'Ciclo'],
        #     ['02/01/2019', '2', 'Não ciclo'],
        #     ['03/01/2019', '3', 'Ciclo']
        # ] 
  
        # teste = pd.DataFrame(data, columns = ['data', 'quantidade_notificacoes', 'final_label']) 
        # print(teste)
        utils.save_figure(data_labeled, municipio)

        utils.close_log(log)
