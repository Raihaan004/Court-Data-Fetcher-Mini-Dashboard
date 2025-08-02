Court Case Data Fetcher
A simple web app to quickly fetch case details from the Delhi High Court website.

This project was built to satisfy the requirements for Task 1 of the internship assignment. It lets you enter a case type, number, and year to get the latest case status and party details without having to manually navigate the court's website.

Features
Simple Web Form: An easy-to-use interface with a dropdown for case types and inputs for case number and year.

Automated Scraping: The backend automatically navigates the court website, enters your details, and fetches the information.

CAPTCHA Handling: The scraper is smart enough to read and solve the simple text-based CAPTCHA on the website.

Query Logging: Every search you make is logged in an SQLite database for your records.

Clean Results Display: Shows you the parsed case details in a clean and simple format.

Court Chosen
Court: Delhi High Court

URL: https://dhconline.nic.in/dhc_case_status_v1/

CAPTCHA Strategy
The Delhi High Court website uses a simple but effective text-based CAPTCHA. The numeric code is displayed directly in the HTML of the page.

Our approach is straightforward:

The scraper reads the CAPTCHA code from the webpage's HTML.

It then types that same code into the CAPTCHA input box before submitting the form.

This method is reliable because it mimics exactly what a human user does and doesn't require any complex image recognition.

Tech Stack
Backend: Python with Flask

Scraping: Selenium

Database: SQLite

Frontend: Basic HTML & CSS

Setup and Run
Here’s how to get the project running on your local machine.

Clone the Repository

git clone <your-repo-url>
cd court-data-fetcher

Set Up a Virtual Environment

# Create the environment
python -m venv venv

# Activate it
.\venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

(Note: You'll need to create a requirements.txt file by running pip freeze > requirements.txt)

Download WebDriver
Make sure you have the Chrome WebDriver that matches your browser version placed in the project's root directory.

Run the App
The most reliable way to run the app is to execute the Python script directly:

python app.py

Your application will be running at http://127.0.0.1:5000.

License
This project is licensed under the MIT License.