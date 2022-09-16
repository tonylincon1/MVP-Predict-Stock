import sys
import pandas as pd
import numpy as np
from datetime import date, datetime
from gluonts.evaluation import Evaluator
from gluonts.model.forecast import SampleForecast
sys.path.insert(1, '../pre_train/')
import load_data

class metrics_models:
    """
    Classe para calcular métricas de desempenho dos modelos.
    
    """
    
    def metrics_media_movel(tss,quant_itens,periodo,freq="M",table_predict=load_data.conect_data.load_table('../../../data/data_processed/', 'processed.predict', 'csv', sep=",")):
        """
        Método para calcular métricas de desempenho do modelo de média móvel.

        Args:
            tss (list): Lista com valores de teste adptados do método predict do DeepAR.
            quant_itens (int): Quantidade de itens que você possui.
            periodo (str): Ano e mês marco utilizados para realizar as predições. Exemplo: "2020-06"
            freq (str, optional): Frequência das predições. Defaults to "M".
            table_predict (dataframe, optional): Dataset que contém as predições do modelo de média móvel. Defaults to load_data.conect_data.load_table('../../data/data_processed/', 'processed.predict', 'csv', sep=",").
        """
        casts = []
        for item in table_predict.NUMERO_REGISTRO_PRODUTO.unique():
            casts.append(table_predict.query(f"NUMERO_REGISTRO_PRODUTO == {item}")["PREDICAO_MEDIA_MOVEL"].dropna().tolist()[-3:])
            
        forecasts = []
        contador = 0
        for n in casts:
            forecasts.append(SampleForecast(samples=np.array([n,n]), start_date=pd._libs.tslibs.period.Period(f"{periodo}", freq=f"{freq}"), item_id=table_predict.NUMERO_REGISTRO_PRODUTO.unique().astype(str).tolist()[contador]))
            contador = contador + 1
        
        data_avaliacao = datetime.today().date()
        
        evaluator = Evaluator(quantiles=[0.5])
        agg_metrics, item_metrics = evaluator(tss, forecasts, num_series=quant_itens)
        item_metrics["Modelo"] = "MediaMovel"
        item_metrics["Tipo"] = "Por Item"
        item_metrics["item_id"] = item_metrics["item_id"].apply(int)
        
        agg_metrics = pd.DataFrame([agg_metrics])
        agg_metrics["Modelo"] = "MediaMovel"
        agg_metrics["Tipo"] = "Agregado"
        agg_metrics["item_id"] = 0
        
        metrics = pd.concat([item_metrics, agg_metrics])
        metrics["Avaliacao"] = data_avaliacao
        metrics = metrics.rename(columns=({"item_id":"NUMERO_REGISTRO_PRODUTO",
                                          "QuantileLoss[0.5]":"QuantileLoss_median",
                                          "Coverage[0.5]":"Coverage_median",
                                          "wQuantileLoss[0.5]":"wQuantileLoss_median"}))
        
        metrics = pd.concat([load_data.conect_data.load_table('../../../data/data_processed/', 'processed.metrics', 'csv', sep=None),metrics])
        
        load_data.conect_data.save_table(metrics, '../../../data/data_processed/', 'processed.metrics', 'csv')
    
    def metrics_DeepAR(tss, forecasts,quant_itens):
        """
        Método para calcular métricas de desempenho do modelo DeepAR.

        Args:
            tss (list): Lista com valores de teste adptados do método predict do DeepAR.
            forecasts (list): Predições do modelo DeepAR.
            quant_itens (int): Quantidade de itens que você possui.
        """
        data_avaliacao = datetime.today().date()
        
        evaluator = Evaluator(quantiles=[0.5])
        agg_metrics, item_metrics = evaluator(tss, forecasts, num_series=quant_itens)
        item_metrics["Modelo"] = "DeepAR"
        item_metrics["Tipo"] = "Por Item"
        item_metrics["item_id"] = item_metrics["item_id"].apply(int)
        
        agg_metrics = pd.DataFrame([agg_metrics])
        agg_metrics["Modelo"] = "DeepAR"
        agg_metrics["Tipo"] = "Agregado"
        agg_metrics["item_id"] = 0
        
        metrics = pd.concat([item_metrics, agg_metrics])
        metrics["Avaliacao"] = data_avaliacao
        metrics = metrics.rename(columns=({"item_id":"NUMERO_REGISTRO_PRODUTO",
                                          "QuantileLoss[0.5]":"QuantileLoss_median",
                                          "Coverage[0.5]":"Coverage_median",
                                          "wQuantileLoss[0.5]":"wQuantileLoss_median"}))
        
        metrics = pd.concat([load_data.conect_data.load_table('../../../data/data_processed/', 'processed.metrics', 'csv', sep=None),metrics])
        
        load_data.conect_data.save_table(metrics, '../../../data/data_processed/', 'processed.metrics', 'csv')