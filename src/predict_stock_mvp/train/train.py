import pandas as pd
from gluonts.model.deepar import DeepAREstimator
from gluonts.mx.trainer.learning_rate_scheduler import LearningRateReduction
from gluonts.mx.trainer import Trainer
from gluonts.mx.trainer.model_averaging import ModelAveraging, SelectNBestMean

class train_model:
    """
    Classe para realizar treinamento dos modelos para séries temporais.
    """
    
    def train_deepAR(data_train, freq="M", prediction_length=3, context_length=21, num_layers=2, num_cells=50, learning_rate=0.01, epochs=10):
        """
        Função para treinamento do modelo deepAR.

        Args:
            data_train (PandasDataset): PandasDataset com dados de treinamento.
            freq (str, optional): Frequência da predição, exemplos: M -> Mês, D -> Dia. Defaults to "M".
            prediction_length (int, optional): Meses que o modelo irá prever. Defaults to 3.
            context_length (int, optional): O número de pontos de tempo (Vai depender da agregação) que o modelo consegue ver antes de fazer a previsão. Defaults to 21.
            num_layers (int, optional): O número de camadas ocultas na RNN. Defaults to 2.
            num_cells (int, optional): O número de células a serem usadas em cada camada oculta da RNN. Defaults to 50.
            learning_rate (float, optional): Taxa de aprendizado. Defaults to 0.01.
            epochs (int, optional): Épocas de treinamento. Defaults to 10.
        """
        
        callbacks = [LearningRateReduction(objective="min", patience=10, base_lr=1e-3, decay_factor=0.5),
                        ModelAveraging(avg_strategy=SelectNBestMean(num_models=2))]

        estimator = DeepAREstimator(freq=freq,
                                    prediction_length=prediction_length,
                                    context_length=context_length,
                                    num_layers = num_layers,
                                    num_cells = num_cells,
                                    trainer=Trainer(#ctx = mx.context.gpu(),
                                                    epochs=epochs,
                                                    learning_rate=learning_rate,
                                                    callbacks=callbacks))

        predictor = estimator.train(data_train)
        pd.to_pickle(predictor,'data/models/deepAR_model.pickle' )
        
    def train_outhers_models():
        pass