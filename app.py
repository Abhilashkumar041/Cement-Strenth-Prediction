import pickle

import streamlit as st

# Load the saved model and scaler
with open('model_live.pkl', 'rb') as file:
    pipeline = pickle.load(file)
    scaler = pipeline.named_steps['scaler']

st.title("Cement Strength Prediction")

# Collect the input values from the user
material_quantity = st.slider("Material Quantity (in gm) value", min_value=0, max_value=700)
additive_catalyst = st.slider("Additive Catalyst value (in gm)", min_value=0, max_value=500)
ash_component = st.slider("Ash Component values (in gm)", min_value=0, max_value=300)
water_mix = st.slider("Water Mix (in ml)", min_value=0, max_value=400)
plasticizers = st.slider("Plasticisers (in ml)", min_value=0, max_value=50)
moderate_aggregator = st.slider("Moderate Aggregator", min_value=0, max_value=1200)
refined_aggregator = st.slider("Refined Aggregator", min_value=0, max_value=1200)
formulation_duration = st.slider("Formulation Duration (in hrs)", min_value=0, max_value=400)

# Scale the input data
input_data_scaled = scaler.transform([[material_quantity, additive_catalyst, ash_component, water_mix, plasticizers,
                                       moderate_aggregator, refined_aggregator, formulation_duration]])

# Make the prediction using the loaded pipeline
prediction_scaled = pipeline.predict(input_data_scaled)

# Inverse scale the predicted value
prediction_original_scale = scaler.inverse_transform(input_data_scaled)[0, 7]

# Display the predicted value in the original scale
st.write("Predicted Cement Strength: ", prediction_original_scale)


