CREATE SCHEMA `ingestion`;

CREATE SCHEMA `processed`;

CREATE TABLE `ingestion`.`itens_describe_mvp` (
  `NUMERO_REGISTRO_PRODUTO` integer,
  `IDENTIFICADOR_DO_ITEM` integer,
  `NOME_PRODUTO` string,
  `TIPO_PRODUTO` string,
  `CATEGORIA_REGULATORIA` string,
  `CLASSE_TERAPEUTICA` string
);

CREATE TABLE `ingestion`.`itens_input_mvp` (
  `NUMERO_REGISTRO_PRODUTO` integer,
  `IDENTIFICADOR_DO_ITEM` integer,
  `NOME_PRODUTO` string,
  `DATA_DE_PEDIDO_DO_ITEM` datetime,
  `DATA_DE_ENTRADA_DO_ITEM` datetime,
  `DATA_VENCIMENTO_REGISTRO` datetime,
  `QUANTIDADE_ENTRADA` integer,
  `CUSTO_DE_AQUISICAO` integer
);

CREATE TABLE `ingestion`.`itens_output_mvp` (
  `NUMERO_REGISTRO_PRODUTO` integer,
  `IDENTIFICADOR_DO_ITEM` integer,
  `NOME_PRODUTO` string,
  `DATA_DE_CONSUMO` datetime,
  `QUANTIDADE_SAIDA` integer
);

CREATE TABLE `processed`.`curve_ABC` (
  `NUMERO_REGISTRO_PRODUTO` integer,
  `QUANTIDADE_ENTRADA` integer,
  `CUSTO_DE_AQUISICAO` integer,
  `VALOR_ABSOLUTO` integer,
  `PERCENTUAL_ABSOLUTO` integer,
  `PERCENTUAL_ABSOLUTO_ACUMULADO` integer,
  `CLASSIFICACAO_ABC` string
);

CREATE TABLE `processed`.`predict` (
  `NUMERO_REGISTRO_PRODUTO` integer,
  `DATA_DE_ENTRADA_DO_ITEM` datetime,
  `QUANTIDADE_SAIDA` integer,
  `PREDICAO_MEDIA_MOVEL` float,
  `PREDICAO_DEEPAR` float
);

ALTER TABLE `ingestion`.`itens_input_mvp` ADD FOREIGN KEY (`NUMERO_REGISTRO_PRODUTO`) REFERENCES `ingestion`.`itens_describe_mvp` (`NUMERO_REGISTRO_PRODUTO`);

ALTER TABLE `ingestion`.`itens_output_mvp` ADD FOREIGN KEY (`NUMERO_REGISTRO_PRODUTO`) REFERENCES `ingestion`.`itens_describe_mvp` (`NUMERO_REGISTRO_PRODUTO`);

ALTER TABLE `processed`.`curve_ABC` ADD FOREIGN KEY (`NUMERO_REGISTRO_PRODUTO`) REFERENCES `ingestion`.`itens_describe_mvp` (`NUMERO_REGISTRO_PRODUTO`);

ALTER TABLE `processed`.`predict` ADD FOREIGN KEY (`NUMERO_REGISTRO_PRODUTO`) REFERENCES `ingestion`.`itens_describe_mvp` (`NUMERO_REGISTRO_PRODUTO`);
