# 🏛️ Court Case Data Fetcher

A web application built with Python and Flask that allows users to fetch case details from the Delhi High Court website. It provides a simple interface to look up cases by type, number, and year, and view their current status.

---

## 📂 File Structure

The project is organized into the following file structure to keep the backend logic, web templates, and static files separate and maintainable.

```
court-data-fetcher/
│
├── venv/                     # Virtual environment folder
├── static/
│   └── style.css             # CSS for styling the web pages
│
├── templates/
│   ├── index.html            # The main page with the search form
│   └── results.html          # The page to display case results
│
├── app.py                    # The main Flask application file
├── scraper.py                # Contains all the Selenium web scraping logic
├── database.py               # Handles all SQLite database interactions
├── queries.db                # The SQLite database file (created automatically)
├── requirements.txt          # Lists all the Python dependencies
└── chromedriver.exe          # The Selenium WebDriver for Chrome (must be added manually)
```

---

## ⚙️ Setup and Installation

Follow these instructions to get the project up and running on your local machine.

### 1. Clone the Repository
First, clone this repository to your local machine.
```bash
git clone https://github.com/Raihaan004/Court-Data-Fetcher-Mini-Dashboard.git
cd court-data-fetcher
```

### 2. Create a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.
```bash
# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install Flask and Selenium using `pip`.
```bash
pip install Flask selenium
```
*(After installation, you can run `pip freeze > requirements.txt` to generate the requirements file.)*

### 4. Download the WebDriver for Google Chrome
This project uses Selenium to automate Google Chrome, which requires a specific driver.

* **Find your Chrome Version**: Go to `Help` > `About Google Chrome` in your browser to check your version number (e.g., `125.0.6422.112`).
* **Download ChromeDriver**: Go to the official **[Chrome for Testing availability dashboard](https://googlechromelabs.github.io/chrome-for-testing/#stable)**.
* Find the stable version that matches your browser's version, select the `win64` platform for the `chromedriver`, and download the zip file.
* **Place the WebDriver**: Unzip the downloaded file and place `chromedriver.exe` into the root directory of your project folder (`court-data-fetcher/`).

---

## ▶️ Output Process

Here’s what to expect when you run the application.

### 1. Running the App
Execute the main application file from your terminal:
```bash
python app.py
```
The server will start, and you can access the application at **[http://127.0.0.1:5000](http://127.0.0.1:5000)**.

### 2. User Input
You will see a form with three fields:
* A dropdown menu to select the **Case Type**.
* A text box to enter the **Case Number**.
* A text box to enter the **Filing Year**.

Fill in all the details and click the **"Fetch Data"** button.

### 3. Successful Output
If the case is found, you will be redirected to a results page displaying the following details:
* **Parties**: The names of the petitioner and respondent.
* **Case Status / Diary No**: The current status of the case (e.g., PENDING, DISPOSED).
* **Next Hearing Date / Court**: The scheduled date for the next hearing and the court number.

### 4. Error Output
If the case details are incorrect or the case is not found on the court's website, you will see a user-friendly error message on the main page, such as:
* `"Case not found or no data available for the given details."`
* `"An unexpected error occurred..."`

This allows you to correct the details and try your search again.
