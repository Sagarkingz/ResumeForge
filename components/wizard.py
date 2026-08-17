import streamlit as st
from models.resume_model import Experience, SkillCategory
from services.ai_service import AIService

def render_wizard():
    resume = st.session_state.resume
    ai_service = AIService()

    t1, t2, t3, t4 = st.tabs(["1. Personal Info", "2. Summary (AI Engine)", "3. Experience", "4. Skills"])

    # 1. Personal Information
    with t1:
        st.subheader("Personal Details")
        info = resume.personal_info
        info.full_name = st.text_input("Full Name", value=info.full_name)
        info.professional_title = st.text_input("Professional / Target Job Title", value=info.professional_title, placeholder="e.g. Python Developer / Business Analyst")
        
        c1, c2 = st.columns(2)
        with c1:
            info.email = st.text_input("Email Address", value=info.email)
            info.location = st.text_input("Location (City, Country)", value=info.location)
        with c2:
            info.phone = st.text_input("Mobile Number", value=info.phone)
            info.linkedin = st.text_input("LinkedIn Profile", value=info.linkedin)

        # Qualification input for AI engine
        st.session_state["user_qualification"] = st.text_input(
            "Highest Qualification / Degree", 
            value=st.session_state.get("user_qualification", "B.Tech in Computer Science"),
            placeholder="e.g. B.Tech / MBA / B.Com / Higher Secondary"
        )

    # 2. Summary with AI Assistant Engine
    with t2:
        st.subheader("Professional Summary")
        
        # Expander for AI Summary Ideas Engine
        with st.expander("🤖 AI Summary Generator (Click to Get Summary Ideas)", expanded=True):
            st.markdown("Fill in your details below to generate tailored summary ideas:")
            
            c_type, c_qual = st.columns(2)
            with c_type:
                exp_level = st.radio("Experience Level:", ["Fresher", "Experienced Professional"], horizontal=True)
                is_fresher = (exp_level == "Fresher")
            
            with c_qual:
                target_role = st.text_input("Target Role", value=info.professional_title or "Software Engineer", key="ai_target_role")

            qual_val = st.text_input("Degree / Qualification", value=st.session_state.get("user_qualification", ""), key="ai_qual_input")
            
            # Combine skills for AI prompt
            all_skills_str = ", ".join([skill for cat in resume.skill_categories for skill in cat.skills])
            skills_val = st.text_input("Key Skills (comma-separated)", value=all_skills_str or "Python, Problem Solving, Communication", key="ai_skills_input")

            if st.button("✨ Generate Professional Summary Ideas"):
                with st.spinner("AI Engine is crafting personalized summary options..."):
                    ideas = ai_service.generate_summary_ideas(
                        full_name=info.full_name,
                        role=target_role,
                        qualification=qual_val,
                        skills=skills_val,
                        is_fresher=is_fresher
                    )
                    st.session_state["generated_summary_ideas"] = ideas

            # Display generated ideas
            if "generated_summary_ideas" in st.session_state:
                st.markdown("---")
                st.markdown("##### Select a Summary Idea to Apply:")
                for idx, idea in enumerate(st.session_state["generated_summary_ideas"]):
                    st.info(f"**Option {idx+1}:** {idea}")
                    if st.button(f"Use Option {idx+1}", key=f"use_idea_{idx}"):
                        resume.summary = idea
                        st.success("Summary applied to resume!")
                        st.rerun()

        st.markdown("---")
        resume.summary = st.text_area("Final Summary (Editable)", value=resume.summary, height=130)

    # 3. Work Experience
    with t3:
        st.subheader("Work Experience")
        for idx, exp in enumerate(resume.experiences):
            st.markdown(f"**Experience #{idx+1}**")
            exp.job_title = st.text_input("Job Title", value=exp.job_title, key=f"title_{idx}")
            exp.company = st.text_input("Company", value=exp.company, key=f"comp_{idx}")
            exp.description = st.text_area("Description", value=exp.description, key=f"desc_{idx}")
        if st.button("➕ Add Experience"):
            resume.experiences.append(Experience())
            st.rerun()

    # 4. Skills
    with t4:
        st.subheader("Skills & Competencies")
        for idx, cat in enumerate(resume.skill_categories):
            cat.category_name = st.text_input("Category Name", value=cat.category_name, key=f"cat_{idx}")
            raw_skills = st.text_input("Skills (comma-separated)", value=", ".join(cat.skills), key=f"sk_{idx}")
            cat.skills = [s.strip() for s in raw_skills.split(",") if s.strip()]
        if st.button("➕ Add Skill Category"):
            resume.skill_categories.append(SkillCategory())
            st.rerun()