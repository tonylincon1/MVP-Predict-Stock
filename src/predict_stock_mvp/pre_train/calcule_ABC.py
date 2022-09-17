from datetime import datetime
from src.predict_stock_mvp.pre_train.load_data import *
from dateutil.relativedelta import relativedelta

class calcule_curve_ABC:
    """
    Classe que classifica cada item na curva ABC e salva uma tabela processada.
    """
    
    def curve_ABC(data=conect_data.load_table('data/data_ingestion/', 'ingestion.itens_input_mvp', 'csv', sep=None)):
        """
        Método que classifica cada item na curva ABC e salva uma tabela processada.

        Args:
            data (Dataframe, optional): Tabela de input com valores para calcular a curva ABC. Defaults to load_data.conect_data.load_table('../../../data/data_ingestion/', 'ingestion.itens_input_mvp', 'csv', sep=None).
        """
        data_a_3_meses = datetime.strptime(data.DATA_DE_ENTRADA_DO_ITEM.max(), '%Y-%m-%d').date() + relativedelta(months=-2)
        data_input_a_3_meses = data[data.DATA_DE_ENTRADA_DO_ITEM >= str(data_a_3_meses)]
        
        data_ABC = data_input_a_3_meses.groupby(["NUMERO_REGISTRO_PRODUTO"]).agg({"QUANTIDADE_ENTRADA":"median","CUSTO_DE_AQUISICAO":"median"})
        data_ABC["VALOR_ABSOLUTO"] = data_ABC["QUANTIDADE_ENTRADA"] * data_ABC["CUSTO_DE_AQUISICAO"]
        data_ABC["PERCENTUAL_ABSOLUTO"] = [(linha.VALOR_ABSOLUTO / data_ABC.VALOR_ABSOLUTO.sum())*100 for idx, linha in data_ABC.iterrows()]
        data_ABC = data_ABC.sort_values(by="PERCENTUAL_ABSOLUTO", ascending=False)
        data_ABC["PERCENTUAL_ABSOLUTO_ACUMULADO"] = data_ABC.PERCENTUAL_ABSOLUTO.cumsum(axis = 0).values
        
        ABC = []
        for idx, linha in data_ABC.iterrows():
            if int(linha.PERCENTUAL_ABSOLUTO_ACUMULADO) <= 80:
                ABC.append("A")
            elif int(linha.PERCENTUAL_ABSOLUTO_ACUMULADO) > 80 and int(linha.PERCENTUAL_ABSOLUTO_ACUMULADO) <= 95:
                ABC.append("B")
            elif int(linha.PERCENTUAL_ABSOLUTO_ACUMULADO) > 95:
                ABC.append("C")

        data_ABC["CLASSIFICACAO_ABC"] = ABC
        data_ABC = data_ABC.reset_index()
        
        conect_data.save_table(data_ABC, 'data/data_processed/', 'processed.curve_ABC', 'csv')