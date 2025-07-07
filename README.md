
# 📰 Fake News Detector

Fake News Detector is a machine learning-based web application that predicts whether a given news article is **real or fake**. Built to combat the growing issue of misinformation, it uses natural language processing (NLP) techniques and a logistic regression model trained on a labeled dataset of news articles.

## 🚀 Features

- 🧠 **ML-Powered Predictions**: Determines the authenticity of news content using logistic regression.
- 📄 **Text Analysis**: Users can input custom news text or headlines.
- 🌐 **Web Interface**: Simple Flask-based interface for easy user interaction.
- ⚡ **Real-time Results**: Instant prediction output upon submitting the input text.

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Python (Flask)
- **Machine Learning**: Scikit-learn, NLP with CountVectorizer
- **Deployment**: Localhost / Flask server

## 📂 Project Structure

```
FakeNewsDetector/
│
├── templates/           # HTML templates
├── static/              # Static files like CSS
├── model/               # Trained model and vectorizer
├── app.py               # Flask application
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies
```

## 🧪 How It Works

1. The user enters a news headline or paragraph.
2. The text is vectorized using `CountVectorizer`.
3. The logistic regression model predicts whether it's real or fake.
4. The result is displayed instantly.

## 📌 Installation & Usage

1. **Clone the repository**  
```bash
git clone https://github.com/BhavanaMinchu/FakeNewsDetector.git
cd FakeNewsDetector
```

2. **Create virtual environment & activate**  
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install dependencies**  
```bash
pip install -r requirements.txt
```

4. **Run the app**  
```bash
python app.py
```

5. **Visit on browser**  
```
http://127.0.0.1:5000/
```

## 📊 Dataset

This project uses a dataset of labeled news articles with "real" or "fake" labels. You can improve the model by training on more diverse and updated datasets.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

> ⚠️ Disclaimer: This project is built for educational and assistive purposes. Please verify news from official sources.
