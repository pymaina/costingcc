import streamlit as st

# Input fields
partner_cost = st.number_input("Partner/Vendor Cost (USD)", value=0.0)
withholding_tax_rate = st.number_input("Withholding Tax on Partner Cost (%)", value=0.0) / 100
feedback_cost = st.number_input("Feedback Cost (USD)", value=0.0)
usd_cover = st.number_input("USD to KSH Exchange Rate", value=100.0)  # Example default rate
sales_incentive_rate = st.number_input("Sales Incentive (%)", value=12.0) / 100
desired_margin = st.selectbox("Desired Margin (%)", [35, 36, 37, 38, 39, 40,41,42,43,44,45]) / 100

# Calculate the withholding tax on partner cost
withholding_tax_usd = partner_cost * withholding_tax_rate

# Calculate initial total cost in USD
base_cost_usd = partner_cost + feedback_cost + withholding_tax_usd

# Function to calculate final price in USD
def calculate_final_price_usd(base_cost_usd, sales_incentive_rate, desired_margin):
    # Assume a final price to begin with
    estimated_price_usd = base_cost_usd / (1 - desired_margin)

    # Iteratively calculate the correct final price in USD
    for _ in range(10):  # Adjust the number of iterations as needed
        sales_incentive = estimated_price_usd * sales_incentive_rate
        estimated_price_usd = (base_cost_usd + sales_incentive) / (1 - desired_margin)

    return estimated_price_usd, sales_incentive

# Calculate final price in USD and the incentive amount
final_price_usd, sales_incentive_usd = calculate_final_price_usd(base_cost_usd, sales_incentive_rate, desired_margin)

# Convert the final price to KSH
final_price_ksh = final_price_usd * usd_cover

# Display the results
st.write(f"The final price for the tool should be: ${final_price_usd:.2f} USD or KSH {final_price_ksh:.2f}")
st.write(f"Sales Incentive Amount: ${sales_incentive_usd:.2f} USD")
st.write(f"Withholding Tax Passed to Consumer: ${withholding_tax_usd:.2f} USD")
