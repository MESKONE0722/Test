import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="RI DOC Written Test",
    page_icon="📋",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .stRadio > label {
        font-weight: 600;
        font-size: 16px;
        color: #1e293b;
    }
    
    div[data-testid="stMarkdownContainer"] p {
        font-size: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Test questions database (all 50 questions)
questions = {
    # SECTION 1: READING COMPREHENSION
    1: {
        "section": "Reading Comprehension",
        "passage": "The Rhode Island Department of Corrections (RIDOC) maintains strict protocols for inmate movement within facilities. All inmates must be accounted for during shift changes. Officers are required to conduct a standing count at 6:00 AM, 12:00 PM, 6:00 PM, and 10:00 PM daily. During count times, all inmates must be visible in their assigned areas. Any discrepancies must be reported immediately to the shift supervisor.",
        "question": "According to the passage, how many standing counts are conducted daily?",
        "options": ["Two", "Three", "Four", "Five"],
        "correct": "Four"
    },
    2: {
        "section": "Reading Comprehension",
        "question": "What must be done if there is a discrepancy during count?",
        "options": ["Wait until the next count to verify", "Report immediately to the shift supervisor", "Conduct a recount with another officer", "Document it in the daily log"],
        "correct": "Report immediately to the shift supervisor"
    },
    3: {
        "section": "Reading Comprehension",
        "question": "Which of the following is NOT required when logging inmate movement?",
        "options": ["Inmate's ID number", "Escorting officer's signature", "Reason for movement", "Time of movement"],
        "correct": "Reason for movement"
    },
    4: {
        "section": "Reading Comprehension",
        "passage": "Use of force within correctional facilities must follow established guidelines. Officers may only use the minimum force necessary to maintain safety and security. All use of force incidents must be documented within two hours of the occurrence. Documentation must include a detailed description of the events leading to the use of force, the type of force applied, the duration, and the outcome.",
        "question": "According to the passage, when must use of force incidents be documented?",
        "options": ["Within one hour", "Within two hours", "By end of shift", "Within 24 hours"],
        "correct": "Within two hours"
    },
    5: {
        "section": "Reading Comprehension",
        "question": "Medical evaluation following use of force is:",
        "options": ["Optional if no injuries are visible", "Required only for inmates", "Required only for officers", "Mandatory for all parties involved"],
        "correct": "Mandatory for all parties involved"
    },
    
    # SECTION 2: WRITTEN EXPRESSION & GRAMMAR
    6: {
        "section": "Written Expression & Grammar",
        "question": "Which sentence is grammatically correct?",
        "options": ["The officer and supervisor was reviewing the report.", "The officer and supervisor were reviewing the report.", "The officer and supervisor is reviewing the report.", "The officer and supervisor be reviewing the report."],
        "correct": "The officer and supervisor were reviewing the report."
    },
    7: {
        "section": "Written Expression & Grammar",
        "question": "Choose the sentence with correct punctuation:",
        "options": ["The inmate refused to comply, therefore force was necessary.", "The inmate refused to comply therefore, force was necessary.", "The inmate refused to comply; therefore, force was necessary.", "The inmate refused to comply therefore force was necessary."],
        "correct": "The inmate refused to comply; therefore, force was necessary."
    },
    8: {
        "section": "Written Expression & Grammar",
        "question": "Which word is spelled correctly?",
        "options": ["Occurence", "Occurance", "Occurrence", "Ocurrence"],
        "correct": "Occurrence"
    },
    9: {
        "section": "Written Expression & Grammar",
        "question": "Select the clearest way to write this report entry:",
        "options": ["Inmate Smith was seen by me walking in unauthorized area at 14:30 hours.", "I observed Inmate Smith walking in an unauthorized area at 14:30 hours.", "Walking in unauthorized area, Inmate Smith was at 14:30 hours.", "At 14:30 hours in unauthorized area Inmate Smith was walking."],
        "correct": "I observed Inmate Smith walking in an unauthorized area at 14:30 hours."
    },
    10: {
        "section": "Written Expression & Grammar",
        "question": "Which sentence uses the correct verb tense?",
        "options": ["Officer Jones will submitted the report yesterday.", "Officer Jones has submit the report yesterday.", "Officer Jones submitted the report yesterday.", "Officer Jones submitting the report yesterday."],
        "correct": "Officer Jones submitted the report yesterday."
    },
    
    # SECTION 3: MATHEMATICS
    11: {
        "section": "Mathematics",
        "question": "A housing unit has 48 inmates. If 12 inmates are at medical appointments, how many remain in the unit?",
        "options": ["34", "36", "38", "40"],
        "correct": "36"
    },
    12: {
        "section": "Mathematics",
        "question": "During breakfast service, 156 inmates were fed. If each meal costs $2.75, what is the total cost?",
        "options": ["$419.00", "$427.00", "$429.00", "$431.00"],
        "correct": "$429.00"
    },
    13: {
        "section": "Mathematics",
        "question": "An officer works 8-hour shifts for 5 days per week. How many hours does the officer work in 4 weeks?",
        "options": ["120 hours", "140 hours", "160 hours", "180 hours"],
        "correct": "160 hours"
    },
    14: {
        "section": "Mathematics",
        "question": "The facility has 425 inmates. If 68% are enrolled in educational programs, approximately how many inmates are in these programs?",
        "options": ["275", "289", "298", "310"],
        "correct": "289"
    },
    15: {
        "section": "Mathematics",
        "question": "What is the total current population? Unit A: 68, Unit B: 57, Unit C: 74, Unit D: 48",
        "options": ["245", "247", "249", "265"],
        "correct": "247"
    },
    
    # SECTION 4: SITUATIONAL JUDGMENT
    16: {
        "section": "Situational Judgment",
        "passage": "You observe two inmates engaged in a heated verbal argument in the dayroom. The argument is escalating but has not become physical. Other inmates are watching.",
        "question": "What is your MOST appropriate initial response?",
        "options": ["Immediately call for backup and wait", "Approach calmly and order both inmates to separate", "Ignore it unless it becomes physical", "Remove all other inmates from the area first"],
        "correct": "Approach calmly and order both inmates to separate"
    },
    17: {
        "section": "Situational Judgment",
        "question": "After separating the inmates, you should:",
        "options": ["Allow them to return to their activities", "Document the incident and report to your supervisor", "Place both in segregation immediately", "Conduct a thorough search of both inmates"],
        "correct": "Document the incident and report to your supervisor"
    },
    18: {
        "section": "Situational Judgment",
        "passage": "During your shift, you notice an inmate appears to be having a medical emergency. The inmate is clutching his chest and having difficulty breathing.",
        "question": "What is your FIRST action?",
        "options": ["Call for medical assistance immediately", "Attempt to determine what caused the problem", "Move the inmate to the medical unit", "Ask other inmates what happened"],
        "correct": "Call for medical assistance immediately"
    },
    19: {
        "section": "Situational Judgment",
        "question": "While waiting for medical staff, you should:",
        "options": ["Try to make the inmate comfortable and monitor vital signs if trained", "Leave the area to avoid interfering", "Search the inmate for contraband", "Secure all other inmates in their cells"],
        "correct": "Try to make the inmate comfortable and monitor vital signs if trained"
    },
    20: {
        "section": "Situational Judgment",
        "passage": "A new inmate approaches you and claims that another inmate threatened to assault him if he doesn't give up his commissary items.",
        "question": "Your immediate response should be:",
        "options": ["Tell the inmate to handle it himself", "Take the complaint seriously and investigate", "Move the complaining inmate to a different unit immediately", "Confront the alleged threatening inmate"],
        "correct": "Take the complaint seriously and investigate"
    },
    21: {
        "section": "Situational Judgment",
        "question": "When documenting this complaint, you should include:",
        "options": ["Only the names of both inmates", "Detailed account of the complaint, names, location, time, and witnesses", "Your opinion on whether the threat is credible", "Recommendations for disciplinary action"],
        "correct": "Detailed account of the complaint, names, location, time, and witnesses"
    },
    22: {
        "section": "Policy Application",
        "passage": "Policy: Contraband includes weapons, drugs, alcohol, unauthorized medications, electronic devices, excess food items, altered clothing, and currency exceeding $20.",
        "question": "Which item is NOT automatically considered contraband?",
        "options": ["A homemade knife", "$15 in cash", "A modified cell phone charger", "Prescription medication not prescribed to the inmate"],
        "correct": "$15 in cash"
    },
    23: {
        "section": "Policy Application",
        "question": "What is the correct order of actions when contraband is discovered?",
        "options": ["Notify supervisor → Secure item → Document → Photograph", "Photograph → Secure item → Document → Notify supervisor", "Secure item → Photograph → Document → Notify supervisor", "Document → Secure item → Notify supervisor → Photograph"],
        "correct": "Secure item → Photograph → Document → Notify supervisor"
    },
    24: {
        "section": "Policy Application",
        "question": "An inmate requests to speak with you privately. You should:",
        "options": ["Refuse private conversations with inmates", "Allow it but remain in view of cameras or other officers", "Grant the request in a completely private location", "Require a written request first"],
        "correct": "Allow it but remain in view of cameras or other officers"
    },
    25: {
        "section": "Policy Application",
        "question": "You witness another officer using excessive force on a compliant inmate. Your responsibility is to:",
        "options": ["Ignore it to maintain staff solidarity", "Report the incident through proper channels", "Confront the officer privately after shift", "Discuss it with other officers first"],
        "correct": "Report the incident through proper channels"
    },
    26: {
        "section": "Memory & Observation",
        "passage": "Incident: Nov 15, 2024, 14:45 hours, Housing Unit C. Inmate Marcus Johnson ID# 2024-1567. Modified plastic knife found, 6 inches. Officer Sarah Williams Badge #342 discovered it.",
        "question": "What was the inmate's ID number?",
        "options": ["2023-1567", "2024-1567", "2024-1576", "2023-0892"],
        "correct": "2024-1567"
    },
    27: {
        "section": "Memory & Observation",
        "question": "Who discovered the contraband?",
        "options": ["Officer David Chen", "Officer Sarah Williams", "Both officers together", "Inmate Thomas Rivera"],
        "correct": "Officer Sarah Williams"
    },
    28: {
        "section": "Memory & Observation",
        "question": "What was the length of the contraband item?",
        "options": ["4 inches", "5 inches", "6 inches", "7 inches"],
        "correct": "6 inches"
    },
    29: {
        "section": "Additional Scenarios",
        "question": "You find what appears to be a love letter from another staff member to an inmate. What should you do?",
        "options": ["Destroy the letter to protect the staff member", "Return the letter and pretend you never saw it", "Secure the letter and report it to your supervisor", "Confront the staff member directly"],
        "correct": "Secure the letter and report it to your supervisor"
    },
    30: {
        "section": "Additional Scenarios",
        "question": "During count, you notice an inmate is missing from his assigned cell. You should:",
        "options": ["Check common areas before reporting", "Immediately notify the control center and supervisor", "Wait until the next count to see if he returns", "Ask other inmates where he might be"],
        "correct": "Immediately notify the control center and supervisor"
    },
    31: {
        "section": "Additional Scenarios",
        "question": "An inmate offers you a handmade card thanking you for your professionalism. You should:",
        "options": ["Accept it as it's just a card", "Politely decline and explain you cannot accept gifts", "Accept it but don't tell anyone", "Report the inmate for attempted bribery"],
        "correct": "Politely decline and explain you cannot accept gifts"
    },
    32: {
        "section": "Additional Scenarios",
        "question": "You smell marijuana smoke coming from a cell. The MOST appropriate action is:",
        "options": ["Ignore it unless you see physical evidence", "Conduct an immediate search of the cell and secure any contraband", "Wait until your supervisor arrives to investigate", "Ask the inmate to dispose of it"],
        "correct": "Conduct an immediate search of the cell and secure any contraband"
    },
    33: {
        "section": "Additional Scenarios",
        "question": "An inmate claims he needs to call his lawyer immediately. You should:",
        "options": ["Deny the request as it's not your responsibility", "Verify proper procedures and facilitate the call according to policy", "Tell him to submit a request form and wait", "Allow him to use your personal phone"],
        "correct": "Verify proper procedures and facilitate the call according to policy"
    },
    34: {
        "section": "Logical Reasoning",
        "question": "If all correctional officers must complete annual firearms training, and Officer Martinez is a correctional officer, then:",
        "options": ["Officer Martinez completed firearms training last year", "Officer Martinez must complete annual firearms training", "Officer Martinez is qualified to train others", "Officer Martinez carries a firearm daily"],
        "correct": "Officer Martinez must complete annual firearms training"
    },
    35: {
        "section": "Logical Reasoning",
        "question": "Security rounds must be completed every 30 minutes. If rounds begin at 08:00, what time should the fifth round be completed?",
        "options": ["09:30", "10:00", "10:30", "11:00"],
        "correct": "10:00"
    },
    36: {
        "section": "Logical Reasoning",
        "question": "Three inmates scheduled for court: A at 09:00, B at 09:30, C at 10:00. Transport takes 20 min each way. Leave at 08:30 for A. Earliest return from all three?",
        "options": ["11:00", "11:20", "11:40", "12:00"],
        "correct": "11:40"
    },
    37: {
        "section": "Report Writing",
        "question": "Which report entry is most professional and complete?",
        "options": ["Inmate was acting weird so I checked on him.", "At 1530 hours I observed Inmate Jackson #2045 pacing rapidly. Upon welfare check, inmate appeared agitated and reported hearing voices.", "Jackson was crazy again today.", "Checked on inmate. He's fine."],
        "correct": "At 1530 hours I observed Inmate Jackson #2045 pacing rapidly. Upon welfare check, inmate appeared agitated and reported hearing voices."
    },
    38: {
        "section": "Report Writing",
        "question": "When documenting an incident, you should always include:",
        "options": ["Your opinion on the inmate's character", "Rumors you heard about the incident", "Objective facts: who, what, when, where, and how", "Predictions about future behavior"],
        "correct": "Objective facts: who, what, when, where, and how"
    },
    39: {
        "section": "Ethics & Professional Conduct",
        "question": "A local news reporter contacts you asking about a high-profile inmate. You should:",
        "options": ["Provide basic public information only", "Refer them to the Public Information Officer", "Share what you know to maintain good community relations", "Tell them you cannot comment and hang up"],
        "correct": "Refer them to the Public Information Officer"
    },
    40: {
        "section": "Ethics & Professional Conduct",
        "question": "You realize you made an error in an incident report you submitted yesterday. You should:",
        "options": ["Hope no one notices", "Submit a supplemental report correcting the error", "Destroy the original and rewrite it", "Wait to see if anyone questions it"],
        "correct": "Submit a supplemental report correcting the error"
    },
    41: {
        "section": "Ethics & Professional Conduct",
        "question": "An inmate offers information about contraband in exchange for special privileges. You should:",
        "options": ["Accept the deal to maintain security", "Accept the information but provide nothing in return", "Report the conversation and the information through proper channels", "Ignore the inmate completely"],
        "correct": "Report the conversation and the information through proper channels"
    },
    42: {
        "section": "Emergency Procedures",
        "question": "During a facility lockdown, your primary responsibility is to:",
        "options": ["Secure your assigned area and maintain accountability of inmates", "Help other officers in different areas", "Investigate the cause of the lockdown", "Prepare incident reports"],
        "correct": "Secure your assigned area and maintain accountability of inmates"
    },
    43: {
        "section": "Emergency Procedures",
        "question": "An inmate requests a vegetarian meal for religious reasons. You should:",
        "options": ["Deny it as special requests aren't allowed", "Direct the inmate to proper procedures for religious accommodation requests", "Provide it immediately without documentation", "Tell them to discuss it with other inmates"],
        "correct": "Direct the inmate to proper procedures for religious accommodation requests"
    },
    44: {
        "section": "Emergency Procedures",
        "question": "You notice damage to facility equipment during your shift. You should:",
        "options": ["Report it only if asked", "Document and report it immediately", "Try to repair it yourself", "Wait to see if anyone else reports it"],
        "correct": "Document and report it immediately"
    },
    45: {
        "section": "Professional Boundaries",
        "question": "Which behavior demonstrates professional boundaries?",
        "options": ["Sharing personal social media with inmates", "Maintaining appropriate emotional distance while being respectful", "Becoming friends with certain inmates", "Ignoring inmate communications entirely"],
        "correct": "Maintaining appropriate emotional distance while being respectful"
    },
    46: {
        "section": "Emergency Priorities",
        "question": "Rank priority during emergency evacuation: 1.Secure contraband 2.Ensure inmate accountability 3.Check cells 4.Gather belongings. Correct order:",
        "options": ["2, 3, 4, 1", "3, 2, 1, 4", "2, 1, 3, 4", "4, 3, 2, 1"],
        "correct": "3, 2, 1, 4"
    },
    47: {
        "section": "Complaint Handling",
        "question": "An inmate claims another officer was verbally abusive. Your responsibility is to:",
        "options": ["Dismiss it as an inmate trying to cause trouble", "Document the complaint and report it through proper channels", "Tell the inmate to file a formal grievance", "Discuss it with the accused officer first"],
        "correct": "Document the complaint and report it through proper channels"
    },
    48: {
        "section": "Communication Skills",
        "question": "When communicating with inmates, you should:",
        "options": ["Be authoritative but professional and respectful", "Be friendly and casual", "Avoid communication unless absolutely necessary", "Use intimidation to maintain control"],
        "correct": "Be authoritative but professional and respectful"
    },
    49: {
        "section": "Chain of Command",
        "question": "The chain of command is important because it:",
        "options": ["Makes sure everyone knows who is in charge", "Ensures proper communication and accountability", "Prevents inmates from manipulating staff", "Reduces paperwork"],
        "correct": "Ensures proper communication and accountability"
    },
    50: {
        "section": "Core Values",
        "question": "The most important quality for a correctional officer is:",
        "options": ["Physical strength", "Integrity and ethical conduct", "Ability to make friends with inmates", "Willingness to work overtime"],
        "correct": "Integrity and ethical conduct"
    }
}

# Header
st.markdown("""
<div class="main-header">
    <h1>Rhode Island Department of Corrections</h1>
    <h2>Written Examination - Practice Test</h2>
    <p>50 Questions | 70% Passing Score (35 correct) | 90 Minutes</p>
</div>
""", unsafe_allow_html=True)

# Sidebar with progress
with st.sidebar:
    st.header("📊 Test Progress")
    answered = len(st.session_state.answers)
    st.metric("Questions Answered", f"{answered}/50")
    st.progress(answered / 50)
    
    st.markdown("---")
    st.subheader("⏱️ Test Info")
    st.info("**Duration:** 90 minutes\n\n**Passing Score:** 35/50 (70%)\n\n**Sections:**\n- Reading Comprehension\n- Grammar\n- Mathematics\n- Situational Judgment\n- Policy Application\n- Ethics & Professional Conduct")
    
    if answered == 50 and not st.session_state.submitted:
        st.success("✅ All questions answered! Ready to submit.")

# Main test area
if not st.session_state.submitted:
    # Display questions
    current_section = ""
    for q_num in range(1, 51):
        q = questions[q_num]
        
        # Section header
        if q["section"] != current_section:
            current_section = q["section"]
            st.markdown(f"## 📋 Section: {current_section}")
            st.markdown("---")
        
        # Passage if exists
        if "passage" in q and q["passage"]:
            st.info(f"**Passage/Scenario:** {q['passage']}")
        
        # Question
        st.markdown(f"### Question {q_num}")
        st.markdown(f"**{q['question']}**")
        
        # Answer options
        answer = st.radio(
            f"Select your answer for Question {q_num}:",
            options=q["options"],
            key=f"q{q_num}",
            index=None,
            label_visibility="collapsed"
        )
        
        if answer:
            st.session_state.answers[q_num] = answer
        
        st.markdown("---")
    
    # Submit button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("📤 Submit Test", type="primary", use_container_width=True, disabled=(answered < 50)):
            if answered == 50:
                st.session_state.submitted = True
                st.rerun()
            else:
                st.error(f"Please answer all questions. {50 - answered} remaining.")

else:
    # Calculate score
    correct_count = 0
    for q_num, answer in st.session_state.answers.items():
        if answer == questions[q_num]["correct"]:
            correct_count += 1
    
    percentage = (correct_count / 50) * 100
    passed = correct_count >= 35
    
    # Results display
    st.balloons() if passed else None
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if passed:
            st.success("## 🎉 CONGRATULATIONS - YOU PASSED!")
        else:
            st.error("## ❌ TEST NOT PASSED")
        
        st.metric("Your Score", f"{correct_count}/50")
        st.metric("Percentage", f"{percentage:.1f}%")
        st.metric("Result", "PASS ✅" if passed else "FAIL ❌")
        
        if passed:
            st.success(f"You correctly answered {correct_count} out of 50 questions ({percentage:.1f}%). The passing score is 70% (35 correct answers).")
        else:
            st.warning(f"You answered {correct_count} out of 50 questions correctly ({percentage:.1f}%). You need 35 correct answers (70%) to pass.")
    
    st.markdown("---")
    
    # Detailed results
    st.subheader("📊 Detailed Results by Section")
    
    sections = {}
    for q_num in range(1, 51):
        section = questions[q_num]["section"]
        if section not in sections:
            sections[section] = {"correct": 0, "total": 0}
        sections[section]["total"] += 1
        if st.session_state.answers.get(q_num) == questions[q_num]["correct"]:
            sections[section]["correct"] += 1
    
    for section, stats in sections.items():
        pct = (stats["correct"] / stats["total"]) * 100
        st.write(f"**{section}:** {stats['correct']}/{stats['total']} ({pct:.0f}%)")
    
    st.markdown("---")
    
    # Show incorrect answers
    with st.expander("📝 Review Incorrect Answers"):
        for q_num in range(1, 51):
            user_answer = st.session_state.answers.get(q_num)
            correct_answer = questions[q_num]["correct"]
            
            if user_answer != correct_answer:
                st.markdown(f"**Question {q_num}:** {questions[q_num]['question']}")
                st.markdown(f"❌ Your answer: {user_answer}")
                st.markdown(f"✅ Correct answer: {correct_answer}")
                st.markdown("---")
    
    # Restart button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 Restart Test", type="primary", use_container_width=True):
            st.session_state.answers = {}
            st.session_state.submitted = False
            st.rerun()
