from fastapi import FastAPI

app = FastAPI()#インスタンス化

# クエリパラメーター
@app.get("/countries/{country_name}")#ルーティング　@はdecorator
async def country(country_name: str = 'japan',city_name: str = 'Tokyo'):#パスパラメーターはないけど、引数が設定されているのがクエリパラメーター
    return {
        "country_name": country_name,
        "city_name": city_name
    }

#http://127.0.0.1:8000/countries/?country_name=England&country_no=3

#http://127.0.0.1:8000/countries/england?city_name=London

#パスパラメーター
# @app.get("/countries/japan")#ルーティング　@はdecorator
# async def country():
#     return {"message":'日本だー'}

# @app.get("/countries/{country_name}")#ルーティング　@はdecorator
# async def country(country_name:str):
#     return {"country_name":country_name}
