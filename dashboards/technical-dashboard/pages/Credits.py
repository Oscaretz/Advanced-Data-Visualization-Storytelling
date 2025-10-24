import streamlit as st
from PIL import Image

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Credits & Closing",
    layout="centered",
)

# -----------------------------
# HEADER SECTION
# -----------------------------
st.title("Credits & Closing")
st.markdown("""
#### *Corporate Data Visualization Suite*
Thank you for exploring our interactive analytical dashboard built with **Streamlit**, **Plotly**, and **Pandas**.  
This project reflects teamwork, data craftsmanship, and creative visualization.
""")

st.divider()

# -----------------------------
# TEAM SECTION
# -----------------------------
st.markdown("### Project Contributors")

# Animated appreciation
st.balloons()

# Define team members
team = [
    {
        "name": "Oscar Martinez Estevez",
        "role": "Streamlit App Development",
        "github": "https://github.com/Oscaretz"
    },
    {
        "name": "Luis Michel Perez",
        "role": "Streamlit App Development",
        "github": "https://github.com/LuisMichelP"
    },
    {
        "name": "Braulio Perez Tamayo",
        "role": "Data Analysis Scripts",
        "github": "https://github.com/BraulioPerez/Image_processing"
    },
    {
        "name": "Moises Carrillo Alonzo",
        "role": "Data Preprocessing",
        "github": "https://github.com/Moisescar3008"
    },
    {
        "name": "David Hernandez",
        "role": "Data Analysis Scripts",
        "github": "https://github.com/MDavidHernandezP"
    },
    {
        "name": "Gerardo Hernandez Widman",
        "role": "Documentation",
        "github": "https://github.com/widmanhg"
    },
]

# Create team cards
for member in team:
    with st.container():
        col1, col2 = st.columns([1, 5])
        with col1:
            st.image("https://cdn-icons-png.flaticon.com/512/9131/9131529.png", width=60)
        with col2:
            st.markdown(f"**{member['name']}**  \n*{member['role']}*  \n[GitHub Profile]({member['github']})")
        st.markdown("---")

# -----------------------------
# TECHNOLOGIES SECTION
# -----------------------------
st.markdown("### Technologies Used")

with st.expander("View Tools and Libraries", expanded=True):
    st.markdown("""
    #### 🖥️ Core Frameworks
    - **Streamlit** 🎈 — Interactive web framework for data apps  
    - **Python** 🐍 — Main programming language  

    #### 📊 Data Handling
    - **Pandas** 🧮 — Data manipulation and analysis  
    - **NumPy** ⚙️ — Numerical computations  
    - **Pathlib** 🗂️ — File and directory path management  

    #### 📈 Visualization
    - **Plotly Express** 📊 — Fast interactive plotting  
    - **Plotly Graph Objects** 📉 — Advanced chart customization  
    - **Matplotlib** 🎨 — Static plotting for detailed visuals  
    - **Squarify** 🟩 — Treemap generation  
    - **Plotly Figure Factory** 🧩 — Custom chart creation (e.g., dendrograms)  

    #### 🧠 Data Science & Analytics
    - **SciPy** 🧪 — Hierarchical clustering and linkage computation  
    - **Scikit-learn** 🧰 — Data scaling and preprocessing  

    #### 💾 Data Sources
    - **CSV files** — Population, budget, and organizational datasets  
    - **Local data integration** using `Path` for dynamic project portability  

    #### 💡 Development Tools
    - **Git & GitHub** 🧭 — Version control and collaboration  
    - **Visual Studio Code** 💻 — Development environment  
    """)

# -----------------------------
# REPOSITORY SECTION
# -----------------------------
st.divider()
st.markdown("### Project Repository")
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/25/25231.png", width=60)
with col2:
    st.markdown("""
    You can explore the full source code, project documentation, and dashboards in our GitHub repository:  
    👉 [**Advanced Data Visualization Storytelling (Portfolio Branch)**](https://github.com/Oscaretz/Advanced-Data-Visualization-Storytelling/tree/portfolio)
    """)
    st.divider()
    st.markdown("""
    #### *Corporate Data Visualization Suite*
    Thank you for exploring our interactive analytical dashboard built with **Streamlit**, **Plotly**, and **Pandas**.  
    This project showcases a blend of **data storytelling**, **hierarchical analysis**, and **interactive visualization techniques**.

    We applied **exploratory data analysis (EDA)** practices, hierarchical clustering, and visual storytelling to uncover structural and quantitative insights.  
    The suite includes a variety of visualizations such as **treemaps**, **dendrograms**, **sunburst charts**, and **circular treemaps**, each designed to illustrate complex corporate data relationships in a clear and engaging way.
    """)


# -----------------------------
# CLOSING SECTION
# -----------------------------


# Centered goodbye section
st.markdown("<h4 style='text-align:center; color:gray;'> Happy coding! 💻</h4>", unsafe_allow_html=True)


