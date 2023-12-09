import streamlit as st
import pandas as pd
import statsmodels.tsa.arima.model as sm_arima
import plotly.express as px

# Financial Data
financial_data = {
    'FY': ['FY18', 'FY19', 'FY20', 'FY21', 'FY22'],
    'GMV': [51, 688, 3060, 5536, 7683],
    'Revenue': [6, 40, 127, 240, 300],
    'Last Mile Delivery Costs': [7, 54, 125, 228, 248],
    'CM1': [-1, -14, 2, 12, 52],
    'Sales Staff Cost': [12, 35, 95, 165, 205],
    'Marketing Cost': [6, 29, 70, 116, 125],
    'CM2': [-19, -78, -163, -269, -278],
    'Manpower': [5, 25, 34, 45, 75],
    'Warehouse Maintenance': [5, 27, 37, 67, 79],
    'Inventory Wastage provision': [6, 25, 42, 68, 45],
    'CM3': [-35, -155, -276, -449, -477],
    'Corporate Costs': [14, 144, 152, 335, 225],
    'Technology': [12, 74, 96, 124, 130],
    'Admin': [20, 122, 152, 202, 125],
    'EBITDA': [-81, -495, -676, -1110, -957]
}

# Additional Data
stores_data = {
    'Total Stores': [2150, 6450, 19880, 36210, 44770],
    'GMV per store - INR': [23683, 106661, 153926, 152898, 171601],
    'Revenue per store - INR': [2846, 6214, 6391, 6630, 6702],
    'Churn to Existing stores %': [0,37.21, 16.59, 6.89, 3.56],
    'Staple': [0,241, 1224, 2491, 3841],  # This line has one less element
}

sales_staff_data = {
    'Sales Staff': [85, 190, 451, 775, 950],
    'GMV per Staff - INR': [599040, 3620867, 6785024, 7143779, 8086932],
    'Revenue per sales staff': [71975, 210938, 281723, 309758, 315851]
}

order_data = {
    'No. of orders': [14548, 214989, 1049039, 1977296, 2845402],
    'Revenue per order - INR': [421, 186, 121, 121, 105]
}

gmv_composition_data = {
    'FMCG': [51, 447, 1836, 3045, 3841],
    'Staple': [0,241, 1224, 2491, 3841],
    'FMCG %': [100,65, 60, 55, 50],
    'Staple %': [0,35, 40, 45, 50]
}

revenue_composition_data = {
    'FMCG': [6, 35, 105, 190, 225],
    'Staple': [0,5, 22, 50, 75],
    'FMCG %': [98, 87, 83, 79, 75],
    'Staple %': [0, 12, 17, 21, 25],
    'FMCG - Revenue to GMV %': [11.78, 7.83, 5.72, 6.24, 5.86],
    'Staple - Revenue to GMV %': [0,2.08, 1.80, 2.01, 1.95]
}

# Combine Financial Data and Additional Data
financial_df = pd.DataFrame(financial_data)

# Streamlit App
st.title("Retail B2B Platform Valuation")

# Display the financial data
st.subheader("Financial Data")
st.dataframe(financial_df)

# Forecasting using ARIMA for Revenue
st.subheader("Revenue Forecast")

# Prepare data for statsmodels
df = financial_df[['FY', 'Revenue']]
# Convert 'FY' to numeric values
df['FY'] = df['FY'].str.extract('(\d+)').astype(float)
df.set_index('FY', inplace=True)
# Fit an ARIMA model
model = sm_arima.ARIMA(df['Revenue'], order=(1, 1, 1))  # You may need to adjust the order
results = model.fit()

# Forecast future values
forecast_steps = 10
last_index = pd.to_datetime(df.index[-1])
forecast = results.get_forecast(steps=forecast_steps)
forecast_index = pd.date_range(start=last_index, periods=forecast_steps + 1, freq='Y')[1:]
forecast_df = pd.DataFrame({'Revenue Forecast': forecast.predicted_mean}, index=forecast_index)

# Plot forecast
fig = px.line(forecast_df, x=forecast_df.index, y='Revenue Forecast', title='Revenue Forecast')
fig.update_xaxes(title_text='Year')
fig.update_yaxes(title_text='Revenue (INR million)')
st.plotly_chart(fig)

# Valuation Exercise
st.subheader("Valuation Exercise")

# Assume a constant Revenue multiple for valuation
revenue_multiple = st.slider("Select Revenue Multiple for Valuation", 0.5, 2.0, 1.0)

# Calculate Enterprise Value
last_year_revenue = financial_df['Revenue'].iloc[-1]
enterprise_value = last_year_revenue * revenue_multiple

st.write(f"Enterprise Value: {enterprise_value} INR million")

# Display the valuation multiples
st.write("Valuation Multiples:")
st.write(f"Revenue Multiple: {revenue_multiple}")
st.write(f"Enterprise Value to Revenue Multiple: {enterprise_value / last_year_revenue}")
st.write(f"Enterprise Value to GMV Multiple: {enterprise_value / financial_df['GMV'].iloc[-1]}")