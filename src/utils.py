import os
import helpers

PATH_LOG = '/home/franciele/Projetos/rotulacao-dados/src/log/log_{}.csv'

def clean_log (municipio):
    nameMunicipio = helpers.replace_municipio_path(municipio)
    if os.path.exists(PATH_LOG.format(nameMunicipio)):
        os.remove(PATH_LOG.format(nameMunicipio))

def create_log(municipio):
    nameMunicipio = helpers.replace_municipio_path(municipio)
    log = open(PATH_LOG.format(nameMunicipio), 'w')
    return log

def close_log(log):
    log.close()