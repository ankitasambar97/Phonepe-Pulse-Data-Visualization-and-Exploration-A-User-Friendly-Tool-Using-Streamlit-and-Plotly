
Steps are followed to complete this project:
•	Clone the PhonePe Pulse GitHub repository using Git Bash. __ repository
•	Use the OS package in Python to traverse the directory where the JSON files are stored. refer( Phonepay.ipynb )
•	Filter the JSON files from the list of all files using the os.path.splitext() method.
•	Read the JSON files using the json.load() method and store them in a dictionary.
•	Convert the dictionary to a Pandas DataFrame using Pandas.
•	Create a connection to a MySQL database using SQLAlchemy in Python.
•	Use SQLAlchemy to create tables in the MySQL database to store the processed data.
•	Fetch data from a MySQL table using the read_sql_table() method in Pandas to use for visualizations in streamlit platform. refer (phonepay_streamlit.py)
•	Use plotly to create interactive visualizations in Python.
•	Display the visualizations in Streamlit.

Packages used for the projects:
•	from sqlalchemy import create_engine
•	import pandas as pd
•	import json
•	from PIL import Image
•	import streamlit as st
•	import pymysql
•	import sqlalchemy
•	import plotly.express as px
•	import plotly.graph_objects as go
