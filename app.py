import os
import openai
import json

from flask import Flask, request, jsonify, Response

app = Flask(__name__)
openai.api_key = "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"

@app.route('/json-data', methods=['POST'])
def json_data():
    data = request.get_json()
    
    def stream(data):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=data,
            stream=True
        )
        for line in response:
            yield 'data: %s\n' % line
            
    return Response(stream(data), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
