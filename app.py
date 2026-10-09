import streamlit as st
from content.curriculum import SUBJECTS, LESSONS, QUIZ_BANK, GLOSSARY, REFERENCES

st.set_page_config(
    page_title="ElectraPro | Electrical Engineering Academy",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
.block-container{max-width:1250px;padding-top:1.5rem;padding-bottom:3rem}
.hero{padding:2.2rem;border-radius:18px;color:white;background:linear-gradient(120deg,#102a43,#145da0 60%,#168aad)}
.hero h1{color:white;font-size:2.55rem;line-height:1.12;margin:.3rem 0 .7rem}
.hero p{color:#e8f5ff;font-size:1.06rem;max-width:900px}
.eyebrow{font-size:.76rem;letter-spacing:.13em;text-transform:uppercase;font-weight:700;color:#bdeaff}
.metric{border:1px solid #d9e5f0;border-radius:13px;padding:1rem;background:#f5f9fd;min-height:95px}
.metric b{display:block;color:#145da0;font-size:1.5rem}
.metric span{font-size:.88rem;color:#4b6074}
div[data-testid="stSidebar"]{background:#f5f8fc}
.lesson-intro{font-size:1.04rem}
</style>
""", unsafe_allow_html=True)

MENU = ["Home", "Learning Library", "Engineering Calculators", "Practice & Assessment", "Career Roadmaps", "Glossary", "References"]

with st.sidebar:
    st.markdown("## ⚡ ElectraPro")
    st.caption("Electrical Engineering & Technology")
    page = st.radio("MAIN MENU", MENU, label_visibility="collapsed")
    st.divider()
    st.caption("Learn from first principles to applied engineering.")
    st.caption("Safety-first • Subject-based • Practical")

def show_lesson(lesson):
    st.caption(f"{lesson['level']}  ·  {lesson.get('duration','30–45 minutes')}  ·  {lesson['subject']}")
    st.markdown(f"<div class='lesson-intro'>{lesson['intro']}</div>", unsafe_allow_html=True)
    st.divider()
    for section in lesson["sections"]:
        st.markdown(f"### {section['heading']}")
        st.markdown(section["body"])
        if section.get("equation"):
            st.latex(section["equation"])
        if section.get("example"):
            with st.container(border=True):
                st.markdown("**Worked example / engineering application**")
                st.markdown(section["example"])
    if lesson.get("key_points"):
        st.markdown("### Key points")
        for item in lesson["key_points"]:
            st.markdown(f"- {item}")
    if lesson.get("practice"):
        st.markdown("### Practice task")
        st.write(lesson["practice"])
    if lesson.get("safety"):
        st.warning(lesson["safety"])
    if lesson.get("references"):
        st.markdown("### Further reading")
        for ref in lesson["references"]:
            st.markdown(f"- {ref}")
    st.divider()
    st.markdown("### Check your understanding")
    st.write(lesson.get("question", "Summarize the principle and explain where it is used."))
    with st.expander("Show suggested answer"):
        st.write(lesson.get("answer", "Explain the governing principle, assumptions, units and practical limitations."))

if page == "Home":
    st.markdown("""
    <div class="hero">
      <div class="eyebrow">ELECTRICAL ENGINEERING & TECHNOLOGY</div>
      <h1>ElectraPro Learning Academy</h1>
      <p>A structured learning library covering electrical fundamentals, power systems, machines,
      automation, electronics, instrumentation, renewable energy, design, safety and marine electrical technology.</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    a,b,c,d = st.columns(4)
    for col, big, small in [
        (a, str(len(SUBJECTS)), "Core subject areas"),
        (b, str(len(LESSONS)), "Structured lessons"),
        (c, "Basic → Advanced", "Learning progression"),
        (d, "Practice", "Worked examples and checks"),
    ]:
        with col:
            st.markdown(f"<div class='metric'><b>{big}</b><span>{small}</span></div>", unsafe_allow_html=True)
    st.write("")
    st.markdown("### Explore subjects")
    st.write("Choose a subject to open its lessons, study sequence, worked examples, practice prompts and references.")
    cols = st.columns(3)
    for i, (name, info) in enumerate(SUBJECTS.items()):
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"#### {info['icon']} {name}")
                st.write(info["description"])
                st.caption(f"{len([l for l in LESSONS if l['subject']==name])} lessons included")
                if st.button("Open subject", key=f"home_{i}", use_container_width=True):
                    st.session_state["subject_pick"] = name
                    st.session_state["page_pick"] = "Learning Library"
                    st.rerun()
    st.markdown("### Suggested study sequence")
    st.markdown("**Fundamentals → Measurements → Machines → Power Systems → Installation & Safety → Automation → Design & Drives → Renewable Energy → Marine Electrical & ETO**")
    st.info("Educational content only. Real electrical work requires applicable regulations, safe-work procedures, suitable instruments and qualified authorization.")

elif page == "Learning Library":
    st.markdown("# Learning Library")
    st.write("Select a subject and lesson. Each lesson includes theory, assumptions, worked examples or applications, key points, a knowledge check and references.")
    names = list(SUBJECTS.keys())
    default = st.session_state.pop("subject_pick", names[0])
    idx = names.index(default) if default in names else 0
    subject = st.selectbox("Subject", names, index=idx)
    st.markdown(f"## {SUBJECTS[subject]['icon']} {subject}")
    st.write(SUBJECTS[subject]["description"])
    st.markdown("**Recommended topic map**")
    st.markdown("  \n".join([f"- {topic}" for topic in SUBJECTS[subject]["topics"]]))
    lessons = [l for l in LESSONS if l["subject"] == subject]
    if lessons:
        titles = [f"{l['level']} · {l['title']}" for l in lessons]
        title = st.selectbox("Open lesson", titles)
        show_lesson(lessons[titles.index(title)])
    else:
        st.warning("This subject has a topic map but its full lesson set is not yet included in this release.")
    st.caption("Content is original educational writing; use the cited textbooks, current standards and equipment manuals for deeper study and verification.")

elif page == "Engineering Calculators":
    st.markdown("# Engineering Calculators")
    st.write("Simple educational calculations. Results depend on the assumptions shown; they are not a substitute for a complete design calculation.")
    mode = st.selectbox("Calculator", ["Ohm's Law and DC power", "Series / parallel resistance", "Single-phase AC power", "Balanced three-phase power", "Voltage drop (simple DC estimate)", "Transformer ideal ratio"])
    if mode == "Ohm's Law and DC power":
        v = st.number_input("Voltage (V)", min_value=0.0, value=24.0, step=1.0)
        r = st.number_input("Resistance (Ω)", min_value=0.001, value=12.0, step=1.0)
        i = v/r
        st.metric("Current", f"{i:.4g} A")
        st.metric("Power", f"{v*i:.4g} W")
        st.latex(r"I=\\frac{V}{R},\\quad P=VI=I^2R=\\frac{V^2}{R}")
    elif mode == "Series / parallel resistance":
        r1 = st.number_input("R1 (Ω)", min_value=0.001, value=6.0, step=1.0)
        r2 = st.number_input("R2 (Ω)", min_value=0.001, value=3.0, step=1.0)
        st.metric("Series equivalent", f"{r1+r2:.4g} Ω")
        st.metric("Parallel equivalent", f"{r1*r2/(r1+r2):.4g} Ω")
        st.latex(r"R_s=R_1+R_2,\\quad R_p=\\frac{R_1R_2}{R_1+R_2}")
    elif mode == "Single-phase AC power":
        v = st.number_input("Voltage RMS (V)", min_value=0.0, value=230.0, step=5.0)
        i = st.number_input("Current RMS (A)", min_value=0.0, value=5.0, step=0.5)
        pf = st.number_input("Power factor", min_value=0.0, max_value=1.0, value=0.8, step=0.05)
        st.metric("Apparent power", f"{v*i:.3f} VA")
        st.metric("Real power", f"{v*i*pf:.3f} W")
        st.latex(r"S=VI,\\quad P=VI\\,PF")
    elif mode == "Balanced three-phase power":
        v = st.number_input("Line-to-line voltage (V)", min_value=0.0, value=400.0, step=10.0)
        i = st.number_input("Line current (A)", min_value=0.0, value=10.0, step=1.0)
        pf = st.number_input("Power factor", min_value=0.0, max_value=1.0, value=0.85, step=0.05)
        s = 3**0.5*v*i
        st.metric("Apparent power", f"{s/1000:.3f} kVA")
        st.metric("Real power", f"{s*pf/1000:.3f} kW")
        st.latex(r"S=\\sqrt{3}V_LI_L,\\quad P=\\sqrt{3}V_LI_LPF")
        st.caption("Assumes balanced three-phase operation and line-to-line RMS voltage.")
    elif mode == "Voltage drop (simple DC estimate)":
        current = st.number_input("Current (A)", min_value=0.0, value=10.0, step=1.0)
        length = st.number_input("One-way cable length (m)", min_value=0.0, value=20.0, step=1.0)
        rho = st.number_input("Conductor resistivity (Ω·mm²/m)", min_value=0.0001, value=0.0175, format="%.5f")
        area = st.number_input("Conductor cross-section (mm²)", min_value=0.1, value=2.5, step=0.5)
        rloop = rho*(2*length)/area
        vd = current*rloop
        st.metric("Estimated loop resistance", f"{rloop:.4f} Ω")
        st.metric("Estimated voltage drop", f"{vd:.3f} V")
        st.caption("Simplified copper-like DC estimate: ignores temperature, AC reactance, installation method, grouping, protection, and local code requirements. Verify design professionally.")
    else:
        vp = st.number_input("Primary voltage (V)", min_value=0.0, value=230.0, step=5.0)
        np = st.number_input("Primary turns", min_value=1, value=1000, step=10)
        ns = st.number_input("Secondary turns", min_value=1, value=100, step=10)
        st.metric("Ideal secondary voltage", f"{vp*ns/np:.3f} V")
        st.latex(r"\\frac{V_p}{V_s}=\\frac{N_p}{N_s}")
        st.caption("Ideal transformer estimate; real regulation and losses are not included.")

elif page == "Practice & Assessment":
    st.markdown("# Practice & Assessment")
    st.write("Attempt the question first, then check the answer and explanation.")
    sets = list(QUIZ_BANK.keys())
    topic = st.selectbox("Question set", sets)
    qs = QUIZ_BANK[topic]
    for i, q in enumerate(qs, 1):
        with st.container(border=True):
            st.markdown(f"**{i}. {q['question']}**")
            if q.get("options"):
                choice = st.radio("Select an answer", q["options"], key=f"choice_{topic}_{i}", index=None)
                if st.button("Check answer", key=f"check_{topic}_{i}"):
                    if choice == q["answer"]:
                        st.success("Correct.")
                    else:
                        st.error(f"Correct answer: {q['answer']}")
                    st.caption(q["explanation"])
            else:
                with st.expander("Suggested answer"):
                    st.write(q["answer"])
                    st.caption(q["explanation"])

elif page == "Career Roadmaps":
    st.markdown("# Career Roadmaps")
    st.write("Roadmaps are general guidance. Hiring, licensing, visa and certification requirements vary by country, employer and regulator.")
    paths = {
        "Electrical Technician": ["Learn electrical quantities, circuit theory and safe work practices.", "Practice reading schematic, wiring and single-line drawings.", "Learn correct use and limitations of meters under supervision.", "Build supervised installation, maintenance and fault-finding experience.", "Check local licensing, qualification recognition and employer requirements."],
        "Industrial Automation Technician": ["Learn contactors, relays, sensors and motor-control fundamentals.", "Study PLC I/O, scan cycle, ladder logic and interlocks.", "Learn HMI/SCADA architecture and industrial communication basics.", "Use simulators and supervised training rigs before field commissioning.", "Build a documented portfolio with safety and troubleshooting notes."],
        "Power Systems": ["Master circuit theory and three-phase systems.", "Study transformers, generators, cables and switchgear.", "Learn fault calculations, grounding and protection coordination.", "Practice load estimates and engineering calculations.", "Confirm required academic credentials and local professional registration."],
        "Marine Electrical / ETO": ["Strengthen electrical machines, shipboard distribution and automation knowledge.", "Research current approved training and certification pathways.", "Verify medical, sea-service, STCW and flag-state requirements with the competent authority.", "Seek legitimate cadetship/sponsorship routes and verify employers and training providers.", "Keep certificates, sea-service evidence and technical records organized."],
    }
    path = st.selectbox("Choose a pathway", list(paths.keys()))
    for i, item in enumerate(paths[path], 1):
        st.markdown(f"**Step {i}.** {item}")
    st.warning("Do not pay recruitment or training fees based only on informal promises. Verify offers, approved providers and official requirements independently.")

elif page == "Glossary":
    st.markdown("# Glossary")
    query = st.text_input("Search terms")
    for term, definition in GLOSSARY.items():
        if not query or query.lower() in (term + " " + definition).lower():
            with st.expander(term):
                st.write(definition)

elif page == "References":
    st.markdown("# References & Further Reading")
    st.write("These references support deeper study. Confirm the relevant edition, current standard and local applicability before applying requirements to a real installation.")
    for item in REFERENCES:
        with st.container(border=True):
            st.markdown(f"**{item['title']}**")
            st.caption(item["author"])
            st.write(item["use"])
            if item.get("url"):
                st.markdown(f"[Official website / resource]({item['url']})")

st.sidebar.divider()
st.sidebar.caption("ElectraPro • Electrical Engineering & Technology")
st.sidebar.caption("Follow current standards, equipment manuals and safe-work procedures.")
