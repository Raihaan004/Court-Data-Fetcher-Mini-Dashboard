from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

def fetch_case_data(case_type, case_number, case_year):
    """
    Fetches case data from the Delhi High Court website.
    This version clicks the 'Orders' link, navigates to the orders page, 
    and gets the most recent PDF download link.
    """
    options = webdriver.ChromeOptions()
    # Uncomment the next line to run in headless mode (without opening a browser window)
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    
    driver.get("https://delhihighcourt.nic.in/app/get-case-type-status")

    try:
        wait = WebDriverWait(driver, 15)

        # --- Step 1: Fill the form and search for the case ---
        case_type_dropdown = wait.until(EC.presence_of_element_located((By.ID, 'case_type')))
        Select(case_type_dropdown).select_by_value(case_type)

        driver.find_element(By.ID, 'case_number').send_keys(case_number)
        Select(driver.find_element(By.ID, 'case_year')).select_by_value(case_year)

        captcha_text = driver.find_element(By.ID, 'captcha-code').text
        driver.find_element(By.ID, 'captchaInput').send_keys(captcha_text)
        
        submit_button = driver.find_element(By.ID, 'search')
        driver.execute_script("arguments[0].click();", submit_button)

        # --- Step 2: On the results page, find and click the 'Orders' link ---
        wait.until(EC.presence_of_element_located((By.ID, 'caseTable')))
        time.sleep(2)

        first_row = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="caseTable"]/tbody/tr[1]')))
        cells = first_row.find_elements(By.TAG_NAME, 'td')

        if "No data available" in cells[0].text:
             return {"error": "Case not found or no data available for the given details."}

        # Extract data from the row BEFORE clicking away
        case_status_summary = cells[1].text
        parties = cells[2].text
        listing_date_court = cells[3].text

        # Find the "Orders" link within the row and click it
        orders_link = first_row.find_element(By.LINK_TEXT, 'Orders')
        driver.execute_script("arguments[0].click();", orders_link)

        # --- Step 3: On the new 'Orders' page, find the most recent PDF link ---
        pdf_url = "Not Found"
        try:
            # Wait for the new page's table to load
            wait.until(EC.presence_of_element_located((By.ID, 'caseTable')))
            time.sleep(2)

            # Get the link from the first row, second column ('Case No/Order Link.')
            pdf_link_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="caseTable"]/tbody/tr[1]/td[2]/a')))
            pdf_url = pdf_link_element.get_attribute('href')
        except (TimeoutException, NoSuchElementException):
            # It's okay if no PDF is found on the orders page.
            pass

        return {
            "parties": parties,
            "next_hearing_date": listing_date_court,
            "case_status_summary": case_status_summary,
            "pdf_link": pdf_url, # The link to the most recent PDF
            "raw_html": driver.page_source
        }

    except TimeoutException:
        return {"error": "Case not found. The results page did not load as expected."}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}
    finally:
        driver.quit()
