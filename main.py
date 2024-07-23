from fastapi import FastAPI

app = FastAPI()#インスタンス化

@app.get("/countries/japan")#ルーティング　@はdecorator
async def country():
    return {"message":'日本だー'}

@app.get("/countries/{country_name}")#ルーティング　@はdecorator
async def country(country_name:str):
    return {"country_name":country_name}
