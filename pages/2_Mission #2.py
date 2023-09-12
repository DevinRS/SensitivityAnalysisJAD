import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


def generate_surface_data():
    x = np.linspace(0, 300, 20)
    y = np.linspace(0, 300, 20)
    x, y = np.meshgrid(x, y)
    z = 1+(x/y)  # Replace this with your equation
    return x, y, z

def generate_line_data():
    x = np.full((20), num1)
    y = np.linspace(1, 300, 20)
    z = 1+(x/y)
    return x, y, z

def generate_line_data2():
    x = np.linspace(0, 300, 20)
    y = np.full((20), num2)
    z = 1+(x/y)
    return x, y, z

def calculate():
    if num2 == 0:
        st.warning(f"Score = undefined")
    else:
        ans = 1+(num1/num2)
        st.success(f"Score = {ans}")

st.set_page_config(
    page_title="Sensitivity Analysis",
)

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

col1, col2, col3 = st.columns(3)
with col1:
    num1 = st.number_input('Payload Weight', 0, 300, 50)
with col2:
    num2 = st.number_input('3-Lap Time', 1, 300, 100)
with col3:
    # if st.button("Calculate Score"):
    if num1 or num2:
        calculate()


with st.container():
    x, y, z = generate_surface_data()

    # Create a 3D surface plot using Plotly
    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])

    fig.update_layout(title='Mission #2', autosize=False,
                        width=800, height=800,
                        margin=dict(l=65, r=50, b=65, t=90))

    fig.update_layout(scene=dict(xaxis_title='Payload Weight',
                                    yaxis_title='3-Lap Time',
                                    zaxis_title='Score'))

    # Display the plot in Streamlit
    st.plotly_chart(fig)

col4, col5 = st.columns(2)
with col4:
    x2, y2, z2 = generate_line_data()

    d = {'3-Lap Time': y2, 'Score': z2}

    df = pd.DataFrame(data=d)

    st.header(f'Payload Weight: {num1}')
    st.line_chart(data=df, x='3-Lap Time', y='Score')

with col5:
    x3, y3, z3 = generate_line_data2()

    d = {'Payload Weight': x3, 'Score': z3}

    df = pd.DataFrame(data=d)

    st.header(f'3-Lap Time: {num2}')
    st.line_chart(data=df, x='Payload Weight', y='Score')