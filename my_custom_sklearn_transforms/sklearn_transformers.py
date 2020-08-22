from sklearn.base import BaseEstimator, TransformerMixin

class CombMedias:
    def __init__(self, columns, name):
        self.columns = columns
        self.name = name

    def fit(self, X, y=None):
        return self
      
    def comb(self, data):
        return pd.Series([
        np.sum([data[nota] for nota in self.columns])/len(self.columns)], index =[f'COMB_{self.name}']
        )
          
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        data = data.join(data.apply(self.comb, axis=1))
        return data
