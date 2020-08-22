from sklearn.base import BaseEstimator, TransformerMixin

class MediaNotas(BaseEstimator, TransformerMixin):
  '''Rebece uma string para ser o nome da coluna de medias''' 
  def __init__(self, nome_da_coluna):
    self.nome = nome_da_coluna
  
  def fit(self, X, y=None):
    return self

  def media_notas(self, x):
    notas = []
    notas.append(x['NOTA_DE'])
    notas.append(x['NOTA_EM'])
    notas.append(x['NOTA_MF'])
    notas.append(x['NOTA_GO'])
    media = np.sum(notas)/4
    return pd.Series(data=[media], index=[self.nome])

  def transform(self, X):
    data = X.copy()

    coluna_media = data.head().apply(self.media_notas, axis=1)
    data_c_media = data.head().join(coluna_media)
    return data_c_media
