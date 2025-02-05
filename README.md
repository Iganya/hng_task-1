# Number Classification API

## Overview
This API classifies a given number and returns interesting mathematical properties, including whether it's prime, Armstrong, or even/odd. It also fetches a fun fact using the Numbers API.

## Features
- Identifies if a number is prime
- Identifies if a number is an Armstrong number
- Determines whether a number is even or odd
- Computes the sum of its digits
- Fetches a fun fact from the Numbers API
- Returns data in JSON format

## Technology Stack
- **FastAPI** (Backend framework)
- **requests** (For API requests)
- **Python 3.9+**



## Getting Started

### 1. Clone the Repository
```bash
git clone 
cd your-repo
```

### 2. Install Dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run the API
```bash
fastapi dev
```
The API runs on `http://127.0.0.1:8000` by default.


## API Specification

### Endpoint: Classify Number
- **URL:** `GET /api/classify-number?number=<int>`
- **Request Parameter:** `number` (integer)

### Response Format

#### 200 OK 
```json
{
    "number": 429,
    "is_prime": false,
    "is_perfect": false,
    "properties": [
        "odd"
    ],
    "digit_sum": 15,
    "fun_fact": "429 is the 7^{th} Catalan number."
}
```
### Response Format for invalid input

#### 400 Bad Request
```json
{
    "number": "l6",
    "error": true
}
```


## Deployment
The API is deployed to a publicly accessible endpoint.
### **Deploy to Render**
1. Sign up for a free account at Render.
2. Create a new Web Service.
3. Connect your GitHub repository.
4. Set the following configuration:
5. Build Command: pip install -r requirements.txt
6. Start Command: fastapi run main.py
7. Deploy the service.


## License
This project is open-source and available under the MIT License.
