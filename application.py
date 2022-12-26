from request_handler import RequestHandler
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_webhook():

   print("Received POST request")
   handler = RequestHandler()

   # Handle the webhook
   body = request.get_data()
   handler.handle_webhook(body.decode('utf-8'))

   return "Received POST request"

if __name__ == '__main__':
   app.run()