import os
import random
import time
from flask import Flask, request, jsonify
from twilio.rest import Client

app = Flask(__name__)

# Twilio credentials
twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
twilio_auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(twilio_account_sid, twilio_auth_token)

# Commands categories
def get_commands_menu():
    return '''
    🌟 Welcome to the WhatsApp Bot 🌟
        Command Categories:
        1. 🤖 AI Commands
        2. 🎨 Anime Commands
        3. 📥 Download Commands
        4. 🎮 Games Commands
        5. 👥 Group Commands
        6. 🖼️ Logo Commands
        7. 👤 Owner Commands
        8. 🏷️ Sticker Commands
        9. 🛠️ Tools Commands
        10. 🔊 Voice Commands
        11. 🌀 Other Commands

    Use /menu to see this menu anytime!
    '''

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_msg = request.values.get('Body', '').strip()  
    response = ""  

    # Check for menu command
    if incoming_msg.lower() == '/menu':
        response = get_commands_menu()
    else:
        response = "Unknown command. Type /menu to see the options."

    # Send response back to user
    msg = client.messages.create(
        body=response,
        from_='whatsapp:+14155238886',  # Your Twilio number
        to=request.values.get('From')
    )

    return jsonify({'status': 'success', 'message': 'response sent'})

if __name__ == '__main__':
    app.run(debug=True)
