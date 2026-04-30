import json

def generate_variations(base_questions, answer):
    pairs = []
    for q in base_questions:
        pairs.append({"question": q, "answer": answer})
    return pairs

data = []

# 1. Address
addr_questions = [
    "what is the college address?", "where is the college located?", "college location",
    "how to reach college?", "address of kpriet", "where is kpriet?",
    "give me the address of your college", "where exactly is kpriet located?",
    "tell me the location of the college", "college map location", "where is it?",
    "i need the college address", "what's your location?", "address please"
]
addr_answer = "The college is located at: KPR Institute of Engineering and Technology, Arasur, Coimbatore."
data.extend(generate_variations(addr_questions, addr_answer))

# 2. Phone / Contact
contact_questions = [
    "what is the contact number?", "how can i contact the college?", "phone number",
    "give me the college phone number", "who should i call for admission?",
    "contact details", "helpline number", "admission contact number",
    "what are the contact numbers?", "telephone number", "is there a number i can call?",
    "mobile number of kpriet", "how to call kpriet?", "contact info"
]
contact_answer = "You can contact the college at: 75488 88444 or 75488 88555."
data.extend(generate_variations(contact_questions, contact_answer))

# 3. Fees
fees_questions = [
    "what is the fee structure?", "how much is the tuition fee?", "college fees",
    "fees details", "how much does it cost to study here?", "hostel fee structure",
    "what are the fees for btech?", "tell me about the fee", "what's the cost?",
    "yearly fee", "semester fee", "can you provide the fee structure?",
    "is the fee high?", "admission fees"
]
fees_answer = "The fee structure varies by department and admission quota (Government/Management). Please contact the admission office at 75488 88444 for detailed fee information."
data.extend(generate_variations(fees_questions, fees_answer))

# 4. Placements
placement_questions = [
    "how are the placements?", "placement records", "highest package",
    "which companies visit for placements?", "average package",
    "tell me about placement", "do you provide placement?", "placement percentage",
    "top recruiters", "is placement good here?", "will i get a job?",
    "placement statistics", "how many students got placed?", "placement cell"
]
placement_answer = "KPRIET has an excellent placement record with top recruiters like TCS, CTS, Wipro, and Infosys visiting the campus. The placement cell provides extensive training. For detailed statistics, visit the official website."
data.extend(generate_variations(placement_questions, placement_answer))

# 5. MBA
mba_questions = [
    "do you offer mba?", "is mba available in kpriet?", "mba course",
    "details about mba", "mba fee structure", "mba admission",
    "how is mba here?", "tell me about management studies", "pg courses mba"
]
mba_answer = "Currently, KPRIET primarily focuses on Engineering and Technology programs (B.E/B.Tech and M.E/M.Tech). Please verify with the admission office regarding management courses."
data.extend(generate_variations(mba_questions, mba_answer))

# 6. Hostel
hostel_questions = [
    "is hostel available?", "tell me about hostel facilities", "hostel fees",
    "how is the hostel food?", "ac hostel available?", "girls hostel",
    "boys hostel", "hostel rules", "can i get a hostel room?",
    "is hostel compulsory?", "hostel rooms", "do you have accommodation?",
    "where will i stay?", "hostel life"
]
hostel_answer = "Yes, KPRIET provides separate hostel facilities for boys and girls with excellent amenities, Wi-Fi, and quality food. AC and Non-AC rooms are available."
data.extend(generate_variations(hostel_questions, hostel_answer))

# 7. Transport
transport_questions = [
    "is college bus available?", "transport facility", "bus route details",
    "how many buses are there?", "do buses cover tirupur?", "transport fees",
    "bus timing", "do you have transport facility?", "college transport",
    "how to commute to college?", "bus from coimbatore", "bus facilities"
]
transport_answer = "The college operates a fleet of buses covering various routes in and around Coimbatore, Tirupur, and Erode to ensure safe and convenient transport for students."
data.extend(generate_variations(transport_questions, transport_answer))

# 8. Courses / Departments
course_questions = [
    "what courses do you offer?", "list of departments", "available branches",
    "which engineering branch is best?", "btech courses", "be courses",
    "do you have cse?", "do you have artificial intelligence?",
    "what are the branches available?", "departments in kpriet",
    "ug courses", "pg courses", "degrees offered", "courses available"
]
course_answer = "We offer various UG programs including AI & DS, Biomedical, Chemical, Civil, CSE, CSE (AIML), CSBS, Cyber Security, ECE, EEE, IT, Mechanical, and Mechatronics."
data.extend(generate_variations(course_questions, course_answer))

# 9. General Greetings
greeting_questions = [
    "hi", "hello", "hey", "good morning", "good afternoon", "good evening",
    "namaste", "hi there", "hello chatbot", "hey buddy"
]
greeting_answer = "Hello! I am the KPRIET Chatbot. How can I help you today?"
data.extend(generate_variations(greeting_questions, greeting_answer))

# 10. Chatbot Identity
identity_questions = [
    "who are you?", "what is your name?", "are you a human?", "what can you do?",
    "how can you help me?", "about you", "your name"
]
identity_answer = "I am an AI chatbot designed to answer your queries about KPR Institute of Engineering and Technology."
data.extend(generate_variations(identity_questions, identity_answer))

with open('c:/Users/VIGASVEL R/OneDrive/Desktop/chatbot_final/chatbot_data.json', 'w') as f:
    json.dump(data, f, indent=4)

print(f"Generated {len(data)} question-answer pairs.")
