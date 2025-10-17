import plotly.express as px

source_labels = {
    'gallons_from_great_lakes': 'Great Lakes',
    'gallons_from_groundwater': 'Groundwater',
    'gallons_from_inland_surface': 'Inland Surface Water',
    'total_gallons_all_sources': 'Total'
}

def plot_historical_usage(filtered_data, selected_sources):
    figs = []
    for source in selected_sources:
        fig = px.line(filtered_data, x='year', y=source, color='industry',
                      labels={'year': 'Year', source: source_labels[source], 'industry': 'Industry'},
                      markers=True, title=f"{source_labels[source]} Usage Over Time")
        figs.append(fig)
    return figs

def plot_county_usage(filtered_data, selected_sources):
    total_by_county = filtered_data.groupby('county')[selected_sources].sum().reset_index()
    figs = []
    for source in selected_sources:
        fig_pie = px.pie(total_by_county, names='county', values=source,
                         title=f"{source_labels[source]} Usage by County",
                         hole=0.4)
        figs.append(fig_pie)
    return figs

def plot_forecast(forecast_df, industry):
    fig_forecast = px.line(forecast_df, x='ds', y='yhat', labels={'ds': 'Year', 'yhat': 'Predicted Total Gallons (Millions)'},
                           title=f"{industry} Water Usage Forecast")
    fig_forecast.add_scatter(x=forecast_df['ds'], y=forecast_df['yhat_upper'], mode='lines',
                             line=dict(dash='dash', color='red'), name='Upper Bound')
    fig_forecast.add_scatter(x=forecast_df['ds'], y=forecast_df['yhat_lower'], mode='lines',
                             line=dict(dash='dash', color='red'), name='Lower Bound')
    return fig_forecast
