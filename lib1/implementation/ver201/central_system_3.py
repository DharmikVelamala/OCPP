from flask import Flask, request, jsonify
import logging
import requests
from datetime import datetime
import threading
import keyboard

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


class ChargePoint:
    def __init__(self, charge_point_id, server_address):
        self.charge_point_id = charge_point_id
        self.server_address = server_address

    def send_get_base_report(self):
        payload = {
            "request_id": 7,
            "report_base": "SummaryInventory"
        }
        try:
            response = requests.post(f"{self.server_address}/get_base_report", json=payload)
            if response.status_code == 200:
                print(response.json)
                print("Dharmik")
                return response.json()
            else:
                logging.error("GetBaseReport request failed: %s", response.text)
                return None
        except requests.RequestException as e:
            logging.error("Exception during GetBaseReport request: %s", str(e))
            return None


    def initiate_get_base_report(self, event):
        if event.event_type == keyboard.KEY_DOWN:
            logging.info("Initiating GetBaseReport request...")
            threading.Thread(target=self.send_get_base_report).start()
            # self.send_get_base_report()



@app.route('/boot_notification', methods=['POST'])
def handle_boot_notification():
    data = request.get_json()
    charging_station = data.get('charging_station')
    reason = data.get('reason')

    # Handle Boot Notification logic here

    response = {
        # "current_time"=datetime.utcnow().isoformat()
        "status": "Accepted",
        "interval": 10,  # Set the interval as needed
    }
    return jsonify(response)


@app.route('/heartbeat', methods=['POST'])
def handle_heartbeat():
    data = request.get_json()
    charge_point_id = data.get('charge_point_id')
    current_time = data.get('current_time')

    # Handle Heartbeat logic here

    response = {
        "status": "Received",
    }
    return jsonify(response)

def run_server():
    app.run(host='0.0.0.0', port=9000)
    
def initiate_server(event):
    if event.event_type == keyboard.KEY_DOWN:
        logging.info("Starting Flask server...")
        threading.Thread(target=run_server).start()
        # run_server()

if __name__ == '__main__':

    keyboard.on_press_key('u',ChargePoint(charge_point_id="CP001", server_address="http://localhost:9000").initiate_get_base_report)
    keyboard.on_press_key('i', initiate_server)
    logging.info("Press 'u' to send GetBaseReport request. Press 'i' to start the Flask server.")
    
    try:
        keyboard.wait('esc')  # Keeps the main thread active until 'esc' is pressed
    except KeyboardInterrupt:
        logging.info("Exiting...")
