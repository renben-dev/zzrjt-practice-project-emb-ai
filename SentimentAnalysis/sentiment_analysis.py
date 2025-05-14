"""
    this module provide fucntion sentiment_analyzer(text_to_analyze).
    It returns:
        a py dictionary with keys:
            'label':
            'score':
            'status_code':
"""

import json
import requests


def sentiment_analyzer(text_to_analyze):
    """
    Analyzes the sentiment of the provided text using Watson's Sentiment API.

    Parameters:
    text_to_analyze (str): The text whose sentiment is to be analyzed.

    Returns:
    dict: A dictionary containing the sentiment label ('label'), 
          sentiment score ('score'), and the status code ('status_code') 
          of the API response.
    """
    print(text_to_analyze)
    url = (
            'https://sn-watson-sentiment-bert.labs.skills.network/v1/'
            'watson.runtime.nlp.v1/NlpService/SentimentPredict'
    )

    headers= {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    in_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = in_json, headers = headers, timeout = 60)
    dict_response =json.loads(response.text)
    status_code = response.status_code
    if status_code == 200:
        label = dict_response['documentSentiment']['label']
        score = dict_response['documentSentiment']['score']
    else:
        label = None
        score = None
    return {'label': label, 'score': score, 'status_code': status_code}
