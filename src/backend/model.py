import os
import pickle
from backend.environment import fetch

# Predicts Using Loaded Model:
def predict_model(model, data):
  prediction = model.predict(data)
  if prediction > 0.5:
    return 1
  return 0

# Loads ML Models from Directory:
def load_models():
  models = {}
  models_path = fetch('models_path')
  for name in os.listdir(models_path):
    models[name] = _load_model(name)
  return models

# Loads ML Model from Object File:
def _load_model(name):
  if name.endswith('.pkl'):  
    with open(fetch('models_path') + f'/{name}', 'rb') as f:
      return pickle.load(f)
  return None