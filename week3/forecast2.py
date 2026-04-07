import pandas as pd
import json

# Assuming 'result.text' contains the JSON string from the previous API call
data = json.loads(result.text)

# Extract the forecast items
items = data['response']['body']['items']['item']

# Convert to a pandas DataFrame
df = pd.DataFrame(items)

# Filter for temperature ('TMP') category only   #TMP: 1시간 기온 의미
df = df[df['category'] == 'TMP']

# Rename 'fcstValue' column to '예보온도' and 'fcstDate' to '날짜'
df = df.rename(columns={'baseDate':'발표일자','baseTime':'발표시간',
                        'fcstValue': '예보온도', 'fcstDate': '날짜','fcstTime':'예보시간'})

# Convert '예보온도' to numeric, handling potential errors
df['예보온도'] = pd.to_numeric(df['예보온도'], errors='coerce')

# Display the DataFrame
display(df)