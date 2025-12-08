import pandas as pd
import matplotlib.pyplot as plt

# Data provided
data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'MRR_Growth': [2.18, 6.77, 12.26, 13.47]
}
df = pd.DataFrame(data)

# Industry target
industry_target = 15

# Calculate the average
average_growth = df['MRR_Growth'].mean()

# Create the visualization
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))

# Bar chart for quarterly data
bars = ax.bar(df['Quarter'], df['MRR_Growth'], color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], label='Quarterly MRR Growth')

# Industry target line
ax.axhline(y=industry_target, color='r', linestyle='--', linewidth=2, label=f'Industry Target ({industry_target}%)')

# Average growth line
ax.axhline(y=average_growth, color='b', linestyle=':', linewidth=2, label=f'Average Growth ({average_growth:.2f}%)')

# Adding data labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval}%', va='bottom', ha='center', fontsize=10)

# Formatting the chart
ax.set_title('Quarterly MRR Growth vs. Industry Target (2024)', fontsize=16)
ax.set_xlabel('Quarter', fontsize=12)
ax.set_ylabel('MRR Growth Rate (%)', fontsize=12)
ax.set_ylim(0, industry_target + 5)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Save the figure
plt.tight_layout()
plt.savefig('mrr_growth.png')

print("Data analysis complete. Visualization saved to 'mrr_growth.png'")
print(f"Calculated Average MRR Growth: {average_growth:.2f}%")
