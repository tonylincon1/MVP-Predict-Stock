import pandas as pd

class conect_data:
    """
    Classe feita para carregar, salvar e deletar tabelas.
    
    Estou classe trabalha com csv nesse primeiro momento no desenvolvimento do MVP, porém será refatorada quando houver conexão com bancos do cliente.
    """
    def load_table(location_table, name_table, type_table, encoding='ISO-8859-1', sep=';'):
        """
        Carregando uma tabela
        
        Args:
            location_table (String): Local onde está a tabela, exemplo: ../../data/data_ingestion/
            name_table (String): Nome da tabela, exemplo: ingestion.itens_input_mvp
            type_table (String): Tipo da tabela, exemplo: csv (*Só aceita csv no momento)
            encoding (String, optional): Encoding. Defaults to 'ISO-8859-1'.
            sep (String, optional): Separador. Defaults to ';'.

        Returns:
            Dataframe: Retorna um dataframe da tabela que foi carregada.
        """
        data = pd.read_csv(f'{location_table}/{name_table}.{type_table}', encoding=encoding, sep=sep)
        return data
    
    def save_table(data_save, location_table, name_table, type_table):
        """
        Salvando tabelas

        Args:
            data_save (Dataframe): 
            location_table (String): Local onde irá salvar a tabela, exemplo: ../../data/data_ingestion/
            name_table (String): Nome da tabela, exemplo: ingestion.itens_input_mvp
            type_table (String): Tipo da tabela, exemplo: csv (*Só aceita csv no momento)

        Returns:
            String: Retorno sobre o sucesso da operação
        """
        data_save.to_csv(f'{location_table}/{name_table}.{type_table}', index=False)
        return 'save_sucess'
    
    def del_table():
        pass