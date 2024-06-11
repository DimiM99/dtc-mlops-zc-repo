if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

@transformer
def transform(data, *args, **kwargs):
    df = data
    vectorizer = DictVectorizer(sparse=True)
    model = LinearRegression()

    df_train = df[["PULocationID", "DOLocationID", "duration"]]

    df_train.dropna(inplace=True)
    
    df_train.loc[:, 'PULocationID'] = df_train['PULocationID'].astype(str)

    x_train, y_train = df_train.drop(columns='duration'), df_train['duration']
    
    train_dict = x_train.to_dict(orient='records')
    x_train_encoded = vectorizer.fit_transform(train_dict)

    model.fit(x_train_encoded, y_train)
    print(model.intercept_)
    return model, vectorizer
