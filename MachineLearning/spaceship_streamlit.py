import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder



model = pickle.load(open('spaceship_classification.pkl', 'rb'))
label_encoders = pickle.load(open('label_encoders1.pkl', 'rb'))


st.title('Spaceship Transport Prediction')


home_planet = st.selectbox('Home Planet', options=['Earth', 'Mars', 'Europa'])
cryo_sleep = st.selectbox('Cryo Sleep', options=['Yes', 'No'])
destination = st.selectbox('Destination', options=['TRAPPIST-1e', '55 Cancri e', 'PSO J318.5-22'])
age = st.number_input('Age', min_value=0, max_value=100, value=30)
vip = st.selectbox('VIP Status', options=['Yes', 'No'])
room_service = st.number_input('Room Service Spending', min_value=0.0, max_value=10000.0, value=0.0)
food_court = st.number_input('Food Court Spending', min_value=0.0, max_value=10000.0, value=0.0)
shopping_mall = st.number_input('Shopping Mall Spending', min_value=0.0, max_value=10000.0, value=0.0)
spa = st.number_input('Spa Spending', min_value=0.0, max_value=10000.0, value=0.0)
vr_deck = st.number_input('VR Deck Spending', min_value=0.0, max_value=10000.0, value=0.0)


if st.button('Predict'):
    
    input_data = pd.DataFrame({
        'HomePlanet': [home_planet],
        'CryoSleep': [cryo_sleep == 'Yes'],
        'Destination': [destination],
        'Age': [age],
        'VIP': [vip == 'Yes'],
        'RoomService': [room_service],
        'FoodCourt': [food_court],
        'ShoppingMall': [shopping_mall],
        'Spa': [spa],
        'VRDeck': [vr_deck]
    })

    
    input_data['HomePlanet'] = label_encoders['HomePlanet'].transform(input_data['HomePlanet'])
    input_data['CryoSleep'] = label_encoders['CryoSleep'].transform(input_data['CryoSleep'])
    input_data['Destination'] = label_encoders['Destination'].transform(input_data['Destination'])
    input_data['VIP'] = label_encoders['VIP'].transform(input_data['VIP'])

   
    prediction = model.predict(input_data)
    result = 'Transported' if prediction[0] else 'Not Transported'
    
  
    st.write(f'The prediction is: {result}')