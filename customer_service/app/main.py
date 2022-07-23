from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello":"World","customer":"Jason Adoo","id":"16","country":"Ghana"}


@app.get("/customer/{p_id}")
def read_customer(c_id:int,q:Union[str,None]=None):
    return {"id":c_id,"q":"q","name":"Jason Adoo","role":"Distro"}