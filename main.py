from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World, but this time we used github actions"}

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)