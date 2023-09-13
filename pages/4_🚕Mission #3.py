import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def generate_surface_data():
    x = np.linspace(0, 100, 20)
    y = np.linspace(0, 100, 20)
    x, y = np.meshgrid(x, y)
    z = 2+(x*y/num3)  # Replace this with your equation
    return x, y, z

def generate_line_data():
    x = np.full((20), num1)
    y = np.linspace(0, 100, 20)
    z = 2+(x*y/num3)
    return x, y, z

def generate_line_data2():
    x = np.linspace(0, 300, 20)
    y = np.full((20), num2)
    z = 1+(x/y)
    return x, y, z

def calculate():
    if num3 == 0:
        st.warning(f"Score = undefined")
    else:
        ans = 2+(num1*num2/num3)
        st.success(f"Score = {ans}")

st.set_page_config(
    page_title="Mission #3",
    page_icon='🚕'
)

st.title('Sensitivity Analysis')
st.subheader('''
Mission 3: Urban Taxi Flight
- The payload for Mission 3 is Crew and Passengers.
- The airplane will enter the staging box in the parking configuration with the propulsion battery(ies) removed.
- The staging box judge will record the battery capacity and number of passengers flown on the score sheet.
- The ground crew will put the airplane in the flight configuration and install the battery(ies), Crew, floor insert (if used) and Passengers within the 5-minute staging window.
- There will be a 5-minute window for this mission.
- The number of laps flown within the 5-minute window will be recorded.
- The score will be a function of the number of laps flown * number of passengers / rated battery capacity (Wh).
- Time starts when the airplane throttle is advanced for the first take-off (or attempt).
- A lap is complete when the airplane passes over the start/finish line in the air (the landing is not part of the 5-minute time window).
- Must complete a successful landing to get a score.
''')
st.subheader('Score = 2 + (# laps * # passengers / battery capacity)')

col1, col2, col3, col4 = st.columns(4)
with col1:
    num1 = st.number_input('#Laps (0-100)', 0, 100, 20)
with col2:
    num2 = st.number_input('#Passenger (0-100)', 0, 100, 10)
with col3:
    num3 = st.number_input('Battery Capacity', 1, 10000, 5000)
with col4:
    # if st.button("Calculate Score"):
    if num1 or num2:
        calculate()

with st.container():
    x, y, z = generate_surface_data()

    # Create a 3D surface plot using Plotly
    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])

    fig.update_layout(title=f'Score Graph @Battery Capacity: {num3}', autosize=False,
                        width=800, height=800,
                        margin=dict(l=65, r=50, b=65, t=90))

    fig.update_layout(scene=dict(xaxis_title='#Laps',
                                    yaxis_title='#Passenger',
                                    zaxis_title='Score'))

    # Display the plot in Streamlit
    st.plotly_chart(fig)