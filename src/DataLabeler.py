import numpy as np

COL_NOTIFICACOES = 'quantidade_notificacoes'
COL_LABEL = 'label'
MAX_SCORE = 5
INITIAL_SCORE = 2
UP_MEAN = 1
DOWN_MEAN = 0
CICLO = 'Ciclo'
NAO_CICLO =  'Não ciclo'


class DataLabeler:
    def mark_database (self, df):
        margin = 5
        mean = np.mean(list(df[COL_NOTIFICACOES]))

        data = list(map(
            lambda x : UP_MEAN if x > (mean + margin) else DOWN_MEAN,
            list(df[COL_NOTIFICACOES])
        ))
        
        df[COL_LABEL] = data 

        return df

    def find_groups(self, data, log):
        score = INITIAL_SCORE

        result = []
        begin = -1
        end= -1

        isSearchingForBegins = True
        isSeachingForEnds = False

        for i,value in enumerate(data):

            if isSearchingForBegins:
                    
                if value == UP_MEAN:
                    isSearchingForBegins = False
                    score = INITIAL_SCORE
                    begin = i
                    
            elif not isSeachingForEnds:
                
                if i == len(data)-1:
                    if self.is_ciclo_valido(ciclo):
                        ciclo = [begin, end]
                        result.append(ciclo)
                
                elif value == UP_MEAN:
                    score = score +1
                    
                    if score > MAX_SCORE:
                        score = MAX_SCORE
                        
                elif value == DOWN_MEAN:
                    score = score - 1
                
                if score == 0:
                    isSearchingForBegins = True
                    end = i-1
                    ciclo = [begin, end]

                    if self.is_ciclo_valido(ciclo):
                        result.append(ciclo)

                    begin = -1
                    end = -1

        print('Quantidade de grupos: ', len(result))
        
        return result

    def get_column_label(self, sizeDataset, positions_groups):
        column_label = []
        size = len(positions_groups)
        position = 0
        
        group = positions_groups[position]
        
        for i in range(sizeDataset):
            if i >= group[0] and i <= group[1]:
                column_label.append(CICLO)
            else:
                column_label.append(NAO_CICLO)
   
            if(i == group[1] and (position + 1) < size):
                position = position + 1
                group = positions_groups[position]  

        print('Quantidade de dados rotulados como Não ciclo: ', column_label.count('Não ciclo'))
        print('Quantidade de dados rotulados como Ciclo: ', column_label.count('Ciclo'))     
                
        return column_label

    def is_ciclo_valido(self, ciclo):
        return ((ciclo[1] - ciclo[0]) > (MAX_SCORE - INITIAL_SCORE))
    
    def execute(self, df_municipio, path, log):
        self.mark_database(df_municipio)
        groups = self.find_groups(list(df_municipio['label']), log)
        column_final_label = self.get_column_label(len(list(df_municipio['label'])), groups)        
        df_municipio['final_label'] = column_final_label        
        df_municipio = df_municipio.drop(columns=['Unnamed: 0', 'id', 'municipio', 'label'])
        df_municipio.to_csv(path)
