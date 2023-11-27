from flask import Flask, request
from flask_cors import CORS
import getInput
import astar
import helper
import json
app = Flask(__name__)
CORS(app)
@app.route('/calculate', methods=['GET'])
def home():
    raw_input = request.args.get('pntdata').split(',')
    mappedSourceLoc = getInput.getNearestPoint(raw_input[0], raw_input[1])
    mappedDestLoc = getInput.getNearestPoint(raw_input[2], raw_input[3])
    print("Location of the first point " + raw_input[0] + " " + raw_input[1])
    print("Location of the second point " + raw_input[2] + " " + raw_input[3])
    print("nearest of the first point " + mappedSourceLoc[0] + " " + mappedSourceLoc[1])
    print("nearest of the second point " + mappedDestLoc[0] + " " + mappedDestLoc[1])
    start = helper.getOSMId(float(mappedSourceLoc[0]), float(mappedSourceLoc[1]))
    print("Start Id: " + start)
    end = helper.getOSMId(float(mappedDestLoc[0]), float(mappedDestLoc[1]))
    print("End Id: " + end)
    pathDict, finalDistance = astar.astarID(start, end)
    print("Shortest distance: " + str(finalDistance))
    response = helper.getResponseLeafLet2(pathDict, end)
    # response = helper.getResponseLeafLet(pathDict, (float(mappedDestLoc[0]), float(mappedDestLoc[1])))
    # return json.dumps(getInput.getAllPoints())
    return json.dumps(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
