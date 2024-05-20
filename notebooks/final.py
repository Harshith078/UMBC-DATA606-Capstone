import streamlit as st
import pandas as pd
import json

# Function to load data from a JSON file
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return pd.DataFrame(data)

# Path to the dataset
dataset_path = "C:/Capstone/amazon_uk_shoes_dataset.json"

# Load the dataset
df = load_data(dataset_path)

# Streamlit user interface
st.title('Shoe Finder')

# Sidebar for input
st.sidebar.header('Please Select Your Preferences')

# Brands available
brand_names = df['brand'].unique()

# Sidebar for user input
selected_brand = st.sidebar.selectbox('Select a brand:', ['Choose a brand'] + list(brand_names))

# Predict button
if st.sidebar.button('Find Shoe') and selected_brand != 'Choose a brand':
    # Filter DataFrame based on user selection
    filtered_shoes = df[df['brand'] == selected_brand].sort_values('price', ascending=True)

    if not filtered_shoes.empty:
        # Display all shoes of the selected brand
        for _, shoe in filtered_shoes.iterrows():
            st.write(f"Title: {shoe['title']}")
            st.write(f"Brand: {shoe['brand']}, Price: {shoe['price']}")
            st.write(f"Product Details: {shoe['product_details']}")
            st.markdown(f"[View Shoe]({shoe['url']})", unsafe_allow_html=True)
            if isinstance(shoe['images_list'], list) and shoe['images_list']:
                st.image(shoe['images_list'][0], use_column_width=True)
    else:
        st.warning('No shoes found for the selected brand.')
else:
    st.info('Please select a brand to find shoes.')

# Footer with dataset source
st.markdown("#### Dataset Source: Amazon UK Shoes")
