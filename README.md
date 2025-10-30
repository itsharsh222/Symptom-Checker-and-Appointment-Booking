<<<<<<< HEAD
# Symptom Checker & Appointment Scheduler

A full-stack web application that allows patients to input symptoms, get AI-based suggestions using Google's Gemini API, and book appointments.

## Tech Stack
- **Frontend**: React with TypeScript
- **Backend**: Flask (Python)
- **Database**: MySQL
- **AI**: Google Gemini API

## Setup Instructions

### Prerequisites
- Node.js and npm
- Python 3.8+
- MySQL Server
- Google Gemini API key

### Backend Setup
1. Navigate to backend directory:
   ```bash
   cd backend
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Edit `.env` file and add your Gemini API key
   - Update database credentials if needed

4. Set up MySQL database:
   ```bash
   mysql -u root -p < ../database/setup.sql
   ```

5. Run Flask application:
   ```bash
   python app.py
   ```

### Frontend Setup
1. Navigate to frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start React development server:
   ```bash
   npm start
   ```

### Database Setup
1. Start MySQL server
2. Run the setup script:
   ```bash
   mysql -u root -p < database/setup.sql
   ```

## Features
- **Symptom Analysis**: AI-powered symptom analysis using Gemini API
- **Appointment Booking**: Schedule appointments with patient information
- **Patient Management**: Store and retrieve patient data
- **Responsive Design**: Mobile-friendly interface

## API Endpoints
- `POST /api/analyze-symptoms` - Analyze patient symptoms
- `POST /api/patients` - Create/retrieve patient
- `POST /api/appointments` - Book appointment
- `GET /api/appointments/<patient_id>` - Get patient appointments

## Usage
1. Visit the application at `http://localhost:3000`
2. Enter symptoms in the text area
3. Click "Analyze Symptoms" to get AI suggestions
4. Click "Book Appointment" to schedule a visit
5. Fill in patient details and select date/time

## Important Notes
- Replace `your_gemini_api_key_here` in `.env` with your actual Gemini API key
- Update MySQL credentials in `.env` if different from defaults
- The AI analysis is for informational purposes only and not a substitute for professional medical advice
=======
# Symptom-Checker-and-Appointment-Booking
Using Flash 2.0 API to analyze symptoms and book appointment with doctors
>>>>>>> e11da31bc0c769be440aff06ea1cfbfd01089688
