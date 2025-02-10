# HNG12 Backend

## Stage 0

### Description

A public API that returns the following informations in JSON format:
- Personal email address.
- The current datetime as an ISO 8601 formatted timestamp.
- The GitHub URL of the project's codebase.

### Setup Instructions
1. Clone the repository:
    ```
    git clone https://github.com/Imuaz/hng12backend.git
    
    cd hng12backend
    ```
2. Create and activate a virtual environment:
    ```
     python3 -m venv .venv # on Windows: python -m venv .venv

    source .venv/bin/activate #on Windows: .\.venv\Scripts\activate
    ```
3. Install the project dependencies
   ```
   pip3 install -r requirements.txt # use 'pip ..' on Windows
   ```

4. Start the development server:
   ```
   python3 manage.py runserver # 'python' on Windows
   ```

### API Documentation
**Endpoint:**
- GET /api/user/

**Request:**
- No parameters

**Example Usage:**
```
curl http://127.0.0.1:8000/api/user/
```

**Response example:**
```
{
    "email": useremail@email.com",
    "current_datetime": "2025-02-30T09:30:00Z",
    "github_url": "https://github.com/username/repo"
}
```

***Learn more on HNG python developers*** :point_down:
- [HNG Python Developers](https://hng.tech/hire/python-developers)

## Stage 1

### Description
***Number Classification API*** takes a number and returns interesting mathematical properties about it, along with a fun fact.

### API Documentation
**Endpoint**
    - **GET /api/classify-number?number=371**

**Request**
- Query parameter: `number` (integer)

**Response** (200 OK)
```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

**Response (400 Bad Request)**
```json
{
  "number": "alphabet",
  "error": true
}
```
