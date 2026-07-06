import streamlit as st
import datetime
import pandas as pd
import random
import app_fun as af
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://img.magnific.com/premium-photo/sunset-blue-pink-orange-sky_590597-53.jpg");
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<p style="font-family:Georgia; font-size:40px; font-weight:bold;">Weather app</p>', 
    unsafe_allow_html=True
)


### sidebar
with st.sidebar:
    add_radio = st.radio(
        "",
        ["Welcome page","Record a new weather observation", "View weather statistics","Search observations by date","View all observations","temperature trends","Search by month or season","predict tomorrow's weather","compare current year data with previous years","track and display record-breaking temperatures or conditions"]
    )
    

   


### Record a new weather observation
if add_radio=="Record a new weather observation":
    date = st.date_input("Enter Date: ", value=datetime.date.today())
    date = date.strftime("%Y-%m-%d")
    temperature =st.number_input("Enter the temperature in Celsius: ")
    weather_condition = st.selectbox("Choose the weather condition: " ,["Sunny", "Cloudy", "Rainy", "Snowy",   "Stormy","Windy","Foggy"])
    humidity = st.number_input("Enter the humidity: ")
    wind_speed =st.number_input("Enter the wind speed in km/h: ")
    if st.button("Add"):
        af.Record_new_weather_observation(date,temperature,weather_condition,humidity,wind_speed)
        st.success("weather observation saved successfully!")

        
### View weather statistics       
if add_radio=="View weather statistics":
    if st.button("weather statistics"):
        af.view_weather_statistics()


### Search observations by date 
if add_radio=="Search observations by date":
    date = st.date_input("Enter Date: ", value=datetime.date.today())
    date = date.strftime("%Y-%m-%d")
    if st.button("Search"):
        af.search_by_date(date)
        

### View all observations  
if add_radio=="View all observations":
    if st.button("View all observations"):
        af.view_all_observations()
        

### temperature trends
if add_radio=="temperature trends":
    df=pd.read_csv('f.csv')
    st.write("temperature trends")
    st.line_chart(df, x="date", y="temperature")
    

        
### Search by month or season
if add_radio=="Search by month or season":
    choose= st.selectbox("Search data by: " ,["select-data","month", "season"])
    if choose=="month":
        month= st.selectbox("Choose month: ",["select-data","January","February","March","April","May","June","July","August","September", "October", "November","December"])
        af.Search_by_month(month)
        
    elif choose=="season":
        season=st.selectbox("Choose season: " ,["select-data","Spring","Summer","Autumn", "Winter"])
        af.Search_by_season(season)



### predict tomorrow's weather based on historical patterns  
if add_radio=="predict tomorrow's weather":
    # random temperature
    w_condition =random.choice(["☀️Sunny", "☁️Cloudy", "🌧️Rainy", "❄️Snowy","⛈️Stormy","💨Windy"])
    
    if w_condition=="☀️Sunny":
        temperature=random.randint(22, 40)
    elif w_condition=="☁️Cloudy":
        temperature=random.randint(15, 26)
    elif w_condition=="🌧️Rainy":
        temperature=random.randint(10, 22)
    elif w_condition=="❄️Snowy":
        temperature=random.randint(-15, 2)
    elif w_condition=="⛈️Stormy":
        temperature=random.randint(18, 30)
    elif w_condition=="💨Windy":
        temperature=random.randint(8, 20)
    
    humidity = random.randint(10, 100)
    wind_speed = random.randint(0, 85)

    if st.button(" tomorrow's weather "):
        st.write(f" weather condition: {w_condition}")
        st.write(f" temperature: {temperature}")
        st.write(f" humidity : {humidity}")
        st.write(f" wind_speed : {wind_speed}")
        
        
    



### compare current year data with previous years  
if add_radio=="compare current year data with previous years":
    year= st.selectbox("select year: " ,["2018","2019","2020", "2021","2022","2023","2024","2025","2026"])
    if st.button("search"):
       af.compare_years(year)
    


    
### track and display record-breaking temperatures or conditions 
if add_radio=="track and display record-breaking temperatures or conditions":
    df=pd.read_csv('f.csv')
    max_temp=df["temperature"].max()
    min_temp=df["temperature"].min()
    max_humidity=df["humidity"].max()
    max_wind_speed=df["wind_speed"].max()
    
    date = st.date_input("Enter Date: ", value=datetime.date.today())
    date = date.strftime("%Y-%m-%d")
    temp =st.number_input("Enter the temperature in Celsius: ")
    weather_condition = st.selectbox("Choose the weather condition: " ,["Sunny", "Cloudy", "Rainy", "Snowy",   "Stormy","Windy","Foggy"])
    humidity = st.number_input("Enter the humidity: ")
    wind_speed =st.number_input("Enter the wind speed in km/h: ")
    if st.button("Add"):
        af.Record_new_weather_observation(date,temp,weather_condition,humidity,wind_speed)
        st.success("weather observation saved successfully!")
        if temp > max_temp:
            st.success("A new max temperature!")
        if temp < min_temp:
            st.success("A new min temperature!")
        if humidity>max_humidity:
            st.success("A new max humidity!")
        if wind_speed>max_wind_speed:
            st.success("A new max wind speed!")
        

