from flask import Flask, request, jsonify, render_template
import os
import openai
import speech_recognition as sr

app = Flask(__name__, template_folder='templates')

openai.api_key = os.environ["OPENAI_API_KEY"]

@app.route('/')
def index():
    return render_template('TalkApp.html')

@app.route('/chat', methods=['POST'])  
def chat():
    data = request.get_json()
    user_input = data['prompt']

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_input}
        ],
        max_tokens=20
    )

    text = response['choices'][0]['message']['content']
    return jsonify({'response': text})

if __name__ == "__main__":
    app.run(debug=True)
