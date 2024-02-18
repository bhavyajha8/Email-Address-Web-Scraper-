import requests
from bs4 import BeautifulSoup
import pandas as pd

#function to scrape email addresses from the webpage by taking the url as an input
def scrape_emails(url):
    response = requests.get(url)
    if response.status_code == 200: #raises http error for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')
        emails = set() #to eliminate redundancy, stored in set
        for paragraph in soup.find_all('p'):
            for email in paragraph.text.split():
                if '@' in email:
                    emails.add(email)
        return list(emails)
    else:
        print("Failed to fetch the webpage. Status code:", response.status_code)
        return []

#function to create dataframe using pandas with the list of emails and then converts it to Excel file
def save_to_excel(emails, filename):
        df = pd.DataFrame(emails, columns=['Email'])
        df.to_excel(filename, index=False)
        print("Emails saved to", filename, "successfully.")


url = input("Enter the URL of the website to scrape email addresses from: ")
filename = input("Enter the filename to save the emails (e.g., output.xlsx): ")

emails = scrape_emails(url) #collect email addresses
save_to_excel(emails, filename) #save email addresses to excel