import pickle
from backend.environment import fetch

def load_model(name):
  with open(fetch('models_path') + f'/{name}', 'rb') as f:
    return pickle.load(f)

def predict_model(model, data):
  return model.predict(data)