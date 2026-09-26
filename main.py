import streamlit as st
import sqlite3
import pandas as pd

# --- 1. DATABASE FUNCTIONS ---
def init_db():
    # Connects to (or creates) a file called quotes.db
    conn = sqlite3.connect('quotes.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS quotes
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  project_name TEXT, 
                  width REAL, 
                  height REAL, 
                  total_quote REAL)''')
    conn.commit()
    conn.close()

def save_quote(name, w, h, total):
    conn = sqlite3.connect('quotes.db')
    c = conn.cursor()
    c.execute('INSERT INTO quotes (project_name, width, height, total_quote) VALUES (?, ?, ?, ?)', 
              (name, w, h, total))
    conn.commit()
    conn.close()

def get_quotes():
    conn = sqlite3.connect('quotes.db')
    # Pandas reads the SQLite table and formats it beautifully
    df = pd.read_sql_query("SELECT project_name, width, height, total_quote FROM quotes", conn)
    conn.close()
    return df

# Initialize the database when the app starts
init_db()

# --- 2. CALCULATOR UI ---
st.title("🧶 Rug Tufting Quote Estimator")

st.sidebar.header("Job Details")
project_name = st.sidebar.text_input("Project Name", placeholder="e.g., Nike Logo Rug")
width = st.sidebar.number_input("Width (ft)", value=3.0)
height = st.sidebar.number_input("Height (ft)", value=4.0)

st.sidebar.header("Costs")
yarn_price = st.sidebar.number_input("Yarn Price ($/lb)", value=15.0)
labor_rate = st.sidebar.number_input("Hourly Rate ($)", value=25.0)

# The Math Engine
area = width * height
yarn_needed = area * 0.5  
material_cost = (yarn_needed * yarn_price) + 20 
labor_cost = (area * 2) * labor_rate 
total_quote = material_cost + labor_cost

col1, col2 = st.columns(2)
col1.metric("Total Materials", f"${material_cost:.2f}")
col2.metric("Total Quote", f"${total_quote:.2f}")

st.success(f"You need to buy {yarn_needed} lbs of yarn for this project.")

# --- 3. SAVE TO DATABASE ---
# When the user clicks this button, it triggers the save function
if st.button("Save This Quote"):
    if project_name == "":
        st.warning("Please enter a Project Name to save.")
    else:
        save_quote(project_name, width, height, total_quote)
        st.success(f"Saved {project_name}!")

# --- 4. VIEW PAST QUOTES ---
st.markdown("---")
st.subheader("Saved Quotes History")

# Fetch data and display it as an interactive table
saved_data = get_quotes()
if not saved_data.empty:
    st.dataframe(saved_data, use_container_width=True)
else:
    st.info("No quotes saved yet. Calculate and save one above!")