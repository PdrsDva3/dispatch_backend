from fastapi import FastAPI, HTTPException

from deploy.migrations import get_report

app2 = FastAPI()

@app2.get("/get_report")
async def get_report_h(date):
    report = await get_report(date)
    if report is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return report

# @app2.get("/download_report")
# async def download_report(date):
#