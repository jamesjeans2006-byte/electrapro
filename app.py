import streamlit as st
from content.curriculum import SUBJECTS, LESSONS, QUIZ_BANK

st.set_page_config(
    page_title="ElectraPro | Electrical Engineering Academy",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
:root { --ink:#14213d; --blue:#145da0; --cyan:#38bdf8; --paper:#f5f8fc; }
.block-container { padding-top: 1.6rem; padding-bottom: 3rem; max-width: 1250px; }
.hero { padding: 2.1rem 2.2rem; border-radius: 20px; color: white;
        background: linear-gradient(120deg,#102a43 0%,#145da0 58%,#168aad 100%); }
.hero h1 { color:white; font-size:2.55rem; margin-bottom:.5rem; }
.hero p { color:#e6f4ff; font-size:1.08rem; max-width:850px; }
.kpi { background:#f2f7fc; border:1px solid #dce8f3; padding:1rem 1.1rem;
       border-radius:14px; min-height:100px; }
.kpi strong { display:block; color:#145da0; font-size:1.65rem; }
.kpi span { color:#43566b; font-size:.9rem; }
.section-label { color:#145da0; text-transform:uppercase; letter-spacing:.11em;
                 font-weight:700; font-size:.78rem; }
.lesson-box { padding:1rem 1.2rem; border:1px solid #dce8f3; border-radius:12px; }
.small-note { color:#536579; font-size:.9rem; }
div[data-testid="stSidebar"] { background:#f6f9fc; }
</style>
""", unsafe_allow_html=True)

def find_subject(name):
    return SUBJECTS.get(name, {})

with st.sidebar:
    st.markdown("## ⚡ ElectraPro")
    st.caption("Electrical Engineering & Technology")
    page = st.radio(
        "MAIN MENU",
        ["Home", "Learning Library", "Engineering Calculators", "Practice & Assessment", "Career Roadmaps", "Glossary", "References"],
        label_visibility="collapsed",
    )
    st.divider()
    st.caption("Structured learning • Basic to Advanced")
    st.caption("Safety-first engineering education")

if page == "Home":
    st.markdown("""
    <div class="hero">
      <div class="section-label" style="color:#bdeaff">ELECTRICAL ENGINEERING ACADEMY</div>
      <h1>Understand the principles.<br>Build engineering confidence.</h1>
      <p>A structured learning platform for electrical fundamentals, power systems, machines,
      automation, electronics, instrumentation, renewable energy and marine electrical technology.
      Learn from first principles through practical engineering applications.</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    c1,c2,c3,c4 = st.columns(4)
    with c1: st.markdown('<div class="kpi"><strong>12</strong><span>Core subject areas</span></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="kpi"><strong>3 levels</strong><span>Basic • Intermediate • Advanced</span></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="kpi"><strong>Practice</strong><span>Questions and knowledge checks</span></div>', unsafe_allow_html=True)
    with c4: st.markdown('<div class="kpi"><strong>Safety</strong><span>Engineering-safe learning approach</span></div>', unsafe_allow_html=True)
    st.write("")
    st.markdown("### Explore the learning library")
    st.write("Choose a subject to open its learning path. Lessons are organized from core concepts to applied engineering.")
    cols = st.columns(3)
    for i, (name, info) in enumerate(SUBJECTS.items()):
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"#### {info['icon']} {name}")
                st.write(info["description"])
                st.caption(f"{info.get('level', 'Basic')} pathway")
                if st.button("Explore subject", key=f"home_{name}", use_container_width=True):
                    st.session_state["selected_subject"] = name
                    st.session_state["requested_page"] = "Learning Library"
                    st.rerun()
    st.divider()
    st.markdown("### Recommended learning order")
    st.markdown("**Electrical Fundamentals → Measurements → Machines → Power Systems → Protection & Safety → Installation → Automation → Design → Renewable Energy → Marine Electrical & ETO**")
    st.info("Engineering note: This platform is an educational resource. Real installations, testing and repairs must follow applicable codes, risk assessments and qualified supervision.")

elif page == "Learning Library":
    st.markdown("# Learning Library")
    st.write("Select a subject and lesson. Start with prerequisites and progress toward applied and advanced topics.")
    subject_names = list(SUBJECTS.keys())
    default_subject = st.session_state.pop("selected_subject", subject_names[0])
    idx = subject_names.index(default_subject) if default_subject in subject_names else 0
    selected_subject = st.selectbox("Subject", subject_names, index=idx)
    info = SUBJECTS[selected_subject]
    st.markdown(f"### {info['icon']} {selected_subject}")
    st.write(info["description"])
    lessons = [x for x in LESSONS if x["subject"] == selected_subject]
    if not lessons:
        st.warning("This subject's detailed lesson sequence is planned in the curriculum. The topic map below shows the recommended study path.")
        for topic in info["topics"]:
            st.markdown(f"- {topic}")
    else:
        lesson_titles = [f"{x['level']} · {x['title']}" for x in lessons]
        chosen_title = st.selectbox("Lesson", lesson_titles)
        lesson = lessons[lesson_titles.index(chosen_title)]
        st.caption(f"Level: {lesson['level']}  •  Estimated study time: {lesson.get('duration','20–30 minutes')}")
        st.markdown("---")
        st.markdown(lesson["intro"])
        for section in lesson["sections"]:
            st.markdown(f"### {section['heading']}")
            st.markdown(section["body"])
            if section.get("example"):
                with st.container(border=True):
                    st.markdown("**Worked example**")
                    st.markdown(section["example"])
        if lesson.get("key_points"):
            st.markdown("### Key points")
            for point in lesson["key_points"]:
                st.markdown(f"- {point}")
        if lesson.get("references"):
            st.markdown("### Further reading")
            for ref in lesson["references"]:
                st.markdown(f"- {ref}")
        if lesson.get("safety"):
            st.warning(lesson["safety"])
        st.divider()
        st.markdown("### Check your understanding")
        st.write(lesson.get("question", "Explain the main engineering principle covered in this lesson."))
        with st.expander("Show suggested answer"):
            st.write(lesson.get("answer", "Use the lesson sections to form a clear answer, including the relevant principle and units."))

elif page == "Engineering Calculators":
    st.markdown("# Engineering Calculators")
    st.write("Educational calculators for common electrical quantities. Verify results against the actual circuit and applicable standards.")
    mode = st.selectbox("Calculator", ["Ohm's Law", "Electrical Power (DC)", "Three-phase apparent power"])
    if mode == "Ohm's Law":
        c1,c2 = st.columns(2)
        with c1: v = st.number_input("Voltage (V)", min_value=0.0, value=24.0, step=1.0)
        with c2: r = st.number_input("Resistance (Ω)", min_value=0.001, value=12.0, step=1.0)
        st.metric("Current", f"{v/r:.4g} A")
        st.metric("Power", f"{v*v/r:.4g} W")
        st.latex(r"I=\\frac{V}{R},\\qquad P=VI=\\frac{V^2}{R}")
    elif mode == "Electrical Power (DC)":
        c1,c2 = st.columns(2)
        with c1: v = st.number_input("Voltage (V)", min_value=0.0, value=24.0, step=1.0)
        with c2: i = st.number_input("Current (A)", min_value=0.0, value=2.0, step=0.5)
        st.metric("Power", f"{v*i:.4g} W")
        st.latex(r"P=VI")
    else:
        c1,c2,c3 = st.columns(3)
        with c1: vl = st.number_input("Line voltage (V)", min_value=0.0, value=400.0, step=10.0)
        with c2: il = st.number_input("Line current (A)", min_value=0.0, value=10.0, step=1.0)
        with c3: pf = st.number_input("Power factor", min_value=0.0, max_value=1.0, value=0.85, step=0.05)
        kva = (3**0.5)*vl*il/1000
        st.metric("Apparent power", f"{kva:.3f} kVA")
        st.metric("Approx. active power", f"{kva*pf:.3f} kW")
        st.latex(r"S=\\sqrt{3}V_L I_L,\\qquad P=S\\,PF")
        st.caption("Assumes a balanced three-phase system and line-to-line voltage.")

elif page == "Practice & Assessment":
    st.markdown("# Practice & Assessment")
    st.write("Use these questions to check understanding. Try answering before revealing the explanation.")
    topic = st.selectbox("Question set", list(QUIZ_BANK.keys()))
    for i, q in enumerate(QUIZ_BANK[topic], 1):
        with st.container(border=True):
            st.markdown(f"**{i}. {q['question']}**")
            if "options" in q:
                choice = st.radio("Choose one answer", q["options"], key=f"quiz_{topic}_{i}", index=None)
                if st.button("Check answer", key=f"check_{topic}_{i}"):
                    if choice == q["answer"]:
                        st.success("Correct.")
                    else:
                        st.error(f"Not quite. Correct answer: {q['answer']}")
                    st.caption(q["explanation"])
            else:
                st.write("Write your answer in your notebook, then open the suggested answer.")
                with st.expander("Suggested answer"):
                    st.write(q["answer"])
                    st.caption(q["explanation"])

elif page == "Career Roadmaps":
    st.markdown("# Career Roadmaps")
    st.write("Career paths are guidance, not guarantees. Requirements vary by country, employer and regulator.")
    pathways = {
        "Electrical Technician": ["Electrical fundamentals and safe work practices", "Read wiring diagrams and electrical drawings", "Learn testing instruments and fault-finding", "Build supervised installation and maintenance experience", "Study local licensing and workplace requirements"],
        "Industrial Automation Technician": ["Understand sensors, relays and motor control", "Learn PLC logic and I/O concepts", "Study HMI, SCADA and industrial networks", "Practice simulation and safe commissioning procedures", "Build a documented project portfolio"],
        "Power Systems Engineer": ["Master circuit theory and three-phase systems", "Study transformers, machines and power flow", "Learn protection, fault analysis and grounding", "Practice calculations with engineering software", "Check degree, registration and local code requirements"],
        "Marine Electrical / ETO pathway": ["Strengthen electrical machines, distribution and control systems", "Research approved maritime training routes and STCW requirements", "Confirm medical, sea-service and certification requirements with the relevant authority", "Seek legitimate cadetship or employer sponsorship opportunities", "Verify every training provider and employment offer before paying fees"],
    }
    chosen = st.selectbox("Choose a pathway", list(pathways.keys()))
    for i, step in enumerate(pathways[chosen], 1):
        st.markdown(f"**Step {i}.** {step}")
    st.warning("For maritime careers, requirements depend on the flag state and competent maritime authority. Confirm current requirements directly with official authorities and approved training providers.")

elif page == "Glossary":
    st.markdown("# Electrical Glossary")
    glossary = {
        "AC — Alternating Current": "Current that changes magnitude and periodically reverses direction.",
        "DC — Direct Current": "Current that flows in one direction; its magnitude may be constant or varying.",
        "Voltage": "Electric potential difference between two points, measured in volts (V).",
        "Current": "Rate of flow of electric charge, measured in amperes (A).",
        "Resistance": "Opposition to current flow, measured in ohms (Ω).",
        "Power": "Rate of energy transfer, measured in watts (W).",
        "Power factor": "Ratio of real power to apparent power in an AC system.",
        "PLC": "Programmable Logic Controller; an industrial controller used to automate machines and processes.",
        "SCADA": "Supervisory Control and Data Acquisition; a system for monitoring and supervisory control.",
        "VFD": "Variable Frequency Drive; controls AC motor speed by varying supply frequency and voltage as appropriate.",
        "RCD": "Residual Current Device; detects residual current and disconnects a circuit under specified conditions.",
        "ETO": "Electro-Technical Officer; a qualified shipboard electro-technical role subject to applicable maritime requirements.",
        "Insulation resistance": "Resistance of insulation measured using an appropriate test method and instrument.",
    }
    search = st.text_input("Search a term")
    for term, definition in glossary.items():
        if not search or search.lower() in (term + " " + definition).lower():
            with st.expander(term):
                st.write(definition)

elif page == "References":
    st.markdown("# References & Technical Reading")
    st.write("Use these sources to deepen understanding and confirm engineering practice. Edition and applicable requirements should be checked before use.")
    refs = [
        ("Electrical Engineering: Principles and Applications", "Allan R. Hambley", "Foundational circuit theory, devices and systems."),
        ("Electric Machinery Fundamentals", "Stephen J. Chapman", "Transformers, motors and generators."),
        ("Power System Analysis and Design", "J. Duncan Glover, Thomas Overbye and Mulukutla S. Sarma", "Power system modelling and analysis."),
        ("Programmable Logic Controllers", "Frank D. Petruzella", "PLC concepts, programming and industrial control."),
        ("Electrical Wiring: Residential", "Ray C. Mullin and Phil Simmons", "Wiring principles; always apply local regulations and current code."),
        ("IEC standards", "International Electrotechnical Commission", "International electrotechnical standards; use the current relevant standard."),
        ("IEEE standards and learning resources", "Institute of Electrical and Electronics Engineers", "Power, electrical, control and instrumentation engineering resources."),
        ("Manufacturer technical documentation", "Official manufacturer websites", "Datasheets, installation manuals, protection settings and equipment-specific requirements."),
    ]
    for title, author, note in refs:
        with st.container(border=True):
            st.markdown(f"**{title}**")
            st.caption(author)
            st.write(note)
    st.info("This learning app uses original summaries and explanations. It does not reproduce copyrighted textbook chapters. Standards and regulations can change; always verify the current edition.")

st.sidebar.divider()
st.sidebar.caption("ElectraPro • Independent educational project")
st.sidebar.caption("Always follow applicable electrical safety rules and local codes.")
