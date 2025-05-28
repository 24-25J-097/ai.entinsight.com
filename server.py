from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import logging
from routes import router
from fastapi.responses import HTMLResponse
import os

# For specific route
# from routes import predict

# Initialize FastAPI app
app = FastAPI()

app.mount("/static", StaticFiles(directory="public/assets"), name="static")

# Set up logging for server startup and runtime information
logging.basicConfig(level=logging.INFO)

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://entinsight.com", 'https://www.entinsight.com', "https://api.entinsight.com"],  # Adjust based on your frontend's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add a root endpoint to provide information about the API
@app.get("/")
async def root():
   file_path = os.path.join("public", "index.html")  # Adjust if needed
   try:
      with open(file_path, "r", encoding="utf-8") as f:
         html_content = f.read()
      return HTMLResponse(content=html_content, status_code=200)
   except FileNotFoundError:
      return HTMLResponse(content="index.html not found", status_code=404)

# Include the router with all routes
app.include_router(router, prefix="/api")

# Include the specific route from the routes.py file
# app.include_router(predict.router, prefix="/predict", tags=["predict"])

# Log server startup message with a base URL reference
@app.on_event("startup")
async def startup_event():
    logging.info("> ==============================================================")
    logging.info("> Medical Image Analysis API is running...")
    logging.info("> ==============================================================")


# Running the FastAPI server (set to run on port 4000)
# This only work when run: python server.py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=4000)
