import pandas as pd
import numpy as np
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error


def forecast_industry_usage(data, industry_name, target_column='total_gallons_all_sources', years_to_predict=3):
    df = data[data['industry'] == industry_name][['year', target_column]].rename(
        columns={'year': 'ds', target_column: 'y'}
    )
    df['ds'] = pd.to_datetime(df['ds'], format='%Y')

    model = Prophet(yearly_seasonality=False, daily_seasonality=False, weekly_seasonality=False)
    model.fit(df)

    future_years = pd.date_range(start=df['ds'].max() + pd.offsets.YearBegin(),
                                 periods=years_to_predict, freq='YS')
    future = pd.DataFrame({'ds': future_years})

    forecast = model.predict(future)

    df_pred = model.predict(df)
    rmse = np.sqrt(mean_squared_error(df['y'], df_pred['yhat']))
    mae = mean_absolute_error(df['y'], df_pred['yhat'])

    forecast_df = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    return forecast_df, {'RMSE': rmse, 'MAE': mae}
