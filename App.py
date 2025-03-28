import streamlit as st

# Page Configuration
st.set_page_config(page_title="Lawgarithm - Indian Legal Chatbot", layout="wide")

# Custom CSS for Dark Theme
st.markdown("""
    <style>
        /* Global Styles */
        body { background-color: #21212; color: #E0E0E0; }

        /* Title */
        .big-font { font-size: 36px !important; font-weight: bold; color: #FFFFFF; }

        /* Subtitle */
        .subtext { font-size: 18px; color: #A1A1A1; }

        /* Feature Boxes */
        .highlight-box { 
            background-color: #1E1E1E; 
            padding: 15px; 
            border-radius: 10px; 
            border: 1px solid #333;
            box-shadow: 2px 2px 10px rgba(255, 255, 255, 0.1);
        }
            
        .header {
            background-color: #2C2C2C;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 2px 2px 15px rgba(255, 255, 255, 0.1);
        }

        /* About Us Image Styling */
        .team-image { 
            width: 150px; height: 150px; 
            border-radius: 50%; object-fit: cover; 
            border: 2px solid #BB86FC; 
        }

        /* Footer */
        .footer { text-align: center; font-size: 14px; color: #888; margin-top: 30px; }
    </style>
""", unsafe_allow_html=True)

# ---- Header ----
st.markdown('<div class="header"><p class="big-font">⚖️ Welcome to Lawgarithm - Your Indian Legal Assistant</p></div>', unsafe_allow_html=True)
st.write("🚀 **Lawgarithm is your AI-powered legal assistant designed for the **Indian legal system**. Whether you need **instant legal insights, rental agreements, contract generation**, or **Hindi document translations**, we make complex legal processes simple & accessible.**")

# ---- Features Section ----
st.subheader("🌟 What Can Lawgarithm Do?")
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="highlight-box">🤖 <b style="color:#FFFFFF;">Legal Chatbot</b> <br> Get AI-powered answers to your legal questions.</div>', unsafe_allow_html=True)
    st.markdown('<div class="highlight-box">📄 <b style="color:#FFFFFF;">Legal Document Summarization</b> <br> Upload PDFs and get key takeaways instantly.</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="highlight-box">🏠 <b style="color:#FFFFFF;">Rental Agreement Generator</b> <br> Generate legally valid rental agreements in minutes.</div>', unsafe_allow_html=True)
    st.markdown('<div class="highlight-box">🌐 <b style="color:#FFFFFF;">Hindi Legal Document Translation</b> <br> Upload Hindi legal documents and get accurate English translations.</div>', unsafe_allow_html=True)

# ---- About Us ----
st.subheader("👨‍💻 About Us")
st.write("Meet the brilliant minds behind **Lawgarithm**.")

team_col1, team_col2, team_col3 = st.columns(3)

with team_col1:
    st.image("Images\Karunya.png", caption="L Karunya Ronith", use_container_width=True, output_format="PNG", clamp=True)

with team_col2:
    st.image("Images/Manav.png", caption="Manav M Bajaj", use_container_width=True, output_format="PNG", clamp=True)

with team_col3:
    st.image("Images\Abhijith.png", caption="Abhijeet Srivathsan", use_container_width=True, output_format="PNG", clamp=True)



