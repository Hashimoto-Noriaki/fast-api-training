from fastapi import FastAPI

app = FastAPI()#インスタンス化

@app.get("/countries/{country_name}")#ルーティング　@はdecorator
async def country(country_name:str):
    return {"country_name":country_name}
