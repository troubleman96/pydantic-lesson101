Pydantic Learning Project
Welcome to my Pydantic Learning Project! This repository is a hands-on exploration of Pydantic, a powerful Python library for data validation and settings management using type hints. I created this project to learn and demonstrate key Pydantic features, including:

Validating data with Pydantic models.
Printing JSON schemas for models.
Viewing and handling validation errors.
Accessing environment variables using .env files with pydantic-settings.

The project uses FastAPI to build a simple API that showcases these features in a practical context, managing person data.
Table of Contents

Features
Prerequisites
Installation
Project Structure
Usage
Examples
Running the Application
Testing
Common Pitfalls
Contributing
License

Features

Data Validation: Enforce data types, constraints, and formats (e.g., max username length, age range, valid enums) using Pydantic models.
JSON Schema Generation: Generate and display JSON schemas with model_json_schema() to inspect model structures.
Validation Error Handling: Capture and present user-friendly validation errors for invalid data.
Environment Variable Management: Load sensitive configuration (e.g., API keys, database passwords) from .env files using pydantic-settings.
FastAPI Integration: Leverage Pydantic models in a FastAPI application for request/response validation and automatic API documentation.

Prerequisites
Before running this project, ensure you have:

Python 3.8+ (download here).
A code editor like VS Code.
Basic knowledge of Python, FastAPI, and Pydantic.
Git for cloning the repository.

Installation

Clone the Repository:
[git clone https://github.com/your-username/pydantic-learning-project.git](https://github.com/troubleman96/pydantic-lesson101/tree/master)
cd pydantic-learning-project


Create a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:Install the required packages using requirements.txt:
pip install -r requirements.txt

Key dependencies:

fastapi: Builds the API.
pydantic: Handles data validation and model definition.
pydantic-settings: Manages settings via environment variables.
uvicorn: Runs the FastAPI application.


Set Up Environment Variables:Create a .env file in the project root:
touch .env

Add the following content (replace values as needed):
API_KEY=your-api-key-1234567890
DB_PASS=your-secret-password

These settings are loaded by pydantic-settings to configure the application.


Project Structure
