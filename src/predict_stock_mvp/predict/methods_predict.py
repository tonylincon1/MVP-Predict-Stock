import sys
sys.path.insert(1, '../pre_train/')
import load_data
import pandas as pd
from gluonts.evaluation.backtest import make_evaluation_predictions
from tqdm import tqdm

class methods_predict:
    """
    Classe que contém métodos para realizar as predições, tanto dos modelos quanto das outras técnicas para comparação.
    """
    
    def predict_model_deepAR(data_test, data_predict=load_data.conect_data.load_table('../../../data/data_processed/', 'processed.predict', 'csv', sep=None), name_predictor="deepAR_model"):
        """
        Método que calcula a predição baseado no modelo DeepAR.

        Args:
            data_test (Dataframe):  Tabela de teste pré processada para executar predições do modelo DeepAR.
            data_predict (Dataframe, optional): Tabela referência para salvar predições. Defaults to load_data.conect_data.save_table(table_predict, '../../../data/data_processed/', 'processed.predict', 'csv')
            name_predictor (String, optional): Nome do modelo DeepAR
        """
        predictor = pd.read_pickle(f"../../../data/models/{name_predictor}.pickle")
        forecast_it, ts_it = make_evaluation_predictions(dataset=data_test, predictor=predictor, num_samples=100)
        forecasts = list(forecast_it)
        tss = list(ts_it)
        
        for n in data_predict.DATA_DE_CONSUMO:
            if n.find(str(forecasts[0].start_date)) == 0:
                filtro = n
                break
                
        data_input = data_predict.query(f"DATA_DE_CONSUMO >= '{filtro}'")
        lista = []
        contador_itens = 0
        for n in tqdm(data_input.NUMERO_REGISTRO_PRODUTO.unique()):
            lista_de_predicao = forecasts[contador_itens]
            contador_itens = contador_itens + 1
            contador_valores = 0
            for idx, linha in data_input.query(f"NUMERO_REGISTRO_PRODUTO == {n}").iterrows():
                lista.append(lista_de_predicao.quantile(0.5).tolist()[contador_valores])
                contador_valores = contador_valores + 1
        data_input["PREDICAO_DEEPAR"] = lista
        
        table_predict = pd.concat([data_input,data_predict.query(f"DATA_DE_CONSUMO < '{filtro}'")]).sort_values(by=["NUMERO_REGISTRO_PRODUTO",
                                                                                                                  "DATA_DE_CONSUMO"])
        load_data.conect_data.save_table(table_predict, '../../../data/data_processed/', 'processed.predict', 'csv')
    
    def predict_mean(data=load_data.conect_data.load_table('../../../data/data_ingestion/', 'ingestion.itens_output_mvp', 'csv', sep=None)):
        """
        Método que calcula a predição baseado na média móvel.

        Args:
            data (Dataframe, optional): Tabela de input com valores para calcular a predição por média móvel. Defaults to load_data.conect_data.load_table('../../../data/data_ingestion/', 'ingestion.itens_input_mvp', 'csv', sep=None).
        """
        data_predict_media_movel = data[["NUMERO_REGISTRO_PRODUTO","DATA_DE_CONSUMO","QUANTIDADE_SAIDA"]]
        
        predict_media = []
        for item in data_predict_media_movel["NUMERO_REGISTRO_PRODUTO"].unique():
            serie_itens = data_predict_media_movel.query(f"NUMERO_REGISTRO_PRODUTO == {item}")
            media_movel = list(serie_itens.QUANTIDADE_SAIDA.shift(1).rolling(3).mean())
            for n in media_movel[:]:
                predict_media.append(n)
                
        data_predict_media_movel["PREDICAO_MEDIA_MOVEL"] = predict_media
        
        load_data.conect_data.save_table(data_predict_media_movel, '../../../data/data_processed/', 'processed.predict', 'csv')