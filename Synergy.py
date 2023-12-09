import base64
import io

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# Define the Streamlit app layout
st.title("Financial Model Builder")
st.write("Input financial data for the parent company and acquiring company to generate a synergy financial model.")

# Input data for the parent company
st.sidebar.subheader('Parent Company Data')
parent_revenue = st.sidebar.number_input('Parent Company Revenue (FY21 in $000)', value=25039)
parent_cogs = st.sidebar.number_input('Parent Company COGS (FY21 in $000)', value=3064)
parent_gross_margin_percent = st.sidebar.number_input('Parent Company Gross Margin Percentage (FY21)', min_value=0, max_value=100, value=88)
parent_selling_cost = st.sidebar.number_input('Parent Company Selling Cost (FY21 in $000)', value=3105)
parent_customer_success_cost = st.sidebar.number_input('Parent Company Customer Success Cost (FY21 in $000)', value=1830)
parent_marketing_cost = st.sidebar.number_input('Parent Company Marketing Cost (FY21 in $000)', value=926)
parent_total_rnd = st.sidebar.number_input('Parent Company Total R&D (FY21 in $000)', value=5832)
parent_total_gna = st.sidebar.number_input('Parent Company Total G&A (FY21 in $000)', value=5031)
parent_ebitda = st.sidebar.number_input('Parent Company EBITDA (FY21 in $000)', value=5251)
parent_ebitda_percent = st.sidebar.number_input('Parent Company EBITDA Percentage (FY21)', min_value=0, max_value=100, value=21)
# Add more input fields as needed for other financial data

# Input data for the acquiring company
st.sidebar.subheader('Acquiring Company Data')
acq_revenue = st.sidebar.number_input('Acquiring Company Revenue (FY21 in $000)', value=4353)
acq_cogs = st.sidebar.number_input('Acquiring Company COGS (FY21 in $000)', value=2394)
acq_gross_margin_percent = st.sidebar.number_input('Acquiring Company Gross Margin Percentage (FY21)', min_value=0, max_value=100, value=92)
acq_selling_cost = st.sidebar.number_input('Acquiring Company Selling Cost (FY21 in $000)', value=3105)
acq_customer_success_cost = st.sidebar.number_input('Acquiring Company Customer Success Cost (FY21 in $000)', value=1830)
acq_marketing_cost = st.sidebar.number_input('Acquiring Company Marketing Cost (FY21 in $000)', value=926)
acq_total_rnd = st.sidebar.number_input('Acquiring Company Total R&D (FY21 in $000)', value=5832)
acq_total_gna = st.sidebar.number_input('Acquiring Company Total G&A (FY21 in $000)', value=5031)
acq_ebitda = st.sidebar.number_input('Acquiring Company EBITDA (FY21 in $000)', value=5251)
acq_ebitda_percent = st.sidebar.number_input('Acquiring Company EBITDA Percentage (FY21)', min_value=0, max_value=100, value=21)
# Add more input fields as needed for other financial data

# Calculate synergy financials
synergy_revenue = parent_revenue + acq_revenue
synergy_cogs = parent_cogs + acq_cogs
synergy_gross_margin_percent = (parent_gross_margin_percent + acq_gross_margin_percent) / 2
synergy_selling_cost = parent_selling_cost + acq_selling_cost
synergy_customer_success_cost = parent_customer_success_cost + acq_customer_success_cost
synergy_marketing_cost = parent_marketing_cost + acq_marketing_cost
synergy_total_rnd = parent_total_rnd + acq_total_rnd
synergy_total_gna = parent_total_gna + acq_total_gna
synergy_ebitda = parent_ebitda + acq_ebitda
synergy_ebitda_percent = (parent_ebitda_percent + acq_ebitda_percent) / 2
# Add more calculations for other financial metrics

# Display synergy financials
st.subheader('Synergy Financials (FY21)')
synergy_data = {
    'Particulars': ['Revenue', 'COGS', 'Gross Margin %', 'Selling Cost', 'Customer Success Cost', 'Marketing Cost',
                    'Total R&D', 'Total G&A', 'EBITDA', 'EBITDA %'],
    'Parent Company': [parent_revenue, parent_cogs, parent_gross_margin_percent, parent_selling_cost,
                       parent_customer_success_cost, parent_marketing_cost, parent_total_rnd, parent_total_gna,
                       parent_ebitda, parent_ebitda_percent],
    'Acquiring Company': [acq_revenue, acq_cogs, acq_gross_margin_percent, acq_selling_cost,
                          acq_customer_success_cost, acq_marketing_cost, acq_total_rnd, acq_total_gna,
                          acq_ebitda, acq_ebitda_percent],
    'Synergy Company': [synergy_revenue, synergy_cogs, synergy_gross_margin_percent, synergy_selling_cost,
                        synergy_customer_success_cost, synergy_marketing_cost, synergy_total_rnd, synergy_total_gna,
                        synergy_ebitda, synergy_ebitda_percent]
}

synergy_df = pd.DataFrame(synergy_data)
st.write(synergy_df)

import base64
import io

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

# ... (your existing code)

# Input data for forward projection
st.sidebar.subheader('Forward Projection')
growth_rate = st.sidebar.number_input('Revenue Growth Rate (%)', min_value=0, max_value=100, value=5)
gross_margin_lever = st.sidebar.number_input('Gross Margin Change (%)', min_value=-100, max_value=100, value=0)
selling_cost_percent = st.sidebar.number_input('Selling Cost as % of Revenue', min_value=0, max_value=100, value=10)
customer_success_cost_percent = st.sidebar.number_input('Customer Success Cost as % of Revenue', min_value=0, max_value=100, value=5)
marketing_cost_percent = st.sidebar.number_input('Marketing Cost as % of Revenue', min_value=0, max_value=100, value=8)
wacc_rate = st.sidebar.number_input('Weighted Average Cost of Capital (WACC) (%)', min_value=0, max_value=100, value=10)
years_forward = st.sidebar.number_input('Number of Years for Forward Projection', min_value=1, value=5)

# Calculate forward projection
forward_years = range(1, years_forward + 1)
forward_revenue = synergy_revenue * (1 + growth_rate / 100) ** np.array(forward_years)
forward_gross_margin_percent = synergy_gross_margin_percent + gross_margin_lever
forward_cogs = forward_revenue * (1 - forward_gross_margin_percent / 100)
forward_selling_cost = forward_revenue * (selling_cost_percent / 100)
forward_customer_success_cost = forward_revenue * (customer_success_cost_percent / 100)
forward_marketing_cost = forward_revenue * (marketing_cost_percent / 100)
forward_ebitda = forward_revenue - forward_cogs - forward_selling_cost - forward_customer_success_cost - forward_marketing_cost

# Calculate discounted cash flows using WACC
discount_factors = 1 / (1 + wacc_rate / 100) ** np.array(forward_years)
discounted_cash_flows = forward_ebitda * discount_factors

# Display forward projection
st.subheader(f'Forward Projection (Next {years_forward} Years)')
forward_data = {
    'Year': forward_years,
    'Revenue': forward_revenue,
    'Gross Margin %': [forward_gross_margin_percent] * years_forward,
    'COGS': forward_cogs,
    'Selling Cost': forward_selling_cost,
    'Customer Success Cost': forward_customer_success_cost,
    'Marketing Cost': forward_marketing_cost,
    'EBITDA': forward_ebitda
}
forward_df = pd.DataFrame(forward_data)
st.write(forward_df)

# Display discounted cash flows
st.subheader('Discounted Cash Flows using WACC')
st.write(f'Weighted Average Cost of Capital (WACC): {wacc_rate:,.2f}%')
st.write('Discounted Cash Flows:')
st.write(discounted_cash_flows)

# ... (your existing code for displaying financials and visualizing data)




# Download synergy financials as xlsx
xlsx_buffer = io.BytesIO()
synergy_df.to_excel(xlsx_buffer, sheet_name='Synergy Financials', index=False, engine='xlsxwriter')
xlsx_buffer.seek(0)
st.markdown(f"### Download Synergy Financials as xlsx:")
st.markdown(f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{base64.b64encode(xlsx_buffer.read()).decode()}" download="synergy_financials.xlsx">Click here to download</a>', unsafe_allow_html=True)

# Visualize the data
selected_accounts = st.multiselect('Select accounts to visualize', synergy_df.columns[1:])
if selected_accounts:
    plt.figure(figsize=(10, 6))
    for account in selected_accounts:
        plt.bar(synergy_df['Particulars'], synergy_df[account], label=account)

    plt.xlabel('Particulars')
    plt.ylabel('Value ($000)')
    plt.title('Synergy Financials Visualization')
    plt.legend()
    st.pyplot(plt)

    # Save the plot as PNG and provide download link
    plt_buffer = io.BytesIO()
    plt.savefig(plt_buffer, format='png')
    plt_buffer.seek(0)
    st.markdown(f"### Download visualization as png:")
    st.markdown(
        f'<a href="data:image/png;base64,{base64.b64encode(plt_buffer.read()).decode()}" download="synergy_financials.png">Click here to download</a>',
        unsafe_allow_html=True)
