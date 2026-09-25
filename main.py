from fastapi import FastAPI



app = FastAPI()


get("/health")

def health():

    data = {"status": "ok"}

    return data



@app.get("/")

 root():

    return {"message": "Hello



if __name__ == "__main__"

    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
