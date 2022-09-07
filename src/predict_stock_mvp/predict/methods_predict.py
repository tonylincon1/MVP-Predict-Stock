import sys
sys.path.insert(1, '../pre_train/')
import load_data

class metods_predict:
    """
    Classe que contém métodos para realizar as predições, tanto dos modelos quanto das outras técnicas para comparação.
    """
    
    def predict_model ():
        pass
    
    def predict_mean(data=load_data.conect_data.load_table('../../../data/data_ingestion/', 'ingestion.itens_input_mvp', 'csv', sep=None)):
        """
        Método que calcula a predição baseado na média móvel.

        Args:
            data (Dataframe, optional): Tabela de input com valores para calcular a curva ABC. Defaults to load_data.conect_data.load_table('../../../data/data_ingestion/', 'ingestion.itens_input_mvp', 'csv', sep=None).
        """
        data_predict_media_movel = data[["NUMERO_REGISTRO_PRODUTO","DATA_DE_ENTRADA_DO_ITEM","QUANTIDADE"]]
        data_predict_media_movel = data_predict_media_movel.rename(columns={"QUANTIDADE":"QUANTIDADE_REAL"})
        
        predict_media = []
        for item in data_predict_media_movel["NUMERO_REGISTRO_PRODUTO"].unique():
            serie_itens = data_predict_media_movel.query(f"NUMERO_REGISTRO_PRODUTO == {item}")
            media_movel = list(serie_itens.QUANTIDADE_REAL.shift(1).rolling(3).mean())
            for n in media_movel[:]:
                predict_media.append(n)
                
        data_predict_media_movel["PREDICAO_MEDIA_MOVEL"] = predict_media
        
        load_data.conect_data.save_table(data_predict_media_movel, '../../../data/data_processed/', 'processed.predict', 'csv')