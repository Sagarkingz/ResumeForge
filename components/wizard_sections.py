"""Step-by-step editor for all resume sections."""

import streamlit as st
from models.resume_model import Experience, Education, SkillCategory, Project, Certification, Language

def render_editor_sections():
    resume = st.session_state.resume

    tabs = st.tabs([
        "1. Personal", "2. Summary", "3. Experience", 
        "4. Education", "5. Skills", "6. Projects", "7. Certs & Languages"
    ])

    # 1. Personal Info
    with tabs[0]:
        st.subheader("Personal Information")
        info = resume.personal_info
        info.full_name = st.text_input("Full Name *", value=info.full_name)
        info.professional_title = st.text_input("Professional Title *", value=info.professional_title)
        
        c1, c2 = st.columns(2)
        with c1:
            info.email = st.text_input("Email *", value=info.email)
            info.phone = st.text_input("Phone Number *", value=info.phone)
            info.location = st.text_input("Location (City, State/Country)", value=info.location)
            info.website = st.text_input("Personal Website", value=info.website)
        with c2:
            info.linkedin = st.text_input("LinkedIn URL", value=info.linkedin)
            info.github = st.text_input("GitHub URL", value=info.github)
            info.portfolio = st.text_input("Portfolio URL", value=info.portfolio)
            info.career_level = st.selectbox("Career Level", ["Fresher", "Entry-Level", "Mid-Level", "Senior", "Executive"], index=2)

    # 2. Summary
    with tabs[1]:
        st.subheader("Professional Summary")
        resume.summary = st.text_area("Write or edit your summary:", value=resume.summary, height=140)

    # 3. Work Experience
    with tabs[2]:
        st.subheader("Work Experience")
        for idx, exp in enumerate(resume.experiences):
            with st.expander(f"Position {idx+1}: {exp.job_title or 'Untitled'} at {exp.company or 'Company'}", expanded=True):
                exp.job_title = st.text_input("Job Title", value=exp.job_title, key=f"exp_title_{idx}")
                exp.company = st.text_input("Company Name", value=exp.company, key=f"exp_comp_{idx}")
                exp.location = st.text_input("Location", value=exp.location, key=f"exp_loc_{idx}")
                
                d1, d2 = st.columns(2)
                with d1:
                    exp.start_date = st.text_input("Start Date", value=exp.start_date, key=f"exp_sd_{idx}")
                with d2:
                    exp.end_date = st.text_input("End Date", value=exp.end_date, key=f"exp_ed_{idx}")
                
                exp.is_current = st.checkbox("Currently work here", value=exp.is_current, key=f"exp_curr_{idx}")
                exp.description = st.text_area("Role Summary", value=exp.description, key=f"exp_desc_{idx}")
                
                raw_ach = st.text_area("Bullet Achievements (One per line)", value="\n".join(exp.achievements), key=f"exp_ach_{idx}")
                exp.achievements = [a.strip() for a in raw_ach.split("\n") if a.strip()]

                if st.button("🗑️ Delete Position", key=f"del_exp_{idx}"):
                    resume.experiences.pop(idx)
                    st.rerun()

        if st.button("➕ Add Work Experience"):
            resume.experiences.append(Experience())
            st.rerun()

    # 4. Education
    with tabs[3]:
        st.subheader("Education")
        for idx, edu in enumerate(resume.educations):
            with st.expander(f"Degree {idx+1}: {edu.degree or 'Degree'}", expanded=True):
                edu.degree = st.text_input("Degree / Certificate", value=edu.degree, key=f"edu_deg_{idx}")
                edu.institution = st.text_input("Institution / University", value=edu.institution, key=f"edu_inst_{idx}")
                edu.location = st.text_input("City / Location", value=edu.location, key=f"edu_loc_{idx}")
                
                d1, d2, d3 = st.columns(3)
                with d1:
                    edu.start_date = st.text_input("Start Year", value=edu.start_date, key=f"edu_sd_{idx}")
                with d2:
                    edu.end_date = st.text_input("End Year", value=edu.end_date, key=f"edu_ed_{idx}")
                with d3:
                    edu.gpa = st.text_input("GPA / Score", value=edu.gpa, key=f"edu_gpa_{idx}")

                if st.button("🗑️ Delete Education", key=f"del_edu_{idx}"):
                    resume.educations.pop(idx)
                    st.rerun()

        if st.button("➕ Add Education"):
            resume.educations.append(Education())
            st.rerun()

    # 5. Skills
    with tabs[4]:
        st.subheader("Skills & Competencies")
        for idx, cat in enumerate(resume.skill_categories):
            c1, c2 = st.columns([1, 2])
            with c1:
                cat.category_name = st.text_input("Category", value=cat.category_name, key=f"cat_name_{idx}")
            with c2:
                raw_s = st.text_input("Skills (comma-separated)", value=", ".join(cat.skills), key=f"cat_s_{idx}")
                cat.skills = [s.strip() for s in raw_s.split(",") if s.strip()]

        if st.button("➕ Add Skill Category"):
            resume.skill_categories.append(SkillCategory(category_name="Technical Skills", skills=[]))
            st.rerun()

    # 6. Projects
    with tabs[5]:
        st.subheader("Key Projects")
        for idx, proj in enumerate(resume.projects):
            with st.expander(f"Project {idx+1}: {proj.name or 'New Project'}", expanded=True):
                proj.name = st.text_input("Project Name", value=proj.name, key=f"proj_name_{idx}")
                proj.description = st.text_area("Description", value=proj.description, key=f"proj_desc_{idx}")
                raw_tech = st.text_input("Technologies (comma-separated)", value=", ".join(proj.technologies), key=f"proj_tech_{idx}")
                proj.technologies = [t.strip() for t in raw_tech.split(",") if t.strip()]
                proj.github_url = st.text_input("GitHub Repo URL", value=proj.github_url, key=f"proj_gh_{idx}")

        if st.button("➕ Add Project"):
            resume.projects.append(Project())
            st.rerun()

    # 7. Certifications & Languages
    with tabs[6]:
        st.subheader("Certifications")
        for idx, cert in enumerate(resume.certifications):
            c1, c2 = st.columns(2)
            with c1:
                cert.name = st.text_input("Certification Name", value=cert.name, key=f"cert_n_{idx}")
            with c2:
                cert.issuing_organization = st.text_input("Issuer", value=cert.issuing_organization, key=f"cert_o_{idx}")

        if st.button("➕ Add Certification"):
            resume.certifications.append(Certification())
            st.rerun()

        st.divider()
        st.subheader("Languages")
        for idx, lang in enumerate(resume.languages):
            c1, c2 = st.columns(2)
            with c1:
                lang.language = st.text_input("Language", value=lang.language, key=f"lang_n_{idx}")
            with c2:
                lang.proficiency = st.selectbox("Proficiency", ["Native", "Professional", "Intermediate", "Basic"], key=f"lang_p_{idx}")

        if st.button("➕ Add Language"):
            resume.languages.append(Language())
            st.rerun()