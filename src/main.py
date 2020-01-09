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

        dataLabeler.execute(df_municipio, PATH_LABELED.format(municipio), log)

        data_labeled = pd.read_csv(PATH_LABELED.format(municipio))

        utils.clean_figure(municipio)

        utils.save_figure(data_labeled, municipio)

        utils.close_log(log)
