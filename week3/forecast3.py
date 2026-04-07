import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Configure font to support Korean characters
# Find the path to the NanumGothic font
font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
fm.fontManager.addfont(font_path)
plt.rcParams['font.family'] = 'NanumGothic'

# Create a bar plot for forecast temperature by date
plt.figure(figsize=(6, 6)) # Increased figure size for more dates
sns.barplot(x='날짜', y='예보온도', data=df, palette='viridis', hue='날짜', legend=False)

# Add title and labels
plt.title('예보 온도', fontsize=16)
plt.xlabel('날짜', fontsize=12)
plt.ylabel('예보 온도 (°C)', fontsize=12)

# Rotate x-axis labels if there are many dates for better readability
plt.xticks(rotation=45, ha='right')

# Display the value on top of the bar (optional for many dates, keep for now)
# for index, row in df.iterrows():
#     plt.text(index, row['예보온도'], str(row['예보온도']), color='black', ha="center", va='bottom')

plt.ylim(bottom=0) # Ensure y-axis starts from 0 for temperature
plt.tight_layout() # Adjust layout to prevent labels from being cut off
plt.show()