from src.predict_stock_mvp.pre_train.load_data import *
from src.predict_stock_mvp.pre_train.pre_process import *
from src.predict_stock_mvp.train.train import *
from src.predict_stock_mvp.predict.methods_predict import *
from src.predict_stock_mvp.metrics.calcule_metrics import *

class fitting:
    methods_predict.predict_mean()
    n_itens = len(conect_data.load_table('data/data_ingestion/', 'ingestion.itens_describe_mvp', 'csv', sep=None))
    data_train, data_test = pre_process.pre_process_deepar()
    train_model.train_deepAR(data_train,learning_rate=0.008)
    forecasts, tss = methods_predict.predict_model_deepAR(data_test)
    metrics_models.metrics_media_movel(tss,n_itens,"2021-10")
    metrics_models.metrics_DeepAR(tss,forecasts,n_itens)

if __name__ == '__main__':
    fitting()