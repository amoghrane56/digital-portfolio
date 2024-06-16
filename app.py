from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "my-profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Portfolio | Amogh Rane"
PAGE_ICON = ":wave:"
NAME = "Amogh Rane"
DESCRIPTION = """
Aspiring Data Scientist and Machine Learning Enthusiast.
"""
EMAIL = "amoghrane56@gmail.com"
SOCIAL_MEDIA = {
    "GitHub": "https://github.com/amoghrane56",
    "Kaggle" : "https://www.kaggle.com/work",
}
PROJECTS = {
    "🏆 Market Regime Clustering - Identify Indian Market Behaviour using GMM.": "https://github.com/amoghrane56/Market-Regime-Clustering",
    "🏆 Football Player Recommender - Detects Club's Weaknesses & Recommends Players.": "https://football-player-recommender-system.streamlit.app/",
    "🏆 IPL Dream Team Predictor - Generates Player Ranks based on Cricketing Factors.": "https://github.com/amoghrane56/ipl-dream11-predictor",
    "🏆 Movie Recommendation System - A Content based Movie Recommendation System.": "https://github.com/amoghrane56/Movie-recommendation-system",
    "🏆 Diabetes Prediction System - Implemented SVM Classifier to detect Diabetes.": "https://github.com/amoghrane56/Diabetes_prediction_system",
    "🏆 Housing Price Predcition - Used Linear Regression (L1 & L2 Regularisation).": "https://github.com/amoghrane56/House_Price_Prediction_Model",
    "🏆 Super Sales Dashboard - Utilized PowerBI to visulaize key Sales Insights.": "https://github.com/amoghrane56/Power_Bi_SuperStoreSales_Dashboard",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=250)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('#')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- About me ---
st.subheader("About Myself")
st.write("---")
st.write(
    """
    - ✔️ Solid foundation in Mathematics, Statistics and Python.
    \n
    - ✔️ Passionate about Machine Learning and unlocking data's potential to drive meaningful insights and data-driven decisions.
    \n
    - ✔️ Quick learner with good teamwork, time management, logical reasoning and data interpretability skills.
    \n
    - ✔️ Always curious and adaptable in this ever-evolving world.
    \n
    - ✔️ Committed to continuous self-learning and rapid improvement in life.
    \n 
    """
)

st.write('\n')


# --- EXPERIENCE & QUALIFICATIONS ---
st.subheader("Education & Qualifications")
st.write("---")
st.write(
    """
    - 🎓 **Bachelor of Engineering (BE), Mechanical Engineering**
      St. Francis Institute Of Technology, Mumbai |
      Timeline: 2019 - 2023 |
      CGPA: 8.45/10
      
    \n
    - 🏫 **Senior Secondary (XII), Science**
      D.G. Ruparel College |
      Year of completion: 2019 |
      Percentage: 72.6%
      
    \n
    - 📖 **Secondary (X)**
      Thakur Vidya Mandir High School |
      Year of completion: 2017 |
      Percentage: 94.2%
      
    """
)

st.write('\n')

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
# st.write('\n')
st.write(
    """
    - 👩‍💻 **Programming:** Python, SQL, HTML & CSS (Basics).
    - 📊 **Data Visualization:** Power BI, Plotly, Matplotlib, Seaborn,
    - 📚 **Machine Learning:** Supervised and Unsupervised Learning Algorithms, Model Training, Model Evaluation, Hyperparameter Tuning, etc,
    - 🗄️ **Databases:** MySQL.
    - 🛠️ **Tools:** Jupyter Notebook, Anaconda, Git, VS Code.
    - 📈 **Data Skills:** Data Cleaning, Data Wrangling, Statistical Analysis, etc.
    - 💼 **Microsoft Office:** Excel, Word, PowerPoint.
    """
)

st.write("\n")

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work Experience")
st.write("---")

# --- JOB 1
st.write("🚧", "**Quant Programmer | PL Capital**")
st.write("01/2024 - Present")
st.write(
    """
- ► Quantitative Analysis and Financial Modeling - *Proficiently developed and implemented models including
Sharpe/Sortino Ratios, and regression models like RSI and Beta. Conducted factor-based investing focusing on
Alpha Momentum, Growth, Quality, Low Volatility, and Value factors. Utilized quantitative analysis to construct
and manage smart equity portfolios and mutual fund analysis based on fund type.*
- ► Portfolio Backtesting and Optimization - *Back-tested various combinations of different indicators used to
construct asset allocation portfolios to optimize returns and mitigate risks across diverse market conditions.*
- ► Statistical Modeling and Machine Learning - *Applied Unsupervised Learning techniques such as Gaussian
Mixture Models (GMM) for market regime clustering and pattern recognition.*
- ► Data Automation and Web Development - *Developed automated tools for web scraping and news aggregation,
enhancing data-driven decision-making processes. Automated operational tasks and reporting for Portfolio
Management Services (PMS) through web-based dashboards. Created web-based quantitative indicators for
real-time analysis of market momentum, technical, macro and risk indicators.*

"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Intern | PL Capital**")
st.write("08/2023 - 31/2023")
st.write(
    """
- ► Risk Management and Quant Reporting - *Populated quant-based risk heatmaps to visualize and assess portfolio
risk exposure across different asset classes. Utilized Power BI for dynamic business mapping and interactive data
visualizations to interpret market trends and investor sentiment.*
- ► Market Insights and Visualization - *Conducted research on market trends, industry sectors, and macroeconomic
factors influencing equity markets to provide actionable recommendations. Leveraged tools like Power BI to create
interactive dashboards and visualize complex market data, facilitating informed decision-making and significant
insights. Analyzed and presented key indicators to provide insights into global bond market trends and their
impact on investments.*
- ► Data Wrangling - *Did necessary pre-processing tasks like Web Scrapping, Fetching Data via APIs, Data Cleaning, Data Quality Check,
 Outlier Detection, Handling poorly formatted & missing data, etc.* 
"""
)

st.write("\n")

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
