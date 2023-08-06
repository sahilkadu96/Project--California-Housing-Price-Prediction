import pickle
from fastapi import FastAPI
from pydantic import BaseModel
from starlette import status

app = FastAPI()

class UserInput(BaseModel):
    medinc: float
    houseage: int
    averooms: float
    avebdrms: float
    population: float
    aveoccup: float
    latitude: float
    longitude: float


with open(r'C:\Users\Sahil\.spyder-py3\california_housing\model.pkl', 'rb') as f:
    model = pickle.load(f)


@app.post('/predict')
def predict_price(input_:UserInput):
    result = model.predict([[input_.medinc, input_.houseage, input_.averooms, input_.avebdrms, input_.population, input_.aveoccup,
                             input_.latitude, input_.longitude ]])
    return result[0]