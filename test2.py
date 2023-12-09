import base64
import io
import altair
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import xlsxwriter

# Define the Streamlit app layout
st.title("Basic DCF and Financial Forecasting Tool - Gordon's method")
st.write("The forecast is based on three year historicals and will prepare a ten year forward statement")
st.write("Please note that Y minus 2, Y minus 1 and Y0 i.e. present year are historical years. Please key in information for them on the left side.")
st.write("Please also adjust the forecast parameters as the case be on the left side for Income Statement and Discounted Cash flows such as discount rate.")
st.write("For the purposes of terminal value please set year of terminal value years, terminal growth rate and terminal year")
st.write("Note - In the context of a DCF analysis, you typically project cash flows explicitly for a certain number of years (forecast period) and then assume that from the terminal year onward, the company's cash flows will grow at a constant rate. The Terminal Value Years refer to the number of years in which this constant growth assumption applies, and the Terminal Year specifies when this assumption starts.")
st.write("You can also choose to visualise them at the end.")
st.write("This product belongs to Bullring Private Limited 2023 (c). All rights reserved. Designed & Developed by CEO Ankit Kotriwal")


# Input historical data for Y-2, Y-1, and Y0
st.sidebar.subheader('Input Parameters')
historical_data_input = st.sidebar.text_input('Enter Historical Data for GMV (comma-separated, FY18, FY19, FY20, FY21, FY22):', value='51, 688, 3060, 5536, 7683', key='historical_data')
revenue_historical_data_input = st.sidebar.text_input('Enter Historical Data for Revenue (comma-separated, FY18, FY19, FY20, FY21, FY22):', value='6, 40, 127, 240, 300', key='revenue_historical_data')
last_mile_costs_historical_data_input = st.sidebar.text_input('Enter Historical Data for Last Mile Delivery Costs (comma-separated, FY18, FY19, FY20, FY21, FY22):', value='7, 54, 125, 228, 248', key='last_mile_costs_historical_data')
cm1_historical_data_input = st.sidebar.text_input('Enter Historical Data for CM1 (comma-separated, FY18, FY19, FY20, FY21, FY22):', value='-1, -14, 2, 12, 52', key='cm1_historical_data')
sales_staff_cost_historical_data_input = st.sidebar.text_input('Enter Historical Data for Sales Staff Cost (comma-separated, FY18, FY19, FY20, FY21, FY22):', value='12, 35, 95, 165, 205', key='sales_staff_cost_historical_data')
marketing_cost_historical_data_input = st.sidebar.text_input('Enter Historical Data for Marketing Cost (comma-separated, FY18, FY19, FY20, FY21, FY22):', value='6, 29, 70, 116, 125', key='marketing_cost_historical_data')
cm2_historical_data_input = st.sidebar.text_input('Enter Historical Data for CM2 (comma-separated, FY18, FY19, FY20, FY21, FY22):', value='-19, -78, -163, -269, -278', key='cm2_historical_data')
manpower_historical_data_input = st.sidebar.text_input('Enter Historical Data for Manpower (comma-separated, FY18, FY19, FY20, FY21, FY22):', value='5, 25, 34, 45, 75', key='manpower_historical_data')
warehouse_maintenance_historical_data_input = st.sidebar.text_input('Enter Historical Data for Warehouse Maintenance (comma-separated, FY18, FY19, FY20, FY21, FY22):', value='5, 27, 37, 67, 79', key='warehouse_maintenance_historical_data')
inventory_wastage_historical_data_input = st.sidebar.text_input('Enter Historical Data for Inventory Wastage Provision (comma-separated, FY18, FY19, FY20, FY21, FY22):', value='6, 25, 42, 68, 45', key='inventory_wastage_historical_data')
cm3_historical_data_input = st.sidebar.text_input('Enter Historical Data for CM3 (comma-separated, FY18, FY19, FY20, FY21, FY22):', value='-35, -155, -276, -449, -477', key='cm3_historical_data')



# Convert input strings to lists of float values
historical_data = [float(value.strip()) for value in historical_data_input.split(',')]
revenue_historical_data = [float(value.strip()) for value in revenue_historical_data_input.split(',')]
last_mile_costs_historical_data = [float(value.strip()) for value in last_mile_costs_historical_data_input.split(',')]
cm1_historical_data = [float(value.strip()) for value in cm1_historical_data_input.split(',')]
sales_staff_cost_historical_data = [float(value.strip()) for value in sales_staff_cost_historical_data_input.split(',')]
marketing_cost_historical_data = [float(value.strip()) for value in marketing_cost_historical_data_input.split(',')]
cm2_historical_data = [float(value.strip()) for value in cm2_historical_data_input.split(',')]
manpower_historical_data = [float(value.strip()) for value in manpower_historical_data_input.split(',')]
warehouse_maintenance_historical_data = [float(value.strip()) for value in warehouse_maintenance_historical_data_input.split(',')]
inventory_wastage_historical_data = [float(value.strip()) for value in inventory_wastage_historical_data_input.split(',')]
cm3_historical_data = [float(value.strip()) for value in cm3_historical_data_input.split(',')]


# Calculate growth rates and parameters based on Y0
# Calculate growth rates and parameters based on FY22
revenue_growth_rate = ((revenue_historical_data[4] - revenue_historical_data[3]) / abs(revenue_historical_data[3])) * 100 if revenue_historical_data[3] != 0 else 0
last_mile_costs_margin = (last_mile_costs_historical_data[4] / abs(revenue_historical_data[4])) * 100 if revenue_historical_data[4] != 0 else 0
cm1_margin = (cm1_historical_data[4] / abs(revenue_historical_data[4])) * 100 if revenue_historical_data[4] != 0 else 0
sales_staff_cost_margin = (sales_staff_cost_historical_data[4] / abs(revenue_historical_data[4])) * 100 if revenue_historical_data[4] != 0 else 0
marketing_cost_margin = (marketing_cost_historical_data[4] / abs(revenue_historical_data[4])) * 100 if revenue_historical_data[4] != 0 else 0
cm2_margin = (cm2_historical_data[4] / abs(revenue_historical_data[4])) * 100 if revenue_historical_data[4] != 0 else 0
manpower_margin = (manpower_historical_data[4] / abs(revenue_historical_data[4])) * 100 if revenue_historical_data[4] != 0 else 0
warehouse_maintenance_margin = (warehouse_maintenance_historical_data[4] / abs(revenue_historical_data[4])) * 100 if revenue_historical_data[4] != 0 else 0
inventory_wastage_margin = (inventory_wastage_historical_data[4] / abs(revenue_historical_data[4])) * 100 if revenue_historical_data[4] != 0 else 0
cm3_margin = (cm3_historical_data[4] / abs(revenue_historical_data[4])) * 100 if revenue_historical_data[4] != 0 else 0
# ... (similar updates for other growth rates and parameters)


# Input forecast parameters using sliders
st.sidebar.subheader('Forecast Parameters')
st.sidebar.subheader('Forecast Parameters')
revenue_growth_rate = st.sidebar.slider('Revenue Growth Rate (%)', min_value=0.0, max_value=100.0, value=revenue_growth_rate, step=0.1, key='revenue_growth_rate')
last_mile_costs_margin = st.sidebar.slider('Last Mile Costs Margin (%)', min_value=0.0, max_value=100.0, value=last_mile_costs_margin, step=0.1, key='last_mile_costs_margin')
cm1_margin = st.sidebar.slider('CM1 Margin (%)', min_value=0.0, max_value=100.0, value=cm1_margin, step=0.1, key='cm1_margin')
sales_staff_cost_margin = st.sidebar.slider('Sales Staff Cost Margin (%)', min_value=0.0, max_value=100.0, value=sales_staff_cost_margin, step=0.1, key='sales_staff_cost_margin')
marketing_cost_margin = st.sidebar.slider('Marketing Cost Margin (%)', min_value=0.0, max_value=100.0, value=marketing_cost_margin, step=0.1, key='marketing_cost_margin')
cm2_margin = st.sidebar.slider('CM2 Margin (%)', min_value=0.0, max_value=100.0, value=cm2_margin, step=0.1, key='cm2_margin')
manpower_margin = st.sidebar.slider('Manpower Margin (%)', min_value=0.0, max_value=100.0, value=manpower_margin, step=0.1, key='manpower_margin')
warehouse_maintenance_margin = st.sidebar.slider('Warehouse Maintenance Margin (%)', min_value=0.0, max_value=100.0, value=warehouse_maintenance_margin, step=0.1, key='warehouse_maintenance_margin')
inventory_wastage_margin = st.sidebar.slider('Inventory Wastage Margin (%)', min_value=0.0, max_value=100.0, value=inventory_wastage_margin, step=0.1, key='inventory_wastage_margin')
cm3_margin = st.sidebar.slider('CM3 Margin (%)', min_value=0.0, max_value=100.0, value=cm3_margin, step=0.1, key='cm3_margin')
discount_rate = st.sidebar.slider('Discount Rate (%)', min_value=1.0, max_value=100.0, value=10.0, step=0.1, key='discount_rate')
terminal_value_year = st.sidebar.slider('Terminal Value Years', min_value=1, max_value=13, value=5, step=1, key='terminal_value_years')
terminal_growth_rate = st.sidebar.slider('Terminal Growth Rate', min_value=1, max_value=10, value=5, step=1, key='terminal_growth rate')


# Calculate financial metrics
# Calculate financial metrics
def calculate_metrics(years, historical_revenue, historical_last_mile_costs, historical_cm1, historical_sales_staff_cost, historical_marketing_cost, historical_cm2, historical_manpower, historical_warehouse_maintenance, historical_inventory_wastage, historical_cm3):
    metrics = []

    for i, year in enumerate(years):
        if i < 5:  # FY18, FY19, FY20, FY21, FY22
            revenue_actual = historical_revenue[i]
            last_mile_costs_actual = historical_last_mile_costs[i]
            cm1_actual = historical_cm1[i]
            sales_staff_cost_actual = historical_sales_staff_cost[i]
            marketing_cost_actual = historical_marketing_cost[i]
            cm2_actual = historical_cm2[i]
            manpower_actual = historical_manpower[i]
            warehouse_maintenance_actual = historical_warehouse_maintenance[i]
            inventory_wastage_actual = historical_inventory_wastage[i]
            cm3_actual = historical_cm3[i]
            # ... (similar updates for other actual values)
        else:  # Forecasted years
            revenue_actual = metrics[i-1]['Revenue'] * (1 + revenue_growth_rate / 100)
            last_mile_costs_actual = revenue_actual * (last_mile_costs_margin / 100)
            cm1_actual = revenue_actual * (cm1_margin / 100)
            sales_staff_cost_actual = revenue_actual * (sales_staff_cost_margin / 100)
            marketing_cost_actual = revenue_actual * (marketing_cost_margin / 100)
            cm2_actual = revenue_actual * (cm2_margin / 100)
            manpower_actual = revenue_actual * (manpower_margin / 100)
            warehouse_maintenance_actual = revenue_actual * (warehouse_maintenance_margin / 100)
            inventory_wastage_actual = revenue_actual * (inventory_wastage_margin / 100)
            cm3_actual = revenue_actual * (cm3_margin / 100)
            # ... (similar updates for other forecasted values)

        metrics.append({
            'Year': year,
            'Revenue': revenue_actual,
            'Last Mile Costs': last_mile_costs_actual,
            'CM1': cm1_actual,
            'Sales Staff Cost': sales_staff_cost_actual,
            'Marketing Cost': marketing_cost_actual,
            'CM2': cm2_actual,
            'Manpower': manpower_actual,
            'Warehouse Maintenance': warehouse_maintenance_actual,
            'Inventory Wastage': inventory_wastage_actual,
            'CM3': cm3_actual,
            # ... (similar updates for other metrics)
        })

    return metrics

def calculate_unlevered_cash_flows(metrics):
    unlevered_cash_flows = []

    for i, metric in enumerate(metrics):
        if i < 2:  # Historical years
            unlevered_cash_flow = metric['CM3']  # Replace this with your actual calculation
        else:  # Forecasted years
            unlevered_cash_flow = metric['CM3'] - metric['Taxes'] - metric['CAPEX'] + metric['Change in working capital']

        unlevered_cash_flows.append({
            'Year': metric['Year'],
            'Unlevered cash flow': unlevered_cash_flow
        })

    return unlevered_cash_flows


# Define years
all_years = ['Y-2', 'Y-1', 'Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10']
# ... (previous code)

# Calculate financial metrics using the function
metrics = calculate_metrics(all_years, historical_data, last_mile_costs_historical_data, cm1_historical_data, sales_staff_cost_historical_data, marketing_cost_historical_data, cm2_historical_data, manpower_historical_data, warehouse_maintenance_historical_data, inventory_wastage_historical_data, cm3_historical_data)

# Display forecasted financial metrics
st.subheader('Forecasted Financial Metrics')
combined_metrics = pd.DataFrame(metrics)
rounded_metrics = combined_metrics.round(2)  # Round values to two decimals
st.write(rounded_metrics)

# Download the metrics table as xlsx
xlsx_buffer = io.BytesIO()
rounded_metrics.to_excel(xlsx_buffer, sheet_name='Forecasted Metrics', index=False, engine='xlsxwriter')
xlsx_buffer.seek(0)
st.markdown(f"### ")
st.markdown(f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{base64.b64encode(xlsx_buffer.read()).decode()}" download="forecasted_metrics.xlsx">Click here to download</a>', unsafe_allow_html=True)

# ... (define and implement the calculate_unlevered_cash_flows function - as shown in the previous messages)

# Calculate unlevered cash flows using the function
unlevered_cash_flows = calculate_unlevered_cash_flows(metrics)

# Prepare a dictionary to store the calculated values for each year
results_dict = {
    'Year': [metric['Year'] for metric in metrics],
    'EBITDA': [metric['EBITDA'] for metric in metrics],
    'Taxes': [metric['Taxes'] for metric in metrics],
    'CAPEX': [metric['CAPEX'] for metric in metrics],
    'Change in working capital': [metric['Change in working capital'] for metric in metrics],
    'Unlevered cash flow': [metric['Unlevered cash flow'] for metric in unlevered_cash_flows]
}

# Create a DataFrame from the dictionary
results_df = pd.DataFrame(results_dict)

# Display the DataFrame
st.subheader('Unlevered Cash Flows')
st.write(results_df)

# Download the unlevered cash flows table as xlsx
xlsx_buffer = io.BytesIO()
results_df.to_excel(xlsx_buffer, sheet_name='Unlevered Cash Flows', index=False, engine='xlsxwriter')
xlsx_buffer.seek(0)
st.markdown(f"### ")
st.markdown(f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{base64.b64encode(xlsx_buffer.read()).decode()}" download="unlevered_cash_flows.xlsx">Click here to download</a>', unsafe_allow_html=True)

# ... (continue with the remaining code - as shown in the previous messages)
# ... (previous code)

# Calculate discounted cash flow metrics using the function
cash_flow_metrics_discounted = calculate_unlevered_cash_flows(metrics)  # Assuming you have a function for calculating unlevered cash flows

# Calculate present value of unlevered cash flows for forecasted years
discounted_unlevered_cash_flows = []
for i, cash_flow_data in enumerate(unlevered_cash_flows):
    if i >= 3:  # Forecasted years
        year = cash_flow_data['Year']
        unlevered_cash_flow = cash_flow_data['Unlevered cash flow']

        # Discount the cash flow
        discount_factor = 1 / (1 + discount_rate / 100) ** (i - 2)  # Adjust the exponent based on zero-based index
        discounted_cash_flow = unlevered_cash_flow * discount_factor

        discounted_unlevered_cash_flows.append({
            'Year': year,
            'Unlevered cash flow': unlevered_cash_flow,
            'Discounted Unlevered cash flow': discounted_cash_flow
        })
    else:
        discounted_unlevered_cash_flows.append({
            'Year': cash_flow_data['Year'],
            'Unlevered cash flow': cash_flow_data['Unlevered cash flow'],
            'Discounted Unlevered cash flow': None  # No discounting for historical years
        })

# Prepare a dictionary to store the calculated values for each year
results_dict = {
    'Year': [data['Year'] for data in discounted_unlevered_cash_flows],
    'Unlevered cash flow': [data['Unlevered cash flow'] for data in discounted_unlevered_cash_flows],
    'Discounted Unlevered cash flow': [data['Discounted Unlevered cash flow'] for data in discounted_unlevered_cash_flows]
}

# Create a DataFrame from the dictionary
results_df = pd.DataFrame(results_dict)

# Display the DataFrame
st.subheader('Discounted Unlevered Cash Flows')
st.write(results_df)

# Download the discounted unlevered cash flows table as xlsx
xlsx_buffer = io.BytesIO()
results_df.to_excel(xlsx_buffer, sheet_name='Discounted Unlevered Cash Flows', index=False, engine='xlsxwriter')
xlsx_buffer.seek(0)
st.markdown(f"### ")
st.markdown(f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{base64.b64encode(xlsx_buffer.read()).decode()}" download="discounted_unlevered_cash_flows.xlsx">Click here to download</a>', unsafe_allow_html=True)

# Calculate the terminal value using Gordon Growth Model
terminal_year_index = terminal_value_year - 1
terminal_cash_flow = cash_flow_metrics_discounted[terminal_year_index]['Unlevered cash flow']
terminal_growth_rate_decimal = terminal_growth_rate / 100
terminal_value = terminal_cash_flow * (1 + terminal_growth_rate_decimal) / (discount_rate / 100 - terminal_growth_rate_decimal)

# Add the terminal value to the terminal year's discounted cash flow
cash_flow_metrics_discounted[terminal_year_index]['Terminal Value'] = terminal_value

# Calculate present value of terminal value using the discount rate
discounted_terminal_value = terminal_value / (1 + discount_rate / 100) ** terminal_value_year
cash_flow_metrics_discounted[terminal_year_index]['Discounted Terminal Value'] = discounted_terminal_value

# Calculate present value of all cash flows
total_discounted_cash_flows = 0
cash_flow_details = []
for i, year_data in enumerate(cash_flow_metrics_discounted):
    if i < terminal_year_index:
        discounted_unlevered_cash_flows = year_data.get('Discounted Unlevered cash flow', 0)
        if discounted_unlevered_cash_flows is not None:
            total_discounted_cash_flows += discounted_unlevered_cash_flows
    else:
        discounted_terminal_value = year_data.get('Discounted Terminal Value', 0)
        if discounted_terminal_value is not None:
            total_discounted_cash_flows += discounted_terminal_value

    cash_flow_details.append({
        'Year': year_data['Year'],
        'Discounted Cash Flow': discounted_unlevered_cash_flows if i < terminal_year_index else discounted_terminal_value,
        'Total Discounted Cash Flow': total_discounted_cash_flows
    })

# Display discounted cash flow metrics
st.subheader('Discounted Cash Flows using Gordon\'s Method considering Terminal Value')
combined_cash_flow_metrics_discounted = pd.DataFrame(cash_flow_metrics_discounted)
rounded_cash_flow_metrics_discounted = combined_cash_flow_metrics_discounted.round(2)
st.dataframe(rounded_cash_flow_metrics_discounted)

# Download the discounted cash flow metrics table as xlsx
xlsx_buffer = io.BytesIO()
rounded_cash_flow_metrics_discounted.to_excel(xlsx_buffer, sheet_name='Discounted Cash Flow Metrics', index=False, engine='xlsxwriter')
xlsx_buffer.seek(0)
st.markdown(f"### ")
st.markdown(f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{base64.b64encode(xlsx_buffer.read()).decode()}" download="discounted_cash_flow_metrics.xlsx">Click here to download</a>', unsafe_allow_html=True)

# Display total discounted cash flows table
total_cash_flows_table = pd.DataFrame(cash_flow_details)
st.subheader('Total Discounted Cash Flows')
st.write(total_cash_flows_table)

# Download the total discounted cash flows table as xlsx
xlsx_buffer = io.BytesIO()
total_cash_flows_table.to_excel(xlsx_buffer, sheet_name='Total Discounted Cash Flows', index=False, engine='xlsxwriter')
xlsx_buffer.seek(0)
st.markdown(f"### ")
st.markdown(f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{base64.b64encode(xlsx_buffer.read()).decode()}" download="total_discounted_cash_flows.xlsx">Click here to download</a>', unsafe_allow_html=True)

# ... (remaining code for visualization and any additional features)
# ... (previous code)

# Visualization
selected_income_accounts3 = st.multiselect('Select income statement accounts to visualize', combined_metrics.columns, key='income_accounts1')
selected_cash_flow_accounts3 = st.multiselect('Select cash flow accounts to visualize', total_cash_flows_table.columns, key='cash_flow_accounts1')

if selected_income_accounts3 or selected_cash_flow_accounts3:
    plt.figure(figsize=(10, 6))

    line_colors_light = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
    bar_colors_dark = ['red', 'darkred', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

    # Plot selected income accounts as lines
    for idx, account in enumerate(selected_income_accounts3):
        plt.plot(combined_metrics['Year'], combined_metrics[account], label=account, color=line_colors_light[idx % len(line_colors_light)], alpha=0.6)

    # Plot selected cash flow accounts as bar graphs
    for idx, account in enumerate(selected_cash_flow_accounts3):
        plt.bar(total_cash_flows_table['Year'], total_cash_flows_table[account], label=account, color=bar_colors_dark[idx % len(bar_colors_dark)], alpha=0.6)

    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title('Visualization')
    plt.legend()
    st.pyplot(plt)

    # Save the plot as PNG and provide download link
    plt_buffer = io.BytesIO()
    plt.savefig(plt_buffer, format='png')
    plt_buffer.seek(0)
    st.markdown(f"### Download visualization as png:")
    st.markdown(f'<a href="data:image/png;base64,{base64.b64encode(plt_buffer.read()).decode()}" download="forecasted_metrics.png">Click here to download</a>', unsafe_allow_html=True)

# ... (any other code or features you want to include in your app)
