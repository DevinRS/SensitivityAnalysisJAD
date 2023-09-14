import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def generate_surface_data():
    x = np.linspace(0, 100, 20)
    y = np.linspace(0, 100, 20)
    x, y = np.meshgrid(x, y)
    z = 2+(x*y/battery_capacity)  # Replace this with your equation
    return x, y, z

def generate_line_data():
    x = np.full((50), laps)
    y = np.linspace(30, 300, 50)
    z = 2+(x*y/battery_capacity)
    return x, y, z

def generate_line_data2():
    x = np.linspace(0, 300, 50)
    y = np.full((50), passenger)
    z = 2+(x*y/battery_capacity)
    return x, y, z

def calculate():
    ans = 2+(laps*passenger/battery_capacity)
    st.sidebar.info(f"Score = {ans}")

# 1. Page Config
st.set_page_config(
    page_title="Mission #3",
    page_icon='🚕'
)

# 2. Sidebar
st.sidebar.success('Select Mission Above 👆')
st.sidebar.title("Sensitivity Analysis")
input_form = st.sidebar.form("input_form")
input_form.header("Set Input Variable")
laps = input_form.number_input('#Laps (0-100)', 0, 100, 20)
passenger = input_form.number_input('#Passenger (0-100)', 0, 100, 10)
battery_capacity = input_form.number_input('Battery Capacity (1-10000)', 1, 10000, 5000)
submit_button = input_form.form_submit_button("Calculate Score and Update Graph", on_click=calculate())

# 3. Description Section
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

# 4. 3D graph
with st.container():
    x, y, z = generate_surface_data()

    # Create a 3D surface plot using Plotly
    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])

    fig.update_layout(title=f'Score Graph @Battery Capacity: {battery_capacity}', autosize=False,
                        width=800, height=800,
                        margin=dict(l=65, r=50, b=65, t=90))

    fig.update_layout(scene=dict(xaxis_title='#Laps',
                                    yaxis_title='#Passenger',
                                    zaxis_title='Score'))

    # Display the plot in Streamlit
    st.plotly_chart(fig)

# 5. Line Graph
x2, y2, z2 = generate_line_data()
x3, y3, z3 = generate_line_data2()
if submit_button:
    x2, y2, z2 = generate_line_data()
    x3, y3, z3 = generate_line_data2()

col1, col2 = st.columns(2)
with col1:
    d = {'#Passengers': y2, 'Score': z2}

    df = pd.DataFrame(data=d)

    st.header(f'#Laps: {laps}')
    st.subheader(f'Battery Capacity: {battery_capacity}')
    st.line_chart(data=df, x='#Passengers', y='Score')


with col2:
    d = {'#Laps': x3, 'Score': z3}

    df = pd.DataFrame(data=d)

    st.header(f'#Passengers: {passenger}')
    st.subheader(f'Battery Capacity: {battery_capacity}')
    st.line_chart(data=df, x='#Laps', y='Score')