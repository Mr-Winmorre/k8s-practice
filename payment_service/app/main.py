from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello":"World","payment":"GHC 7000","id":"123"}


@app.get("/payment/{p_id}")
def read_payment(p_id:int,q:Union[str,None]=None):
    return {"id":p_id,"q":"q","number":"+233 55 455 0436"}