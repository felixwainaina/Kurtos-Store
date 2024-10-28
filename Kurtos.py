import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

def scrape_jumia_smartphones():
    url = 'https://www.jumia.co.ke/smartphones/'
    response = requests.get(url)
    
    if response.status_code != 200:
        st.error(f"Failed to retrieve data: {response.status_code}")
        return pd.DataFrame()  # Return an empty DataFrame on failure
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract smartphone details
    smartphones = soup.find_all('div', class_='product-item')
    data = []

    for phone in smartphones:
        name = phone.find('h2', class_='title').text.strip()
        price = phone.find('span', class_='price').text.strip()
        data.append({'Name': name, 'Price': price})

    return pd.DataFrame(data)

def main():
    st.title("Jumia Kenya Smartphones Scraper")
    
    if st.button("Scrape Data"):
        with st.spinner("Scraping data..."):
            df = scrape_jumia_smartphones()
            if not df.empty:
                st.success("Data scraped successfully!")
                st.dataframe(df)  # Display the DataFrame in the app
                
                # Option to download CSV
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name='smartphones.csv',
                    mime='text/csv'
                )
            else:
                st.warning("No data found.")

if __name__ == '__main__':
    main()
