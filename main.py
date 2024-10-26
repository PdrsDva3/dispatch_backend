from fastapi import FastAPI
from internal.app.app import app
from internal.tg_bot.init import start_tg
import internal.tg_bot.bot

if __name__ == "__main__":
    import uvicorn
    start_tg()

    uvicorn.run(app, host="0.0.0.0", port=8000)
