import streamlit as st
import pandas as pd
import pickle



model = pickle.load(open('IRIS_model.pkl', 'rb'))



st.title('Prediction IRIS flower')



sepal_length = st.number_input('sepal_length', min_value=0.0, max_value=100.0, value=2.5)
sepal_width = st.number_input('sepal width', min_value=0.0, max_value=100.0, value=2.5)
petal_length = st.number_input('petal length', min_value=0.0, max_value=100.0, value=2.5)
petal_width = st.number_input('petal width', min_value=0.0, max_value=100.0, value=2.5)



if st.button('Predict'):
    
    input_data = pd.DataFrame({
        'sepal_length': [sepal_length],
        'sepal_width': [sepal_width],
        'petal_length': [petal_length],
        'petal_width': [petal_width]
    })

   
    prediction = model.predict(input_data)
    
    species_dict = {
        'Iris-setosa': 'Setosa', 
        'Iris-versicolor': 'Versicolor', 
        'Iris-virginica': 'Virginica'
    }
    
    predicted_species = species_dict[prediction[0]]
    
  
    st.write(f'The prediction is: {predicted_species}')