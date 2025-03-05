<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dataset to API - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2, h3 {
            color: #333;
        }
        code {
            background: #eee;
            padding: 3px 5px;
            border-radius: 5px;
        }
        pre {
            background: #eee;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📌 Dataset to API</h1>
        <p><strong>Convert datasets (CSV, JSON, Excel) into a FastAPI-powered API.</strong></p>

        <h2>🚀 Features</h2>
        <ul>
            <li>Upload CSV, JSON, or Excel datasets</li>
            <li>View dataset in JSON format</li>
            <li>Fetch column names dynamically</li>
            <li>Retrieve data from specific columns</li>
        </ul>

        <h2>📂 Installation</h2>
        <pre><code>git clone https://github.com/your-username/Dataset-to-API.git
cd Dataset-to-API
pip install -r requirements.txt
</code></pre>

        <h2>▶️ Run Locally</h2>
        <pre><code>uvicorn main:app --reload</code></pre>

        <h2>🖥️ API Endpoints</h2>
        <ul>
            <li><code>GET /</code> - Home page (Upload UI)</li>
            <li><code>POST /upload/</code> - Upload dataset</li>
            <li><code>GET /data/</code> - View dataset</li>
            <li><code>GET /columns/</code> - Get column names</li>
            <li><code>GET /column/{col_name}</code> - Get data from a column</li>
        </ul>

        <h2>🌍 Deployment on Render</h2>
        <p>To deploy on Render, follow these steps:</p>
        <ol>
            <li>Push the project to GitHub</li>
            <li>Go to <a href="https://render.com" target="_blank">Render</a> & create a new Web Service</li>
            <li>Select your GitHub repo & configure settings</li>
            <li>Use the command <code>uvicorn main:app --host 0.0.0.0 --port 10000</code> to start the app</li>
            <li>Deploy & get your API URL!</li>
        </ol>

        <h2>📜 License</h2>
        <p>MIT License</p>

        <h2>🤝 Contributing</h2>
        <p>Pull requests are welcome! 😊</p>
    </div>
</body>
</html>
