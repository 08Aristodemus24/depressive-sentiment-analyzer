from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

# ff. imports are for getting secret values from .env file
from pathlib import Path
import os

from modelling.utilities.loaders import load_model
from modelling.utilities.preprocessors import (
    lower_words,
    remove_contractions,
    rem_non_alpha_num,
    rem_numeric,
    rem_stop_words,
    stem_corpus_words,
    lemmatize_corpus_words,
    strip_final_corpus,
    translate_labels)

from modelling.utilities.feature_engineers import (
    # pre feature engineering
    count_capital_chars,
    count_capital_words,
    count_punctuations,
    count_sent,
    count_stopwords,

    # you can use this for X/twitter posts
    count_htags,
    count_mentions,
    
    # post feature engineering
    count_chars,
    count_words,
    count_unique_words)

import numpy as np

# configure location of build file and the static html template file
app = Flask(__name__, template_folder='static')

# since simple html from url http://127.0.0.1:5000 requests to
# api endpoint at http://127.0.0.1:5000/ we must set the allowed
# origins or web apps with specific urls like http://127.0.0.1:5000
# to be included otherwise it will be blocked by CORS policy
CORS(app, origins=["http://localhost:5173", "http://127.0.0.1:5000", "https://dsa-api.vercel.app"])

models = {}
saved_ddr_tfidf_vec = None
saved_ddr_le = None

def load_models():
    """
    prepares and loads sample input and custom model in
    order to use trained weights/parameters/coefficients
    """

    # recreate model architecture
    saved_lgbm_clf = load_model('./modelling/saved/models/lgbm_clf.pkl')
    saved_xgb_clf = load_model('./modelling/saved/models/xgb_clf.pkl')
    saved_ada_clf = load_model('./modelling/saved/models/ada_clf.pkl')
    models[type(saved_lgbm_clf).__name__] = saved_lgbm_clf
    models[type(saved_xgb_clf).__name__] = saved_xgb_clf
    models[type(saved_ada_clf).__name__] = saved_ada_clf

def load_preprocessors():
    """
    prepares and loads the saved encoders, normalizers of
    the dataset to later transform raw user input from
    client-side
    """

    global saved_ddr_tfidf_vec, saved_ddr_le
    saved_ddr_tfidf_vec = load_model('./modelling/saved/misc/ddr_tfidf_vec.pkl')
    saved_ddr_le = load_model('./modelling/saved/misc/ddr_le.pkl')

load_models()
load_preprocessors()

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return 'This page does not exist', 404

# upon loading of client side fetch the model names
@app.route('/model-names', methods=['GET'])
def retrieve_model_names():
    """
    flask app will run at http://127.0.0.1:5000 if /
    in url succeeds another string <some string> then
    app will run at http://127.0.0.1:5000/<some string>

    returns json object of all model names loaded upon
    start of server and subsequent request of client to
    this view function
    """

    data = {
        'model_names': list(models.keys())
    }

    # return data at once since no error will most likely
    # occur on mere loading of the model
    return jsonify(data)

@app.route('/predict', methods=['POST'])
def predict():
    # extract raw data from client
    raw_data = request.form
    print(raw_data)

    # encoding and preprocessing
    message = raw_data['message']

    # pre feature engineering
    n_capital_chars = count_capital_chars(message)
    n_capital_words = count_capital_words(message)
    n_sents = count_sent(message)
    n_stopwords = count_stopwords(message)

    # preprocessing
    message = lower_words(message)
    message = remove_contractions(message)
    message = rem_non_alpha_num(message)
    message = stem_corpus_words(message)
    message = lemmatize_corpus_words(message)
    message = strip_final_corpus(message)

    # post feature engineering
    n_chars = count_chars(message)
    n_words = count_words(message)
    n_unique_words = count_unique_words(message)


    model_name = raw_data['model_name']
    print(model_name)
    model = models[model_name]

    # once x features are collected normalize the array on the 
    # saved scaler
    X_vec = saved_ddr_tfidf_vec.transform(message).toarray().flatten()
    print(X_vec)
    
    features = np.hstack([[n_capital_chars, n_capital_words, n_sents, n_stopwords, n_chars, n_words, n_unique_words], X_vec]).reshape(1, -1)
    
    # predictor
    Y_preds = model.predict(features)
    print(Y_preds)
    decoded_sparse_Y_preds = saved_ddr_le.inverse_transform(Y_preds)
    print(decoded_sparse_Y_preds)
    translated_labels = translate_labels(decoded_sparse_Y_preds, translations={'mild': 'mild', 'minimum': 'minimum', 'moderate': 'moderate', 'severe': 'severe'})
    print(translated_labels)

    return jsonify({'sentiment': translated_labels.tolist()})