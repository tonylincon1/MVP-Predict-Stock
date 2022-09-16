import sys
import pandas as pd
sys.path.insert(1, '../pre_train/')
import load_data

class revenue:
    """
    Classe para calcular impacto de redução de custo para as modelagens.
    """
    
    def calcule_revenue (data_predict=load_data.conect_data.load_table('../../../data/data_processed/', 'processed.predict', 'csv', sep=None), data_value=load_data.conect_data.load_table('../../../data/data_ingestion/', 'ingestion.itens_input_mvp', 'csv', sep=None)):
        """
        Método para calcular o valor financeiro de cada mês para todos os métodos de predição.

        Args:
            data_predict (dataframe, optional): Dataframe com dados de predições. Defaults to load_data.conect_data.load_table('../../../data/data_processed/', 'processed.predict', 'csv', sep=None).
            data_value (dataframe, optional): Dataframe com valores dos itens. Defaults to load_data.conect_data.load_table('../../../data/data_ingestion/', 'ingestion.itens_input_mvp', 'csv', sep=None).
        """
        valores = []
        for item in data_value.NUMERO_REGISTRO_PRODUTO.unique():
            frame = data_value.query(f"NUMERO_REGISTRO_PRODUTO == {item}")
            value = frame[frame.DATA_DE_PEDIDO_DO_ITEM == frame.DATA_DE_PEDIDO_DO_ITEM.max()].CUSTO_DE_AQUISICAO
            valores.append([item,value.iloc[0],frame.DATA_DE_PEDIDO_DO_ITEM.max()])
        valores = pd.DataFrame(valores, columns=['NUMERO_REGISTRO_PRODUTO', 'VALORES', 'DATA_REFERENCIA'])
        
        predicoes = data_predict[["NUMERO_REGISTRO_PRODUTO","DATA_DE_CONSUMO","QUANTIDADE_SAIDA","PREDICAO_MEDIA_MOVEL","PREDICAO_DEEPAR"]]
        
        merge = pd.merge(predicoes,valores,how='left',on='NUMERO_REGISTRO_PRODUTO')
        
        merge["PREDICAO_MEDIA_MOVEL"] = merge.PREDICAO_MEDIA_MOVEL.fillna(-9999999999).apply(int)
        merge["PREDICAO_DEEPAR"] = merge.PREDICAO_DEEPAR.fillna(-9999999999).apply(int)

        receita = []
        for idx,linha in merge.iterrows():
            if linha.PREDICAO_MEDIA_MOVEL < 0:
                receita_media_movel = 0
            else:
                receita_media_movel = linha.PREDICAO_MEDIA_MOVEL * linha.VALORES
            if linha.PREDICAO_DEEPAR < 0:
                receita_deepAR = 0
            else:
                receita_deepAR = linha.PREDICAO_DEEPAR * linha.VALORES

            receita.append([linha.NUMERO_REGISTRO_PRODUTO,linha.DATA_DE_CONSUMO,receita_media_movel,receita_deepAR])
        receita_calculada = pd.DataFrame(receita, columns=['NUMERO_REGISTRO_PRODUTO','DATA_DE_CONSUMO','CUSTO_MEDIA_MOVEL','CUSTO_DEEPAR'])
        
        merge_1 = pd.merge(merge,receita_calculada,how='left',on=['NUMERO_REGISTRO_PRODUTO','DATA_DE_CONSUMO'])
        load_data.conect_data.save_table(merge_1, '../../../data/data_processed/', 'processed.revenue', 'csv')