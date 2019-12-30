import pandas as pd
import utils

# Definição de constantes
PATH_DATABASE = '/home/franciele/Projetos/rotulacao-dados/src/data/data_base.csv'



df = pd.read_csv(PATH_DATABASE)
# print(df.head())

list_municipios = df.municipio.unique()

for municipio in list_municipios:
    print(municipio)
    utils.clean_log(municipio)
    log = utils.create_log(municipio)
    utils.close_log(log)
