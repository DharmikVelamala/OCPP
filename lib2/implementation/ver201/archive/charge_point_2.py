import requests
from flask import Flask, request, jsonify
import logging
from datetime import datetime
import keyboard

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
        response = requests.post(f"{self.server_address}/boot_notification", json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            logging.error("Boot notification failed: %s", response.text)
            return None

    

    def send_heartbeat(self):
        payload = {
            "charge_point_id": self.charge_point_id,
            "current_time": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S") + "Z"
        }
        response = requests.post(f"{self.server_address}/heartbeat", json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            logging.error("Heartbeat request failed: %s", response.text)
            return None


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
    
    
def main():
    while True:
        if keyboard.is_pressed("i"):
            server_address = "http://localhost:9000"
            charge_point = ChargePoint(charge_point_id="CP001", server_address=server_address)
            
            # Send Boot Notification
            boot_response = charge_point.send_boot_notification(reason="PowerUp")
            if boot_response is not None and boot_response.get("status") == "Accepted":
                print("Boot notification successful")
            
            # # Send GetBaseReport
            # get_base_report_response = charge_point.send_get_base_report()
            # if get_base_report_response is not None:
            #     print("GetBaseReport response:", get_base_report_response)

            # Send Heartbeatiu
            heartbeat_response = charge_point.send_heartbeat()
            if heartbeat_response is not None:
                print("Heartbeat response:", heartbeat_response)
        if keyboard.is_pressed("u"):
            app.run(host="0.0.0.0",port=9048)
if __name__ == "__main__":
    main()
