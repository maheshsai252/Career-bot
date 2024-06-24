# Streamlit Application

This is a Streamlit application that requires a secret key for proper functioning. Follow the instructions below to set up and run the application.

 Video Demonstration - https://youtu.be/0GX4GHMyNNI

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
### 3. Obtain API key from Google AI Studio

- visit https://aistudio.google.com/app/apikey
- Accept terms and conditions
- click on "Create API Key" and select existing project or create new project.
- Copy the API key and use as secret key in following section

### 4. Set Up Environment Variables
Create a .env file in the root directory of the project and add your secret key to it.

Example .env File:
```
SECRET_KEY=your_secret_key_here
```

### 5. Run the Streamlit Application

Run the Streamlit application using the following command:

```
streamlit run app.py
```
### 6. Access the Application

Open your web browser and go to http://localhost:8501 to access the application.

## License

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.