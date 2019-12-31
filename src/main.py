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
        df_municipio.to_csv(PATH_LABELED.format(municipio))

        utils.clean_figure(municipio)
        utils.save_figure(df_municipio, municipio)

        utils.close_log(log)
