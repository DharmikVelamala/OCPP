import asyncio
import logging
from datetime import datetime
import central_system_1
connected = set()
key = '0'

try:
    import websockets
except ModuleNotFoundError:
    print("This example relies on the 'websockets' package.")
    print("Please install it by running: ")
    print()
    print(" $ pip install websockets")
    import sys

    sys.exit(1)


async def api_handle(charge_point):
    loop = asyncio.get_running_loop()
    while True:
        user_input = int(await loop.run_in_executor(None, input, "Enter a valid number (1: Boot Notification, 2: Heartbeat): "))
        if user_input == 1:
            reservation_id_value = 123
            await charge_point.send_cancel_reservation(reservation_id_value)
            
        elif user_input == 2:
            certificate_chain_value = "PI Square"
            await charge_point.send_certificate_signed(certificate_chain_value)
            
        elif user_input == 3:
            operational_status_value="Inoperative"
            await charge_point.send_change_availability(operational_status_value)
            
        elif user_input == 4:
            await charge_point.send_clear_cache()
            
        elif user_input == 5:
            await charge_point.send_clear_charging_profile()
            
        elif user_input == 6:
            id_value=5
            await charge_point.send_clear_display_message(id_value)
            
        elif user_input == 7:
            id_list_value = [5]
            await charge_point.send_clear_variable_monitoring(id_list_value)
            
        elif user_input == 8:
            total_cost_value = 195.45
            transaction_id_value = "123123"
            await charge_point.send_cost_updated(total_cost_value,transaction_id_value)
            
        elif user_input == 9:
            request_id_value = 7
            report_value = True
            clear_value = True
            await charge_point.send_customer_information(request_id_value,report_value,clear_value)
            
        elif user_input == 10:
            vendor_id_value="This identifies the Vendor specifics"
            await charge_point.send_data_transfer(vendor_id_value)
            
        elif user_input == 11:
            certificate_hash_data_value={
                "hashAlgorithm":"SHA256",
                "issuerNameHash":"Admin",
                "issuerKeyHash":"Admin@123",
                "serialNumber":"20"}
            await charge_point.send_delete_certificate(certificate_hash_data_value)
            
        elif user_input == 12:
            request_id_value = 7
            report_base_value = "SummaryInventory"
            await charge_point.send_get_base_report(request_id_value,report_base_value)
            
        elif user_input == 13:
            request_id_value=7
            charging_profile_value={
                "customData": {"vendorId": "VendorName"},
                "chargingProfilePurpose": "ChargingStationExternalConstraints",
                "stackLevel": 1,
                "chargingProfileId": [789],
                "chargingLimitSource": ["EMS"]
            }
            await charge_point.send_get_charging_profiles(request_id_value,charging_profile_value)
            
        elif user_input == 14:
            duration_value=70
            evse_id_value=123
            await charge_point.send_get_composite_schedule(duration_value,evse_id_value)
            
        elif user_input == 15:
            await charge_point.send_get_installed_certificate_ids()
            
        elif user_input == 16:
            await charge_point.send_get_local_list_version()
            
        elif user_input == 17:
            log_value={"remoteLocation":"Remote_ Location"}
            log_type_value="DiagnosticsLog"
            request_id_value=7
            await charge_point.send_get_log(log_value,log_type_value,request_id_value)
            
        elif user_input == 18:
            request_id_value=7
            await charge_point.send_get_monitoring_report(request_id_value)
            
        elif user_input == 19:
            request_id_value=7
            await charge_point.send_get_report(request_id_value)
            
        elif user_input == 20:
            await charge_point.send_get_transaction_status()
            
        elif user_input == 21:
            get_variable_data_value=[
                {
                    "component": {"name": "ChargingStation"},
                    "variable": {"name": "VariableName"}
                }
            ]
            await charge_point.send_get_variables(get_variable_data_value)
            
        elif user_input == 22:
            certificate_value="A PEM encoded X.509 certificate"
            certificate_type_value="V2GRootCertificate"
            await charge_point.send_install_certificate(certificate_value,certificate_type_value)
            
        elif user_input == 23:
            location_value="HTTTP//pisquare.co.in"
            checksum_value="123123123"
            request_id_value=7
            await charge_point.send_publish_firmware(location_value,checksum_value,request_id_value)
            
        elif user_input == 24:
            id_token_value={
                "idToken":"hold hidden id of an RFID tag",
                "type":"Central"
                }
            remote_start_id_value=7
            await charge_point.send_request_start_transaction(id_token_value,remote_start_id_value)
            
        elif user_input == 25:
            transaction_id_value = "AB1234"
            await charge_point.send_request_stop_transaction(transaction_id_value)
            
        elif user_input == 26:
            id_value = 7
            expiry_date_time_value =  datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
            id_token_value= {
                "idToken":"rfid1234567890",
                "type":"Central"
            }
            await charge_point.send_reserve_now(id_value,expiry_date_time_value,id_token_value)
            
        elif user_input == 27:
            type_value="Immediate"
            await charge_point.send_reset_request(type_value)
            
        elif user_input == 28:
            version_number_value=12
            update_type_value="Differential"
            await charge_point.send_send_local_list(version_number_value,update_type_value)
            
        elif user_input == 29:
            evse_id_value = 32 
            charging_profile_value = {
                "id": 11,
                "stackLevel" : 9 ,
                "chargingProfilePurpose" : "ChargingStationMaxProfile",
                "chargingProfileKind" :"Recurring" ,
                "chargingSchedule":[{
                    "id": 11,
                    "chargingRateUnit": "A",
                    "chargingSchedulePeriod" :[{
                        "startPeriod":13,
                        "limit": 1
                    }]
                }]
            }
            await charge_point.send_set_charging_profile(evse_id_value,charging_profile_value)
            
        elif user_input == 30:
            message_value = {"id":12,
                    "priority": "AlwaysFront",
                    "message":{
                                "format":"ASCII",
                                "content":"Ritika"}}
            await charge_point.send_set_display_message(message_value)
            
        elif user_input == 31:
            monitoring_base_value="FactoryDefault"
            await charge_point.send_set_monitoring_base(monitoring_base_value)
            
        elif user_input == 32:
            severity_value = 9
            await charge_point.send_set_monitoring_level(severity_value)
            
        elif user_input == 33:
            configuration_slot_value = 24
            connection_data_value = {"ocppVersion" : "OCPP15" ,
                                "ocppTransport" : "JSON",
                                "ocppCsmsUrl" : "Ritika" ,
                                "messageTimeout" : 34,
                                "securityProfile" : 25 ,
                                "ocppInterface" : "Wireless0" ,
            }
            await charge_point.send_set_network_profile(configuration_slot_value,connection_data_value)
            
        elif user_input == 34:
            set_monitoring_data_value=[
                {"value":9,
                "type": "UpperThreshold",
                "severity": 9,
                "component": {"name": "ChargingStation"},
                "variable": {"name": "VariableName"}}
            ]
            await charge_point.send_set_variable_monitoring(set_monitoring_data_value)
            
        elif user_input == 35:
            set_variable_data_value=[
                {
                    "component": {"name": "componentName"},
                    "variable": {"name": "variableName"},
                    "attributeValue": "newValue"
                }
            ]
            await charge_point.send_set_variables(set_variable_data_value)
            
        elif user_input == 36:
            requested_message_value = "BootNotification"
            await charge_point.send_trigger_message(requested_message_value)
            
        elif user_input == 37:
            evse_id_value = 122
            connector_id_value=3
            await charge_point.send_unlock_connector(evse_id_value,connector_id_value)
            
        elif user_input == 38:
            checksum_value="checksum over the entire"
            await charge_point.send_unpublish_firmware(checksum_value)
            
        elif user_input == 39:
            location = "http://localhost:8000/firmware_update.bin"
            retrieve_date_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
            retries_value=3
            request_id_value=7
            firmware_value={
                "location":location,
                "retrieveDateTime":retrieve_date_time
            }
            await charge_point.send_update_firmware(retries_value,request_id_value,firmware_value)
            
        else:
            logging.warning("Invalid number entered. Please try again.")





async def on_connect(websocket, path):
    """For every new charge point that connects, create a ChargePoint
    instance and start listening for messages.
    """
    try:
        requested_protocols = websocket.request_headers["Sec-WebSocket-Protocol"]
    except KeyError:
        logging.error("Client hasn't requested any Subprotocol. Closing Connection")
        return await websocket.close()
    if websocket.subprotocol:
        logging.info("Protocols Matched: %s", websocket.subprotocol)
    else:
        # In the websockets lib if no subprotocols are supported by the
        # client and the server, it proceeds without a subprotocol,
        # so we have to manually close the connection.
        logging.warning(
            "Protocols Mismatched | Expected Subprotocols: %s,"
            " but client supports %s | Closing connection",
            websocket.available_subprotocols,
            requested_protocols,
        )
        return await websocket.close()
    charge_point_id = path.strip("/")
    charge_point = central_system_1.ChargePoint(charge_point_id, websocket)
    logging.info(f"New connection from {charge_point_id}")
    api_event=asyncio.ensure_future(api_handle(charge_point))
    await asyncio.gather(
            charge_point.start(),api_event
        )
    


async def main():
    #  deepcode ignore BindToAllNetworkInterfaces: <Example Purposes>
    server = await websockets.serve(
        on_connect, "10.10.0.221", 9876, subprotocols=["ocpp2.0.1"]
    )
    logging.info("Server Started listening to new connections...")
    
    await server.wait_closed()


if __name__ == "__main__":
    # asyncio.run() is used when running this example with Python >= 3.7v
    asyncio.run(main())
