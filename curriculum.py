SUBJECTS = {
    "Electrical Fundamentals": {
        "icon":"⚡","level":"Basic → Advanced",
        "description":"Build the mathematical and physical foundations used throughout electrical engineering.",
        "topics":["Charge, current, voltage and energy","Ohm’s law and resistance","Series and parallel circuits","Kirchhoff’s laws","Electrical power and energy","Circuit analysis methods","Capacitance and inductance","Transient response","AC waveforms, RMS and phasors","Complex impedance and resonance","Network theorems","First-order circuit analysis"]
    },
    "Power Systems": {
        "icon":"🔌","level":"Intermediate → Advanced",
        "description":"Understand generation, transmission, distribution, load flow and system reliability.",
        "topics":["Single-line diagrams","Three-phase systems","Per-unit system","Transformers and substations","Transmission-line parameters","Load-flow concepts","Short-circuit calculations","Earthing and grounding","Protection coordination","Power quality and harmonics"]
    },
    "Industrial Automation & Control": {
        "icon":"🏭","level":"Basic → Advanced",
        "description":"Learn industrial control architecture, PLCs, sensors, actuators and supervisory systems.",
        "topics":["Control-system fundamentals","Relays and contactors","Sensors and actuators","PLC hardware and scan cycle","Ladder logic concepts","Timers and counters","HMI design principles","SCADA architecture","Industrial communication networks","VFDs and motor control","Commissioning and fault diagnosis"]
    },
    "Electrical Machines": {
        "icon":"⚙️","level":"Intermediate → Advanced",
        "description":"Study the operating principles, equivalent circuits, performance and testing of electrical machines.",
        "topics":["Magnetic circuits","Transformers","DC machines","Three-phase induction motors","Synchronous machines","Motor starting methods","Efficiency and losses","Nameplate interpretation","Machine testing and maintenance"]
    },
    "Electronics & Embedded Systems": {
        "icon":"🔧","level":"Basic → Advanced",
        "description":"Explore semiconductor devices, analog and digital electronics, microcontrollers and interfaces.",
        "topics":["Semiconductor basics","Diodes and rectifiers","BJT and MOSFET fundamentals","Operational amplifiers","Digital logic","Power electronics","Microcontroller architecture","ADC and PWM","Embedded communication interfaces","Circuit protection and EMC"]
    },
    "Installation & Maintenance": {
        "icon":"🧰","level":"Basic → Advanced",
        "description":"Learn how electrical installations are planned, inspected, maintained and safely diagnosed.",
        "topics":["Reading electrical drawings","Cable selection principles","Conduit and wiring systems","Distribution boards","Protective devices","Inspection and testing","Preventive maintenance","Fault-finding method","Documentation and isolation procedures"]
    },
    "Measurements & Instrumentation": {
        "icon":"📏","level":"Basic → Advanced",
        "description":"Understand measurement principles, instrument selection, uncertainty and industrial instrumentation.",
        "topics":["Units and measurement error","Multimeters and clamp meters","Oscilloscopes","Current and voltage transformers","Sensors and transducers","4–20 mA loops","Calibration","Process instrumentation","Measurement uncertainty"]
    },
    "Renewable Energy": {
        "icon":"☀️","level":"Basic → Advanced",
        "description":"Study photovoltaic systems, inverters, storage, grid integration and energy assessment.",
        "topics":["Solar radiation basics","PV cell and module characteristics","Series-parallel PV arrays","MPPT principles","Inverter operation","Battery storage concepts","System sizing","Protection and isolation","Grid connection and monitoring"]
    },
    "Electrical Design & Calculations": {
        "icon":"📐","level":"Intermediate → Advanced",
        "description":"Develop the calculation workflow behind loads, cables, voltage drop and equipment selection.",
        "topics":["Load estimation","Demand and diversity","Cable ampacity concepts","Voltage-drop calculations","Short-circuit withstand","Breaker and fuse selection","Power-factor correction","Single-line diagrams","Design calculations and documentation"]
    },
    "Control Systems & Drives": {
        "icon":"🎛️","level":"Intermediate → Advanced",
        "description":"Learn feedback control, dynamic response, motor drives and practical tuning concepts.",
        "topics":["Open-loop and closed-loop systems","Transfer functions","Block diagrams","Stability concepts","PID control","Motor-drive architecture","VFD parameter fundamentals","Servo systems","Control-loop troubleshooting"]
    },
    "Electrical Safety & Standards": {
        "icon":"🦺","level":"All levels",
        "description":"Understand electrical hazards, safe systems of work, protective measures and standards awareness.",
        "topics":["Electric shock and arc hazards","Risk assessment","Isolation and lockout/tagout principles","Protective earthing","Overcurrent and residual-current protection","Safe test-instrument use","PPE and safe boundaries","IEC/IEEE standards awareness","Incident reporting"]
    },
    "Marine Electrical & ETO": {
        "icon":"🚢","level":"Intermediate → Advanced",
        "description":"Explore shipboard generation, distribution, automation, emergency systems and ETO career preparation.",
        "topics":["Shipboard electrical architecture","Marine generators and switchboards","Parallel generator operation","Power management systems","Emergency generator and batteries","Marine motors and drives","Alarm monitoring systems","Navigation and communication equipment overview","Planned maintenance","STCW and certification research"]
    },
}

LESSONS = [
{
"subject":"Electrical Fundamentals","level":"Basic","title":"1. Electric Charge, Current, Voltage and Energy",
"duration":"25–35 minutes",
"intro":"Electrical engineering begins with charge and the movement of charge. Voltage describes energy transferred per unit charge, while current describes how quickly charge passes a point.",
"sections":[
{"heading":"1.1 Electric charge","body":"Electric charge is a property of matter. Its SI unit is the coulomb (C). Electrons carry negative charge and protons carry positive charge. In ordinary conductors, current is mainly associated with the movement of electrons, although conventional current is defined in the direction positive charge would move.","example":"The magnitude of the elementary charge is approximately \\(1.602\\times10^{-19}\\,C\\). One coulomb corresponds to about \\(6.24\\times10^{18}\\) elementary charges."},
{"heading":"1.2 Electric current","body":"Current is the rate at which charge passes a cross-section: \\(I=\\frac{dQ}{dt}\\). For a constant current, \\(I=Q/t\\). The unit is the ampere (A), equivalent to one coulomb per second. Current is not consumed by a series component; energy is transferred to components while charge continues around a closed circuit.","example":"If 30 C passes a point in 10 s, the average current is \\(I=30/10=3\\,A\\)."},
{"heading":"1.3 Voltage and potential difference","body":"Voltage between two points is the work or energy transferred per unit charge: \\(V=W/Q\\). Its unit is the volt (V), equal to one joule per coulomb. A voltage source provides an energy difference that can drive current when a complete conductive path exists."},
{"heading":"1.4 Electrical energy and power","body":"Energy is measured in joules (J). Electrical power is the rate of energy transfer: \\(P=dW/dt\\). In a simple DC circuit, \\(P=VI\\). For a component obeying Ohm’s law, this can also be written as \\(P=I^2R\\) or \\(P=V^2/R\\)."},
{"heading":"1.5 Circuit model and units","body":"A basic circuit model contains a source, conductors, a load and a closed path. Use SI units consistently: charge in coulombs, current in amperes, voltage in volts, resistance in ohms, power in watts and energy in joules or kilowatt-hours. A kilowatt-hour is a unit of energy, not power."}
],
"key_points":["Current is charge flow per unit time.","Voltage is energy transferred per unit charge.","Power is the rate of energy transfer.","A circuit needs a complete path for sustained current.","Conventional current direction is opposite to electron drift in a metal conductor."],
"question":"A current of 2.5 A flows for 8 seconds. How much charge passes the point? Explain the difference between voltage and current.",
"answer":"Q = It = 2.5 × 8 = 20 C. Current describes the rate of charge flow; voltage describes energy transferred per unit charge.",
"references":["Hambley, Electrical Engineering: Principles and Applications — introductory electrical quantities.","IEC Electropedia (IEV): terminology for current, voltage, charge and power."]
},
{
"subject":"Electrical Fundamentals","level":"Basic","title":"2. Ohm’s Law and Resistance",
"duration":"25–35 minutes",
"intro":"Ohm’s law relates voltage, current and resistance for an ohmic element under specified physical conditions. It is a foundational circuit-analysis relationship, not a universal law for every device.",
"sections":[
{"heading":"2.1 The relationship","body":"For an ohmic resistor at constant physical conditions, voltage is proportional to current: \\(V=IR\\). Rearranging gives \\(I=V/R\\) and \\(R=V/I\\). Resistance is measured in ohms (Ω)."},
{"heading":"2.2 What affects resistance?","body":"For a uniform conductor, \\(R=\\rho L/A\\), where \\(\\rho\\) is resistivity (Ω·m), \\(L\\) is conductor length (m) and \\(A\\) is cross-sectional area (m²). A longer conductor generally has greater resistance; a larger cross-sectional area generally lowers resistance. Resistivity also depends on material and temperature.","example":"A conductor has resistivity \\(1.7\\times10^{-8}\\,Ω·m\\), length 10 m and area \\(2.0\\times10^{-6}\\,m²\\). Then \\(R=\\rho L/A=0.085\\,Ω\\) approximately."},
{"heading":"2.3 Worked circuit example","body":"A 12 V source is connected to a 6 Ω resistor. Assuming ideal source and resistor, the current is \\(I=V/R=12/6=2\\,A\\). Power dissipated is \\(P=VI=24\\,W\\). The resistor must be appropriately rated; the calculation alone does not confirm thermal suitability."},
{"heading":"2.4 Limits of Ohm’s law","body":"Incandescent lamps, diodes, transistors and many electrochemical devices do not have a constant resistance over all operating conditions. For nonlinear components, voltage-current curves or device models are needed. In AC circuits, impedance—not resistance alone—describes the opposition from resistance and reactance."}
],
"key_points":["V = IR for an ohmic element under specified conditions.","R = ρL/A for a uniform conductor.","Check component power ratings and temperature limits.","Do not assume every electrical device is ohmic."],
"question":"A 24 V supply is applied to a 8 Ω resistor. Calculate current and power.",
"answer":"I = V/R = 24/8 = 3 A. P = VI = 24 × 3 = 72 W. A real design must select a resistor with an appropriate power rating and thermal margin.",
"references":["Hambley, Electrical Engineering: Principles and Applications — resistive circuits.","IEC 60028: International standard of resistance for copper (for relevant material reference)."]
},
{
"subject":"Electrical Fundamentals","level":"Basic","title":"3. Series and Parallel Resistors",
"duration":"30–40 minutes",
"intro":"Series and parallel combinations allow larger circuits to be simplified into equivalent resistances. The defining test is whether components share the same current or the same voltage.",
"sections":[
{"heading":"3.1 Series circuits","body":"Components are in series when the same current flows through each component with no branching node between them. Equivalent resistance is \\(R_{eq}=R_1+R_2+\\cdots+R_n\\). The supply voltage divides among the resistors according to their resistance values."},
{"heading":"3.2 Parallel circuits","body":"Components are in parallel when they connect across the same two nodes and therefore have the same voltage. For resistors, \\(1/R_{eq}=1/R_1+1/R_2+\\cdots+1/R_n\\). For two resistors, \\(R_{eq}=R_1R_2/(R_1+R_2)\\). The equivalent resistance of positive resistors in parallel is lower than the smallest branch resistance."},
{"heading":"3.3 Worked series example","body":"Two resistors, 4 Ω and 8 Ω, are connected in series to 24 V. Equivalent resistance is 12 Ω and current is 24/12 = 2 A. Voltage drops are 8 V and 16 V respectively; their sum equals the source voltage."},
{"heading":"3.4 Worked parallel example","body":"Two resistors, 6 Ω and 3 Ω, are connected in parallel. \\(R_{eq}=6×3/(6+3)=2\\,Ω\\). With 12 V across the combination, total current is 12/2 = 6 A. Branch currents are 2 A through 6 Ω and 4 A through 3 Ω; their sum is 6 A."},
{"heading":"3.5 Practical reasoning","body":"Series arrangements are common in voltage dividers and some protective or sensing circuits; parallel arrangements are common where loads share a supply voltage. Actual installations require proper protective devices, conductor sizing and fault-current assessment."}
],
"key_points":["Series: same current; resistances add.","Parallel: same voltage; conductances add.","Check equivalent values against limiting cases.","Voltage-divider and current-divider results follow from Ohm’s law."],
"question":"Calculate the equivalent resistance of 10 Ω and 15 Ω in parallel.",
"answer":"Req = (10 × 15)/(10 + 15) = 150/25 = 6 Ω.",
"references":["Hambley, Electrical Engineering: Principles and Applications — resistive networks."]
},
{
"subject":"Electrical Fundamentals","level":"Intermediate","title":"4. Kirchhoff’s Current and Voltage Laws",
"duration":"30–40 minutes",
"intro":"Kirchhoff’s laws express conservation principles and form the basis of systematic circuit analysis.",
"sections":[
{"heading":"4.1 Kirchhoff’s Current Law (KCL)","body":"KCL states that the algebraic sum of currents at a node is zero. Equivalently, total current entering a node equals total current leaving it. This follows from conservation of charge for a node under the usual lumped-circuit assumptions."},
{"heading":"4.2 Kirchhoff’s Voltage Law (KVL)","body":"KVL states that the algebraic sum of voltage rises and drops around a closed loop is zero. This expresses energy conservation in a lumped circuit model. Sign conventions must be consistent as the loop is traversed."},
{"heading":"4.3 Node example","body":"A node receives 5 A and 1.5 A. One branch carries 4 A away. If the only other outgoing branch carries current I, KCL gives 5 + 1.5 = 4 + I, so I = 2.5 A."},
{"heading":"4.4 Loop example","body":"A 12 V source supplies two series resistors with drops V1 and V2. KVL gives +12 − V1 − V2 = 0, hence V1 + V2 = 12 V. If V1 is 4 V, then V2 is 8 V."},
{"heading":"4.5 Analysis workflow","body":"Choose reference ground and current directions; label node voltages and element polarities; write independent KCL or KVL equations; use component relationships such as V=IR; solve algebraically; then verify units, signs and power balance."}
],
"key_points":["KCL is based on charge conservation.","KVL is based on energy conservation in the circuit model.","A negative calculated current usually means the actual direction is opposite to the assumed reference.","Check the solution using power balance where practical."],
"question":"At a node, 8 A enters while 3 A and 2 A leave. Find the remaining outgoing current.",
"answer":"KCL: 8 = 3 + 2 + I, so I = 3 A leaving the node.",
"references":["Hambley, Electrical Engineering: Principles and Applications — circuit laws."]
},
{
"subject":"Electrical Fundamentals","level":"Intermediate","title":"5. AC Quantities, RMS and Power Factor",
"duration":"35–45 minutes",
"intro":"Alternating current changes with time. Sinusoidal steady-state analysis uses RMS quantities and phase relationships to describe voltage, current and power.",
"sections":[
{"heading":"5.1 Sinusoidal waveform","body":"A sinusoid can be written as \\(v(t)=V_m\\sin(\\omega t+\\phi)\\), where \\(V_m\\) is peak value, \\(\\omega=2\\pi f\\) is angular frequency, f is frequency in hertz and φ is phase angle. The period is \\(T=1/f\\)."},
{"heading":"5.2 RMS value","body":"RMS is the square root of the mean of the squared waveform over one period. For a pure sinusoid, \\(V_{rms}=V_m/\\sqrt{2}\\) and \\(I_{rms}=I_m/\\sqrt{2}\\). RMS allows resistive heating to be compared with an equivalent DC value. These peak-to-RMS relationships do not apply to every waveform."},
{"heading":"5.3 Real, reactive and apparent power","body":"For sinusoidal single-phase conditions, real power is \\(P=VI\\cos\\phi\\) watts, reactive power is \\(Q=VI\\sin\\phi\\) var and apparent power is \\(S=VI\\) VA. The power factor is \\(PF=P/S\\); for sinusoidal voltage and current it equals cos φ. Distorted waveforms can require a more careful power-factor definition."},
{"heading":"5.4 Worked example","body":"A single-phase load uses 230 V RMS, 5 A RMS and power factor 0.8. Real power is \\(P=230×5×0.8=920\\,W\\). Apparent power is 1150 VA. The remaining relationship is \\(S^2=P^2+Q^2\\) for sinusoidal conditions."},
{"heading":"5.5 Safety and measurement","body":"Use an instrument rated for the circuit category, voltage and environment. Never assume a circuit is de-energized from a switch position alone. Isolation and verification must follow approved procedures and be performed by qualified personnel."}
],
"key_points":["Frequency and period are reciprocals.","For a sine wave only, RMS = peak/√2.","Real power performs useful work or produces heat.","Power factor describes how effectively apparent power is converted to real power under the stated definitions."],
"question":"A 230 V RMS load draws 4 A at 0.75 power factor. Calculate real power.",
"answer":"P = VI PF = 230 × 4 × 0.75 = 690 W, assuming the stated power-factor definition is appropriate.",
"references":["Hambley, Electrical Engineering: Principles and Applications — AC circuits and power."]
},
{
"subject":"Electrical Safety & Standards","level":"Basic","title":"1. Electrical Risk Awareness and Safe Work Principles",
"duration":"20–30 minutes",
"intro":"Electrical hazards can cause serious injury, fire and equipment damage. Engineering competence includes recognizing when work must stop and be transferred to qualified personnel.",
"sections":[
{"heading":"1.1 Recognize hazards","body":"Common hazards include electric shock, arc flash, burns, fire, unexpected motor start, stored energy in capacitors and backfeed from alternate sources. Risk depends on voltage, available fault current, exposure time, environment, equipment condition and the task."},
{"heading":"1.2 Safe work planning","body":"Use the approved site procedure, risk assessment and permit system where required. Identify all energy sources, isolate them using approved means, prevent re-energization, and verify the safe state with correctly rated test equipment and the required proving process. A control switch alone is not reliable isolation."},
{"heading":"1.3 Protection is layered","body":"Protective earthing, overcurrent protection, residual-current protection, insulation, enclosures, barriers, equipment ratings and safe work practices serve different purposes. No single device makes every electrical task safe."},
{"heading":"1.4 Stop-work conditions","body":"Stop and contact a qualified supervisor if drawings do not match the installation, isolation is uncertain, equipment is damaged, the environment is wet or hazardous beyond the procedure, or the task exceeds your training and authorization."}
],
"key_points":["Never work on live equipment unless a formally approved, legally permitted procedure specifically requires it and qualified controls are in place.","Verify isolation; do not rely only on labels, indicator lights or switch position.","Use correctly rated equipment and follow site rules and applicable standards.","Training material does not replace authorization, supervision or a formal risk assessment."],
"question":"Why is operating a switch not sufficient proof that a circuit is safe to touch?",
"answer":"A switch may not isolate every source, may be faulty or incorrectly labelled, and the circuit may have stored energy or backfeed. An approved isolation and verification procedure is required.",
"references":["Applicable local electrical regulations and workplace safety procedures.","Relevant current IEC/IEEE standards and manufacturer instructions."],
"safety":"This lesson is awareness training, not authorization to perform electrical work. Follow local laws, approved procedures and qualified supervision."
},
{
"subject":"Electrical Machines","level":"Intermediate","title":"1. Transformer Operating Principle",
"duration":"30–40 minutes",
"intro":"A transformer transfers AC energy between windings through a changing magnetic flux. It can change voltage and current levels while frequency remains the same.",
"sections":[
{"heading":"1.1 Mutual induction","body":"AC in the primary winding creates changing magnetic flux in the core. The changing flux links the secondary winding and induces an EMF according to Faraday’s law. A transformer needs changing flux for sustained transformer action; a conventional transformer must not be connected directly to a DC supply."},
{"heading":"1.2 Ideal turns ratio","body":"For an ideal transformer, \\(V_p/V_s=N_p/N_s\\). Current ratio is inverse: \\(I_p/I_s=N_s/N_p\\), with input power approximately equal to output power. Real transformers have winding resistance, leakage flux, core losses and magnetizing current."},
{"heading":"1.3 Worked example","body":"An ideal transformer has 1000 primary turns and 100 secondary turns. If the primary voltage is 230 V AC, secondary voltage is \\(230×100/1000=23\\,V\\). Actual output varies with regulation and load."},
{"heading":"1.4 Losses and ratings","body":"Copper losses are associated with winding resistance; core losses include hysteresis and eddy-current effects. Nameplate kVA, frequency, cooling, insulation class, impedance and temperature limits are important when selecting and operating equipment."}
],
"key_points":["Transformer action relies on changing magnetic flux.","Ideal voltage ratio follows turns ratio.","Ideal current ratio is inverse to turns ratio.","Never assume an ideal calculation alone establishes a safe transformer design."],
"question":"A transformer has a 5:1 primary-to-secondary turns ratio and 200 V applied to the primary. Find ideal secondary voltage.",
"answer":"Vs = Vp × Ns/Np = 200 × 1/5 = 40 V AC.",
"references":["Chapman, Electric Machinery Fundamentals — transformers.","Manufacturer transformer nameplate and installation documentation."]
},
{
"subject":"Power Systems","level":"Intermediate","title":"1. Three-Phase Power Fundamentals",
"duration":"30–40 minutes",
"intro":"Three-phase systems use three sinusoidal quantities separated by 120 electrical degrees. They are widely used for generation, transmission and industrial loads.",
"sections":[
{"heading":"1.1 Balanced system","body":"In a balanced system, phase magnitudes are equal and phase angles are separated by 120°. Balanced three-phase loads simplify power calculations and often produce nearly constant total instantaneous power."},
{"heading":"1.2 Star and delta relationships","body":"For a balanced star (wye) connection, line voltage is \\(\\sqrt{3}\\) times phase voltage and line current equals phase current. For a balanced delta connection, line voltage equals phase voltage and line current is \\(\\sqrt{3}\\) times phase current."},
{"heading":"1.3 Three-phase power","body":"For a balanced system using line-to-line RMS voltage and line RMS current, apparent power is \\(S=\\sqrt{3}V_LI_L\\). Real power is \\(P=\\sqrt{3}V_LI_LPF\\) when the power-factor definition applies."},
{"heading":"1.4 Worked example","body":"A balanced 400 V line-to-line system draws 10 A at PF 0.85. Approximate real power is \\(P=1.732×400×10×0.85≈5.89\\,kW\\). Confirm the system is balanced and the measured values are appropriate before using this simplified calculation."}
],
"key_points":["Phase quantities and line quantities are not interchangeable.","The √3 formulas assume a balanced three-phase system.","Power factor and harmonics affect system performance.","Correct instrument category and safe measurement procedures are essential."],
"question":"A balanced 400 V three-phase load draws 8 A at 0.9 power factor. Estimate real power.",
"answer":"P ≈ √3 × 400 × 8 × 0.9 ≈ 4.99 kW.",
"references":["Glover, Overbye and Sarma, Power System Analysis and Design."]
},
{
"subject":"Industrial Automation & Control","level":"Basic","title":"1. PLC Architecture and Scan Cycle",
"duration":"25–35 minutes",
"intro":"A Programmable Logic Controller (PLC) is an industrial controller designed to read inputs, execute a user program and update outputs predictably.",
"sections":[
{"heading":"1.1 Main hardware","body":"A typical PLC system includes a power supply, CPU, memory, input modules, output modules and communication interfaces. Inputs may come from pushbuttons, limit switches or sensors; outputs may drive interface relays, contactors or other approved devices."},
{"heading":"1.2 Typical scan cycle","body":"A simplified scan reads input states, executes the program, updates outputs and performs housekeeping/communications. Real PLCs can support interrupts, tasks and process-image variations, so consult the model-specific manual."},
{"heading":"1.3 Interlocks and fail-safe design","body":"Interlocks prevent incompatible commands and help coordinate sequences. Safety-related functions require appropriately designed and rated safety systems; ordinary PLC logic must not be assumed to provide a certified safety function."},
{"heading":"1.4 Example sequence","body":"A motor start request may be accepted only when the guard status, overload status and stop circuit are healthy. In a real system, safety functions and hardwired protections must be designed according to risk assessment and relevant standards; this simplified example is conceptual only."}
],
"key_points":["Know the exact PLC model and its documentation.","Separate ordinary process control from safety-related control.","Document I/O, interlocks, fault states and recovery behavior.","Test programs in simulation or a controlled environment before commissioning."],
"question":"What are the main stages of a simplified PLC scan?",
"answer":"Read inputs, execute the user program, update outputs, then perform communications and housekeeping; exact behavior depends on the PLC and task configuration.",
"references":["Petruzella, Programmable Logic Controllers.","Official PLC manufacturer programming and hardware manuals."]
},
{
"subject":"Renewable Energy","level":"Basic","title":"1. Photovoltaic System Fundamentals",
"duration":"25–35 minutes",
"intro":"Photovoltaic (PV) modules convert part of incident sunlight into DC electrical energy. A practical PV system combines modules with suitable conversion, protection, mounting and monitoring equipment.",
"sections":[
{"heading":"1.1 Cell, module and array","body":"PV cells are connected into modules; modules are connected in series to increase voltage or in parallel to increase current, within equipment limits. Shading, temperature, orientation and irradiance affect output."},
{"heading":"1.2 Maximum power point","body":"A PV module has a nonlinear current-voltage curve. Maximum power point tracking (MPPT) adjusts the operating point to extract available power as conditions change. The inverter or charge controller implements the relevant control strategy."},
{"heading":"1.3 Energy estimate","body":"A rough daily energy estimate may use installed peak power multiplied by equivalent peak-sun-hours and a performance ratio. It is an estimate, not a guarantee; seasonal weather, shading, system losses and equipment limits matter."},
{"heading":"1.4 Safety and system design","body":"PV strings can remain energized in daylight. Correct DC-rated isolation, overcurrent protection where required, connector compatibility, earthing/bonding, surge protection and code-compliant installation are critical. Design and installation should be performed by qualified people."}
],
"key_points":["PV modules produce DC power.","Series connections increase voltage; parallel connections increase current.","MPPT helps operate near the maximum-power point.","PV design requires local code compliance and DC-specific safety controls."],
"question":"What does MPPT mean, and why is it useful?",
"answer":"Maximum Power Point Tracking. It adjusts the electrical operating point so a PV system can extract power near the module/array's maximum-power point as sunlight and temperature change.",
"references":["PV equipment manufacturer datasheets and installation manuals.","Applicable current electrical and grid-connection standards."]
}
]

QUIZ_BANK = {
    "Electrical Fundamentals": [
        {"question":"Which quantity is measured in amperes?","options":["Voltage","Current","Resistance","Energy"],"answer":"Current","explanation":"Current is the rate of charge flow and is measured in amperes."},
        {"question":"A 12 V supply is applied across 4 Ω. What is the ideal current?","options":["0.33 A","3 A","16 A","48 A"],"answer":"3 A","explanation":"Ohm's law gives I = V/R = 12/4 = 3 A."},
        {"question":"What is the equivalent resistance of 6 Ω and 3 Ω in parallel?","options":["9 Ω","4.5 Ω","2 Ω","18 Ω"],"answer":"2 Ω","explanation":"Req = (6×3)/(6+3) = 2 Ω."},
        {"question":"A 2 A current flows for 5 seconds. Charge transferred is:","options":["2.5 C","7 C","10 C","20 C"],"answer":"10 C","explanation":"Q = It = 2×5 = 10 C."},
    ],
    "Power Systems": [
        {"question":"For a balanced three-phase system, the common real-power formula is:","options":["P = V/I","P = √3 VL IL PF","P = I/R","P = f/T"],"answer":"P = √3 VL IL PF","explanation":"This uses line-to-line RMS voltage and line RMS current for a balanced system."},
        {"question":"What does power factor relate?","options":["Real power to apparent power","Voltage to resistance only","Frequency to period","Charge to time"],"answer":"Real power to apparent power","explanation":"PF = P/S under the relevant power definitions."},
    ],
    "Electrical Safety": [
        {"question":"Does switching a circuit off always prove it is safe to touch?","options":["Yes","No"],"answer":"No","explanation":"Approved isolation and verification are required; alternate supplies and stored energy may exist."},
        {"question":"What should you do if you are not trained or authorized for a task?","options":["Try carefully","Stop and seek qualified supervision","Use a smaller tool","Ignore the procedure"],"answer":"Stop and seek qualified supervision","explanation":"Work must remain within training, authorization and approved procedures."},
    ]
}
