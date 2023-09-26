import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def generate_surface_data():
    x = np.linspace(0, 20, 50)
    y = np.linspace(50, 300, 50)
    x, y = np.meshgrid(x, y)
    z = 1+((x/y)/0.4)  # Replace this with your equation
    return x, y, z

def generate_line_data():
    x = np.full((100), payload_weight)
    y = np.linspace(50, 300, 100)
    z = 1+((x/y)/0.4)
    return x, y, z

def generate_line_data2():
    x = np.linspace(0, 20, 100)
    y = np.full((100), lap_time)
    z = 1+((x/y)/0.4)
    return x, y, z

def calculate():
    ans = 1+((payload_weight/lap_time)/0.4)
    st.sidebar.info(f"Score = {ans}")

# 1. Page Config
st.set_page_config(
    page_title="Mission #2",
    page_icon='🚑'
)

# 2. Sidebar
st.sidebar.success('Select Mission Above 👆')
st.sidebar.title("Sensitivity Analysis")
input_form = st.sidebar.form("input_form")
input_form.header("Set Input Variable")
payload_weight = input_form.number_input('Payload Weight (0-20 lbs)', 0., 20., 10., 1e-2)
lap_time = input_form.number_input('3-Lap Time (50-300 s)', 50., 300., 100., 1e-2)
submit_button = input_form.form_submit_button("Calculate Score and Update Graph", on_click=calculate())

# 3. Description Section
st.title('Sensitivity Analysis')
st.subheader('''
Mission 2: Medical Transport Flight
- The payload for Mission 2 is the Crew, EMTs, Patient on gurney, and Medical Supply Cabinet.
- The airplane will enter the staging box in the parking configuration with the propulsion battery(ies) removed.
- The staging box judge will weigh the Medical Supplies Cabinet and record the weight on the score sheet.
- The ground crew will put the airplane in the flight configuration and install the battery(ies), Crew, floor insert (if used), EMTs, Patient on gurney, and Medical Supply Cabinet within the 5-minute staging window.
- There will be a 5-minute window for this mission.
- Teams will be timed for 3 laps.
- The score will be a function of the Medical Supply Cabinet weight / time to fly 3 laps.
- Time starts when the airplane throttle is advanced for the first take-off (or attempt).
- A lap is complete when the airplane passes over the start/finish line in the air (the landing is not part of the 5-minute time window).
- Must complete a successful landing to get a score.
''')
st.subheader('Score = 1 + (payload weight / time)')

# 4. 3D Graph
with st.container():
    x, y, z = generate_surface_data()

    # Create a 3D surface plot using Plotly
    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])

    fig.update_layout(title='Mission #2', autosize=False,
                        width=800, height=800,
                        margin=dict(l=65, r=50, b=65, t=90))

    fig.update_layout(scene=dict(xaxis_title='Payload Weight (lbs)',
                                    yaxis_title='3-Lap Time (s)',
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
    d = {'3-Lap Time (s)': y2, 'Score': z2}

    df = pd.DataFrame(data=d)

    st.subheader(f'Payload Weight: {payload_weight}lbs')
    st.line_chart(data=df, x='3-Lap Time (s)', y='Score')


with col2:
    d = {'Payload Weight (lbs)': x3, 'Score': z3}

    df = pd.DataFrame(data=d)

    st.subheader(f'3-Lap Time: {lap_time}s')
    st.line_chart(data=df, x='Payload Weight (lbs)', y='Score')