from flask import Flask, render_template, request, jsonify
import nltk
import pickle
from nltk.corpus import stopwords
import re
from nltk.stem.porter import PorterStemmer
from googlesearch import search

app = Flask(__name__)
ps = PorterStemmer()
model = pickle.load(open('model.pkl', 'rb'))
tfidfvect = pickle.load(open('vectorizer.pkl', 'rb'))
def get_reliable_source(query):
    search_results = search(query, num_results=5)  
    source_url = next(search_results, None)
    return source_url
def predict(text):
    review = re.sub('[^a-zA-Z]', ' ', text)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    review_vect = tfidfvect.transform([review]).toarray()
    prediction = 'FAKE' if model.predict(review_vect) == 0 else 'REAL'
    if prediction == 'REAL':
        source_url = get_reliable_source(text)
        return prediction, source_url
    else:
        return prediction, None
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
@app.route('/', methods=['POST'])
def webapp():
    text = request.form['text']
    prediction, source_url = predict(text)
    return render_template('index.html', text=text, result=prediction, source_url=source_url)
@app.route('/predict/', methods=['GET', 'POST'])
def api():
    text = request.args.get("text")
    prediction, source_url = predict(text)
    return jsonify(prediction=prediction, source_url=source_url)
if __name__ == "__main__":
    app.run()
