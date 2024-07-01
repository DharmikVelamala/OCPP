import logging
from flask import Flask, request, jsonify
from datetime import datetime
import keyboard
import requests
import threading
import time

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

class ChargePoint:
    def __init__(self, charge_point_id, server_address):
        self.charge_point_id = charge_point_id
        self.server_address = server_address

    def send_boot_notification(self, reason):
        payload = {
            "charging_station": {"model": "Wallbox XYZ", "vendor_name": "anewone"},
            "reason": reason,
        }
        time.sleep(3)
        try:
            response = requests.post(f"{self.server_address}/boot_notification", json=payload)
            if response.status_code == 200:
                print("Velamala")
                logging.info("BootNotification response: %s", response.json())
                return response.json()
            else:
                logging.error("BootNotification failed: %s", response.text)
                return None
        except requests.RequestException as e:
            logging.error("Exception during BootNotification request: %s", str(e))
            return None

    def send_heartbeat(self):
        payload = {
            "charge_point_id": self.charge_point_id,
            "current_time": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S") + "Z"
        }
        try:
            response = requests.post(f"{self.server_address}/heartbeat", json=payload)
            if response.status_code == 200:
                logging.info("Heartbeat response: %s", response.json())
                return response.json()
            else:
                logging.error("Heartbeat request failed: %s", response.text)
                return None
        except requests.RequestException as e:
            logging.error("Exception during Heartbeat request: %s", str(e))
            return None

    def initiate_get_boot_notification(self, event):
        if event.event_type == keyboard.KEY_DOWN:
            threading.Thread(target=self.send_boot_notification,args=("PowerUp",)).start()

@app.route('/get_base_report', methods=['POST'])
def handle_get_base_report():
    data = request.get_json()
    request_id = data.get('request_id')
    report_base = data.get('report_base')
    
    # Handle GetBaseReport logic here
    
    response = {
        "status": "Accepted",
    }
    return jsonify(response)

def run_server():
    app.run(host='0.0.0.0', port=9000)
    
def initiate_server(event):
    if event.event_type == keyboard.KEY_DOWN:
        threading.Thread(target=run_server).start()
        # run_server()
        
# def main():

#     while True:
#         if keyboard.is_pressed("u"):
#             app.run(host="0.0.0.0",port=9000)
#         if keyboard.is_pressed("i"):
#             charge_point = ChargePoint(charge_point_id="CP001", server_address="http://localhost:9000")
#             charge_point.send_boot_notification(reason="PowerUp")
#             charge_point.send_heartbeat()


if __name__ == "__main__":
    keyboard.on_press_key('o',ChargePoint(charge_point_id="CP001", server_address="ws://10.10.0.126:8765").initiate_get_boot_notification)
    keyboard.on_press_key('p', initiate_server)
    
    logging.info("Press 'o' to send BootNotification. Press 'p' to start the Flask server.")
    
    try:
        keyboard.wait('esc')  # Keeps the main thread active until 'esc' is pressed
    except KeyboardInterrupt:
        logging.info("Exiting...")
