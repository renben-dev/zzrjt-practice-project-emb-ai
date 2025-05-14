''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the sentiment_analyzer function from the package created: TODO
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer


#Initiate the flask app : TODO

app = Flask("SentimentAnalyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''

    text_to_analyze = request.args.get('textToAnalyze')

    resp = sentiment_analyzer(text_to_analyze)

    label = resp['label']
    score = resp['score']

    return f"The provided test has a {label} sentiment with a score of {score}"
    # TODO

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')
    #TODO

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''#TODO

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)
