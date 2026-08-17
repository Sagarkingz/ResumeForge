"""Visual Template Gallery component."""

import streamlit as st
from config.settings import TEMPLATE_METADATA, COLOR_PALETTES

def render_template_gallery():
    st.subheader("🎨 Resume Template Gallery")
    st.write("Select a professionally crafted template tailored for your industry and experience level.")

    categories = ["All", "Modern", "Corporate", "Creative", "Fresher", "ATS"]
    selected_cat = st.radio("Filter by Category:", categories, horizontal=True)

    st.write("")

    filtered_templates = {
        tid: meta for tid, meta in TEMPLATE_METADATA.items()
        if selected_cat == "All" or meta["category"] == selected_cat
    }

    cols = st.columns(3)
    for idx, (tid, meta) in enumerate(filtered_templates.items()):
        col = cols[idx % 3]
        with col:
            with st.container(border=True):
                st.markdown(f"#### {meta['name']}")
                st.caption(f"Category: **{meta['category']}**")
                st.write(meta["description"])
                
                is_current = (st.session_state.resume.style.template_id == tid)
                if is_current:
                    st.success("✓ Currently Active")
                else:
                    if st.button(f"Use {meta['name']}", key=f"tpl_select_{tid}"):
                        st.session_state.resume.style.template_id = tid
                        st.success(f"Selected {meta['name']}!")
                        st.rerun()

    st.divider()
    st.subheader("🎨 Customization Settings")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        palette_choice = st.selectbox("Color Palette", list(COLOR_PALETTES.keys()))
        st.session_state.resume.style.primary_color = COLOR_PALETTES[palette_choice]["primary"]
    
    with c2:
        st.session_state.resume.style.font_family = st.selectbox("Font Family", ["Helvetica", "Times-Roman", "Courier"])
    
    with c3:
        st.session_state.resume.style.length_option = st.selectbox("Resume Page Budget", ["1 Page", "2 Pages", "Auto"])