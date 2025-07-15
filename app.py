import streamlit as st
from utils.resume_parser import parse_resume
from utils.match_engine import calculate_match
from utils.assignment_suggester import suggest_assignments

st.set_page_config(page_title="Requirement Analyser", layout="centered")
st.title("🧠 Requirement Analyser")

st.markdown("""
This tool analyzes an uploaded resume against your required tech stack and suggests skill-based assignments.
""")

# Step 1: Input requirements
st.header("🔧 Enter Required Skills / Tech Stack")
required_skills = st.text_area("Enter comma-separated skills (e.g., Python, Flask, SQL)", "Python, Machine Learning, Flask, SQL")

# Step 2: Upload resume
st.header("📄 Upload Resume File")
uploaded_file = st.file_uploader("Upload a resume (PDF format preferred)", type=["pdf", "txt"])

if uploaded_file and required_skills:
    with st.spinner("Reading and analyzing the resume..."):
        resume_text = parse_resume(uploaded_file)
        match_score, matched, missing = calculate_match(required_skills, resume_text)
        suggestions = suggest_assignments(missing)

    st.subheader("📊 Match Analysis")
    st.write(f"**Match Score:** {match_score}%")
    st.write("**Matched Skills:**", ', '.join(matched) if matched else "None")
    st.write("**Missing Skills:**", ', '.join(missing) if missing else "None")

    st.subheader("🧑‍💻 Personalized Assignment Suggestions")
    if suggestions:
        for s in suggestions:
            st.markdown(f"- {s}")
    else:
        st.markdown("✅ All required skills are matched. No assignments needed!")
