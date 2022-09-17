import pandas as pd
from src.predict_stock_mvp.pre_train.load_data import *
from datetime import date, datetime
from gluonts.dataset.pandas import PandasDataset

class pre_process:
    """
    Classe feita para realizar o pré processamento dos dados para as IAs de séries temporais.
    """
    def pre_process_deepar(data=conect_data.load_table('data/data_ingestion/', 'ingestion.itens_output_mvp', 'csv', sep=None), prediction_length = 6):
        """
        Função para pré processar, em treinamento e teste, os dados da série temporal no formato de input do modelo deepAR.

        Args:
            data (Dataframe, optional): Tabela de output com valores para pré processar. Defaults to load_data.conect_data.load_table('../../data/data_ingestion/', 'ingestion.itens_output_mvp', 'csv', sep=None).
            prediction_length (int, optional): Meses que o modelo irá prever. Defaults to 6.

        Returns:
            Dataframe: Retorna dois dataframes, um de trainamento e outro de teste para inputar no modelo.
        """
        data_para_processamento = data[["QUANTIDADE_SAIDA","NUMERO_REGISTRO_PRODUTO","DATA_DE_CONSUMO"]]
        data_para_processamento["DATA_DE_CONSUMO"] = data_para_processamento.DATA_DE_CONSUMO.apply(lambda linha: datetime.strptime(linha, '%Y-%m-%d').date())
        data_para_processamento = data_para_processamento.set_index("DATA_DE_CONSUMO")
        
        data_para_processamento_new = pd.DataFrame(None, columns = data_para_processamento.columns)
        for n in data_para_processamento.NUMERO_REGISTRO_PRODUTO.unique():
            frame_train = data_para_processamento.query(f"NUMERO_REGISTRO_PRODUTO == {n}").iloc[:-prediction_length]
            data_para_processamento_new = pd.concat([data_para_processamento_new, frame_train])
            
        train = PandasDataset.from_long_dataframe(data_para_processamento_new, target="QUANTIDADE_SAIDA", item_id="NUMERO_REGISTRO_PRODUTO")
        test = PandasDataset.from_long_dataframe(data_para_processamento, target="QUANTIDADE_SAIDA", item_id="NUMERO_REGISTRO_PRODUTO")
        
        return train, test
    
    def pre_process_deepar_predict(data=conect_data.load_table('data/data_ingestion/', 'ingestion.itens_output_mvp', 'csv', sep=None)):
        """
        Função para pré processar, para predição, os dados da série temporal no formato de input do modelo deepAR.

        Args:
            data (Dataframe, optional): Tabela de output com valores para pré processar. Defaults to load_data.conect_data.load_table('../../data/data_ingestion/', 'ingestion.itens_output_mvp', 'csv', sep=None).

        Returns:
            Dataframe: Retorna um dataframe com os dados pré processados para realizar predição.
        """
        data_para_processamento = data[["QUANTIDADE_SAIDA","NUMERO_REGISTRO_PRODUTO","DATA_DE_CONSUMO"]]
        data_para_processamento["DATA_DE_CONSUMO"] = data_para_processamento.DATA_DE_CONSUMO.apply(lambda linha: datetime.strptime(linha, '%Y-%m-%d').date())
        data_para_processamento = data_para_processamento.set_index("DATA_DE_CONSUMO")
        
        test = PandasDataset.from_long_dataframe(data_para_processamento, target="QUANTIDADE_SAIDA", item_id="NUMERO_REGISTRO_PRODUTO")
        
        return test