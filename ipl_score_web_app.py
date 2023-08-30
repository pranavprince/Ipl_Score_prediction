import streamlit as st
import numpy as np
import math
import pickle

#Giving a title and setting the configuration
st.set_page_config(page_title="IPL SCORE PREDICTOR",layout = 'centered')


#loading the pickle file

file = 'ipl_score_prediction.pkl'
model=pickle.load(open(file,'rb'))

#setting the main heading and description
st.markdown("<h1 style='text-align:center;color:rgb(151, 85, 142)'>IPL SCORE PREDICTION </h1>",True)

#Background Image
background = '''
<style>
body{
    background-image:url("images.jpeg");
    background-sixe:cover;
}
</style>
'''
st.markdown(background,unsafe_allow_html=True)


with st.expander("About Project"):
    st.info('''This project is all about the score predictions of the ipl matches held between
     2008 to 2017 considering only the 8 teams
     Chennai Super Kings,Delhi Daredevils,Kings XI Punjab,Kolkata Knight Riders,Mumbai Indians,Rajasthan Royals,
     Royal Challengers Bangalore,Sunrisers Hyderabad into consideration.This model was build by the Random forest Regressor.Hope you Like it!!''')

#collecting the information about the batting team and bowling team


#selecting the batting team
batting_team = st.selectbox('Batting Team',('Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab','Kolkata Knight Riders','Mumbai Indians','Rajasthan Royals','Royal Challengers Bangalore','Sunrisers Hyderabad'))

prediction_array=[]

if batting_team=="Chennai Super Kings":
    prediction_array+=[1,0,0,0,0,0,0,0]
elif batting_team=="Delhi Daredevils":
    prediction_array+=[0,1,0,0,0,0,0,0]
elif batting_team=="Kings XI Punjab":
    prediction_array+=[0,0,1,0,0,0,0,0]
elif batting_team=="Kolkata Knight Riders":
    prediction_array+=[0,0,0,1,0,0,0,0]
elif batting_team=="Mumbai Indians":
    prediction_array+=[0,0,0,0,1,0,0,0]
elif batting_team=="Rajasthan Royals":
    prediction_array+=[0,0,0,0,0,1,0,0]
elif batting_team=="Royal Challengers Banglore":
    prediction_array+=[0,0,0,0,0,0,1,0]
elif batting_team=="Sunrisers Hyderabad":
    prediction_array+=[0,0,0,0,0,0,0,1]

#Selecting the bowling Team
bowling_team = st.selectbox('Bowling Team',('Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab','Kolkata Knight Riders','Mumbai Indians','Rajasthan Royals','Royal Challengers Bangalore','Sunrisers Hyderabad'))
if bowling_team==batting_team:
    st.error("The Bowling and Batting Teams can't be same")

if bowling_team=="Chennai Super Kings":
    prediction_array+=[1,0,0,0,0,0,0,0]
elif bowling_team=="Delhi Daredevils":
    prediction_array+=[0,1,0,0,0,0,0,0]
elif bowling_team=="Kings XI Punjab":
    prediction_array+=[0,0,1,0,0,0,0,0]
elif bowling_team=="Kolkata Knight Riders":
    prediction_array+=[0,0,0,1,0,0,0,0]
elif bowling_team=="Mumbai Indians":
    prediction_array+=[0,0,0,0,1,0,0,0]
elif bowling_team=="Rajasthan Royals":
    prediction_array+=[0,0,0,0,0,1,0,0]
elif bowling_team=="Royal Challengers Banglore":
    prediction_array+=[0,0,0,0,0,0,1,0]
elif bowling_team=="Sunrisers Hyderabad":
    prediction_array+=[0,0,0,0,0,0,0,1]

col1,col2 = st.columns(2)
with col1:
    overs = st.number_input("Current Over",min_value=5.1,max_value=19.5,value=5.1,step=0.1)
    if overs-math.floor(overs)>0.5:
        st.error('Please enter valid over input as one over only contains 6 balls')
with col2:
    runs = st.number_input("Runs Scored",min_value =0,max_value=400,value = 0,step=1,format="%i")

wickets = st.slider("Wickets",0,9)
wickets = int(wickets)

col3,col4=st.columns(2)

with col3:
    last_five_runs=st.number_input("Runs in last five overs",min_value=0,max_value=runs,value =0,step=1,format="%i")
with col4:
    last_five_wickets=st.number_input("Wickets in last five overs",min_value=0,max_value=wickets,step=1,format="%i")

prediction_array = prediction_array + [runs,wickets,overs,last_five_runs,last_five_wickets]
prediction_array = np.array([prediction_array])
prediction = model.predict(prediction_array)


if st.button("Predict score"):
    score = int(round(prediction[0]))

    x=f'Predicted Match Score:{score-5} to {score+5}'
    st.success(x)