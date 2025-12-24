import pickle

def load_model():
  with open('/main/src/ddm.pkl', 'rb') as f:
    return pickle.load(f)

def predict_model(model, data):
  return model.predict(data)