import streamlit as st
import random
import math
import uuid
import os
from datetime import datetime, timezone

try:
    import requests
except ImportError:
    requests = None

st.set_page_config(
    page_title="ElectraPro | Electrical Knowledge & Career Hub",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------- Styling --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] {font-family: Inter, sans-serif;}
.block-container {padding-top: 1.5rem; padding-bottom: 3rem; max-width: 1440px;}
.hero {
  padding: 2rem 2.2rem; border-radius: 22px; color: #fff;
  background: radial-gradient(circle at 90% 10%, rgba(45,212,191,.28), transparent 28%),
              linear-gradient(125deg, #071a2e 0%, #123b5d 54%, #087f8c 100%);
  margin-bottom: 1.2rem; border: 1px solid rgba(255,255,255,.12);
}
.hero h1 {color:#fff; font-size:2.4rem; font-weight:800; letter-spacing:-.04em; margin:0;}
.hero p {color:#e0f2fe; font-size:1.06rem; margin:.6rem 0 0;}
.kicker {color:#5eead4; text-transform:uppercase; letter-spacing:.14em; font-size:.76rem; font-weight:700;}
.card {
  border:1px solid rgba(120,140,160,.25); border-radius:16px;
  padding:1rem 1.1rem; background:rgba(120,140,160,.055); height:100%;
}
.card h3 {margin:.2rem 0 .45rem; font-size:1.06rem;}
.muted {opacity:.76; font-size:.91rem;}
.pill {display:inline-block; border-radius:999px; padding:.2rem .6rem; background:rgba(20,184,166,.13); color:#0f766e; font-size:.78rem; font-weight:700;}
div[data-testid="stMetric"] {border:1px solid rgba(120,140,160,.2); border-radius:15px; padding:13px 15px; background:rgba(120,140,160,.05);}
[data-testid="stSidebar"] {border-right:1px solid rgba(120,140,160,.2);}
</style>
""", unsafe_allow_html=True)

# -------------------- Structured knowledge library --------------------
LIBRARY = {
    "Electrical Fundamentals": {
        "level": "Foundation",
        "intro": "Build a reliable understanding of electrical quantities, circuit behaviour, AC/DC and calculations.",
        "modules": [
            ("Voltage, current and resistance", "Voltage is electric potential difference (volt, V). Current is rate of charge flow (ampere, A). Resistance opposes current (ohm, Ω). For an ohmic resistor under suitable conditions, V = I × R.", "V = I × R | I = V/R | R = V/I"),
            ("Power and energy", "Power is the rate of energy transfer. Energy consumption is commonly measured in kilowatt-hours (kWh). In DC circuits, P = V × I; for sinusoidal single-phase AC real power, P = V × I × cosφ.", "P = V × I | E = P × t | kWh = kW × hours"),
            ("Series and parallel networks", "Series elements carry the same current; ideal parallel branches share the same voltage. Equivalent resistance depends on topology. Use circuit diagrams and verify units before calculating.", "Rseries = R1 + R2 + … | 1/Rparallel = Σ(1/Ri)"),
            ("AC, frequency and phase", "Alternating current changes periodically. Frequency is measured in hertz. Phase describes the relative position of periodic waveforms. Resistive, inductive and capacitive loads affect phase relationships.", "ω = 2πf"),
            ("Measurements and instruments", "Understand meter ranges, resolution, accuracy, measurement category and correct connection. Ammeter connections and live measurements require proper training and approved safe-work procedures.", "Error (%) = |measured − reference| / reference × 100"),
        ],
    },
    "Machines & Transformers": {
        "level": "Core engineering",
        "intro": "Study electromagnetic conversion, transformers, motors, generators, losses and performance.",
        "modules": [
            ("Transformer operation", "A transformer transfers AC energy between windings through changing magnetic flux. In the ideal case, voltage ratio equals turns ratio. Real transformers have copper, core and stray losses.", "Vp/Vs = Np/Ns (ideal)"),
            ("Three-phase induction motors", "A three-phase stator creates a rotating magnetic field. During motoring, rotor speed is below synchronous speed. Learn starting methods, nameplate data, protection and efficiency concepts.", "Ns = 120f/P rpm | slip = (Ns − Nr)/Ns"),
            ("Synchronous machines", "Synchronous machines run in step with the rotating field when synchronized. Applications include alternators and synchronous motors. Synchronizing a generator requires approved procedures and protection.", "Ns = 120f/P rpm"),
            ("Generator fundamentals", "Generators convert mechanical energy into electrical energy through electromagnetic induction. Review excitation, voltage regulation, frequency control, load sharing and protective functions.", "η = output power / input power × 100%"),
            ("Losses and efficiency", "Copper losses are approximately I²R. Core losses include hysteresis and eddy-current losses. Efficiency depends on operating conditions and should be calculated with consistent units.", "Pcu ≈ I²R | η = Pout/Pin × 100%"),
        ],
    },
    "Power Systems & Protection": {
        "level": "Core / advanced",
        "intro": "Understand grid architecture, fault protection, switchgear, power quality and electrical safety.",
        "modules": [
            ("Generation to distribution", "Power systems commonly include generation, step-up transformation, transmission, substations, distribution and loads. System voltage and design vary by network and jurisdiction.", "Balanced 3-phase: P = √3 VL IL cosφ"),
            ("Relays and circuit breakers", "Protective relays evaluate measured quantities and issue trip commands when configured criteria are met. Breakers interrupt current within their ratings. Protection coordination is an engineering task.", "Study: overcurrent, earth fault, differential, distance protection"),
            ("Earthing and bonding", "Protective earthing and bonding reduce risk from dangerous touch voltages and support protective-device operation. Requirements depend on the installation and applicable code.", "Verify against applicable local regulations and design standards"),
            ("Power factor and power quality", "Power factor is real power divided by apparent power. Harmonics, voltage dips, unbalance and transients can affect equipment. Any correction solution needs a system-specific assessment.", "PF = kW/kVA"),
            ("Electrical safety fundamentals", "Electrical hazards can be fatal. Follow authorization, isolation, lockout/tagout, prove-dead verification, PPE and permit procedures as applicable. Practical work requires qualified supervision.", "Never assume equipment is de-energized; follow approved procedures"),
        ],
    },
    "Industrial Automation & Electronics": {
        "level": "Industry skills",
        "intro": "Explore PLCs, sensors, control loops, power electronics, instrumentation and fault-finding concepts.",
        "modules": [
            ("PLC fundamentals", "A programmable logic controller reads inputs, executes a control program and updates outputs. Core concepts include digital logic, timers, counters, analog signals and interlocks.", "Input → logic/program → output"),
            ("Sensors and instrumentation", "Sensors convert physical conditions into signals. Study range, accuracy, calibration, signal conditioning, 4–20 mA loops and common wiring concepts.", "Check sensor range, scaling, supply and signal type"),
            ("Control systems", "Open-loop systems act without output feedback; closed-loop systems use feedback to reduce error. Understand setpoint, process variable, controller output and stability.", "Error = setpoint − measured process variable"),
            ("Power electronics", "Rectifiers, inverters, DC-DC converters and motor drives control electrical power. Device selection, thermal management, harmonics and protection are key design considerations.", "Review switching, conversion efficiency and thermal limits"),
            ("Systematic troubleshooting", "Gather symptoms, review drawings and logs, identify likely causes, assess risk, isolate safely, test using authorized methods, document findings and verify restoration.", "Observe → assess risk → isolate → diagnose → verify → document"),
        ],
    },
    "Renewables, EVs & Smart Grids": {
        "level": "Modern technology",
        "intro": "Learn the electrical principles behind solar, storage, EV charging, grid modernization and emerging technologies.",
        "modules": [
            ("Solar PV systems", "PV modules produce DC power. Inverters convert power for suitable loads or grid interconnection. Output depends on irradiance, temperature, shading, orientation and system losses.", "Energy (kWh) = average power (kW) × time (h)"),
            ("Batteries and storage", "Battery systems have voltage, capacity, energy, charge/discharge limits and lifecycle characteristics. Use the manufacturer's specifications and an appropriate battery management system.", "Energy (Wh) ≈ nominal voltage × capacity (Ah)"),
            ("Electric vehicles", "EVs combine battery packs, traction inverters, electric motors, charging systems and thermal management. High-voltage vehicle systems require dedicated training and safety procedures.", "Learn AC charging, DC fast charging and connector standards"),
            ("Smart grids", "Smart grids combine sensing, communications, automation and control to improve visibility and flexibility. Cybersecurity, interoperability and data quality are important.", "Explore AMI, demand response, microgrids and grid storage"),
            ("AI in electrical engineering", "AI can support load forecasting, condition monitoring and fault analytics. It should be validated against reliable data and used with engineering judgement, not as an unverified safety authority.", "Check data quality, false alarms, validation and human oversight"),
        ],
    },
    "Marine ETO & Shipboard Systems": {
        "level": "Maritime career",
        "intro": "A structured study route for shipboard electrical, electronic, control and automation systems.",
        "modules": [
            ("ETO role and boundaries", "An Electro-Technical Officer supports electrical, electronic, control and automation systems within assigned duties, certification scope, vessel procedures and company requirements.", "Study technical principles alongside current flag-state and employer requirements"),
            ("Shipboard generation and distribution", "Study alternators, switchboards, generator protection, load sharing, emergency power and distribution architecture. Real operations must follow the vessel's approved procedures.", "Review voltage, frequency, load, protection and redundancy concepts"),
            ("Motors, drives and automation", "Review pumps, fans, motor starters, variable-frequency drives, sensors, actuators, alarms, PLCs and control-system fault diagnosis.", "Explain the principle, likely faults, safe response and documentation"),
            ("Emergency systems and safety", "Understand the purpose of emergency power, alarms, protective devices, permits and emergency procedures. Vessel-specific drills and manuals take precedence.", "Know who to notify and which approved procedure applies"),
            ("COC and STCW study planning", "Certification routes depend on the relevant maritime administration, approved training, sea service, assessments and current regulations. Confirm exact eligibility directly with the competent authority.", "Maintain an official-source checklist; do not rely on an unofficial summary as a final eligibility decision"),
        ],
    },
    "WAPDA & Public-Sector Jobs": {
        "level": "Recruitment preparation",
        "intro": "Prepare systematically for electrical vacancies, technical MCQs, interviews and aptitude tests.",
        "modules": [
            ("Syllabus-first preparation", "Read the current vacancy advertisement and official syllabus. Eligibility, exam pattern, topics and dates can differ by employer and post.", "Create a checklist from the exact recruitment notice"),
            ("Technical revision", "Prioritize fundamentals, machines, transformers, power systems, protection, measurements, basic electronics and safety according to the published syllabus.", "Study concepts, then practise timed MCQs"),
            ("Interview structure", "For technical answers: define the term, explain the principle, give an application and mention a relevant limitation or safety point.", "Definition → principle → example → safety/limitation"),
            ("CV and practical skills", "Present qualifications, training, projects and skills accurately. Distinguish classroom knowledge from supervised practical experience and licensed work.", "Use evidence-based, truthful examples"),
            ("Test review system", "Maintain an error log with topic, reason for error, corrected concept and revision date. Practise under time limits and re-test weak areas.", "Track accuracy by topic rather than memorizing answers alone"),
        ],
    },
    "Electrical Interview Workshop": {
        "level": "Career readiness",
        "intro": "Practise explaining technical concepts clearly for technician, engineer, industrial and maritime interviews.",
        "modules": [
            ("Use a clear answer structure", "Start with a direct definition. Explain how it works, give one practical example, and finish with a limitation or safety consideration.", "Definition → working principle → application → safety"),
            ("Scenario-based questions", "Describe how you gather facts, consult drawings, assess risk, follow authorized isolation procedures and document findings. Never claim to work beyond your competence.", "Safety and process before speculative troubleshooting"),
            ("Behavioural questions", "Use a real example and structure it as Situation, Task, Action and Result. Be concise and honest about your own contribution.", "STAR: Situation, Task, Action, Result"),
            ("Explain diagrams", "Practise reading single-line diagrams, control schematics, motor circuits, protection diagrams and instrumentation loops relevant to the role.", "Name components, trace function, explain protection"),
            ("Professional communication", "If unsure, say what you know, identify what must be checked and explain how you would verify it using approved references.", "Clear reasoning is better than unsupported certainty"),
        ],
    },
}

QUIZ_BANK = [
    ("What is the SI unit of current?", ["Volt", "Ampere", "Ohm", "Watt"], 1, "Current is measured in amperes (A)."),
    ("For an ideal transformer, Vp/Vs equals:", ["Np/Ns", "Ns/Np always", "Frequency × current", "Resistance ratio in all cases"], 0, "The ideal voltage ratio equals the winding turns ratio."),
    ("What does kWh measure?", ["Power", "Energy", "Resistance", "Frequency"], 1, "A kilowatt-hour is a unit of energy."),
    ("Which formula gives synchronous speed in rpm?", ["120f/P", "V/I", "I²R", "P/V"], 0, "Ns = 120f/P, where f is frequency and P is the number of poles."),
    ("A protective relay primarily:", ["Stores mechanical energy", "Detects abnormal electrical conditions and initiates protection", "Increases frequency", "Measures room temperature only"], 1, "A relay operates as part of a coordinated protection system."),
    ("What does PLC stand for?", ["Power Line Converter", "Programmable Logic Controller", "Primary Load Circuit", "Phase Logic Capacitor"], 1, "PLCs are industrial automation controllers."),
    ("For a balanced three-phase system, real power is:", ["√3 VL IL cosφ", "VL/IL", "I²/R", "V + I"], 0, "Use line voltage, line current and power factor for this common formula."),
    ("What is an essential principle before electrical maintenance?", ["Assume it is safe", "Follow approved isolation and verification procedures", "Ignore drawings", "Bypass protection"], 1, "Never assume equipment is safe; follow authorized procedures and qualified supervision."),
    ("Power factor is commonly expressed as:", ["kW/kVA", "kVA/kWh", "Ohms/volt", "Hz/ampere"], 0, "Power factor is real power divided by apparent power."),
    ("A PV module normally produces:", ["DC electricity", "Only compressed air", "Mechanical torque directly", "AC at all conditions without electronics"], 0, "PV cells produce DC; power conversion depends on the system."),
    ("Which is a typical PLC input?", ["Limit switch signal", "Paint colour", "Cabinet label", "Operator's job title"], 0, "A limit switch can provide a discrete input to a PLC."),
    ("An induction motor in motoring operation typically has rotor speed:", ["Above synchronous speed", "Below synchronous speed", "Always zero", "Equal to supply frequency in rpm"], 1, "Motoring operation involves slip relative to synchronous speed."),
]

CAREER_PLANS = {
    "Merchant Navy ETO": [
        "Review electrical fundamentals, AC theory, machines, transformers and measurements.",
        "Study marine generation, switchboards, protection, emergency power and distribution.",
        "Review motors, drives, automation, sensors, alarms and control systems.",
        "Practise oral explanations and structured fault-analysis scenarios.",
        "Verify current eligibility, approved courses, sea-service requirements and COC pathway with the relevant maritime administration.",
    ],
    "WAPDA / public-sector electrical posts": [
        "Download and read the exact current advertisement and official syllabus.",
        "Build a topic list: fundamentals, machines, transformers, power systems, protection and measurements.",
        "Complete timed topic-wise MCQ sets and keep an error log.",
        "Prepare aptitude or general sections only where required by the official syllabus.",
        "Verify eligibility, test dates and selection steps through the official recruitment notice.",
    ],
    "Industrial electrical / maintenance roles": [
        "Revise motors, starters, contactors, overload protection and drawings.",
        "Study preventive maintenance documentation and basic instrumentation.",
        "Learn PLC/VFD principles and safe troubleshooting workflows.",
        "Prepare honest examples of training, projects and supervised work.",
        "Follow employer authorization, permit and safety requirements for practical tasks.",
    ],
    "Electrical technician / DAE roles": [
        "Revise electrical quantities, wiring theory, measurements and protection basics.",
        "Practise reading schematic and single-line diagrams.",
        "Review motor, transformer, distribution and maintenance concepts.",
        "Prepare concise examples of practical training and fault reporting.",
        "Check job-specific qualifications, licences and experience requirements.",
    ],
    "Electrical engineering interviews": [
        "Practise core definitions and explain the underlying principles.",
        "Prepare machines, transformers, protection, power systems and power electronics.",
        "Practise one-minute technical answers and scenario questions.",
        "Use STAR for behavioural examples and be accurate about your contribution.",
        "Prepare questions about the role, safety culture, training and performance expectations.",
    ],
}

# -------------------- Optional privacy-aware analytics --------------------
def _get_secret(key, default=""):
    try:
        return st.secrets.get(key, default)
    except Exception:
        return os.getenv(key, default)

def analytics_configured():
    return bool(_get_secret("SUPABASE_URL") and _get_secret("SUPABASE_SERVICE_ROLE_KEY") and requests)

def record_event(event_name, page_name):
    if not st.session_state.get("analytics_consent", False):
        return
    if not analytics_configured():
        return
    # A random session ID is used; do not collect IP address, name, email or precise location.
    if "visitor_session_id" not in st.session_state:
        st.session_state.visitor_session_id = str(uuid.uuid4())
    payload = {
        "visitor_session_id": st.session_state.visitor_session_id,
        "event_name": event_name,
        "page_name": page_name,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "app_version": "1.0.0",
    }
    try:
        url = _get_secret("SUPABASE_URL").rstrip("/") + "/rest/v1/analytics_events"
        key = _get_secret("SUPABASE_SERVICE_ROLE_KEY")
        requests.post(
            url,
            headers={"apikey": key, "Authorization": f"Bearer {key}",
                     "Content-Type": "application/json", "Prefer": "return=minimal"},
            json=payload, timeout=3
        )
    except Exception:
        # Analytics failure must never stop the learning app.
        pass

def get_analytics_rows():
    if not analytics_configured():
        return None
    try:
        url = _get_secret("SUPABASE_URL").rstrip("/") + "/rest/v1/analytics_events"
        key = _get_secret("SUPABASE_SERVICE_ROLE_KEY")
        r = requests.get(
            url,
            headers={"apikey": key, "Authorization": f"Bearer {key}"},
            params={"select": "visitor_session_id,event_name,page_name,created_at,app_version",
                    "order": "created_at.desc", "limit": "5000"},
            timeout=5
        )
        if r.ok:
            return r.json()
    except Exception:
        return None
    return None

# -------------------- Shared UI helpers --------------------
def hero():
    st.markdown("""
    <div class="hero">
      <div class="kicker">Learn • Practise • Build your career</div>
      <h1>ElectraPro</h1>
      <p>Electrical Engineering, Technology & Career Preparation Hub</p>
    </div>
    """, unsafe_allow_html=True)

def section_card(col, icon, title, desc):
    with col:
        st.markdown(f'<div class="card"><h3>{icon} {title}</h3><div class="muted">{desc}</div></div>', unsafe_allow_html=True)

def render_learning():
    st.title("📚 Learning Library")
    st.write("Choose a subject, open a module and build knowledge from foundations to career-focused topics.")
    selected = st.selectbox("Subject area", list(LIBRARY.keys()))
    data = LIBRARY[selected]
    st.caption(f"Learning level: {data['level']}")
    st.write(data["intro"])
    for i, (title, body, formula) in enumerate(data["modules"], start=1):
        with st.expander(f"{i:02d} · {title}"):
            st.write(body)
            st.markdown("**Formula / quick reference**")
            st.code(formula)
            if st.button("Mark module reviewed", key=f"review_{selected}_{i}"):
                st.session_state.setdefault("reviewed_modules", set()).add(f"{selected}:{title}")
                st.success("Marked as reviewed for this session.")
    reviewed = len(st.session_state.get("reviewed_modules", set()))
    st.caption(f"Modules marked reviewed this session: {reviewed}")

def render_quiz():
    st.title("🧠 Exam Practice Centre")
    topics = ["Mixed fundamentals", "Machines & transformers", "Power systems", "Automation", "Modern technology", "Marine ETO"]
    chosen_topic = st.selectbox("Practice set", topics)
    count = st.slider("Number of questions", 5, min(12, len(QUIZ_BANK)), 8)
    if st.button("Create new question set"):
        st.session_state.quiz_ids = random.sample(range(len(QUIZ_BANK)), count)
        st.session_state.pop("quiz_result", None)
    if "quiz_ids" not in st.session_state or len(st.session_state.quiz_ids) != count:
        st.session_state.quiz_ids = random.sample(range(len(QUIZ_BANK)), count)
    st.caption(f"Set: {chosen_topic}. Starter question bank currently contains general electrical fundamentals.")
    with st.form("exam_practice"):
        answers = {}
        for n, idx in enumerate(st.session_state.quiz_ids, 1):
            q, options, correct, why = QUIZ_BANK[idx]
            answers[idx] = st.radio(f"Q{n}. {q}", options, key=f"answer_{idx}")
        submit = st.form_submit_button("Submit answers", type="primary")
    if submit:
        score = sum(answers[i] == QUIZ_BANK[i][1][QUIZ_BANK[i][2]] for i in answers)
        st.session_state.quiz_result = {"score": score, "total": len(answers), "answers": answers}
    result = st.session_state.get("quiz_result")
    if result:
        st.metric("Your result", f"{result['score']} / {result['total']}", f"{result['score']/result['total']:.0%}")
        for idx in st.session_state.quiz_ids:
            q, options, correct, why = QUIZ_BANK[idx]
            if result["answers"].get(idx) == options[correct]:
                st.success(f"Correct — {q}")
            else:
                st.error(f"Review — {q} Correct answer: {options[correct]}")
            st.caption(why)
        st.info("This starter question bank is not an official exam paper. More role-specific, syllabus-mapped question banks can be added.")

def render_calculators():
    st.title("🧮 Engineering Calculators")
    st.warning("Educational estimates only. These simple tools are not a substitute for approved engineering design, equipment manuals, standards or qualified safety review.")
    mode = st.selectbox("Calculator", [
        "Ohm's law", "DC / resistive power", "Balanced three-phase power",
        "Transformer ideal ratio", "Motor synchronous speed", "Energy and cost"
    ])
    if mode == "Ohm's law":
        c1, c2 = st.columns(2)
        v = c1.number_input("Voltage (V)", 0.0, value=12.0, step=1.0)
        r = c2.number_input("Resistance (Ω)", min_value=0.01, value=6.0, step=0.5)
        st.metric("Current", f"{v/r:.3f} A")
        st.metric("Power (ideal resistor)", f"{v*v/r:.3f} W")
    elif mode == "DC / resistive power":
        c1, c2 = st.columns(2)
        v = c1.number_input("Voltage (V)", 0.0, value=24.0, step=1.0)
        i = c2.number_input("Current (A)", 0.0, value=2.0, step=0.5)
        st.metric("Power", f"{v*i:.2f} W")
    elif mode == "Balanced three-phase power":
        c1, c2, c3 = st.columns(3)
        v = c1.number_input("Line voltage (V)", 0.0, value=400.0, step=10.0)
        i = c2.number_input("Line current (A)", 0.0, value=10.0, step=1.0)
        pf = c3.number_input("Power factor", 0.0, 1.0, value=0.85, step=0.05)
        st.metric("Real power", f"{math.sqrt(3)*v*i*pf/1000:.3f} kW")
        st.caption("Assumes a balanced three-phase system.")
    elif mode == "Transformer ideal ratio":
        c1, c2 = st.columns(2)
        vp = c1.number_input("Primary voltage (V)", min_value=0.0, value=230.0, step=10.0)
        np = c2.number_input("Primary turns", min_value=1, value=1000, step=100)
        ns = st.number_input("Secondary turns", min_value=1, value=200, step=10)
        st.metric("Ideal secondary voltage", f"{vp*ns/np:.2f} V")
        st.caption("Ideal turns-ratio estimate; real equipment has losses and design constraints.")
    elif mode == "Motor synchronous speed":
        c1, c2 = st.columns(2)
        f = c1.number_input("Frequency (Hz)", min_value=0.1, value=50.0, step=1.0)
        poles = c2.selectbox("Number of poles", [2, 4, 6, 8, 10, 12], index=1)
        st.metric("Synchronous speed", f"{120*f/poles:.0f} rpm")
        st.caption("An induction motor rotor runs below synchronous speed during normal motoring.")
    else:
        c1, c2 = st.columns(2)
        kw = c1.number_input("Load power (kW)", min_value=0.0, value=1.5, step=0.5)
        hours = c2.number_input("Hours used", min_value=0.0, value=4.0, step=0.5)
        rate = st.number_input("Tariff per kWh (optional)", min_value=0.0, value=0.0, step=1.0)
        energy = kw * hours
        st.metric("Energy", f"{energy:.2f} kWh")
        if rate > 0:
            st.metric("Estimated cost", f"{energy*rate:,.2f}")

def render_career():
    st.title("🎯 Career & Certification Roadmaps")
    path = st.selectbox("Choose your target", list(CAREER_PLANS.keys()))
    st.write("Use this as a planning checklist, then tailor it to the exact vacancy, employer or competent authority.")
    completed = 0
    for n, task in enumerate(CAREER_PLANS[path], 1):
        if st.checkbox(task, key=f"path_{path}_{n}"):
            completed += 1
    st.progress(completed / len(CAREER_PLANS[path]))
    st.caption(f"{completed} of {len(CAREER_PLANS[path])} checklist items completed in this session.")
    st.subheader("Interview answer practice")
    q = st.selectbox("Question", [
        "Explain how a transformer works.",
        "What is power factor and why does it matter?",
        "How does an induction motor work?",
        "What is the role of an ETO?",
        "How should you approach an electrical fault?",
        "Explain a PLC in simple terms.",
    ])
    answers = {
        "Explain how a transformer works.": "A transformer transfers AC energy between windings through changing magnetic flux. In an ideal transformer, voltage ratio follows the turns ratio; actual units have losses and operating limits.",
        "What is power factor and why does it matter?": "Power factor is real power divided by apparent power. A lower value can mean higher current for the same real power. Any correction must be designed for the actual installation.",
        "How does an induction motor work?": "Three-phase stator currents create a rotating magnetic field that induces rotor current and torque. In motoring operation, rotor speed is below synchronous speed.",
        "What is the role of an ETO?": "An ETO supports assigned shipboard electrical, electronic, control and automation systems within their certification scope and vessel procedures.",
        "How should you approach an electrical fault?": "Assess risk, notify the responsible person, follow approved isolation and verification procedures, consult documentation, diagnose only within your authorization, test restoration as required and record findings.",
        "Explain a PLC in simple terms.": "A PLC is an industrial controller that reads input signals, runs programmed logic and updates outputs to automate machinery or a process.",
    }
    with st.expander("Reveal a sample answer structure"):
        st.write(answers[q])
        st.caption("Adapt this to your own knowledge and experience; never claim qualifications or practical experience you do not have.")

def render_ask():
    st.title("💬 Electrical Question Desk")
    st.write("Use the form to structure a question for a clear, level-appropriate explanation.")
    with st.form("question_form"):
        question = st.text_area("Your question", placeholder="Example: Explain induction motor slip in Urdu and English.")
        field = st.selectbox("Field", list(LIBRARY.keys()))
        level = st.selectbox("Your level", ["Beginner", "DAE / technician", "Engineering student", "Job-test candidate", "Marine ETO candidate", "Working professional"])
        language = st.selectbox("Answer language", ["Urdu + English", "Simple English", "Detailed English"])
        detail = st.selectbox("Detail level", ["Quick explanation", "Step-by-step explanation", "Exam-focused answer", "Interview-style answer"])
        submitted = st.form_submit_button("Prepare my question")
    if submitted:
        if not question.strip():
            st.warning("Please write your question first.")
        else:
            st.markdown("### Question brief")
            st.write(f"**Question:** {question}")
            st.write(f"**Field:** {field} · **Level:** {level}")
            st.write(f"**Language:** {language} · **Style:** {detail}")
            st.info("Automatic AI answers are not enabled in this release. This page prepares a structured request; a real answer engine can be integrated in the next phase with a securely stored API key.")
    st.divider()
    st.markdown("**Want to contribute?** A future release can include verified article submissions, moderated Q&A, citations and revision history.")

def render_glossary():
    st.title("📖 Electrical Glossary")
    terms = {
        "AC": "Alternating current; current whose direction and magnitude vary periodically.",
        "DC": "Direct current; current with one direction of flow in a circuit reference.",
        "EMF": "Electromotive force; energy supplied per unit charge by a source.",
        "PF": "Power factor; ratio of real power to apparent power.",
        "PLC": "Programmable Logic Controller; industrial automation controller.",
        "VFD": "Variable-Frequency Drive; controls AC motor speed by varying supply frequency and voltage as designed.",
        "COC": "Certificate of Competency; exact meaning and requirements depend on the competent authority and certification scheme.",
        "ETO": "Electro-Technical Officer; a maritime role focused on electrical, electronic, control and automation systems.",
        "STCW": "International convention framework for standards of training, certification and watchkeeping for seafarers.",
        "PV": "Photovoltaic; technology that converts light into electrical energy.",
        "RCD": "Residual Current Device; protective device that detects residual current under specified conditions.",
        "MCB": "Miniature Circuit Breaker; protective device commonly used for overcurrent protection in suitable installations.",
    }
    search = st.text_input("Search terms", placeholder="Try: transformer, ETO, PLC…")
    for term, meaning in terms.items():
        if not search or search.lower() in term.lower() or search.lower() in meaning.lower():
            with st.expander(term):
                st.write(meaning)

def render_resources():
    st.title("🔎 Reference & Verification Centre")
    st.write("Use authoritative sources for technical standards, recruitment, certification and regulated work.")
    resources = [
        ("International Electrotechnical Commission (IEC)", "https://www.iec.ch/", "International electrotechnical standards information."),
        ("IEEE", "https://www.ieee.org/", "Engineering publications, professional knowledge and technical communities."),
        ("International Maritime Organization (IMO)", "https://www.imo.org/", "International maritime framework and STCW information."),
        ("WAPDA Pakistan", "https://www.wapda.gov.pk/", "Official WAPDA information; verify current recruitment through official notices."),
        ("NEPRA Pakistan", "https://nepra.org.pk/", "Pakistan power-sector regulator and published documents."),
        ("Streamlit Community Cloud", "https://share.streamlit.io/", "Deployment platform for this app."),
    ]
    for title, url, desc in resources:
        st.markdown(f"**[{title}]({url})**  \n{desc}")
    st.warning("A link to an organization is not confirmation of a specific job opening, course approval, COC eligibility or current exam syllabus. Check the relevant official notice.")

def render_privacy():
    st.title("🔐 Privacy & Visitor Analytics")
    st.write("ElectraPro can optionally record aggregate usage events to help the site owner understand which pages are used. Tracking is disabled unless the visitor explicitly opts in.")
    st.markdown("""
**If enabled and configured, the app stores:**
- A random session identifier (not your name)
- Page name and event type
- Timestamp and app version

**The app is designed not to collect:** names, email addresses, IP addresses or precise location through its own analytics code.

**Important:** A random session identifier is still a pseudonymous online identifier. Do not enable tracking until you have published a suitable privacy notice and checked applicable privacy requirements. You can decline tracking and continue using the learning features.
""")
    consent = st.checkbox("I agree to optional anonymous usage analytics for this session.", value=st.session_state.get("analytics_consent", False))
    if consent != st.session_state.get("analytics_consent", False):
        st.session_state.analytics_consent = consent
        if consent:
            record_event("analytics_consent", "Privacy")
        st.rerun()
    if not analytics_configured():
        st.info("Visitor analytics is not connected yet. After setting up Supabase and Streamlit secrets, consented page visits can be recorded. No visitor records are currently being saved by this app.")
    else:
        st.success("Analytics backend is configured. Tracking is only attempted after session consent.")

def render_admin():
    st.title("📊 Owner Analytics Dashboard")
    if not analytics_configured():
        st.info("Connect Supabase using the setup guide before analytics can be displayed.")
        return
    admin_password = _get_secret("ADMIN_DASHBOARD_PASSWORD")
    if not admin_password:
        st.warning("Set ADMIN_DASHBOARD_PASSWORD in Streamlit secrets before using this page.")
        return
    entered = st.text_input("Owner dashboard password", type="password")
    if not entered or entered != admin_password:
        st.caption("This private page requires the owner password configured in app secrets.")
        return
    rows = get_analytics_rows()
    if rows is None:
        st.error("Could not read analytics. Check Supabase URL, service-role key and table setup.")
        return
    sessions = len(set(x.get("visitor_session_id") for x in rows if x.get("visitor_session_id")))
    pageviews = sum(x.get("event_name") == "page_view" for x in rows)
    c1, c2, c3 = st.columns(3)
    c1.metric("Recorded events", len(rows))
    c2.metric("Distinct session IDs in retained rows", sessions)
    c3.metric("Page views", pageviews)
    counts = {}
    for row in rows:
        if row.get("event_name") == "page_view":
            p = row.get("page_name", "Unknown")
            counts[p] = counts.get(p, 0) + 1
    st.subheader("Page views by page")
    if counts:
        st.bar_chart(counts)
    st.caption("This is consent-based, pseudonymous session analytics—not verified unique people. Counts cover only retained records returned by the query.")

def main():
    if "analytics_consent" not in st.session_state:
        st.session_state.analytics_consent = False
    hero()
    with st.sidebar:
        st.markdown("## ⚡ ElectraPro")
        st.caption("Electrical knowledge & career hub")
        page = st.radio("Navigate", [
            "Overview", "Learning Library", "Exam Practice", "Engineering Calculators",
            "Career Roadmaps", "Question Desk", "Glossary", "References",
            "Privacy & Analytics", "Owner Analytics"
        ])
        st.divider()
        st.caption("Version 1.0 • Learning prototype")
        st.caption("For education only; follow approved standards and qualified supervision.")
    if page == "Overview":
        st.markdown("### Your electrical learning workspace")
        st.write("A structured starting point for students, DAE technicians, engineering learners, job applicants and marine ETO candidates.")
        cols = st.columns(4)
        cols[0].metric("Learning pathways", len(LIBRARY))
        cols[1].metric("Study modules", sum(len(v["modules"]) for v in LIBRARY.values()))
        cols[2].metric("Practice MCQs", len(QUIZ_BANK))
        cols[3].metric("Calculators", 6)
        st.markdown("### Explore the platform")
        cards = st.columns(3)
        section_card(cards[0], "📚", "Learn", "Structured learning from electrical fundamentals to modern systems.")
        section_card(cards[1], "🎯", "Prepare", "Job roadmaps, quiz practice, interview structures and study checklists.")
        section_card(cards[2], "🧮", "Calculate", "Useful educational calculators with assumptions explained.")
        st.markdown("### Recommended study sequence")
        st.write("**Fundamentals → Machines & Transformers → Power Systems → Automation → Choose your career pathway.**")
        st.markdown("### Choose a starting point")
        choice = st.selectbox("What are you here for?", [
            "Learn from basics", "Prepare for Merchant Navy ETO", "Prepare for WAPDA / public-sector jobs",
            "Industrial electrical work", "Interview preparation", "Modern electrical technology"
        ])
        st.info({
            "Learn from basics": "Open Learning Library → Electrical Fundamentals.",
            "Prepare for Merchant Navy ETO": "Open Career Roadmaps → Merchant Navy ETO and study the Marine ETO modules.",
            "Prepare for WAPDA / public-sector jobs": "Open Career Roadmaps and Exam Practice; verify the current official syllabus.",
            "Industrial electrical work": "Start with Industrial Automation & Electronics, then Machines & Transformers.",
            "Interview preparation": "Use Electrical Interview Workshop and Career Roadmaps.",
            "Modern electrical technology": "Explore Renewables, EVs & Smart Grids.",
        }[choice])
        st.markdown("### Our quality promise")
        st.write("We aim to make technical concepts clear, label assumptions, and distinguish learning guidance from official certification or safety-critical instructions.")
        st.warning("This first release has a starter knowledge base and quiz bank. Automatic AI answers, user accounts, progress sync and a full citation-managed article library are not enabled yet.")
    elif page == "Learning Library":
        render_learning()
    elif page == "Exam Practice":
        render_quiz()
    elif page == "Engineering Calculators":
        render_calculators()
    elif page == "Career Roadmaps":
        render_career()
    elif page == "Question Desk":
        render_ask()
    elif page == "Glossary":
        render_glossary()
    elif page == "References":
        render_resources()
    elif page == "Privacy & Analytics":
        render_privacy()
    else:
        render_admin()
    # Track page view once per session per selected page, only with opt-in.
    seen = st.session_state.setdefault("tracked_pages", set())
    if st.session_state.get("analytics_consent", False) and page not in seen:
        record_event("page_view", page)
        seen.add(page)
    st.divider()
    st.caption("ElectraPro • Educational prototype • Verify regulations, job requirements and technical design against authoritative current sources.")

if __name__ == "__main__":
    main()
