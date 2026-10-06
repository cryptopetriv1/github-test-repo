from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from app.api.endpoints import router as api_router

app = FastAPI(
    title="DexTokenomics API",
    description="An API to fetch tokenomics data from DexScreener for AI agents like Claude.",
    version="1.0.0"
)

# Setup templates
templates = Jinja2Templates(directory="app/templates")

# Include our API routes
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
