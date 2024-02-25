# CS361PartnerMicroservice

Microservice File: microservice.py

# Instructions

**Pre Step**
Start the microservice

**Step 1**
You have to have some sort of API POST request set up. This can be done through a variety of different ways such as Axios for JS, or the Requests module in Python. 

**Step 2**
Send the POST Request to "http://localhost:5000/process", which is what the microservice server will be running on, make sure to send a JSON file with the request styled like this:
example = {
        "Name": "John Doe",
        "TransactionType": "expenses",
        "TimeFrame": "sixMonths"
    };

Here is an example call to the microservice:

"""async function runPythonScript() {
    const example = {
        "Name": "John Doe",
        "TransactionType": "expenses",
        "TimeFrame": "sixMonths"
    };

    try {
        const pythonResponse = await axios.post('http://localhost:5000/process', example);
        console.log("Response from Python script:");
        console.log(pythonResponse.data);
        
    } catch (error) {
        console.error("Error sending request to Python script:", error.message);
       
    }
}"""

**Step 3**
The microservice will automatically handle retrieving the data.

**Step 4**
Once you send the request, make sure you have some way to receive the response. You can look at my request.js for an example of that. That response will be a JSON containing the amount that 
the user has spent in the timeframe given.
The response will have the structure of this:
{
  Amount: 0,
  Name: 'John Doe',
  TimeFrame: 'sixMonths',
  TransactionType: 'expenses'
}

To handle the reponse, you can assign it to a variable like so:

"""const pythonResponse = await axios.post('http://localhost:5000/process', example);"""


This will let you handle the the response data.

**Step 5**
Be happy that you have successfully accessed your microservice!
