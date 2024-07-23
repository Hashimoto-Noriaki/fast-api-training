from typing import Optional
from fastapi import FastAPI

app = FastAPI()#インスタンス化

#必須でないパラメーター
@app.get("/countries/")#ルーティング　@はdecorator
async def country(country_name: Optional[str] = None, country_no: Optional[int] = None):
    return {
        "country_name": country_name,
        "country_no": country_no
    }
#http://127.0.0.1:8000/countries/

# クエリパラメーター
# @app.get("/countries/")#ルーティング　@はdecorator
# async def country(country_name: str = 'japan',country_no: int =1):#パスパラメーターはないけど、引数が設定されているのがクエリパラメーター
#     return {
#         "country_name": country_name,
#         "country_no": country_no
#     }

#http://127.0.0.1:8000/countries/?country_name=England&country_no=3

#パスパラメーター
# @app.get("/countries/japan")#ルーティング　@はdecorator
# async def country():
#     return {"message":'日本だー'}

# @app.get("/countries/{country_name}")#ルーティング　@はdecorator
# async def country(country_name:str):
#     return {"country_name":country_name}
