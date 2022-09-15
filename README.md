# 1) Sobre o Predict Stock
Entendemos que o modelo atual de gerenciamento de mercadorias e estoques hospitalares é manual e bastante lento o que, em algumas ocasiões, pode gerar desperdícios que poderiam ser evitados. Um caso que podemos perceber esse problema foi o caso relatado segundo reportagem realizada no site de notícias “Infonet” foram encontradas 11 toneladas de medicamentos e insumos vencidos na SMS (Secretaria Municipal de Saúde) de Aracaju/SE. Esse tipo de problema acontece tanto no setor público, quanto no setor privado e tem gerado um volume de desperdícios e tem reduzido o desempenho financeiro de muitas empresas.

Diante desse problema, sentimos a necessidade de ajudar os hospitais, clínicas e empreendimentos correlatos na melhor forma de gerenciamento dos seus suprimentos, conseguindo oferecer insights através de inteligência artificial e métricas que os auxiliam tanto na compra quanto na saída dos materiais. O **Predict Stock** tem como objetivo otimizar os estoques das instituições hospitalares através de um sistema inteligente de predição de estoque.

# 2) Descrição do MVP do Predict Stock
O MVP do Predict Stock tem como objetivo ter algumas funcionalidades que compõe o produto como um todo afim de realizar a validação da ideia. Esse MVP conterá apenas a algumas funcionalidades de back-end da inteligência que faz as predições de pedido de materiais/medicamentos e uma interface com o mínimo de funcionalidade para apresentar principalmente alguns resultados utilizando dados fictícios.

# 3) Features/Estruturas Previstas no MVP
## 3.1) Back-end (Status: Em desenvolvimento🛠️)

### 3.1.1) Conector com Tabelas de Dados (Status: Desenvolvido ✅ | src.predict_stock_mvp.pre_train.load_data.conect_data)
Objeto que irá servir para conectar, salvar, carregar e excluir tabelas e dados que serão utilizados no processamento.
**OBS, foi feito com base em arquivos csv, quando for evoluido para produto precisaremos refatorar para conexão com o banco de dados

### 3.1.2) Identificação da Curva ABC (Status: Desenvolvido ✅ | src.predict_stock_mvp.pre_train.calcule_ABC)
Cálculos (Volume multiplicado pelo custo) e classificação dos itens que estão na curva ABC ('A' representa 80% do custo, 'B' representa 15% do custo e 'C' representa 5% do custo).

### 3.1.3) Cálculo de Baseline de Pedido (Status: Desenvolvido ✅ | src.predict_stock_mvp.predict.methods_predict)
Cálculos considerando outros métodos de pedido menos eficientes, como por exemplo média móvel, para serem comparados com os modelos atuais.

### 3.1.4) Preparação dos Dados (Status: Desenvolvido ✅ | src.predict_stock_mvp.pre_train.pre_process)
Pré-processamento, transformações e outros tratamentos envolvendo os dados de consumo do estoque antes do processo de treinamento.

### 3.1.5) Treinamento dos Modelos (Status: Desenvolvido ✅ | src.predict_stock_mvp.train.train)
Treinamento de diferentes tipos de modelos de séries temporais e verificação do melhor modelos para cada item de consumo do estoque.

### 3.1.6) Predições (Status: Desenvolvido ✅ | src.predict_stock_mvp.predict.methods_predict)
Utilizando o modelo treinado, essa funcionalidade irá chamar as predições dos itens de consumo para datas futuras.

### 3.1.7) Avaliação (Status: Em desenvolvimento🛠️)
Após a predição, essa funcionalidade irá chamar as predições dos itens de consumo e comparar com os dados reais e obter uma série de indicadores dos modelos.

## 3.2) Front-end (Interface com Resultados) (Status: Em desenvolvimento🛠️)
### 3.2.1) Tela de Diagnóstico de Estoque (Status: Em desenvolvimento🛠️)
Diagnóstico contendo a diferença entre utilizar a IA para realizar as previsões com previsões de 3 meses futuros.

### 3.2.2) Tela com Dados de Redução Economica & Estoque (Status: Em desenvolvimento🛠️)
Detalhamento do ganho financeiro e da economia do volume de estoque.

### 3.2.3) Tela com Deadline de Itens com Risco de Passar da Validade (Status: Em desenvolvimento🛠️)
Detalhamento da régua dos itens que estão prestes a passar da validade.

### 3.2.4) Tela com Relatório de Pedido (Status: Em desenvolvimento🛠️)
Detalhamento da lista de pedidos que precisa ser feito de acordo com as predições do modelo.

## 3.3) Estrutura/Bancos de Dados (Status: Em desenvolvimento🛠️)
### 3.3.1) Formato dos Dados do Cliente (Status: Em desenvolvimento🛠️)
Estrutura e formato dos dados dos clientes que precisam ser adaptados para o funcionamento do MVP.

### 3.3.2) Diagrama Relacional (Status: Em desenvolvimento🛠️)
Diagrama com a relação de todas as tabelas que serão utilizadas para o funcionamento do MVP.
![image](data/diagrams_data/MVP%20Predict%20Stock.png)

# 4) Pipelines de Execução do Sistema
## 4.1) Treinamento - pipeline_train (Status: Em desenvolvimento🛠️)
Essa pipeline de treinamento será executada apenas uma única vez, pois a ideia é que quando houver uma implementação o modelo seja treinado com os dados do cliente (*Futuramente será criado o processo de re-treino automático, que será uma outra pipeline)

## 4.2) Predição - pipeline_predict (Status: Em desenvolvimento🛠️)
Essa pipeline de predição será executada com recorrência (Idealmente mensalmente), pois irá para todos os modelos disponíveis executar a predição do próximo período (Idealmente será predição mensal) para cada item do estoque e gerar o próximo pedido + todos os outros indicadores que serão alimentados no sistema.

# 5) Features/Estruturas Não Previstas no MVP, Mas Previstas no Produto
## 5.1) Back-end
### 5.1.1) Sistema de Usuários
### 5.1.2) Sistema de Envio de Alertas
### 5.1.3) Otimização de Hiperparâmetros dos Modelos
### 5.1.4) Monitoramento dos Modelos
### 5.1.5) Re-treino Automático
### 5.1.6) Atualização real-time

## 5.2) Front-end
### 5.2.1) Plataforma

## 5.3) Estrutura/Bancos de Dados
### 5.3.1) Criação da Estrutura do Banco
### 5.3.2) Criação do ETL
