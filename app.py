import streamlit as st
from data_loading import load_and_preprocess_data
from forecast import forecast_industry_usage
from visualization import plot_historical_usage, plot_county_usage, plot_forecast

# Load data
file_path = '/Users/admin/Desktop/GIT/Michigan_water_usage_dashboard/water_use_data_2013_to_2022.csv'
data = load_and_preprocess_data(file_path)

st.set_page_config(page_title="Michigan Water Usage Dashboard", layout="wide")
st.title("Michigan Water Usage Dashboard (2013-2022 + Forecast)")

# Sidebar filters
st.sidebar.header("Filters")

years = sorted(data['year'].unique())
selected_years = st.sidebar.multiselect("Select Years", options=years, default=years)

industries = sorted(data['industry'].unique())
selected_industries = st.sidebar.multiselect("Select Industries", options=industries, default=industries)

source_options = ['gallons_from_great_lakes', 'gallons_from_groundwater', 'gallons_from_inland_surface', 'total_gallons_all_sources']
selected_sources = st.sidebar.multiselect("Select Water Sources", options=source_options, default=source_options)

# Filter data
filtered_data = data[
    (data['year'].isin(selected_years)) &
    (data['industry'].isin(selected_industries))
]

# Historical Water Usage Graph
st.subheader("Historical Water Usage")
historical_figs = plot_historical_usage(filtered_data, selected_sources)
for fig in historical_figs:
    st.plotly_chart(fig, use_container_width=True)

# County-wise Water Usage Pie Chart
st.subheader("County-wise Water Usage")
county_figs = plot_county_usage(filtered_data, selected_sources)
for fig in county_figs:
    st.plotly_chart(fig, use_container_width=True)

# Forecasted Water Usage
st.subheader("Forecasted Water Usage (Next 3 Years)")
for industry in selected_industries:
    forecast_df, metrics = forecast_industry_usage(data, industry)
    st.markdown(f"**{industry} Forecast** (RMSE: {metrics['RMSE']:.2f}, MAE: {metrics['MAE']:.2f})")
    fig_forecast = plot_forecast(forecast_df, industry)
    st.plotly_chart(fig_forecast, use_container_width=True)

# Download Filtered Data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df(filtered_data)
st.download_button(label="Download Filtered Data as CSV", data=csv, file_name='filtered_water_usage.csv', mime='text/csv')
