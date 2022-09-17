from src.predict_stock_mvp.pre_train.load_data import *
from src.predict_stock_mvp.pre_train.calcule_ABC import *
from src.predict_stock_mvp.pre_train.pre_process import *
from src.predict_stock_mvp.train.train import *
from src.predict_stock_mvp.predict.methods_predict import *
from src.predict_stock_mvp.metrics.calcule_metrics import *
from src.predict_stock_mvp.metrics.revenue import *

class predict:
    methods_predict.predict_mean()
    calcule_curve_ABC.curve_ABC()
    n_itens = len(conect_data.load_table('data/data_ingestion/', 'ingestion.itens_describe_mvp', 'csv', sep=None))
    data_test = pre_process.pre_process_deepar_predict()
    forecasts, tss = methods_predict.predict_model_deepAR(data_test)
    metrics_models.metrics_media_movel(tss,n_itens,"2021-10")
    metrics_models.metrics_DeepAR(tss,forecasts,n_itens)
    revenue.calcule_revenue()
    

if __name__ == '__main__':
    predict()