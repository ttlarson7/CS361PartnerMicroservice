from flask import Flask, request, jsonify
import json
app = Flask(__name__)

@app.route('/process', methods=['POST'])
def handle_post_request():
    if request.method == 'POST':
        #This code here gets the JSON file that was sent to the microservice
        data = request.json
        print("Received POST request from the API Call")

        #This code gets the information from the JSON file that was sent to the microservice
        name = data['Name']
        transactionType = data['TransactionType']
        timeFrame = data['TimeFrame']

        #This code here reads from teh JSON where all the information is stored.
        f = open('storage.json')
        database = json.load(f)
        f.close()


        response = {
            "Name": name,
            "TransactionType": transactionType,
            "TimeFrame": timeFrame,
            "Amount": database[name][transactionType][timeFrame]
        }
        

        return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)  
