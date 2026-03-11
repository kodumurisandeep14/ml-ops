from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression #importing linear regression algorithm from scikitlearn library
from pydantic import BaseModel
app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials= True,
                   allow_methods=["*"],
                   allow_headers=["*"])

df= pd.read_csv("house_data.csv")
X= df[["size","bedrooms","age"]]
y=df["price"]
model = LinearRegression()
model.fit(X,y)
class HouseInput(BaseModel):
    size :float
    bedrooms: int
    age: int
@app.post("/predict")
def predict_price(input:HouseInput):
    features = np.array([[input.size,input.bedrooms,input.age]])
    price = model.predict(features)
    return {
        "Predicted_price": int (price[0])
    }


