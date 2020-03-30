from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api/v1')
def greeting():
  return 'Welcome JW Machine Learning API'


@app.route('/api/v1/getsentiment', methods=['POST'])
def getSentiment():
  sentence = request.json['sentence']
  # you need to perform sentiment analysis here.
  return sentence 

@app.route('/api/v1/gettaggedpartsofspeech', methods=['POST'])
def getTaggedPartsOfSpeech():
  sentence = request.json['sentence']
  # you need to perform part of speech analysis and respond the client
  return sentence
