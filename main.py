from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from fastapi.responses import JSONResponse


app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["GET"],  # Allow only GET requests
    allow_headers=["*"],  # Allow all headers
)

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_perfect(n: int) -> bool:
    """Check if a number is perfect."""
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n


def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    num_digits = len(digits)
    return sum(d**num_digits for d in digits) == n


def get_digit_sum(n: int) -> int:
    """Calculate the sum of the digits of a number."""
    return sum(int(d) for d in str(n))


def get_fun_fact(n: int) -> str:
    """Fetch a fun fact about the number from the Numbers API."""
    url = f"http://numbersapi.com/{n}/math"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return "No fun fact available."


@app.get("/api/classify-number")
async def classify_number(number: str = None):
    try:
        number = int(number)
        # Determine properties
        properties = []
        if is_armstrong(number):
            properties.append("armstrong")
        properties.append("odd" if number % 2 else "even")

        # Fetch fun fact
        fun_fact = get_fun_fact(number)

        # Return response
        response_data = {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": get_digit_sum(number),
            "fun_fact": fun_fact,
        }
        return JSONResponse(content=response_data, status_code=200)
    
    except ValueError:
        return JSONResponse(content={"number": str(number) if number else None, "error": True}, status_code=400)
    