from flask import Flask, request, jsonify
import json
import requests
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/adams', methods=['GET'])
def api_all():
    # Create some test data for our catalog in the form of a list of dictionaries.
    response = [
        {
         'id': '1',
         'title': ' නිමල් පෙරේරා කමල් සිල්වා සුනිල් නිශාන්ත',
         'name': 'කමල්',
         'status': 'newuser',
         'identification': 'false',
         'attempt': '6',
         'confirm': '1'
         }

    ]
    now = datetime.now()
    print(now)
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8001)
