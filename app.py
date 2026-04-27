import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# --- Page Setup ---
st.set_page_config(page_title="Crusader Function Lab", page_icon="⚔️")

# --- MLK Custom Styling ---
st.markdown("""
<style>
body {
    background-color: #0a0a0a;
}
h1, h2, h3 {
    color: #C5A100;
}
.stApp {
    background-color: #111111;
    color: white;
}
.css-1d391kg {
    background-color: #0b3d2e;
}
</style>
""", unsafe_allow_html=True)

# --- Header ---
col1, col2 = st.columns([1, 4])
with col1:
    try:
        st.image("mlk_highschool_logo.png", width=90)
    except:
        pass

with col2:
    st.markdown("### www.cognitivecloud.ai")
    st.markdown("**Developed for Martin Luther King High School (Detroit) by Xavier Honablue M.Ed**")
    st.markdown("**Principal: Dr. Damian Perry**")

st.markdown("---")

# --- Title ---
st.title("⚔️ Crusader Function Lab: See the Math in Detroit")

st.markdown("""
Welcome, **MLK Crusaders**.

This isn’t just math — this is **Detroit in motion**.

Functions help explain:
- Your paycheck 💵  
- Your ride across the city 🚌  
- Your growth 📈  

---

### 🎯 Objective:
- Recognize functions in real life
- Connect math to your environment
- Build models that reflect your world
""")

# --- Standards ---
st.info("📚 **Michigan Learning Standards (HSF):** Functions, modeling, and real-world interpretation.")

# --- Student Identity ---
name = st.text_input("Enter your name:")
avatar = st.selectbox("Choose your multidimensional shape avatar:", [
    "🔺 Tetrahedron", "🚘 Dodecahedron", "⬛ Cube", "🌀 Torus"
])

if name:
    st.success(f"{name}, you're locked in. Welcome to the Lab ⚔️")

# --- Detroit-Based Matching ---
st.header("🎯 Detroit Function Matching Challenge")

matching_data = {
    "Function Name": [
        "Factory Pay", "Lions Ticket Growth", "DDOT Bus Time",
        "Phone Battery", "Jump Shot Arc", "YouTube Growth",
        "Gym Strength", "Heating Bill", "Temperature Drop", "Water Bill"
    ],
    "Rule f(x)": [
        "f(x) = 18x", "f(x) = 200 × 1.4^x", "f(x) = 12x + 5",
        "f(x) = 100 - 10x", "f(x) = -1(x-5)^2 + 25",
        "f(x) = 1000 + 75x", "f(x) = 100 log(x+1)",
        "f(x) = 50 + 2x", "f(x) = 65 - 3x", "f(x) = 30 + 1.5x"
    ],
    "Real-Life Context": [
        "🏭 Earn $18/hr at a Detroit plant",
        "🏈 Lions fanbase growth over seasons",
        "🚌 DDOT route time increases per stop",
        "🔋 Battery drains with use",
        "🏀 Jump shot arc at the park",
        "📺 Growing a Detroit YouTube channel",
        "🏋🏽 Strength gains slow over time",
        "🔥 Winter heating cost increases",
        "🌡️ Cold Detroit night temperature drop",
        "🚿 Water bill usage in the city"
    ]
}

df = pd.DataFrame(matching_data)
st.dataframe(df, use_container_width=True, hide_index=True)

# --- Function Visualizer ---
st.header("📊 Explore Detroit Functions")

examples = [
    {"label": "Factory Pay", "rule": lambda x: 18*x, "desc": "Detroit factory wages"},
    {"label": "DDOT Bus Time", "rule": lambda x: 12*x + 5, "desc": "Stops increase travel time"},
    {"label": "Lions Growth", "rule": lambda x: 200*(1.4**x), "desc": "Fanbase growth"},
    {"label": "Jump Shot", "rule": lambda x: -1*(x-5)**2 + 25, "desc": "Basketball arc"},
    {"label": "Heating Bill", "rule": lambda x: 50 + 2*x, "desc": "Winter heating cost"}
]

choice = st.selectbox("Choose a Detroit scenario:", [e["label"] for e in examples])

selected = next(e for e in examples if e["label"] == choice)

x = np.linspace(0, 10, 100)
y = selected["rule"](x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title(choice)
ax.grid()

st.pyplot(fig)
st.info(selected["desc"])

# --- Interactive Input ---
st.header("🧮 Test It")

val = st.slider("Choose an input value:", 0, 20, 5)
result = selected["rule"](val)

st.success(f"f({val}) = {result:.2f}")

# --- Reflection ---
st.header("🧾 Reflection")

reflection = st.text_area("Where do YOU see math in Detroit?")

if st.button("Submit"):
    if reflection:
        st.success("That's real-world math thinking. Keep building. ⚔️")
        st.balloons()

# --- Closing ---
st.markdown("---")
st.markdown("""
### 🏁 Final Thought

Math isn't just something you learn.

It's something you **use to understand your environment**.

Detroit runs on patterns.  
Functions help you see them.

⚔️ Stay sharp, Crusader.
""")
