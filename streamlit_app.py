import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭Build your own smoothie🥝🍇')

import pandas 
# Load CSV Data Into Variable
my_fruits_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

# Choose the fruits name column as the Index
my_fruits_list = my_fruits_list.set_index('Fruit')

# Let's put list here so they can pick the fruits they want to include
fruits_selected = streamlit.multiselect("Pick Some Fruits : ", list(my_fruits_list.index), ['Avocado', 'Strawberries'])

# Display the table on the page.
streamlit.dataframe(fruits_selected)

