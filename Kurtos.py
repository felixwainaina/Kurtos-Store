import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.title("Jumia Smartphone Scraper")

url = "https://www.jumia.co.ke/smartphones/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

products = []
for item in soup.find_all('h3', class_='name'):
    products.append(item.text.strip())

df = pd.DataFrame(products, columns=["Product Name"])
csv = df.to_csv(index=False)

if st.button("Download CSV"):
    st.download_button("Download", csv, "smartphones.csv", "text/csv")
