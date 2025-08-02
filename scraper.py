from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

def fetch_case_data(case_type, case_number, case_year):
    """
    Fetches case data from the Delhi High Court website.
    This version uses a JavaScript click to prevent interception errors.
    """
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    
    driver.get("https://delhihighcourt.nic.in/app/get-case-type-status")

    try:
        wait = WebDriverWait(driver, 10)

        # 1. Select Case Type
        case_type_dropdown = wait.until(EC.presence_of_element_located((By.ID, 'case_type')))
        select_case_type = Select(case_type_dropdown)
        select_case_type.select_by_value(case_type)

        # 2. Enter Case Number
        case_no_input = driver.find_element(By.ID, 'case_number')
        case_no_input.send_keys(case_number)

        # 3. Select Case Year
        case_year_dropdown = driver.find_element(By.ID, 'case_year')
        select_case_year = Select(case_year_dropdown)
        select_case_year.select_by_value(case_year)

        # 4. Read and Enter CAPTCHA
        captcha_code_element = driver.find_element(By.ID, 'captcha-code')
        captcha_text = captcha_code_element.text
        
        captcha_input = driver.find_element(By.ID, 'captchaInput')
        captcha_input.send_keys(captcha_text)

        # 5. Click the Submit Button using JavaScript
        # This is the fix for the "element click intercepted" error.
        submit_button = driver.find_element(By.ID, 'search')
        driver.execute_script("arguments[0].click();", submit_button)

        # 6. Scrape the Results Table
        wait.until(EC.presence_of_element_located((By.ID, 'caseTable')))
        time.sleep(2) 

        first_row = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="caseTable"]/tbody/tr[1]')))
        cells = first_row.find_elements(By.TAG_NAME, 'td')
        
        if "No data available" in cells[0].text:
             return {"error": "Case not found or no data available for the given details."}

        case_status_summary = cells[1].text
        parties = cells[2].text
        listing_date_court = cells[3].text
        
        return {
            "parties": parties,
            "next_hearing_date": listing_date_court,
            "case_status_summary": case_status_summary,
            "raw_html": driver.page_source
        }

    except TimeoutException:
        return {"error": "Case not found. The results page did not load as expected."}
    except Exception as e:
        # Pass the specific Selenium error message to the UI
        return {"error": f"An unexpected error occurred: {e}"}
    finally:
        driver.quit()