import streamlit as st
from resume_parser import extract_text_from_resume
from gemini_helper import configure_gemini, generate_cover_letter
from profile_helper import load_user_profile, save_user_profile

st.set_page_config(page_title="Cover-Craft | Cover Letter Generator", layout="centered")
st.title("📄 Cover-Craft AI-Powered Cover Letter Generator")

model = configure_gemini()

# -----------------------
# 👤 LOAD SAVED PROFILE
# -----------------------
if "user_profile" not in st.session_state:
    st.session_state.user_profile = load_user_profile()

# -----------------------
# 👤 USER PROFILE FORM
# -----------------------
with st.form("user_profile_form"):
    st.subheader("👤 Your Info (Saved Automatically)")

    full_name = st.text_input("Full Name", value=st.session_state.user_profile.get("full_name", ""))
    email = st.text_input("Email", value=st.session_state.user_profile.get("email", ""))
    role = st.text_input("Role You're Applying For", value=st.session_state.user_profile.get("role", ""))
    company = st.text_input("Company Name", value=st.session_state.user_profile.get("company", ""))

    submitted = st.form_submit_button("Save Info")

if submitted:
    profile_data = {
        "full_name": full_name,
        "email": email,
        "role": role,
        "company": company
    }
    st.session_state.user_profile = profile_data
    save_user_profile(profile_data)
    st.success("✅ Profile saved!")

# -----------------------
# 📄 Resume + Job Desc
# -----------------------
st.subheader("1. Upload Your Resume")
resume_file = st.file_uploader("Upload PDF", type="pdf")

st.subheader("2. Paste Job Description")
job_desc = st.text_area("Paste the job description here...")

# -----------------------
# 🚀 Generate Cover Letter
# -----------------------
if resume_file and job_desc:
    if st.button("✨ Generate Cover Letter"):
        resume_text = extract_text_from_resume(resume_file)

        # Use saved user profile
        profile = st.session_state.user_profile
        user_intro = f"""
Personal Info:
- Name: {profile['full_name']}
- Email: {profile['email']}
- Role: {profile['role']}
- Company: {profile['company']}
"""

        with st.spinner("Generating..."):
            full_prompt = user_intro + "\n" + job_desc
            letter = generate_cover_letter(model, resume_text, full_prompt)

        st.success("✅ Cover Letter Generated!")
        st.text_area("📄 Your Cover Letter", letter, height=300)
        st.download_button("📥 Download as .txt", letter, file_name="cover_letter.txt")
