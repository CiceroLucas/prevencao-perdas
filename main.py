from fastapi import FastAPI, UploadFile, File
from models.predictor import treinar_modelo, prever_perda
import pandas as pd

app = FastAPI()

@app.post("/prever")
async def upload_csv(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    modelo, encoder = treinar_modelo(df)
    predicoes = prever_perda(df, modelo, encoder)
    return {"previsoes": predicoes.to_dict(orient="records")}
