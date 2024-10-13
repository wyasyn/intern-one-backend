from flask import Flask, jsonify, request
from flask_cors import CORS
from chat import get_response
import logging

app = Flask(__name__)
CORS(app)

def is_valid_text(text):
    """Validates user input to ensure it's non-empty and non-whitespace"""
    return text and not text.isspace()

@app.route('/chat', methods=['POST'])
def chat():
    try:
        text = request.get_json().get("message")
        
        if not is_valid_text(text):
            return jsonify({'error': 'Invalid text input'}), 400  
        
        response = get_response(text)
        answer = {'answer': response}
        return jsonify(answer)
    
    except Exception as e:
        logging.error(f'Error in chat: {str(e)}')
        return jsonify({'error': 'An error occurred'}), 500



if __name__ == '__main__':
    app.run(host="0.0.0.0" ,debug=True)