import pandas as pd
import scipy.stats as stats

# Load the dataset
file_path = "/Users/zeyadosama/Desktop/CodeAlpha/Task3/AdSmartABdata.csv"
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Data preprocessing
# Remove rows with missing values
data = data.dropna()

# Calculate the conversion rates
control_group = data[data['experiment'] == 'control']
exposed_group = data[data['experiment'] == 'exposed']

control_conversion_rate = control_group['yes'].sum() / len(control_group)
exposed_conversion_rate = exposed_group['yes'].sum() / len(exposed_group)

print(f"Control Conversion Rate: {control_conversion_rate}")
print(f"Exposed Conversion Rate: {exposed_conversion_rate}")

# Conduct A/B test
# We use a chi-squared test for independence
contingency_table = pd.DataFrame({
    'control': [control_group['yes'].sum(), control_group['no'].sum()],
    'exposed': [exposed_group['yes'].sum(), exposed_group['no'].sum()]
}, index=['yes', 'no'])

chi2, p, _, _ = stats.chi2_contingency(contingency_table)

print(f"Chi-squared test statistic: {chi2}")
print(f"P-value: {p}")

# Drawing actionable insights
if p < 0.05:
    print("The results are statistically significant. The exposed group performed differently from the control group.")
    if exposed_conversion_rate > control_conversion_rate:
        print("The creative ad resulted in a higher conversion rate.")
    else:
        print("The creative ad resulted in a lower conversion rate.")
else:
    print("The results are not statistically significant. There is no evidence to suggest that the exposed group performed differently from the control group.")

# Save the contingency table and conversion rates to a file
output_path = "/Users/zeyadosama/Desktop/CodeAlpha/Task3/AdSmartABdata.csv"
with open(output_path, 'w') as f:
    f.write("Contingency Table:\n")
    f.write(contingency_table.to_string())
    f.write("\n\n")
    f.write(f"Control Conversion Rate: {control_conversion_rate}\n")
    f.write(f"Exposed Conversion Rate: {exposed_conversion_rate}\n")
    f.write(f"Chi-squared test statistic: {chi2}\n")
    f.write(f"P-value: {p}\n")
    if p < 0.05:
        f.write("The results are statistically significant. The exposed group performed differently from the control group.\n")
        if exposed_conversion_rate > control_conversion_rate:
            f.write("The creative ad resulted in a higher conversion rate.\n")
        else:
            f.write("The creative ad resulted in a lower conversion rate.\n")
    else:
        f.write("The results are not statistically significant. There is no evidence to suggest that the exposed group performed differently from the control group.\n")

print(f"The results have been saved to {output_path}")
