#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import chart_studio
import plotly.express as px
import chart_studio.plotly as py
import pandas as pd

username = 'maxito4730' 
api_key = 'VqiInn2eFZEFQXTLTIJB' # your api key - go to profile > settings > regenerate key
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)



url = 'https://raw.githubusercontent.com/elizabethts/publish-plotly-website/master/airbnb.csv'
df = pd.read_csv(url, error_bad_lines=False)
#print(df.head(12))
def clean_data(df):
    
    # replace numbers with strings
    df.neighborhood = df.neighborhood.map({1 : 'Friedrichshain-Kreuzberg', 2 : 'Mitte', 3 : 'Pankow', 4 : 'Neukölln', 5 :'Charlottenburg-Wilm',
                        6 : 'Tempelhof - Schöneberg', 7 : 'Lichtenberg', 8 : 'Treptow - Köpenick', 9 : 'Steglitz - Zehlendorf',
                        10 : 'Reinickendorf', 11 : 'Marzahn - Hellersdorf', 12 : 'Spandau'})

    df.room_type = df.room_type.map({1 : 'Entire home/apt', 2 : 'Private room', 3 : 'Shared room'})

    yes_no_dict = {0: 'No', 1:'Yes'}
    df.wifi = df.wifi.map(yes_no_dict)
    df.washer = df.washer.map(yes_no_dict)
    df.cable_tv = df.cable_tv.map(yes_no_dict)
    df.kitchen = df.kitchen.map(yes_no_dict)
    
    # rename columns
    df.rename(columns={'neighborhood': 'Neighborhood', 'room_type': 'Room Type', 'accommodates': 'Accommodates',
                      'bedrooms': 'Bedrooms', 'number_of_reviews': 'Number of Reviews', 'wifi': 'Wifi', 'cable_tv': 'Cable TV',
                      'washer': 'Washer', 'kitchen': 'Kitchen', 'price': 'Price (US Dollars)'}, inplace=True)
    
    # remove outliers
    df = df[df['Price (US Dollars)']<501]
    
    return df

# clean data
df = clean_data(df)
#df.head(4)

fig = px.scatter(df, x='Neighborhood', y='Price (US Dollars)'
                 ,size='Accommodates'
                 , hover_data=['Bedrooms', 'Wifi', 'Cable TV', 'Kitchen', 'Washer', 'Number of Reviews']
                 ,color= 'Room Type')
fig.update_layout(template='plotly_white')
fig.update_layout(title='How much should you charge in a Berlin neighborhood?')
fig.show()

#py.plot(fig, filename='airbnb', auto_open=True)

import plotly.io as pio
#pio.write_html(fig, file=’index.html’, auto_open=True)
pio.write_html(fig, file='index.html', auto_open=True)


# In[ ]:




