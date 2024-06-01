if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

from mlops.utils.data_preparation.cleaning import clean
from mlops.utils.data_preparation.feature_engineering import combine_features
from mlops.utils.data_preparation.feature_selector import select_features
from mlops.utils.data_preparation.splitters import split_on_value

from typing import Tuple

import pandas as pd

@transformer
def transform(
    df: pd.DataFrame, **kwargs
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    split_on_feature = kwargs.get('split_on_feature', 'lpep_pickup_datetime')
    split_on_feature_value = kwargs.get('split_on_feature_value', '2024-02-01')
    target = kwargs.get('target', 'duration')

    df = clean(df)
    df = combine_features(df)
    df = select_features(df, features=[split_on_feature, target])

    df_train, df_val = split_on_value(
        df,
        split_on_feature,
        split_on_feature_value
    )

    return df, df_train, df_val
    