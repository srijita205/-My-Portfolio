import streamlit as st
from PIL import Image

# --- Page Configuration ---
st.set_page_config(page_title="Srijita Kayal | Data Analyst Portfolio", page_icon="📈", layout="centered")

# --- Header ---
st.title("Srijita Kayal")
st.subheader("Data & Business Analyst | Python Enthusiast | Power BI Explorer")
st.write("📍 Uluberia, Howrah, West Bengal | 📧 kayalsrijita2000@gmail.com | 📞 +91 6291184806")

with st.sidebar:
    image = Image.open("Srijita Kayal.JPG")  # Replace with your actual image file name
    st.image(image, width=180)
    st.markdown("### Srijita Kayal")
    st.markdown("📍 Uluberia, Howrah, West Bengal")
    st.markdown("[📧 kayalsrijita2000@gmail.com](mailto:kayalsrijita2000@gmail.com)")
    st.markdown("📞 +91 6291184806")
    # st.markdown("[GitHub](https://github.com/srijita205)")
    # st.markdown("[LinkedIn](https://www.linkedin.com/in/srijita-kayal-data-analytic-business-analytic)")
    # st.markdown("[Kaggle](https://www.kaggle.com/srijitakayal)")
# --- Social Media Links ---
st.sidebar.write("""


[![GitHub](https://img.shields.io/badge/GitHub-srijita205-181717?style=flat&logo=github)](https://github.com/srijita205)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Srijita_Kayal-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/srijita-kayal-data-analytic-business-analytic)
[![Kaggle](https://img.shields.io/badge/Kaggle-srijitakayal-20BEFF?style=flat&logo=kaggle)](https://www.kaggle.com/srijitakayal)
""")

# --- About Me ---
st.header("🧭 About Me")
st.write("""
I'm a dedicated Data & Business Analyst currently pursuing an MBA in Data Science and Business Analytics. 
With a strong academic background in geology and a growing command of tools like Python, SQL, Excel, and Power BI, 
I thrive on transforming data into strategic insights and meaningful visualizations.

My aim is to bridge the gap between technical data science and real-world business challenges, 
all while staying curious and creative.
""")

# --- Education ---
st.header("🎓 Education")
st.markdown("""
- **MBA in Data Science and Business Analytics**, Bengal Institute of Business Studies, Kolkata (2024 – 2026)  
  *Semester 1 GPA: 80%*
- **M.Sc. in Geology**, Central University of Punjab, Bhatinda (2021 – 2023)  
  *CGPA: 6.5*
- **B.Sc. in Geology**, Jogamaya Devi College, Kolkata (2018 – 2021)  
  *CGPA: 7.04*
""")

# --- Skills ---
st.header("🛠️ Skills")
st.markdown("""
- **Languages**: Python, SQL  
- **Tools**: Excel, Power BI, MS Office, CorelDraw  
- **Data Expertise**: Data Cleaning, Data Manipulation, Visualization, Statistical Analysis, Machine Learning  
""")

# --- Projects ---
st.header("📊 Projects")

st.markdown("""
### 📌 Unemployment Data Analysis (Power BI)
- Designed interactive dashboards visualizing unemployment trends across states.
- Cleaned and structured large datasets to ensure accurate reporting.

### 📌 Accenture Sales & Revenue Dashboard (Power BI)
- Built a detailed sales dashboard to analyze business performance.
- Enabled data-driven decision-making through dynamic visuals and KPIs.

### 📌 Deloitte Data Analytics Job Simulation (Forage)
- Gained experience in forensic data analysis and analytics-based decision-making.
- Explored data interpretation in a business investigation setting.  
📄 [View Certificate](https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/9PBTqmSxAf6zZTseP/io9DzWKe3PTsiS6GG_9PBTqmSxAf6zZTseP_dbyr7GbLstnn4wGX2_1741614764886_completion_certificate.pdf)

### 📌 Commonwealth Bank Data Science Simulation (Forage)
- Completed real-world tasks including data anonymisation, aggregation, and proposing analytical solutions.
- Designed a mock database and analysis approach to inform business insights.  
📄 [View Certificate](https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/2sNmYuurxgpFYawco/smwfytX3mcLboA9bf_2sNmYuurxgpFYawco_dbyr7GbLstnn4wGX2_1741614250847_completion_certificate.pdf)
""")

# --- Certifications ---
st.header("📑 Certifications")
st.markdown("""
- **Machine Learning with Python** – Winter Training Program (2024-2025), IIT Kanpur  
- **Machine Learning with Python** – Student Development Program (2024)  
- **Deloitte Data Analytics Simulation** – Forage (2025)  
- **Earth Day Model Competition (2022)** – Central University of Punjab  
""")

# --- Contact ---
st.header("📬 Contact Me")
st.write("I'd love to connect, collaborate, or just chat about data, analytics, or your next project!")
st.markdown("""
- 📧 [kayalsrijita2000@gmail.com](mailto:kayalsrijita2000@gmail.com)  
- 📞 +91 6291184806  
""")

