from flask import Flask, render_template, request, jsonify, session
from chatbot_model import get_response
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Department cutoff dictionary
DEPARTMENTS = {
    "AI and DS": "180+",
    "Biomedical": "165+",
    "Chemical": "165+",
    "Civil": "165+",
    "Computer Science": "185+",
    "Computer Science (AIML)": "185+",
    "CS & Business Systems": "180+",
    "Cyber Security": "185+",
    "Electronics and Communication": "175+",
    "Electrical": "175+",
    "Information Technology": "175+",
    "Mechanical": "170+",
    "Mechatronics": "170+"
}

DEPARTMENT_EXPLANATIONS = {
    "AI and DS": "focuses on machine learning, data science, and artificial intelligence.",
    "Biomedical": "focuses on applying engineering principles to biology and medicine for healthcare.",
    "Chemical": "focuses on chemical manufacturing processes, materials, and sustainable energy.",
    "Civil": "focuses on the design, construction, and maintenance of the physical and naturally built environment.",
    "Computer Science": "focuses on programming, software development, algorithms, and computational theory.",
    "Computer Science (AIML)": "focuses on advanced programming specialized in Artificial Intelligence and Machine Learning.",
    "CS & Business Systems": "focuses on blending computer science with business management and enterprise dynamics.",
    "Cyber Security": "focuses on protecting computer systems, networks, and data from cyber attacks.",
    "Electronics and Communication": "focuses on electronic devices, circuits, communication equipment, and networking.",
    "Electrical": "focuses on circuits, power systems, electromagnetism, and electrical machinery.",
    "Information Technology": "focuses on computing infrastructure, networking, and information management systems.",
    "Mechanical": "focuses on machines, manufacturing, thermodynamics, and robotics.",
    "Mechatronics": "focuses on the integration of mechanical engineering with electronics and intelligent computer control."
}

@app.route("/")
def index():
    return render_template("index.html", departments=DEPARTMENTS)

@app.route("/start", methods=["POST"])
def start():
    data = request.get_json()
    name = data.get("name", "").strip()
    department = data.get("department", "").strip()
    
    if not name or not department:
        return jsonify({"error": "Name and department are required."}), 400
        
    if department not in DEPARTMENTS:
        return jsonify({"error": "Invalid department selected."}), 400
        
    session['name'] = name
    session['department'] = department
    
    cutoff = DEPARTMENTS[department]
    explanation = DEPARTMENT_EXPLANATIONS.get(department, "is a great field of study.")
    
    welcome_msg = f"Hi {name} 👋\n"
    welcome_msg += f"You selected {department} (Cutoff: {cutoff})\n\n"
    welcome_msg += f"This department {explanation}\n\n"
    welcome_msg += "You can now ask me anything about college 😊"
    
    return jsonify({"message": "User set successfully.", "welcome_msg": welcome_msg})

@app.route("/chat", methods=["POST"])
def chat():
    if 'name' not in session or 'department' not in session:
        return jsonify({"error": "Session expired or user not set."}), 403

    user_input = request.json.get("message")
    
    if not user_input or not user_input.strip():
        return jsonify({"response": "Please enter a valid message."}), 400
        
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=5002)
