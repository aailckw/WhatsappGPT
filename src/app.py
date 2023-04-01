from flask import Flask, request, jsonify
from helper.openai_api import chat_complition, generate_image
from helper.twilio_api import send_message
from helper.user_management import save_message, get_user_messages, limit_requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(
        {
            'status': 'OK',
            'wehook_url': 'BASEURL/twilio/receiveMessage',
            'message': 'The webhook is ready.',
        }
    )

@app.route('/twilio/receiveMessage', methods=['POST'])
def receiveMessage():
    try:
        message = request.form['Body']
        sender_id = request.form['From']
        save_message(sender_id, 'user', message)

        if limit_requests(sender_id):
            return 'OK', 200

        if message.startswith('/image'):
            user_prompt = message.replace('/image', '').strip()
            image_url = generate_image(user_prompt)
            send_message(sender_id, "Here is the image you requested:", image_url)
        else:
            messages = get_user_messages(sender_id)
            result = chat_complition(message, messages)
            if result['status'] == 1:
                send_message(sender_id, result['response'])
                save_message(sender_id, 'system', result['response'])

        print(message, sender_id)
    except:
        pass

    return 'OK', 200