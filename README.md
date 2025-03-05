# 📌 Dataset to API

Convert datasets (CSV, JSON, Excel) into a FastAPI-powered API.

## 🚀 Features
- Upload CSV, JSON, or Excel datasets
- View dataset in JSON format
- Fetch column names dynamically
- Retrieve data from specific columns

## 📂 Installation
```bash
git clone https://github.com/your-username/Dataset-to-API.git
cd Dataset-to-API
pip install -r requirements.txt
```

## ▶️ Run Locally  
Start the FastAPI application:  
```bash
uvicorn main:app --reload
```

## 🖥️ API Endpoints  
- **`GET /`** - Home page (Upload UI)  
- **`POST /upload/`** - Upload dataset  
- **`GET /data/`** - View dataset  
- **`GET /columns/`** - Get column names  
- **`GET /column/{col_name}`** - Get data from a column  

## 🌍 Deployment on Render  
To deploy on Render:  

1. Push the project to GitHub.  
2. Go to [Render](https://render.com) and create a new Web Service.  
3. Select your GitHub repository and configure settings.  
4. Use the command below as the start command:  
```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```
5. Deploy and get your API URL!  

## 🛠 Requirements  
- Python 3.7+  
- FastAPI  
- Uvicorn  
- Pandas  

## 🔧 Usage Example  
After starting the API, you can test it using `curl` or Postman:  
```bash
curl -X POST "http://127.0.0.1:8000/upload/" -F "file=@your_dataset.csv"
```
## 🏗 Project Structure  
```bash
/Dataset-to-API
  ├── uploaded_files/     # Stores uploaded datasets
  ├── main.py             # API Code
  ├── templates/          # HTML UI Files
  │    ├── index.html     # Upload page
  ├── requirements.txt
```
## 📜 License  
MIT License  

## 🤝 Contributing  
Pull requests are welcome! 😊  
