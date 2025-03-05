from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
import pandas as pd
import shutil
import os
import glob

# Initialize FastAPI
app = FastAPI()

# Create a folder to store uploaded files
UPLOAD_FOLDER = "uploaded_files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Function to load the latest uploaded dataset
def load_latest_dataset():
    files = glob.glob(f"{UPLOAD_FOLDER}/*")
    if not files:
        return None
    latest_file = max(files, key=os.path.getctime)

    # Load dataset dynamically based on file type
    try:
        if latest_file.endswith(".csv"):
            return pd.read_csv(latest_file)
        elif latest_file.endswith(".json"):
            return pd.read_json(latest_file)
        elif latest_file.endswith(".xlsx"):
            return pd.read_excel(latest_file)
        else:
            return None
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

# 1. Home Page - UI for Uploading Dataset
@app.get("/", response_class=HTMLResponse)
def serve_ui():
    try:
        with open("templates/index.html", "r") as file:
            return HTMLResponse(content=file.read())
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="index.html not found in 'templates' folder")

# 2. Upload Dataset API
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    
    # Prevent duplicate file uploads
    if os.path.exists(file_path):
        raise HTTPException(status_code=400, detail="File with the same name already exists!")

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"message": f"File '{file.filename}' uploaded successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving file: {str(e)}")

# 3. View Dataset as API
@app.get("/data/")
def get_data():
    df = load_latest_dataset()
    if df is None:
        raise HTTPException(status_code=400, detail="No dataset uploaded.")
    return JSONResponse(content=df.to_dict(orient="records"))

# 4. Get Column Names
@app.get("/columns/")
def get_columns():
    df = load_latest_dataset()
    if df is None:
        raise HTTPException(status_code=400, detail="No dataset uploaded.")
    return {"columns": df.columns.tolist()}

# 5. Get Data from a Specific Column
@app.get("/column/{col_name}")
def get_column_data(col_name: str):
    df = load_latest_dataset()
    if df is None:
        raise HTTPException(status_code=400, detail="No dataset uploaded.")

    if col_name not in df.columns:
        raise HTTPException(status_code=404, detail=f"Column '{col_name}' not found.")

    return {col_name: df[col_name].tolist()}
