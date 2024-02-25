const PORT = process.env.PORT || 3000;
const express = require('express');
const app = express();
const axios = require('axios');

async function runPythonScript() {
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
}

runPythonScript();
// app.use(express.json());

// app.post("/run", async (req, res) => {
    
// });

// app.listen(PORT, () => {
//     console.log(`Server running on port ${PORT}`);
// });
