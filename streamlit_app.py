import streamlit
streamlit.title("My Moms New Healthy dinner")

streamlit.header("Breakfast Favorites")
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard Bolied Free-Range egg")
streamlit.text("🥑🍞 Avacado toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

#new section to dispaly fruityvise api response
streamlit.header('Fruityvise Fruit Advice')

import requests
fruityvise_response=requests.get("https://fruityvice.com/api/fruit/watermelon")

streamlit.text(fruityvise_response.json())

fruityvise_normalized=pandas.json_normalize(fruityvise_response.json())
streamlit.dataframe(fruityvise_normalized)
