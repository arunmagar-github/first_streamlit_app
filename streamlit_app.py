import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("My Moms New Healthy dinner")

streamlit.header("Breakfast Favorites")
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard Bolied Free-Range egg")
streamlit.text("🥑🍞 Avacado toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

#new section to dispaly fruityvise api response
def get_fruityvice_data(this_fruit_choice):
  fruityvise_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  fruityvise_normalized=pandas.json_normalize(fruityvise_response.json())
  return fruityvise_normalized

streamlit.header('Fruityvise Fruit Advice')
try:
  fruit_choice=streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select fruit to get information")
    #streamlit.write('The user entered',fruit_choice)
  else:
    #import requests
    back_from_function=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()


#import snowflake.connector


#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
#my_data_rows = my_cur.fetchall()
streamlit.text("The fruit load list contains")

#snowflake related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
    return my_cur.fetchall()

if streamlit.button('Get Fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows=get_fruit_load_list()
  streamlit.dataframe(my_data_rows)

#allow the user to add fruit to list
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values('from streamlit');");
    return "Thanks for adding"+new_fruit

add_my_fruit=streamlit.text_input('What fruit would you like add?')
if streamlit.button('Add a fruit to a list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function=insert_row_snowflake()
  streamlit.text(back_from_function)




