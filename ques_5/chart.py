import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducible results
np.random.seed(42)

# Generate realistic synthetic data for customer engagement patterns
# Engagement metrics across different channels and time periods

# Define channels and time periods
channels = ['Email', 'Social Media', 'Website', 'Mobile App', 'SMS', 'Direct Mail']
time_periods = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']

# Create engagement data (values represent engagement rate as percentage)
# Higher values indicate better engagement
engagement_data = []

for i, period in enumerate(time_periods):
    row_data = []
    for j, channel in enumerate(channels):
        # Create realistic patterns:
        # - Social Media and Mobile App tend to have higher engagement
        # - Email has moderate engagement
        # - Direct Mail has lower engagement
        # - Seasonal variations (Q4 typically higher due to holidays)
        
        base_rate = {
            'Email': 25,
            'Social Media': 45,
            'Website': 35,
            'Mobile App': 50,
            'SMS': 30,
            'Direct Mail': 15
        }[channel]
        
        # Add seasonal variation (Q4 boost)
        seasonal_boost = 8 if 'Q4' in period else 0
        
        # Add year-over-year improvement
        yearly_improvement = 3 if '2024' in period else 0
        
        # Add some random variation
        random_variation = np.random.normal(0, 5)
        
        engagement_rate = base_rate + seasonal_boost + yearly_improvement + random_variation
        
        # Ensure values stay within reasonable bounds (5-70%)
        engagement_rate = max(5, min(70, engagement_rate))
        
        row_data.append(engagement_rate)
    
    engagement_data.append(row_data)

# Create DataFrame
df_engagement = pd.DataFrame(engagement_data, 
                           index=time_periods, 
                           columns=channels)

# Set Seaborn style and context for professional appearance
sns.set_style("whitegrid")
sns.set_context("paper", font_scale=1.2)

# Create the figure with specified size for 512x512 output
plt.figure(figsize=(8, 8))

# Create the heatmap with professional styling
heatmap = sns.heatmap(df_engagement, 
                     annot=True,  # Show values in cells
                     fmt='.1f',   # Format numbers to 1 decimal place
                     cmap='RdYlGn',  # Red-Yellow-Green color palette (intuitive for performance)
                     cbar_kws={'label': 'Engagement Rate (%)'},  # Color bar label
                     linewidths=0.5,  # Add lines between cells
                     linecolor='white',  # White lines for clean appearance
                     square=True,  # Make cells square-shaped
                     vmin=0,  # Set color scale minimum
                     vmax=70)  # Set color scale maximum

# Customize the chart with professional titles and labels
plt.title('Customer Engagement Heatmap by Channel and Quarter', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Marketing Channels', fontsize=12, fontweight='bold')
plt.ylabel('Time Periods', fontsize=12, fontweight='bold')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the chart as PNG with exact 512x512 pixel dimensions
plt.savefig('chart.png', dpi=64, bbox_inches=None, pad_inches=0,
           facecolor='white', edgecolor='none')

# Display the chart
plt.show()

# Print summary statistics for verification
print("Customer Engagement Analysis Summary:")
print("=" * 40)
print(f"Data shape: {df_engagement.shape}")
print(f"Average engagement rate: {df_engagement.values.mean():.1f}%")
print(f"Highest engagement: {df_engagement.values.max():.1f}%")
print(f"Lowest engagement: {df_engagement.values.min():.1f}%")
print("\nTop performing channels:")
print(df_engagement.mean().sort_values(ascending=False).head(3))