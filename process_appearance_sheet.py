import datetime
import pandas as pd

df = pd.read_csv("Appearance/Appearance_sheet.csv")
df['TimeStamp'] = df['TimeStamp'].apply(lambda x: str(datetime.timedelta(seconds=x)))
df.to_csv('Appearance/AppearanceSheet_in_minutes.csv', index=False)
