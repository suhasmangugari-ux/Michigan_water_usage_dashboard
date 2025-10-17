# Michigan Water Usage Dashboard

This project is a Streamlit-based interactive dashboard for exploring historical water usage data in Michigan from 2013 to 2022, along with forecasted water usage for the next three years. The dashboard allows users to filter data by year, industry, and water source, and provides visualizations including line charts, pie charts, and forecasting trends using the Prophet model.



## Features

- **Data Loading & Preprocessing**  
  Loads Michigan water usage data, normalizes gallons to millions, and standardizes industry names.

- **Historical Data Visualization**  
  Displays water usage trends over time by industry and water source using interactive line plots.

- **County-wise Usage Breakdown**  
  Shows water usage distribution by county with pie charts for selected water sources.

- **Forecasting**  
  Predicts water usage for the next three years per industry using Facebook Prophet, displaying forecasts with confidence intervals.

- **Data Download**  
  Allows downloading the filtered dataset as a CSV file for further analysis.



## Installation

1. Clone this repository:

   ```
   git clone <repository-url>
   cd michigan-water-usage-dashboard
   ```

2. Create and activate a Python virtual environment (recommended):

   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install required dependencies:

   ```
   pip install -r requirements.txt
   ```

   Make sure the `requirements.txt` includes essential packages such as:
   ```
   streamlit
   pandas
   numpy
   prophet
   scikit-learn
   plotly
   ```



## Usage

1. Place the water usage data CSV file at the specified path or update the path in `app.py` accordingly:

   ```
   /Users/admin/Desktop/GIT/Michigan_water_usage_dashboard/water_use_data_2013_to_2022.csv
   ```

2. Run the Streamlit app:

   ```
   streamlit run app.py
   ```

3. Use the sidebar filters to select years, industries, and water sources of interest.

4. Explore the visualizations and forecasts for Michigan water usage.

5. Download the filtered data if needed.



## Project Structure

- `app.py` — Main Streamlit application file handling UI and interactions
- `data_loading.py` — Module for loading and preprocessing the dataset
- `forecast.py` — Functions for forecasting water usage by industry using Prophet
- `visualization.py` — Plotting functions for historical usage, county distribution, and forecast charts
- `requirements.txt` — Python dependencies



## Notes

- The forecasting model is built with Prophet and disables seasonalities for yearly data.
- Water usage values are normalized to millions of gallons for better readability.
- Industry names are standardized to a predefined set.
- The app is designed for desktop use with a wide layout.



## License

This project is licensed under the MIT License. See the LICENSE file for details.



## Acknowledgments

- Data provided by Michigan water usage statistics (2013-2022).
- Forecasting powered by Facebook Prophet.
- Visualizations created with Plotly and Streamlit.

