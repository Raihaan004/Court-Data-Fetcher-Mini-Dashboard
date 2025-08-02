# 🏛️ Court Case Data Fetcher

This is a web application built with **Python** and **Flask** that allows users to fetch case details from the Delhi High Court website. It provides a simple interface to look up cases and view their status.

This project was bootstrapped with a standard Flask application structure.

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need to have the following software installed on your machine:

* [Python 3.8+](https://www.python.org/downloads/)
* `pip` (Python package installer)
* [Google Chrome](https://www.google.com/chrome/)
* [ChromeDriver](https://chromedriver.chromium.org/downloads) that matches your Chrome version

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd court-data-fetcher
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You'll need to create a `requirements.txt` file by running `pip freeze > requirements.txt` in your terminal after installing the dependencies.)*

4.  **Set up the WebDriver:**
    Download the correct version of ChromeDriver for your operating system and Chrome browser, and place the executable in the root directory of the project.

---

## ▶️ Running the Application

First, run the development server:

```bash
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) with your browser to see the result.

The page will have a form where you can select a case type and enter a case number and year. Upon submission, the app will scrape the court's website and display the results.

---

## 📚 Learn More

To learn more about the technologies used in this project, check out the following resources:

* [Flask Documentation](https://flask.palletsprojects.com/) - learn about the Flask web framework.
* [Selenium Documentation](https://www.selenium.dev/documentation/) - learn about browser automation.
* [Jinja Documentation](https://jinja.palletsprojects.com/) - learn about the templating engine used by Flask.

---

## 📄 License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.
