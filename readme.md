# Streamlit Application

This is a Streamlit application that requires a secret key for proper functioning. Follow the instructions below to set up and run the application.

## Prerequisites

Make sure you have the following installed:
- Python 3.6 or later
- pip (Python package installer)

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine.

```sh
git clone https://github.com/maheshsai252/Career-bot.git
cd app
```
### 2. Install Requirements
Install the necessary Python packages using pip:

```
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a .env file in the root directory of the project and add your secret key to it.

Example .env File:
```
SECRET_KEY=your_secret_key_here
```

### 4. Run the Streamlit Application

Run the Streamlit application using the following command:

```
streamlit run app.py
```
### 5. Access the Application

Open your web browser and go to http://localhost:8501 to access the application.