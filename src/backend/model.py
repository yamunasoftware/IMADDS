import os
import pickle
from backend.environment import fetch

# Loads ML Models from Directory:
def load_models():
  models = {}
  models_path = fetch('models_path')
  for name in os.listdir(models_path):
    if name.endswith('.pkl'):  
      with open(f'{models_path}/{name}', 'rb') as file:
        models[name] = pickle.load(file)
  return models

# Loads ML Model from Object File:
def load_model(name):
  if name.endswith('.pkl'):  
    with open(fetch('models_path') + f'/{name}', 'rb') as f:
      return pickle.load(f)
  return None

# Predicts Using Loaded Model:
def predict_model(model, data):
  prediction = model.predict(data)
  if prediction > 0.5:
    return 1
  return 0