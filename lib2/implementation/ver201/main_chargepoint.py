import asyncio
import logging
from OCPP_LIB.ocpp_routing import on
from datetime import datetime


"""
@brief Ensures the presence of the 'websockets' package for the example.

This script attempts to import the 'websockets' package. If the package is not found,
it provides instructions to install it using pip.

@details
If 'websockets' is not installed, the script prints an error message and exits with
a non-zero status code.

Example usage:
@code
python your_script.py
@endcode
"""
try:
    import websockets
except ModuleNotFoundError:
    print("This example relies on the 'websockets' package.")
    print("Please install it by running: ")
    print()
    print(" $ pip install websockets")
    import sys
    
    sys.exit(1)
    
    
    
import charge_point_1
from OCPP_LIB.ver201 import ChargePoint as cp
from OCPP_LIB.ver201 import ocpp_request
from OCPP_LIB.ver201 import ocpp_response
logging.basicConfig(level=logging.INFO)

async def api_handle(charge_point):
    loop = asyncio.get_running_loop()
    while True:
        user_input = int(await loop.run_in_executor(None, input, "Enter a valid number (1: Boot Notification, 2: Heartbeat): "))
        if user_input == 1:
            id_token_value={"idToken": "75", "type": "Central"}
            await charge_point.send_authorize(id_token_value)
            
        elif user_input == 2:
            charging_station_value={"model": "SingleSocketCharger", "vendor_name": "Pisquare"}
            reason_value="PowerUp"
            await charge_point.send_boot_notification(charging_station_value,reason_value)
            
        elif user_input == 3:
            charging_limit_source_value="EMS"
            await charge_point.send_cleared_charging_limit(charging_limit_source_value)
            
        elif user_input == 4:
            vendor_id_str_value="This identifies the Vendor specific implementation"
            await charge_point.send_data_transfer(vendor_id_str_value)
            
        elif user_input == 5:
            status_value="Downloaded"
            await charge_point.send_firmware_status_notification(status_value)
            
        elif user_input == 6:
            iso15118_schema_version_value="version_201"
            action_value="Install"
            exi_request_value="Raw CertificateInstallationReq request from EV, Base64"
            await charge_point.send_get_15118_ev_certificate(iso15118_schema_version_value,action_value,exi_request_value)
            
        elif user_input == 7:
            ocsp_request_data_value={
                "hashAlgorithm":"SHA256",
                "issuerNameHash":"Admin",
                "issuerKeyHash":"Admin@123",
                "serialNumber":"20",
                "responderURL":"ANY URL SHOULD BE TYPED HEREY"
                }
            await charge_point.send_get_certificate_status(ocsp_request_data_value)
            
        elif user_input == 8:
            request_id_value=7
            await charge_point.send_get_display_messages(request_id_value)
            
        elif user_input == 9:
            interval=5
            await charge_point.send_heartbeat(interval)
            
        elif user_input == 10:
            status_value="BadMessage"
            await charge_point.send_log_status_notification(status_value)
            
        elif user_input == 11:
            evse_id_value=123
            meter_value_value=[
                {
                "timestamp":datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S"),
                "sampledValue":[{"value":9}]
            }
            ]
            await charge_point.send_meter_values(evse_id_value,meter_value_value)
            
        elif user_input == 12:
            charging_limit_value={
                "chargingLimitSource":"EMS"
            }
            await charge_point.send_notify_charging_limit(charging_limit_value)
            
        elif user_input == 13:
            data_value="(Part of) the requested data. No format specified in which the data is returned. Should be human readable"
            seq_no_value=5
            generated_at_value=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
            request_id_value=7
            await charge_point.send_notify_customer_information(data_value,seq_no_value,generated_at_value,request_id_value)
            
        elif user_input == 14:
            request_id_value=7
            await charge_point.send_notify_display_messages(request_id_value)
            
        elif user_input == 15:
            evse_id_value=123
            charging_needs_value={"requestedEnergyTransfer":"DC"}
            await charge_point.send_notify_ev_charging_needs(evse_id_value,charging_needs_value)
            
        elif user_input == 16:
            time_base_value=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
            evse_id_value=123
            charging_schedule_value={
                "id":5,
                "chargingRateUnit":"W",
                "chargingSchedulePeriod":[{
                    "startPeriod":4800,
                    "limit":9000
                }]
            }
            await charge_point.send_notify_ev_charging_schedule(time_base_value,evse_id_value,charging_schedule_value)
            
        elif user_input == 17:
            generated_at_value=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
            seq_no_value=0
            event_data_value=[
                {
                    "eventId":5,
                    "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")+"z",
                    "trigger":"Periodic",
                    "actualValue":"Dharmik",
                    "eventNotificationType":"HardWiredNotification",
                    "component": {"name": "ChargingStation"},
                    "variable": {"name": "VariableName"}
                }
            ]
            await charge_point.send_notify_event(generated_at_value,seq_no_value,event_data_value)
            
        elif user_input == 18:
            generated_at_value=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
            seq_no_value=0
            request_id_value=7
            
            await charge_point.send_notify_monitoring_report(generated_at_value,seq_no_value,request_id_value)
            
        elif user_input == 19:
            generated_at_value=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
            seq_no_value=0
            request_id_value=7
            await charge_point.send_notify_report(generated_at_value,seq_no_value,request_id_value)
            
        elif user_input == 20:
            status_value="DownloadScheduled"
            await charge_point.send_publish_firmware_status_notification(status_value)
            
        elif user_input == 21:
            request_id_value=7
            charging_limit_source_value="EMS"
            charging_profile_value=[{
                "id":5,
                "stackLevel":2,
                "chargingProfilePurpose":"ChargingStationExternalConstraints",
                "chargingProfileKind":"Absolute",
                "chargingSchedule":[{"id":5,
                                    "chargingRateUnit":"W",
                                    "chargingSchedulePeriod":[{"startPeriod":4800,
                                                                "limit":90}]
                                                            }]
            }]
            evse_id_value=5
            await charge_point.send_report_charging_profiles(request_id_value,charging_limit_source_value,charging_profile_value,evse_id_value)
            
        elif user_input == 22:
            reservation_id_value = 1234
            reservation_update_status_value= "Expired"
            await charge_point.send_reservation_status_update(reservation_id_value,reservation_update_status_value)
            
        elif user_input == 23:
            type_value = "Ritika"
            timestamp_value = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
            await charge_point.send_security_event_notification(type_value,timestamp_value)
            
        elif user_input == 24:
            csr = "bjcverhvijejbvbnktejbcjf"
            await charge_point.send_sign_certificate()
            
        elif user_input == 25:
            timestamp_value = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
            connector_status_value = "Available"
            evse_id_value = 13
            connector_id_value = 56
            
            await charge_point.send_status_notification(timestamp_value,connector_status_value,evse_id_value,connector_id_value)
            
        elif user_input == 26:
            event_type_value = "Started" 
            timestamp_value= datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
            trigger_reason_value="Authorized"
            seq_no_value = 1
            transaction_info_value={
                "transactionId":"123123123123"
            }
            await charge_point.send_transaction_event(event_type_value,timestamp_value,trigger_reason_value,seq_no_value,transaction_info_value)
            
        else:
            logging.warning("Invalid number entered. Please try again.")

    
async def main():
    async with websockets.connect(
        "ws://10.10.0.221:9876/CP_1", subprotocols=["ocpp2.0.1"]
    ) as ws:
        print(ws)
        charge_point = charge_point_1.ChargePoint("CP_1", ws)
        api_event=asyncio.ensure_future(api_handle(charge_point))
        await asyncio.gather(
            charge_point.start(),api_event
        )

if __name__ == "__main__":
    # asyncio.run() is used when running this example with Python >= 3.7v
    asyncio.run(main())
