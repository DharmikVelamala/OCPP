from flask import Flask, request, jsonify
import logging
import requests
from datetime import datetime
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
            response = requests.post(f"{self.server_address}/get_base_report", json=payload)
            if response.status_code == 200:
                print("get_base_report")
                return response.json()
            else:
                logging.error("GetBaseReport request failed: %s", response.text)
                return None   
        

# charge_point = ChargePoint(charge_point_id="CP001", server_address="http://localhost:9000")
# get_base_report_response = charge_point.send_get_base_report()


@app.route('/boot_notification', methods=['POST'])
def handle_boot_notification():
    data = request.get_json()
    charging_station = data.get('charging_station')
    reason = data.get('reason')
    
    # Handle Boot Notification logic here
    
    response = {
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

if __name__ == '__main__':
    while True:
        if keyboard.is_pressed('i'):
            app.run(host='0.0.0.0', port=9000)
        if keyboard.is_pressed("u"):
            server_address = "http://localhost:9048"
            charge_point = ChargePoint(charge_point_id="CP001", server_address=server_address)
            get_base_report_response = charge_point.send_get_base_report()
            if get_base_report_response is not None:
                print("GetBaseReport response:", get_base_report_response)

