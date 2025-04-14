from flask import Flask, render_template, request, jsonify
import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Get API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    """Render the main chat interface"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Process chat requests and return AI responses"""
    user_input = request.json.get("message", "")
    
    # Add context for IIT(ISM)-specific information
    system_prompt = """
    You are an AI assistant for IIT(ISM) Dhanbad (Indian Institute of Technology, Indian School of Mines) website.
    Provide helpful, accurate, and concise information about admissions, courses, departments,
    faculty, campus facilities, events, and other college-related topics.
    
    Some key information about IIT(ISM) Dhanbad:
    - Founded in 1926 as the Indian School of Mines
    - Converted to an IIT in 2016
    - Located in Dhanbad, Jharkhand, India
    - Known for excellence in mining, petroleum, earth sciences, and engineering
    - Offers B.Tech, M.Tech, MSc, MBA, and PhD programs
    - Has 18 academic departments
    - Campus spans over 218 acres with modern facilities
    
    If you don't know something specific to IIT(ISM), acknowledge that
    and provide general information that might be helpful.
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            max_tokens=500,
            temperature=0.7
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"Sorry, I encountered an error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)