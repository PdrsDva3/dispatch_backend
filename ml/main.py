from ml.internal.app.vision import app1

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app1, host="0.0.0.0", port=8001)

