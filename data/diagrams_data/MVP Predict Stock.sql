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

CREATE TABLE `processed`.`metrics` (
  `NUMERO_REGISTRO_PRODUTO` integer,
  `MSE` float,
  `abs_error` float,
  `abs_target_sum` float,
  `abs_target_mean` float,
  `seasonal_error` float,
  `MASE` float,
  `MAPE` float,
  `sMAPE` float,
  `ND` float,
  `MSIS` float,
  `QuantileLoss_median` float,
  `Coverage_median` float,
  `Modelo` string,
  `Tipo` string,
  `RMSE` float,
  `NRMSE` float,
  `wQuantileLoss_median` float,
  `mean_absolute_QuantileLoss` float,
  `mean_wQuantileLoss` float,
  `MAE_Coverage` float,
  `OWA` float,
  `Avaliacao` float
);

CREATE TABLE `processed`.`revenue` (
  `NUMERO_REGISTRO_PRODUTO` integer,
  `DATA_DE_CONSUMO` datetime,
  `QUANTIDADE_SAIDA` integer,
  `PREDICAO_MEDIA_MOVEL` integer,
  `PREDICAO_DEEPAR` integer,
  `VALORES` integer,
  `DATA_REFERENCIA` datetime,
  `CUSTO_MEDIA_MOVEL` integer,
  `CUSTO_DEEPAR` integet
);

ALTER TABLE `ingestion`.`itens_input_mvp` ADD FOREIGN KEY (`NUMERO_REGISTRO_PRODUTO`) REFERENCES `ingestion`.`itens_describe_mvp` (`NUMERO_REGISTRO_PRODUTO`);

ALTER TABLE `ingestion`.`itens_output_mvp` ADD FOREIGN KEY (`NUMERO_REGISTRO_PRODUTO`) REFERENCES `ingestion`.`itens_describe_mvp` (`NUMERO_REGISTRO_PRODUTO`);

ALTER TABLE `processed`.`curve_ABC` ADD FOREIGN KEY (`NUMERO_REGISTRO_PRODUTO`) REFERENCES `ingestion`.`itens_describe_mvp` (`NUMERO_REGISTRO_PRODUTO`);

ALTER TABLE `processed`.`predict` ADD FOREIGN KEY (`NUMERO_REGISTRO_PRODUTO`) REFERENCES `ingestion`.`itens_describe_mvp` (`NUMERO_REGISTRO_PRODUTO`);

ALTER TABLE `processed`.`metrics` ADD FOREIGN KEY (`NUMERO_REGISTRO_PRODUTO`) REFERENCES `ingestion`.`itens_describe_mvp` (`NUMERO_REGISTRO_PRODUTO`);

ALTER TABLE `processed`.`revenue` ADD FOREIGN KEY (`NUMERO_REGISTRO_PRODUTO`) REFERENCES `ingestion`.`itens_describe_mvp` (`NUMERO_REGISTRO_PRODUTO`);
