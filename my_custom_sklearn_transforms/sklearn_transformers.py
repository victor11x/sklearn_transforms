class DropColumns(BaseEstimator, TransformerMixin):
        def __init__(self, columns):
            self.columns = columns
        def fit(self, X, y=None):
            return self
        def transform(self, X):
            # Primeiro realizamos a cópia do dataframe 'X' de entrada
            data = X.copy()
            # Retornamos um novo dataframe sem as colunas indesejadas
            return data.drop(labels=self.columns, axis='columns')
      
        def comb(self, data):
            return pd.Series([
        np.sum([data[nota] for nota in self.columns])/len(self.columns)], index =[f'COMB_{self.name}']
        )
          
        def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
            data = X.copy()
            data = data.join(data.apply(self.comb, axis=1))
            return data
