

import streamlit as st
import requests
import pandas as pd
from io import StringIO

# Function to call ScraperAPI
def scrape_data(api_key):
    payload = {
        '313bbb817130b6ce2caf0dcdcca60f68': api_key,
        'url': 'https://www.jumia.co.ke/smartphones/',
        'autoparse': 'true',
        'output_format': 'csv',
        'device_type': 'mobile',
        'keep_headers': 'true',
        'binary_target': 'true'
    }
    
    response = requests.get('https://api.scraperapi.com/', params=payload)
    
    if response.status_code == 200:
        return response.text
    else:
        st.error("Error fetching data from the API.")
        return None

# Streamlit app layout
st.title("Jumia Smartphone Scraper")
st.write("Enter your ScraperAPI key to fetch smartphone data from Jumia.")

# API Key input
api_key = st.text_input("API Key", type="password")

# Button to scrape data
if st.button("Scrape Data"):
    if api_key:
        csv_data = scrape_data(api_key)
        
        if csv_data:
            # Convert CSV data to DataFrame for display
            df = pd.read_csv(StringIO(csv_data))
            st.write("Data fetched successfully!")
            st.dataframe(df)  # Display the dataframe
            
            # Option to download the CSV file
            csv_file = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download CSV",
                data=csv_file,
                file_name='jumia_smartphones.csv',
                mime='text/csv'
            )
    else:
        st.warning("Please enter your API Key.")
