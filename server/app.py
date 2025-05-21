from flask import Flask, jsonify
from flask_cors import CORS

# Importing files that I made:
from data import *


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

#Route to get data
@app.route('/getDataForGraphs', methods=['GET'])
def getDataForGraphs():
    db_obj = ExamineData()
    regression_json = db_obj.linear_regression_basic()
    return jsonify(regression_json)


if __name__ == '__main__':
    app.run(debug=True)