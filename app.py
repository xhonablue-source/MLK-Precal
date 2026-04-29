import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# --- Page Setup ---
st.set_page_config(page_title="Crusader Vision: See the Function", page_icon="👁️")

# --- Developer Credit ---
col1, col2 = st.columns([1, 4])
with col1:
    # MLK High School Logo - you'll need to add the logo file to your project
    try:
        st.image("mlk_hs_logo.png", width=80)
    except:
        pass  # No fallback if logo file not found

with col2:
    st.markdown("### www.cognitivecloud.ai")
    st.markdown("**Developed for Martin Luther King High School by Xavier Honablue M.Ed**")
    st.markdown("**Principal: Damian Perry | Detroit, Michigan**")

st.markdown("---")

# --- Title and Intro ---
st.title("👁️ Crusader Vision: See the Function")
st.markdown("""
Welcome, **MLK Standards Crusaders**!  
This MathCraft lesson helps you **see, understand, and recognize** real-life functions — and what they mean for your world.

---

### 📘 Classic Explanation:
A **function** is a rule that connects every input to exactly one output.  
Think of it like a vending machine: press a button (input), get a snack (output).  
You wouldn't press one button and get random snacks — that's not a function.

---

### 🎯 Objective:
By the end of this lesson, you'll be able to:
- Define and identify functions
- Distinguish between function types
- Match real-life examples to function models
- Interpret graphs and expressions
""")

# Michigan Learning Standards Alignment
st.info("📚 **Michigan Merit Curriculum Standards:** This lesson aligns with high school function standards including interpreting, building, and graphing functions in real-world contexts.")

# Michigan Standards Dropdown
michigan_standard = st.selectbox("📋 Select specific Michigan Merit Curriculum Standard:", [
    "HSA.F.IF.1 - Understand that a function assigns to each input exactly one output",
    "HSA.F.IF.2 - Use function notation, evaluate functions for inputs in their domains", 
    "HSA.F.IF.4 - Interpret key features of graphs and tables in terms of quantities",
    "HSA.F.IF.5 - Relate domain of a function to its graph and to relationships it describes",
    "HSA.F.IF.7 - Graph functions expressed symbolically and show key features",
    "HSA.F.IF.8 - Write a function defined by an expression in different equivalent forms",
    "HSA.F.IF.9 - Compare properties of two functions each represented in a different way",
    "HSA.F.BF.1 - Write a function that describes a relationship between two quantities",
    "HSA.F.BF.3 - Identify the effect on the graph of replacing f(x) by f(x) + k",
    "HSA.F.LE.1 - Distinguish between situations that can be modeled with linear functions",
    "HSA.F.LE.2 - Construct linear and exponential functions given a graph or description",
    "HSA.F.LE.3 - Observe using graphs and tables that exponential functions grow by factors"
])

# --- Student Info ---
name = st.text_input("Enter your name:")
avatar = st.selectbox("Choose your multidimensional shape avatar:", [
    "🔺 Tetrahedron", "🚘 Dodecahedron", "⬛ Cube", "🌀 Torus"
])

if name:
    st.success(f"Welcome, {name} the {avatar}! Let's begin Crusader Vision.")

# --- Role or Identity Selection ---
role_options = [
    "🌟 Skill Mastery Star",
    "🚀 Growth Mode",
    "🎮 Level-Up Leader",
    "🎯 Focus Champ",
    "📊 Data Boss",
    "🧠 Brain Builder",
    "🎓 Crusader Scholar",
    "📈 Goal Getter",
    "🛠️ Problem Solver",
    "💡 Idea Generator"
]
role = st.selectbox("Pick your learning mode or style:", role_options)

# --- Function Explorer Section ---
st.header("🔍 Let's explore what a function looks like in real life...")

# Matching Activity Section
st.header("🎯 Function Matching Challenge")
st.markdown("**Match each function rule to its real-life context before exploring the visualizations!**")

# Create the matching data - DETROIT EDITION
matching_data = {
    "Function Name": [
        "Auto Factory Pay", "TikTok Followers", "Lyft Ride", "Phone Battery", 
        "Lions QB Throw", "Instagram Growth", "Gym Progress", "DDOT Bus Route", 
        "Winter Temp Drop", "DTE Energy Bill"
    ],
    "Rule f(x)": [
        "f(x) = 28x (USD)", "f(x) = 500 × 1.4^x", "f(x) = 3x + 2.5", 
        "f(x) = 100 - 10x (%)", "f(x) = -1(x - 15)² + 35 (feet)", 
        "f(x) = 1000 + 75x (followers)", "f(x) = 100 × log(x+1) (lbs)", 
        "f(x) = 12x + 8 (minutes)", "f(x) = 32 - 3x (°F)", 
        "f(x) = 45 + 0.12x (USD)"
    ],
    "Real-Life Context": [
        "🏭 Earn $28/hour at Detroit auto plant",
        "📱 Start with 500, grow 40% daily when viral", 
        "🚗 $2.50 base + $3 per mile on Lyft",
        "🔋 Lose 10% battery/hour",
        "🏈 Lions QB throw arc - Jared Goff style",
        "📸 Start with 1000 followers, gain 75/week",
        "🏋🏽 Build strength at Detroit gym - slows over time",
        "🚌 DDOT bus: 8 min base + 12 min per stop",
        "🌡️ Detroit winter: drops 3°F/hour after sunset",
        "⚡ DTE bill: $45 base + $0.12 per kWh"
    ]
}

# Display as a styled table
df = pd.DataFrame(matching_data)
st.dataframe(df, use_container_width=True, hide_index=True)

# Interactive matching quiz
st.subheader("📝 Quick Matching Quiz")
st.markdown("Test your understanding by matching these function types:")

# Quiz questions for matching - DETROIT EDITION
quiz_options = {
    "Which function represents EXPONENTIAL growth?": {
        "options": ["f(x) = 28x", "f(x) = 500 × 1.4^x", "f(x) = 3x + 2.5", "f(x) = 100 - 10x"],
        "correct": "f(x) = 500 × 1.4^x",
        "explanation": "Exponential functions have the variable in the exponent (1.4^x), showing rapid growth like viral content!"
    },
    "Which function shows a QUADRATIC relationship?": {
        "options": ["f(x) = 32 - 3x", "f(x) = -1(x - 15)² + 35", "f(x) = 100 × log(x+1)", "f(x) = 45 + 0.12x"],
        "correct": "f(x) = -1(x - 15)² + 35",
        "explanation": "Quadratic functions have x², creating parabolic shapes like a Lions QB throw!"
    },
    "Which function has a CONSTANT rate of change?": {
        "options": ["f(x) = 500 × 1.4^x", "f(x) = 100 × log(x+1)", "f(x) = 28x", "f(x) = -1(x - 15)² + 35"],
        "correct": "f(x) = 28x",
        "explanation": "Linear functions like f(x) = 28x have constant rates - you earn the same $28 every hour at the auto plant!"
    }
}

for question, data in quiz_options.items():
    st.write(f"**{question}**")
    user_answer = st.radio("Select your answer:", data["options"], key=question)
    
    if st.button(f"Check Answer", key=f"check_{question}"):
        if user_answer == data["correct"]:
            st.success(f"✅ Correct! {data['explanation']}")
        else:
            st.error(f"❌ Try again! The correct answer is {data['correct']}. {data['explanation']}")

st.markdown("---")

# Real-Life Function Examples - DETROIT EDITION
st.header("🔟 Interactive Function Visualizations")

examples = [
    {
        "label": "Auto Factory Pay",
        "rule": lambda x: 28 * x,
        "expr": "f(x) = 28x",
        "unit": "(USD)",
        "desc": "🏭 Earn $28 per hour working at a Detroit auto plant (Ford, GM, Stellantis).",
        "domain": "Hours worked (0-40)",
        "range": "Weekly pay ($0-$1,120)"
    },
    {
        "label": "TikTok Followers",
        "rule": lambda x: 500 * (1.4 ** x),
        "expr": "f(x) = 500 × 1.4^x",
        "unit": "(followers)",
        "desc": "📱 Start with 500 followers, grow exponentially by 40% each day when content goes viral.",
        "domain": "Days (0-10)",
        "range": "Follower count (500-14,347)"
    },
    {
        "label": "Lyft Ride",
        "rule": lambda x: 3 * x + 2.5,
        "expr": "f(x) = 3x + 2.5",
        "unit": "(USD)",
        "desc": "🚗 $2.50 base fare + $3 per mile for Lyft ride around Detroit.",
        "domain": "Miles traveled (0-20)",
        "range": "Total fare ($2.50-$62.50)"
    },
    {
        "label": "Phone Battery",
        "rule": lambda x: np.maximum(0, 100 - 10 * x),
        "expr": "f(x) = 100 - 10x",
        "unit": "(%)",
        "desc": "🔋 Lose 10% battery per hour streaming music or gaming.",
        "domain": "Hours of use (0-10)",
        "range": "Battery percentage (0-100%)"
    },
    {
        "label": "Lions QB Throw",
        "rule": lambda x: np.maximum(0, -1 * (x - 15)**2 + 35),
        "expr": "f(x) = -1(x - 15)² + 35",
        "unit": "(feet)",
        "desc": "🏈 Detroit Lions quarterback throw arc - parabolic path from release to catch.",
        "domain": "Horizontal distance (0-30 yards)",
        "range": "Height (0-35 feet)"
    },
    {
        "label": "Instagram Growth",
        "rule": lambda x: 1000 + 75 * x,
        "expr": "f(x) = 1000 + 75x",
        "unit": "(followers)",
        "desc": "📸 Start with 1000 followers, gain 75 per week posting Detroit content.",
        "domain": "Weeks (0-52)",
        "range": "Follower count (1,000-4,900)"
    },
    {
        "label": "Gym Progress",
        "rule": lambda x: 100 * np.log(x + 1),
        "expr": "f(x) = 100 × log(x + 1)",
        "unit": "(lbs)",
        "desc": "🏋🏽 Build strength at Detroit Athletic Club - rapid gains early, then slows.",
        "domain": "Weeks of training (0-52)",
        "range": "Strength gained (0-395 lbs)"
    },
    {
        "label": "DDOT Bus Route",
        "rule": lambda x: 12 * x + 8,
        "expr": "f(x) = 12x + 8",
        "unit": "(minutes)",
        "desc": "🚌 DDOT bus route: 8 minute base time + 12 minutes per stop.",
        "domain": "Number of stops (0-15)",
        "range": "Total time (8-188 minutes)"
    },
    {
        "label": "Winter Temp Drop",
        "rule": lambda x: 32 - 3 * x,
        "expr": "f(x) = 32 - 3x",
        "unit": "(°F)",
        "desc": "🌡️ Detroit winter temperature drops 3°F per hour after sunset.",
        "domain": "Hours after sunset (0-12)",
        "range": "Temperature (-4°F to 32°F)"
    },
    {
        "label": "DTE Energy Bill",
        "rule": lambda x: 45 + 0.12 * x,
        "expr": "f(x) = 45 + 0.12x",
        "unit": "(USD)",
        "desc": "⚡ DTE Energy bill: $45 base charge + $0.12 per kilowatt-hour used.",
        "domain": "Kilowatt-hours (0-1000)",
        "range": "Bill amount ($45-$165)"
    },
]

# Function Selection and Visualization
selected = st.selectbox("Choose a real-life function to explore:", [ex["label"] for ex in examples])

# Find the selected example
selected_ex = None
for ex in examples:
    if selected == ex["label"]:
        selected_ex = ex
        break

if selected_ex:
    # Create two columns for layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Generate appropriate x values based on the function
        if selected == "Lions QB Throw":
            x_vals = np.linspace(0, 30, 100)
        elif selected == "Phone Battery":
            x_vals = np.linspace(0, 10, 100)
        elif selected == "Gym Progress":
            x_vals = np.linspace(0, 52, 100)
        elif selected == "Instagram Growth":
            x_vals = np.linspace(0, 52, 100)
        elif selected == "DTE Energy Bill":
            x_vals = np.linspace(0, 1000, 100)
        elif selected == "DDOT Bus Route":
            x_vals = np.linspace(0, 15, 100)
        elif selected == "Winter Temp Drop":
            x_vals = np.linspace(0, 12, 100)
        else:
            x_vals = np.linspace(0, 10, 100)
        
        y_vals = selected_ex["rule"](x_vals)
        
        # Create the plot with gold accent
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(x_vals, y_vals, linewidth=3, color='#FFD700')  # Gold color
        ax.set_title(f"{selected_ex['label']} {selected_ex['expr']} {selected_ex['unit']}", 
                    fontsize=14, fontweight='bold')
        ax.set_xlabel("Input (x)", fontsize=12)
        ax.set_ylabel(f"Output f(x) {selected_ex['unit']}", fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.set_facecolor('#f8f9fa')
        
        st.pyplot(fig)
    
    with col2:
        st.info(f"**Description:** {selected_ex['desc']}")
        st.write(f"**Domain:** {selected_ex['domain']}")
        st.write(f"**Range:** {selected_ex['range']}")
        st.write(f"**Expression:** `{selected_ex['expr']}`")

# Interactive Input Testing
st.header("🧮 Test Your Function")
if selected_ex:
    st.write(f"Try different inputs for the **{selected}** function:")
    
    # Get appropriate input range - DETROIT EDITION
    if selected == "Auto Factory Pay":
        test_input = st.slider("Hours worked:", 0, 40, 8)
    elif selected == "TikTok Followers":
        test_input = st.slider("Days:", 0, 10, 3)
    elif selected == "Lyft Ride":
        test_input = st.slider("Miles traveled:", 0, 20, 5)
    elif selected == "Phone Battery":
        test_input = st.slider("Hours of use:", 0, 10, 3)
    elif selected == "Lions QB Throw":
        test_input = st.slider("Horizontal distance (yards):", 0, 30, 15)
    elif selected == "Instagram Growth":
        test_input = st.slider("Weeks:", 0, 52, 12)
    elif selected == "Gym Progress":
        test_input = st.slider("Weeks of training:", 0, 52, 12)
    elif selected == "DDOT Bus Route":
        test_input = st.slider("Number of stops:", 0, 15, 5)
    elif selected == "Winter Temp Drop":
        test_input = st.slider("Hours after sunset:", 0, 12, 4)
    else:  # DTE Energy Bill
        test_input = st.slider("Kilowatt-hours used:", 0, 1000, 500)
    
    # Calculate and display result
    result = selected_ex["rule"](test_input)
    st.success(f"When x = {test_input}, f(x) = {result:.2f} {selected_ex['unit']}")

# Function Types Classification - DETROIT EDITION
st.header("🎯 Function Types in Action")

function_types = {
    "Linear Functions": {
        "examples": ["Auto Factory Pay", "Lyft Ride", "Instagram Growth", "DDOT Bus Route", "Winter Temp Drop", "DTE Energy Bill"],
        "form": "f(x) = mx + b",
        "description": "Constant rate of change - creates straight lines"
    },
    "Exponential Functions": {
        "examples": ["TikTok Followers"],
        "form": "f(x) = a × b^x",
        "description": "Rapid growth or decay - creates curved lines"
    },
    "Quadratic Functions": {
        "examples": ["Lions QB Throw"],
        "form": "f(x) = ax² + bx + c",
        "description": "Parabolic shape - has maximum or minimum point"
    },
    "Logarithmic Functions": {
        "examples": ["Gym Progress"],
        "form": "f(x) = a × log(x + b)",
        "description": "Rapid change initially, then levels off"
    }
}

type_selected = st.selectbox("Explore function types:", list(function_types.keys()))
type_info = function_types[type_selected]

st.write(f"**Form:** {type_info['form']}")
st.write(f"**Description:** {type_info['description']}")
st.write(f"**Examples from our list:** {', '.join(type_info['examples'])}")

# Quick Quiz Section
st.header("🎲 Quick Understanding Check")

quiz_questions = [
    {
        "question": "Which situation represents a linear function?",
        "options": ["Earning $28 per hour at auto plant", "Viral TikTok growth", "Lions QB throw arc", "Gym strength gains"],
        "correct": 0,
        "explanation": "Linear functions have a constant rate of change - $28 per hour is constant!"
    },
    {
        "question": "What makes something a function?",
        "options": ["It has an x and y", "Each input has exactly one output", "It creates a curve", "It uses numbers"],
        "correct": 1,
        "explanation": "Functions must pass the vertical line test - each input (x) gives exactly one output (y)!"
    },
    {
        "question": "Which function type would model a football's flight path?",
        "options": ["Linear", "Exponential", "Quadratic", "Logarithmic"],
        "correct": 2,
        "explanation": "Quadratic functions create parabolic shapes, perfect for projectile motion like a Lions QB throw!"
    }
]

for i, q in enumerate(quiz_questions):
    st.write(f"**Question {i+1}:** {q['question']}")
    answer = st.radio(f"Select your answer for Q{i+1}:", q['options'], key=f"q{i}")
    
    if st.button(f"Check Answer {i+1}", key=f"check{i}"):
        if q['options'].index(answer) == q['correct']:
            st.success(f"✅ Correct! {q['explanation']}")
        else:
            st.error(f"❌ Try again! {q['explanation']}")

# Exit Reflection
st.header("🧾 Reflection")
reflection = st.text_area("What is one real-world situation you could model with a function? Describe the input, output, and what type of function it might be.")

if st.button("Submit Reflection"):
    if reflection.strip():
        st.success("✅ Excellent mathematical thinking! You're seeing functions everywhere now!")
        st.balloons()
    else:
        st.warning("Please share your thoughts to complete the reflection.")

# IXL Integration Section
st.header("📚 IXL Practice & Related Lessons")

# Common Core Strand Selection for Targeted Resources
st.subheader("🎯 Choose Your Learning Focus")
strand = st.selectbox("Select a Common Core Math Strand to customize your resources:", [
    "HSA-CED.A.1 – Create equations",
    "HSF-IF.B.4 – Interpret key features of functions", 
    "HSF-IF.C.7 – Graph functions expressed symbolically",
    "HSF-BF.A.1 – Build a function that models a relationship"
])

# Adaptive content based on strand selection
if "HSA-CED.A.1" in strand:
    st.info("🎯 **Focus: Creating Equations** - Resources emphasize building function equations from word problems and real-world scenarios.")
    emphasis = "equation_building"
elif "HSF-IF.B.4" in strand:
    st.info("🎯 **Focus: Interpreting Key Features** - Resources emphasize domain, range, intercepts, and analyzing function behavior.")
    emphasis = "key_features"
elif "HSF-IF.C.7" in strand:
    st.info("🎯 **Focus: Graphing Functions** - Resources emphasize visual interpretation, graphing techniques, and reading graphs.")
    emphasis = "graphing"
else:  # HSF-BF.A.1
    st.info("🎯 **Focus: Building Function Models** - Resources emphasize real-world modeling and creating functions from situations.")
    emphasis = "modeling"

# IXL lessons organized by grade level and topic - now adaptive based on strand
ixl_lessons = {
    "Algebra 1": {
        "Function Basics": [
            "A.1 - Identify functions",
            "A.2 - Evaluate functions", 
            "A.3 - Domain and range of functions",
            "A.5 - Graph a function",
            "A.6 - Find the slope of a graph"
        ],
        "Linear Functions": [
            "B.1 - Identify linear functions",
            "B.2 - Find the slope of a linear function",
            "B.3 - Graph a linear function", 
            "B.4 - Write linear functions: word problems",
            "B.5 - Interpret the graph of a linear function"
        ],
        "Exponential Functions": [
            "P.1 - Identify exponential functions",
            "P.2 - Evaluate exponential functions",
            "P.3 - Graph exponential functions",
            "P.4 - Exponential growth and decay: word problems"
        ],
        "Quadratic Functions": [
            "Q.1 - Identify quadratic functions",
            "Q.2 - Evaluate quadratic functions", 
            "Q.3 - Graph quadratic functions",
            "Q.4 - Solve quadratic equations by graphing"
        ]
    },
    "Algebra 2": {
        "Advanced Functions": [
            "A.1 - Domain and range of functions",
            "A.2 - Identify functions: graphs",
            "A.3 - Evaluate functions",
            "A.4 - Function transformation rules",
            "A.5 - Transformations of functions"
        ],
        "Polynomial Functions": [
            "B.1 - Polynomial vocabulary",
            "B.2 - Evaluate polynomials", 
            "B.3 - Add and subtract polynomials",
            "B.4 - Graph polynomial functions"
        ],
        "Logarithmic Functions": [
            "M.1 - Convert between exponential and logarithmic form",
            "M.2 - Evaluate logarithms",
            "M.3 - Graph logarithmic functions",
            "M.4 - Domain and range of logarithmic functions"
        ]
    },
    "Precalculus": {
        "Function Analysis": [
            "A.1 - Function composition",
            "A.2 - Inverse functions",
            "A.3 - Even and odd functions", 
            "A.4 - Domain and range of functions"
        ],
        "Trigonometric Functions": [
            "C.1 - Graph sine and cosine functions",
            "C.2 - Graph tangent and cotangent functions",
            "C.3 - Amplitude, period, and phase shift",
            "C.4 - Write equations of sine and cosine functions"
        ]
    }
}

# Adaptive IXL recommendations based on strand
if emphasis == "equation_building":
    st.markdown("**🎯 Recommended for Creating Equations:**")
    priority_lessons = [
        "Algebra 1 > B.4 - Write linear functions: word problems", 
        "Algebra 1 > P.4 - Exponential growth and decay: word problems", 
        "Algebra 1 > A.2 - Evaluate functions"
    ]
elif emphasis == "key_features":
    st.markdown("**🎯 Recommended for Interpreting Key Features:**") 
    priority_lessons = [
        "Algebra 1 > A.3 - Domain and range of functions", 
        "Algebra 1 > B.5 - Interpret the graph of a linear function", 
        "Algebra 2 > A.1 - Domain and range of functions"
    ]
elif emphasis == "graphing":
    st.markdown("**🎯 Recommended for Graphing Functions:**")
    priority_lessons = [
        "Algebra 1 > A.5 - Graph a function", 
        "Algebra 1 > B.3 - Graph a linear function", 
        "Algebra 1 > P.3 - Graph exponential functions", 
        "Algebra 1 > Q.3 - Graph quadratic functions"
    ]
else:  # modeling
    st.markdown("**🎯 Recommended for Building Function Models:**")
    priority_lessons = [
        "Algebra 1 > B.4 - Write linear functions: word problems", 
        "Algebra 1 > P.4 - Exponential growth and decay: word problems", 
        "Algebra 1 > A.2 - Evaluate functions"
    ]

for lesson in priority_lessons:
    st.write(f"⭐ **{lesson}**")

st.markdown("---")

# Let user select grade level for IXL recommendations
grade_level = st.selectbox("Select your grade level for IXL recommendations:", list(ixl_lessons.keys()))
selected_ixl = ixl_lessons[grade_level]

# Display IXL lessons in expandable sections
for topic, lessons in selected_ixl.items():
    with st.expander(f"📖 {topic} - IXL Lessons"):
        for lesson in lessons:
            st.write(f"• {lesson}")
        st.markdown(f"**🎯 Practice Tip:** Complete these lessons on IXL to master {topic.lower()} concepts!")

# Outside Resources Section
st.header("🌐 Additional Learning Resources")

# Categorized external resources
resources = {
    "📺 Video Tutorials": [
        {
            "name": "Khan Academy - Intro to Functions",
            "url": "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:functions",
            "description": "Comprehensive video series on function basics, domain, range, and graphing"
        },
        {
            "name": "Professor Leonard - Function Fundamentals",
            "url": "https://www.youtube.com/watch?v=kvGsIo1TmsM",
            "description": "Clear, detailed explanations of function concepts with worked examples"
        },
        {
            "name": "3Blue1Brown - Essence of Calculus",
            "url": "https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr",
            "description": "Visual and intuitive approach to understanding functions and their behavior"
        }
    ],
    "💻 Interactive Tools": [
        {
            "name": "Desmos Graphing Calculator",
            "url": "https://www.desmos.com/calculator",
            "description": "Free online graphing tool to visualize functions and explore their properties"
        },
        {
            "name": "GeoGebra Functions",
            "url": "https://www.geogebra.org/m/x39ys4d7",
            "description": "Interactive function explorer with sliders and dynamic visualization"
        },
        {
            "name": "Wolfram Alpha",
            "url": "https://www.wolframalpha.com/",
            "description": "Computational engine for function analysis, graphing, and problem solving"
        }
    ],
    "📚 Study Guides & Practice": [
        {
            "name": "Paul's Online Math Notes",
            "url": "https://tutorial.math.lamar.edu/Classes/Alg/Functions.aspx",
            "description": "Comprehensive notes on functions with examples and practice problems"
        },
        {
            "name": "Purplemath - Functions",
            "url": "https://www.purplemath.com/modules/fcns.htm",
            "description": "Step-by-step tutorials on function concepts and problem-solving strategies"
        },
        {
            "name": "Mathway Function Solver",
            "url": "https://www.mathway.com/",
            "description": "Online problem solver for function-related homework and practice"
        }
    ],
    "🎮 Educational Games": [
        {
            "name": "Function Machine - Math Playground",
            "url": "https://www.mathplayground.com/functionmachine.html",
            "description": "Interactive game to practice identifying function rules and patterns"
        },
        {
            "name": "Algebra Tiles - National Library of Virtual Manipulatives",
            "url": "https://www.glencoe.com/sites/common_assets/mathematics/ebook_assets/vmf/VMF-Interface.html",
            "description": "Visual tool for understanding algebraic concepts and function building"
        }
    ],
    "📖 Reference Materials": [
        {
            "name": "Common Core State Standards - Functions",
            "url": "http://www.corestandards.org/Math/Content/HSF/",
            "description": "Official standards document outlining function learning objectives"
        },
        {
            "name": "NCTM - Functions Resource",
            "url": "https://www.nctm.org/",
            "description": "National Council of Teachers of Mathematics resources for function instruction"
        }
    ]
}

# Display resources in organized tabs
resource_tabs = st.tabs(list(resources.keys()))

for i, (category, items) in enumerate(resources.items()):
    with resource_tabs[i]:
        for item in items:
            st.markdown(f"**[{item['name']}]({item['url']})**")
            st.write(f"📝 {item['description']}")
            st.write("---")

# Study Plan Generator
st.header("📅 Personalized Study Plan")

# Get student's current level and goals
current_level = st.selectbox("What's your current comfort level with functions?", [
    "Beginner - Just starting to learn about functions",
    "Intermediate - Understand basics, need more practice",
    "Advanced - Ready for complex function types",
    "Expert - Looking for challenge problems"
])

study_time = st.selectbox("How much time can you dedicate to studying functions per week?", [
    "1-2 hours",
    "3-4 hours", 
    "5-6 hours",
    "7+ hours"
])

# Generate personalized recommendations
if st.button("Generate My Study Plan"):
    st.success("🎯 Your Personalized Function Mastery Plan:")
    
    if "Beginner" in current_level:
        st.markdown("""
        **Week 1-2: Foundation Building**
        - Watch Khan Academy's "Intro to Functions" videos
        - Complete IXL lessons A.1-A.3 (Function Basics)
        - Practice with Desmos graphing calculator daily
        
        **Week 3-4: Linear Functions**
        - Focus on IXL lessons B.1-B.5 (Linear Functions)
        - Use Function Machine game for pattern recognition
        - Complete reflection exercises in this app
        """)
    
    elif "Intermediate" in current_level:
        st.markdown("""
        **Week 1: Review & Strengthen**
        - Complete remaining IXL function basics lessons
        - Practice with interactive tools (GeoGebra)
        - Work through Paul's Online Math Notes
        
        **Week 2-3: Expand to New Function Types**
        - Study exponential and quadratic functions
        - Use Wolfram Alpha for complex graphing
        - Create your own real-world function examples
        """)
    
    elif "Advanced" in current_level:
        st.markdown("""
        **Week 1: Master Advanced Concepts**
        - Complete Algebra 2 IXL lessons
        - Study function transformations and composition
        - Explore 3Blue1Brown's visual approach
        
        **Week 2: Real-World Applications**
        - Research functions in your field of interest
        - Create presentations on function modeling
        - Challenge yourself with competition problems
        """)
    
    else:  # Expert
        st.markdown("""
        **Ongoing Challenge Plan:**
        - Complete Precalculus IXL lessons
        - Study advanced function theory
        - Mentor other students learning functions
        - Explore mathematical research involving functions
        """)
    
    # Time-based recommendations
    if study_time == "1-2 hours":
        st.info("💡 **Tip:** Focus on one concept per week with daily 15-minute practice sessions.")
    elif study_time == "3-4 hours":
        st.info("💡 **Tip:** Balance video learning (60%) with hands-on practice (40%).")
    elif study_time == "5-6 hours":
        st.info("💡 **Tip:** Add teaching others to solidify your understanding.")
    else:
        st.info("💡 **Tip:** Consider pursuing advanced topics like calculus or mathematical modeling.")

st.markdown("---")
st.markdown(f"**🎯 Your Selected Focus:** {strand}")
st.markdown("**📍 Michigan Merit Curriculum Standards:** This lesson supports high school function standards and mathematical modeling practices.")

# Final Summary
st.header("🎓 What You've Learned")
st.markdown("""
**Congratulations!** You've explored:
- ✅ **10 real-life Detroit functions** from auto plants to Lions games to DTE bills
- ✅ **4 different function types** and their characteristics  
- ✅ **Interactive testing** to see how inputs affect outputs
- ✅ **Visual representations** that make math come alive

**Remember:** Functions are everywhere in your daily life in Detroit - from your paycheck at the auto plant to the DDOT bus schedule to your DTE bill. Math isn't just numbers on a page - it's the language that describes how our world works!

Keep your **Crusader Vision** sharp and you'll see functions everywhere! ⚔️
""")
