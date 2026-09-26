# TuftQuote: Custom Rug Estimator

TuftQuote is a lightweight Python web application built with Streamlit, designed specifically for the rug tufting community. It replaces complex spreadsheets by instantly calculating material requirements, labor costs, and total project estimates based on rug dimensions.

## Features
* **Instant Material Math:** Automatically calculates the required yarn weight (in lbs) based on total square footage.
* **Dynamic Cost Breakdown:** Adjust material prices and hourly labor rates using sliders to see real-time price updates.
* **Local Quote Database:** Built-in SQLite database to save, track, and review past client quotes in a clean data table.
* **Mobile-Responsive UI:** Built with Streamlit for a seamless experience across desktop and mobile browsers.

## Installation & Local Setup
1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Launch the application:
   ```bash
   streamlit run main.py
   ```
   The app will automatically open in your default web browser at `http://localhost:8501`.

## Tech Stack
* **Framework:** Python, Streamlit
* **Data Processing:** Pandas
* **Database:** SQLite3
