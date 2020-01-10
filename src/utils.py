import os
import helpers
import numpy as np
import matplotlib as mat
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


TITLE = 'CASOS DE DENGUE - {}'
PATH_LOG = '/home/franciele/Projetos/rotulacao-dados/src/log/log_{}.txt'
PATH_FIGURE = '/home/franciele/Projetos/rotulacao-dados/src/figures/{}.png'


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

def save_figure(df, municipio):
    notificacoes = list(df['quantidade_notificacoes'])
    data = tuple(df['data'])
    
    colors = list(map(
        lambda x : 'red' if (x == 'Ciclo') else 'green',
         list(df['final_label'])
    ))
    
    width_in_inches = 18
    height_in_inches = 8
    dots_per_inch = 70
    

    fig = plt.figure(
        figsize=(width_in_inches, height_in_inches),
        dpi=dots_per_inch
    )
    
    fig.suptitle(TITLE.format(municipio), fontsize=16)
    plt.xlabel('Data da notificação', fontsize=12)
    plt.ylabel('Quantidade de notificações', fontsize=12)

    red_patch = mpatches.Patch(color='red', label='Ciclo de dengue')
    green_patch = mpatches.Patch(color='green', label='Não ciclo de dengue')
    plt.legend(handles=[red_patch, green_patch])    
    
    plt.bar(data, notificacoes, color=colors)
    plt.xticks(data)
    plt.savefig(PATH_FIGURE.format(municipio))
    plt.clf()

def clean_figure (municipio):
    if os.path.exists(PATH_FIGURE.format(municipio)):
        os.remove(PATH_FIGURE.format(municipio))
