import requests
from bs4 import BeautifulSoup
import pandas as pd

#function to scrape email addresses from the webpage by taking the url as an input
def scrape_emails(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    #find all text that matches the email pattern
    emails = set(re.findall(r'[a-z0-9.\-+_]+@[a-z0-9.\-+_]+\.[a-z]+', response.text, re.I))

    return emails

#function to create dataframe using pandas with the list of emails and then converts it to Excel file
def save_to_excel(emails, filename):
        df = pd.DataFrame(emails, columns=['Email'])
        df.to_excel(filename, index=False)
        print("Emails saved to", filename, "successfully.")


url = input("Enter the URL of the website to scrape email addresses from: ")
filename = input("Enter the filename to save the emails (e.g., output.xlsx): ")

emails = scrape_emails(url) #collect email addresses
save_to_excel(emails, filename) #save email addresses to excel
