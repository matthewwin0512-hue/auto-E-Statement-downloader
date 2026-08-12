from fastapi import FastAPI
from app.downloader import download_pdf

app = FastAPI(title="E-Statement Downloader API")

@app.get("/")
def read_root():
    return {"message": "PDF Downloader API is running"}

@app.post("/download")
def download():
    result = download_pdf("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf")
    return result