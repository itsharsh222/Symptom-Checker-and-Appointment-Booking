from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mafia@localhost/symptom_checker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure Gemini AI
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-2.0-flash')

# Database Models
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    symptoms = db.Column(db.Text, nullable=False)
    ai_suggestion = db.Column(db.Text)
    appointment_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='scheduled')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Routes
@app.route('/api/analyze-symptoms', methods=['POST'])
def analyze_symptoms():
    data = request.json
    symptoms = data.get('symptoms', '')
    
    try:
        prompt = f"""
        As a medical AI assistant, analyze these symptoms: {symptoms}
        
        Provide:
        1. Possible conditions (3-4 most likely)
        2. Severity level (Low/Medium/High)
        3. Recommended actions
        4. When to seek immediate care
        
        Note: This is for informational purposes only and not a substitute for professional medical advice.
        """
        
        response = model.generate_content(prompt)
        
        return jsonify({
            'success': True,
            'analysis': response.text,
            'symptoms': symptoms
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/patients', methods=['POST'])
def create_patient():
    data = request.json
    
    existing_patient = Patient.query.filter_by(email=data['email']).first()
    if existing_patient:
        return jsonify({'success': True, 'patient_id': existing_patient.id})
    
    patient = Patient(
        name=data['name'],
        email=data['email'],
        phone=data['phone']
    )
    
    db.session.add(patient)
    db.session.commit()
    
    return jsonify({'success': True, 'patient_id': patient.id})

@app.route('/api/appointments', methods=['POST'])
def book_appointment():
    data = request.json
    
    appointment = Appointment(
        patient_id=data['patient_id'],
        symptoms=data['symptoms'],
        ai_suggestion=data.get('ai_suggestion', ''),
        appointment_date=datetime.fromisoformat(data['appointment_date'])
    )
    
    db.session.add(appointment)
    db.session.commit()
    
    return jsonify({'success': True, 'appointment_id': appointment.id})

@app.route('/api/appointments/<int:patient_id>', methods=['GET'])
def get_appointments(patient_id):
    appointments = Appointment.query.filter_by(patient_id=patient_id).all()
    
    result = []
    for apt in appointments:
        result.append({
            'id': apt.id,
            'symptoms': apt.symptoms,
            'ai_suggestion': apt.ai_suggestion,
            'appointment_date': apt.appointment_date.isoformat(),
            'status': apt.status
        })
    
    return jsonify({'success': True, 'appointments': result})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)