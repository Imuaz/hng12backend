# Simple Django API

##  A public API that returns the following informations in JSON format:
- Personal email address.
- The current datetime as an ISO 8601 formatted timestamp.
- The GitHub URL of the project's codebase.

## Setup Instructions
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

## API Documentation
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