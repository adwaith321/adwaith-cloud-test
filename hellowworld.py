from fastapi import FastAPI

app = FastAPI()

@app.get("/hellowworld")
async def read_root():
    return("Meassage":"Hellow world Congrats")