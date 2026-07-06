import pandas as pd
import streamlit as st

''' ### Record a new weather observation  
1. The date in "MM-DD-YYYY" format  
2. The temperature in degrees Celsius  
3. Weather conditions (Sunny, Cloudy, Rainy, Snowy, etc.)  
4. Humidity percentage  
5. Wind speed in km/h 
'''

def Record_new_weather_observation(date,temperature,weather_condition,humidity,wind_speed):
    df=pd.read_csv("f.csv")
    new_observation = {
        "date": date,
        "temperature": temperature,
        "condition": weather_condition,
        "humidity": humidity,
        "wind_speed": wind_speed}
    new_row= pd.DataFrame(new_observation,index=[len(df)])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv('f.csv', index=False)
    return " "

    

'''###view weather statistics:  
1. The program displays the average, minimum, and maximum temperatures  
2. The program displays the most commonly recorded weather condition
'''

def view_weather_statistics():
    df=pd.read_csv("f.csv")
    st.subheader("the average, minimum, and maximum temperatures")
    st.write(df['temperature'].agg(['min', 'max', 'mean']))
    st.subheader("the most commonly weather condition")
    st.write(df.condition.value_counts().idxmax())
    return " "

'''search by date:  
1. The program asks for a date to search for  
2. The program displays all observations from that date
'''

def search_by_date(date):
    df=pd.read_csv("f.csv")
    st.subheader("this is all observations for this date",date)
    the_filter = df.date == date 
    st.write(df[the_filter])
    return " "
    


''' view all observations:  
1. The program displays all recorded weather data in a formatted table Technical
'''

def view_all_observations():
    df=pd.read_csv("f.csv")
    st.subheader("All recorded weather data")
    return st.write(df)

''' 

Search_by_month  -----------------------------------------------------------------------

'''

def Search_by_month(month):
    df=pd.read_csv("f.csv")
    df['date'] = pd.to_datetime(df['date'])
    st.write(df[df['date'].dt.month_name()==month])
    return " "

''' 

Search_by_season  -----------------------------------------------------------------------

'''

def Search_by_season(season):
    df=pd.read_csv("f.csv")
    df['date'] = pd.to_datetime(df['date'])

    # Spring months: March, April, May
    if season=="Spring":
        the_filter=(df['date'].dt.month_name()=="March")|(df['date'].dt.month_name()=="April")|(df['date'].dt.month_name()=="April")
        return st.write(df[the_filter])
        
    # Summer months:June, July, August
    elif season=="Summer":
        the_filter=(df['date'].dt.month_name()=="June")|(df['date'].dt.month_name()=="July")|(df['date'].dt.month_name()=="August")
        return st.write(df[the_filter])
        
    # Autumn months:September, October, November
    elif season=="Autumn":
        the_filter=(df['date'].dt.month_name()=="September")|(df['date'].dt.month_name()=="October")|(df['date'].dt.month_name()=="November")
        return st.write(df[the_filter])
        
     # Winter months:December, January, February  
    elif season=="Winter":
        the_filter=(df['date'].dt.month_name()=="December")|(df['date'].dt.month_name()=="January")|(df['date'].dt.month_name()=="February")
        return st.write(df[the_filter])
        
''' 
compare_years----------------------------------------------------------------------------------------------------

'''

def compare_years(year):
    df=pd.read_csv("f.csv")
    df['date'] = pd.to_datetime(df['date'])
    df["year"]=df['date'].dt.year
    
    st.write(df[df["year"]== int(year)])
    st.write(df[df["year"]== int(year)-1])
    
    return " "








        
    
    
    
    
    
    
    
    
    


