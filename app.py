# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 10:29:00 2021

@author: JEYA KUMAR R
"""

#import numpy as np
import pickle
#import pandas as pd
import streamlit as st
from datetime import datetime, time
from flask import Flask
import pickle



app = Flask(__name__)
# Done using Streamlit
pickle_file = open("flight_price_xgb.pkl",'rb') 
classifier = pickle.load(pickle_file)

def welcome():
    return "Welcome All"

def flight_fare(source, destination, Dept_hour, Dept_min, airlines, Arrival_hour, Arrival_min, Dur_hr, Dur_min):

    #Source -'Chennai', 'Delhi', 'Kolkata', 'Mumbai'
    #Banglore = 0 (not in column)
    if (source == 'Chennai') :
        s_Chennai = 1
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0

    elif (source == 'Delhi'):
        s_Chennai = 0
        s_Delhi = 1
        s_Kolkata = 0
        s_Mumbai = 0

    elif (source == 'Kolkata'):
        s_Chennai = 0
        s_Delhi = 0
        s_Kolkata = 1
        s_Mumbai = 0

    elif (source == 'Mumbai'):
        s_Chennai = 0
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 1

    else:
        s_Chennai = 0
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0

    #Destination - 'Cochin', 'Delhi', 'Hyderabad', 'Kolkata', 'New_Delhi'
    #Banglore = 0 (not in column)

    if (destination == 'Cochin'):
        d_Cochin = 1
        d_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0
        d_New_Delhi = 0

    elif (destination == 'Delhi'):
        d_Cochin = 0
        d_Delhi = 1
        d_Hyderabad = 0
        d_Kolkata = 0
        d_New_Delhi = 0

    elif (destination == 'Hyderabad'):
        d_Cochin = 0
        d_Delhi = 0
        d_Hyderabad = 1
        d_Kolkata = 0
        d_New_Delhi = 0

    elif (destination == 'Kolkata'):
        d_Cochin = 0
        d_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 1
        d_New_Delhi = 0

    elif (destination == 'New_Delhi'):
        d_Cochin = 0
        d_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0
        d_New_Delhi = 1

    else:
        d_Cochin = 0
        d_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0
        d_New_Delhi = 0

    #Airlines - 'IndiGo', 'Jet Airways', 'Multiple carriers', 'SpiceJet', 'Trujet', 'Vistara'
    #Air India = 0(Not in column)
    if (airlines == 'IndiGo'):
        a_IndiGo = 1
        a_Jet_Airways = 0
        a_Multiple_carriers = 0
        a_SpiceJet = 0
        a_Trujet = 0
        a_Vistara = 0

    elif (airlines == 'Jet Airways'):
        a_IndiGo = 0
        a_Jet_Airways = 1
        a_Multiple_carriers = 0
        a_SpiceJet = 0
        a_Trujet = 0
        a_Vistara = 0

    elif (airlines == 'Multiple carriers'):
        a_IndiGo = 0
        a_Jet_Airways = 0
        a_Multiple_carriers = 1
        a_SpiceJet = 0
        a_Trujet = 0
        a_Vistara = 0

    elif (airlines == 'SpiceJet'):
        a_IndiGo = 0
        a_Jet_Airways = 0
        a_Multiple_carriers = 0
        a_SpiceJet = 1
        a_Trujet = 0
        a_Vistara = 0

    elif (airlines == 'Trujet'):
        a_IndiGo = 0
        a_Jet_Airways = 0
        a_Multiple_carriers = 0
        a_SpiceJet = 0
        a_Trujet = 1
        a_Vistara = 0

    elif (airlines == 'Vistara'):
        a_IndiGo = 0
        a_Jet_Airways = 0
        a_Multiple_carriers = 0
        a_SpiceJet = 0
        a_Trujet = 0
        a_Vistara = 1

    else:
        a_IndiGo = 0
        a_Jet_Airways = 0
        a_Multiple_carriers = 0
        a_SpiceJet = 0
        a_Trujet = 0
        a_Vistara = 0


    prediction = classifier.predict([[
        Dept_hour,
        Dept_min,
        Dur_hr,
        Dur_min,
        Arrival_hour,
        Arrival_min,
        a_IndiGo,
        a_Jet_Airways,
        a_Multiple_carriers,
        a_SpiceJet,
        a_Trujet,
        a_Vistara,
        s_Chennai,
        s_Delhi,
        s_Kolkata,
        s_Mumbai,
        d_Cochin,
        d_Delhi,
        d_Hyderabad,
        d_Kolkata,
        d_New_Delhi
    ]])
    output = round(prediction[0], 2)
    print(output)
    return output

def main():
    st.title("Flight Fare Prediction App")

    #Select source
    st.write('Select Source of Journey : ')
    source = st.selectbox('',('Enter the input', 'Chennai', 'Delhi', 'Kolkata', 'Mumbai', 'Banglore'))
    #st.write('You selected:', source)

    #Select Destination
    st.write('Select Journey Destination : ')
    destination = st.selectbox('',
                               ('Enter the input', 'Cochin', 'Delhi', 'Hyderabad', 'Kolkata', 'New_Delhi', 'Banglore'))
    #st.write('You selected:', destination)


    # Departure Hour
    st.write('Select Departure Hour : ')
    Dept_hour = st.slider('', 1, 24, 1)
    #st.write("Selected Departure Hour", Dept_hour)

    # Departure Min
    st.write('Select Departure Minutes : ')
    Dept_min = st.slider("", 0, 60, 0)
    #st.write("Selected Departure Minute", Dept_min)

    # Airlines
    st.write('Select Airlines : ')
    airlines = st.selectbox('',
                            ('Enter the input', 'Air India' ,'IndiGo', 'Jet Airways', 'Multiple carriers', 'SpiceJet',
                             'Trujet', 'Vistara'))
    #st.write("Selected Airline", airlines)


    #Arrival Hour
    st.write('Select Arrival Hour : ')
    Arrival_hour = st.slider("",1,24,1, key="arrhr")
    #st.write("Selected Arrival Hour", Arrival_hour)

    # Arrival Min
    st.write('Select Arrival Minute : ')
    Arrival_min = st.slider("", 0, 60, 0, key="arrmin")
    #st.write("Selected Arrival Minute", Arrival_min)

    #Duration Hour
    Dur_hr = abs(Arrival_hour - Dept_hour)
    #st.write("Duration Hour", Dur_hr)

    #Duration Minute
    Dur_min = abs(Arrival_min - Dept_min)
    #st.write("Duration Minute", Dur_min)

    fare_price = ''
    if st.button('Predict'):
            fare_price = flight_fare(source, destination, Dept_hour, Dept_min, airlines, Arrival_hour, Arrival_min, Dur_hr, Dur_min)

            st.success('The Predicted Flight Fare is  {}'.format(fare_price))
        
    st.write("Created By Jeya Kumar R")


if __name__=='__main__':
    main()
