# AI-Powered Intrusion Detection System

A machine learning-based Intrusion Detection System (IDS) that detects and classifies malicious network activities. This project uses AI and cybersecurity techniques to analyze real-time traffic and identify potential threats.

📌 Features
✅ Real-time network monitoring using AI
✅ Detects cyber threats (DDoS, malware, phishing, etc.)
✅ FastAPI-based REST API for prediction
✅ Machine learning & deep learning models
✅ Docker support for easy deployment

📂 Project Structure

AI-Intrusion-Detection/
│── dataset/                  # NSL-KDD dataset
│── model/                    # Trained ML model
│── src/
│   ├── preprocess.py         # Data preprocessing script
│   ├── train.py              # Model training script
│   ├── predict.py            # Load model & make predictions
│── api/
│   ├── main.py               # FastAPI server
│── Dockerfile                # Containerization
│── requirements.txt          # Dependencies
│── README.md                 # Project documentation


Setup & Installation
1️⃣ Clone the repository
git clone https://github.com/Manikantasai330/cyberai.git
cd AI-Intrusion-Detection
2️⃣ Install dependencies

pip install -r requirements.txt
3️⃣ Preprocess the dataset

python src/preprocess.py
4️⃣ Train the model

python src/train.py
5️⃣ Run FastAPI server

uvicorn api.main:app --host 0.0.0.0 --port 8000
🚀 API Usage
Predict an Intrusion
Send a POST request with network traffic features:

{
    "features": [0.1, 0.5, -1.2, 3.4, ...]
}
📌 Endpoint:

POST http://127.0.0.1:8000/predict/
🐳 Docker Deployment
1️⃣ Build the Docker image

docker build -t ai-ids .
2️⃣ Run the container
docker run -p 8000:8000 ai-ids
📜 License
This project is open-source and available under the MIT License.



