if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter
import mlflow as mf
import numpy as np
import pickle
from mlflow import sklearn as mlflow_sklearn

@data_exporter
def export_data(data, *args, **kwargs):
    model, dv = data

    mf.set_tracking_uri('http://mlflow:5000')

    with mf.start_run():

        with open('dict_vectorizer.bin', 'wb') as f_out:
            pickle.dump(dv, f_out)

        mf.log_artifact( 'dict_vectorizer.bin')
        mlflow_sklearn.log_model(model, 'model')

    print('done')



