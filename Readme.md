# Cosmocloud Assignment Submission ✅

## Assignment Submission

The **Student Management API** assignment has been successfully completed and is now ready for submission. All required functionality has been implemented, including creating, updating, deleting, and retrieving student records, with additional filtering features. The API is fully tested and deployed. You can explore and test the API using the following links:

- [Postman Workspace Link](https://www.postman.com/flight-physicist-9054540/workspace/cosmocloud-assignment/collection/27758306-f45d427e-54c1-4712-8556-fee3ad2b214d?action=share&creator=27758306) to test the API endpoints.
- [Live API Link](https://cosmocloud-assignment-beta.vercel.app/) to interact with the live version of the API.

## Getting Started

Follow these steps to set up the project:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/dee077/Cosmocloud-Assignment.git
   cd Cosmocloud-Assignment
   ```

2. **Create and Activate Virtual Environment:**

    Windows:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

    MacOs:  
    ```bash
    python3 -m venv venv
    source venv/bin/activate  
    ```

3. **Install Dependencies:**
    
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the App:**

    ```
    uvicorn app.main:app --reload
    ```
    Access the app at `http://localhost:8000/`
