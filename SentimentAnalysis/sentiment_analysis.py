
import requests, json

def sentiment_analyzer(text_to_analyze):
    print(text_to_analyze)
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers= {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    in_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = in_json, headers = headers)
    dict_response =json.loads(response.text)
    label = dict_response['documentSentiment']['label']
    score = dict_response['documentSentiment']['score']
    return {label, score}
