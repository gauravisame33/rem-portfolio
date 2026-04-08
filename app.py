import streamlit as st

st.set_page_config(page_title="REM Portfolio", layout="wide")

st.title("🌱 REM WORK PROFILE")
st.subheader("Renewable Energy Management Portfolio")

# Sidebar
st.sidebar.title("👤 Student Info")
st.sidebar.write("Name: Your Name")
st.sidebar.write("Course: REM")
st.sidebar.write("College: Your College")

# About
st.header("📌 About Me")
st.write("I am a Renewable Energy Management student interested in sustainable solutions like solar and wind energy.")

st.image("https://images.unsplash.com/photo-1509391366360-2e959784a276")

# Projects
st.header("⚙️ Projects")

col1, col2 = st.columns(2)

with col1:
    st.subheader("☀️ Solar Energy")
    st.write("Study of solar panel efficiency and applications.")

with col2:
    st.subheader("🌬️ Wind Energy")
    st.write("Analysis of wind turbines and energy generation.")

st.image("https://images.unsplash.com/photo-1466611653911-95081537e5b7")

# Assignments
st.header("📄 Assignments")
st.write("""
• Assignment 9 – Video Analysis  
• Assignment 10 – Web Profile  
• Design Project  
""")

# Skills
st.header("🧠 Skills")
st.write("""
✔ Renewable Energy  
✔ Energy Management  
✔ Sustainability  
✔ Basic Analysis  
""")

# Learnings
st.header("📈 Learnings")
st.write("Learned renewable energy applications and importance of sustainability.")

# Contact
st.header("📞 Contact")
st.write("Email: yourname@gmail.com")
