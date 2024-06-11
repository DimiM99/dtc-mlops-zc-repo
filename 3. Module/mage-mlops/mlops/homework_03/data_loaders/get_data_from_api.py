if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
import requests
from io import BytesIO
import pandas as pd


@data_loader
def load_data(*args, **kwargs):
    response = requests.get(
                "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-03.parquet"
            )
    if response.status_code != 200:
                raise Exception(response.text)

    return pd.read_parquet(BytesIO(response.content))