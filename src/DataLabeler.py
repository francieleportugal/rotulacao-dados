import numpy as np

COL_NOTIFICACOES = 'quantidade_notificacoes'
COL_LABEL = 'label'
MAX_SCORE = 5
INITIAL_SCORE = 0
UP_MEAN = 1
DOWN_MEAN = 0

class DataLabeler():
    def mark_database (self, df):
        margin = 5
        mean = np.mean(list(df[COL_NOTIFICACOES]))

        data = list(map(
            lambda x : UP_MEAN if x > mean + margin else DOWN_MEAN,
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

        for i,value in enumerate(data):
            log.write('----------------------------\n')
            log.write('Position: ' + str(i) + '\n')
            log.write('Value: ' + str(value) + '\n')

            if isSearchingForBegins:
                    
                if value == 1:
                    log.write('Iniciando ciclo\n')
                    isSearchingForBegins = False
                    score = INITIAL_SCORE
                    begin = i
                        
                log.write('Score: ' + str(score) + '\n')
                    
            elif not isSearchingForBegins:
                
                if i == (len(data) - 1):
                    result.append([begin,i])
                
                elif value == UP_MEAN:
                    score = score +1
                    
                    if score > MAX_SCORE:
                        score = MAX_SCORE
                        
                elif value == DOWN_MEAN:
                    score = score - 1
                    
                    if score == 0:
                        log.write('Finalizando ciclo\n')
                        isSearchingForBegins = True
                        end = i - 1
                        result.append([begin,end])
                        begin = -1
                        end = -1

                log.write('Score: ' + str(score) + '\n')
        
        return result