CREATE SCHEMA `ingestion`;

CREATE TABLE `ingestion`.`itens_describe` (
  `NUMERO_REGISTRO_PRODUTO` integer,
  `IDENTIFICADOR_DO_ITEM` integer,
  `NOME_PRODUTO` string,
  `TIPO_PRODUTO` string,
  `CATEGORIA_REGULATORIA` string,
  `CLASSE_TERAPEUTICA` string
);

CREATE TABLE `ingestion`.`itens_input` (
  `NUMERO_REGISTRO_PRODUTO` integer,
  `IDENTIFICADOR_DO_ITEM` integer,
  `NOME_PRODUTO` string,
  `DATA_DE_PEDIDO_DO_ITEM` datetime,
  `DATA_DE_ENTRADA_DO_ITEM` datetime,
  `DATA_VENCIMENTO_REGISTRO` datetime,
  `QUANTIDADE` integer,
  `CUSTO_DE_AQUISICAO` integer
);

CREATE TABLE `ingestion`.`itens_output` (
  `NUMERO_REGISTRO_PRODUTO` integer,
  `IDENTIFICADOR_DO_ITEM` integer,
  `NOME_PRODUTO` string,
  `DATA_DE_CONSUMO` datetime,
  `QUANTIDADE` integer
);

ALTER TABLE `ingestion`.`itens_input` ADD FOREIGN KEY (`IDENTIFICADOR_DO_ITEM`) REFERENCES `ingestion`.`itens_describe` (`IDENTIFICADOR_DO_ITEM`);

ALTER TABLE `ingestion`.`itens_output` ADD FOREIGN KEY (`IDENTIFICADOR_DO_ITEM`) REFERENCES `ingestion`.`itens_describe` (`IDENTIFICADOR_DO_ITEM`);
