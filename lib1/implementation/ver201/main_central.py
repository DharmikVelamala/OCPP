import asyncio
import logging
from datetime import datetime
import central_system_1
import sys

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


# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://Ritika:Ritz123@cluster0.ftwsd1h.mongodb.net/?appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'),tlsAllowInvalidCertificates=True)
# client.admin.command('ping')


db = client.ocpp_database

collection27 = db.CancelReservation
collection28 = db.CertificateSigned
collection29 = db.ChangeAvailability
collection30 = db.ClearCache
collection31 = db.ClearChargingProfile
collection32 = db.ClearDisplayMessage
collection33 = db.ClearVariableMonitoring
collection34 = db.CostUpdated
collection35 = db.CustomerInformation
collection36 = db.DataTransfer
collection37 = db.DeleteCertificate
collection38 = db.GetBaseReport
collection39 = db.GetChargingProfiles
collection40 = db.GetCompositeSchedule
collection41 = db.GetInstalledCertificateIds
collection42 = db.GetLocalListVersion
collection43 = db.GetLog
collection44 = db.GetMonitoringReport
collection45 = db.GetReport
collection46 = db.GetTransactionStatus
collection47 = db.GetVariables
collection48 = db.InstallCertificate
collection49 = db.PublishFirmware
collection50 = db.RequestStartTransaction
collection51 = db.RequestStopTransaction
collection52 = db.ReserveNow
collection53 = db.ResetRequest
collection54 = db.SendLocalList
collection55 = db.SetChargingProfile
collection56 = db.SetDisplayMessage
collection57 = db.SetMonitoringBase
collection58 = db.SetMonitoringLevel
collection59 = db.SetNetworkProfile
collection60 = db.SetVariableMonitoring
collection61 = db.SetVariables
collection62 = db.TriggerMessage
collection63 = db.UnlockConnector
collection64 = db.UnpublishFirmware
collection65 = db.UpdateFirmware



async def api_handle(charge_point):
    loop = asyncio.get_running_loop()
    while True:
        user_input = int(await loop.run_in_executor(None, input, "Enter a valid number (1: Boot Notification, 2: Heartbeat): "))
        if user_input == 1:
            reservation_id_value=123
            # reservation_id_value =await collection2.find({"id_token.type":"Central"},{"_id": 0, "id_token.idToken": 0, "iso15118_certificate_hash_data": 0}).to_list(1)
            # reservation_id_value =collection27.find({"reservation_id_value":123})
            data1= await charge_point.send_cancel_reservation( reservation_id_value)
            data1=data1.__dict__
            collection27.insert_one(data1)
        
            # Retrieve the reservation_id from the database
            # reservation = collection27.find_one({"reservation_id_value": "123"})
            # if reservation and "reservation_id" in reservation:
            #     data_dict = await charge_point.send_cancel_reservation(reservation_id_value)
            #     await collection27.insert_one(data_dict)
        
        elif user_input == 2:
            certificate_chain_value = "PI Square"
            data2=await charge_point.send_certificate_signed(certificate_chain_value)
        
            data2=data2.__dict__
            collection28.insert_one(data2)
        
        elif user_input == 3:
            operational_status_value="Inoperative"
            data3=await charge_point.send_change_availability(operational_status_value)
            data3=data3.__dict__
            collection29.insert_one(data3)
        
        elif user_input == 4:
            data4=await charge_point.send_clear_cache()
            data4=data4.__dict__
            collection30.insert_one(data4)
        
        elif user_input == 5:
            data5=await charge_point.send_clear_charging_profile()
            data5=data5.__dict__
            collection31.insert_one(data5)
        
        elif user_input == 6:
            id_value=5
            data6=await charge_point.send_clear_display_message(id_value)
            data6=data6.__dict__
            collection32.insert_one(data6)
        
        elif user_input == 7:
            id_list_value = [5]
            data7=await charge_point.send_clear_variable_monitoring(id_list_value)
            data7=data7.__dict__
            collection33.insert_one(data7)
        
        elif user_input == 8:
            total_cost_value = 195.45
            transaction_id_value = "123123"
            data8=await charge_point.send_cost_updated(total_cost_value,transaction_id_value)
            print(data8)
            data8=data8.__dict__
            collection34.insert_one(data8)
        
        elif user_input == 9:
            request_id_value = 7
            report_value = True
            clear_value = True
            data9 = await charge_point.send_customer_information(request_id_value,report_value,clear_value)
            data9=data9.__dict__
            collection35.insert_one(data9)
        
        elif user_input == 10:
            vendor_id_value="This identifies the Vendor specifics"
            data10 = await charge_point.send_data_transfer(vendor_id_value)
            data10=data10.__dict__
            collection36.insert_one(data10)
        
        elif user_input == 11:
            certificate_hash_data_value={
                "hashAlgorithm":"SHA256",
                "issuerNameHash":"Admin",
                "issuerKeyHash":"Admin@123",
                "serialNumber":"20"}
            data11=await charge_point.send_delete_certificate(certificate_hash_data_value)
            data11=data11.__dict__
            collection37.insert_one(data11)
            
        elif user_input == 12:
            request_id_value = 7
            report_base_value = "SummaryInventory"
            data12=await charge_point.send_get_base_report(request_id_value,report_base_value)
            data12=data12.__dict__
            collection38.insert_one(data12)
        
        elif user_input == 13:
            request_id_value=7
            charging_profile_value={
                "customData": {"vendorId": "VendorName"},
                "chargingProfilePurpose": "ChargingStationExternalConstraints",
                "stackLevel": 1,
                "chargingProfileId": [789],
                "chargingLimitSource": ["EMS"]
            }
            data13=await charge_point.send_get_charging_profiles(request_id_value,charging_profile_value)
            data13=data13.__dict__
            collection39.insert_one(data13)
        
        elif user_input == 14:
            duration_value=70
            evse_id_value=123
            data14=await charge_point.send_get_composite_schedule(duration_value,evse_id_value)
            data14=data14.__dict__
            collection40.insert_one(data14)
        
        elif user_input == 15:
            data15=await charge_point.send_get_installed_certificate_ids()
            data15=data15.__dict__
            collection41.insert_one(data15)
        
        elif user_input == 16:
            data16=await charge_point.send_get_local_list_version()
            data16=data16.__dict__
            collection42.insert_one(data16)
        
        elif user_input == 17:
            log_value={"remoteLocation":"Remote_ Location"}
            log_type_value="DiagnosticsLog"
            request_id_value=7
            data17=await charge_point.send_get_log(log_value,log_type_value,request_id_value)
            data17=data17.__dict__
            collection43.insert_one(data17)
        
        elif user_input == 18:
            request_id_value=7
            data18=await charge_point.send_get_monitoring_report(request_id_value)
            data18=data18.__dict__
            collection44.insert_one(data18)
        
        elif user_input == 19:
            request_id_value=7
            data19=await charge_point.send_get_report(request_id_value)
            data19=data19.__dict__
            collection45.insert_one(data19)
        
        elif user_input == 20:
            data20=await charge_point.send_get_transaction_status()
            data20=data20.__dict__
            collection46.insert_one(data20)
        
        elif user_input == 21:
            get_variable_data_value=[
                {
                    "component": {"name": "ChargingStation"},
                    "variable": {"name": "VariableName"}
                }
            ]
            data21=await charge_point.send_get_variables(get_variable_data_value)
            data21=data21.__dict__
            collection47.insert_one(data21)
        
        elif user_input == 22:
            certificate_value="A PEM encoded X.509 certificate"
            certificate_type_value="V2GRootCertificate"
            data22=await charge_point.send_install_certificate(certificate_value,certificate_type_value)
            data22=data22.__dict__
            collection48.insert_one(data22)
        
        elif user_input == 23:
            location_value="HTTTP//pisquare.co.in"
            checksum_value="123123123"
            request_id_value=7
            data23=await charge_point.send_publish_firmware(location_value,checksum_value,request_id_value)
            data23=data23.__dict__
            collection49.insert_one(data23)
        
        elif user_input == 24:
            id_token_value={
                "idToken":"hold hidden id of an RFID tag",
                "type":"Central"
                }
            remote_start_id_value=7
            data24=await charge_point.send_request_start_transaction(id_token_value,remote_start_id_value)
            data24=data24.__dict__
            collection50.insert_one(data24)
        
        elif user_input == 25:
            transaction_id_value = "AB1234"
            data25=await charge_point.send_request_stop_transaction(transaction_id_value)
            data25=data25.__dict__
            collection51.insert_one(data25)
        
        elif user_input == 26:
            id_value = 7
            expiry_date_time_value =  datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
            id_token_value= {
                "idToken":"rfid1234567890",
                "type":"Central"
            }
            data26=await charge_point.send_reserve_now(id_value,expiry_date_time_value,id_token_value)
            data26=data26.__dict__
            collection52.insert_one(data26)
        
        elif user_input == 27:
            type_value="Immediate"
            data27=await charge_point.send_reset_request(type_value)
            data27=data27.__dict__
            collection53.insert_one(data27)
        
        elif user_input == 28:
            version_number_value=12
            update_type_value="Differential"
            data28=await charge_point.send_send_local_list(version_number_value,update_type_value)
            data28=data28.__dict__
            collection54.insert_one(data28)
        
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
            data29=await charge_point.send_set_charging_profile(evse_id_value,charging_profile_value)
            data29=data29.__dict__
            collection55.insert_one(data29)
        
        elif user_input == 30:
            message_value = {"id":12,
                    "priority": "AlwaysFront",
                    "message":{
                                "format":"ASCII",
                                "content":"Ritika"}}
            data30=await charge_point.send_set_display_message(message_value)
            data30=data30.__dict__
            collection56.insert_one(data30)
        
        elif user_input == 31:
            monitoring_base_value="FactoryDefault"
            data31=await charge_point.send_set_monitoring_base(monitoring_base_value)
            data31=data31.__dict__
            collection57.insert_one(data31)
        
        elif user_input == 32:
            severity_value = 9
            data32=await charge_point.send_set_monitoring_level(severity_value)
            data32=data32.__dict__
            collection58.insert_one(data32)
        
        elif user_input == 33:
            configuration_slot_value = 24
            connection_data_value = {"ocppVersion" : "OCPP15" ,
                                "ocppTransport" : "JSON",
                                "ocppCsmsUrl" : "Ritika" ,
                                "messageTimeout" : 34,
                                "securityProfile" : 25 ,
                                "ocppInterface" : "Wireless0" ,
            }
            data33=await charge_point.send_set_network_profile(configuration_slot_value,connection_data_value)
            data33=data33.__dict__
            collection59.insert_one(data33)
        
        elif user_input == 34:
            set_monitoring_data_value=[
                {"value":9,
                "type": "UpperThreshold",
                "severity": 9,
                "component": {"name": "ChargingStation"},
                "variable": {"name": "VariableName"}}
            ]
            data34=await charge_point.send_set_variable_monitoring(set_monitoring_data_value)
            data34=data34.__dict__
            collection60.insert_one(data34)
        
        elif user_input == 35:
            set_variable_data_value=[
                {
                    "component": {"name": "componentName"},
                    "variable": {"name": "variableName"},
                    "attributeValue": "newValue"
                }
            ]
            data35=await charge_point.send_set_variables(set_variable_data_value)
            data35=data35.__dict__
            collection61.insert_one(data35)
        
        elif user_input == 36:
            requested_message_value = "BootNotification"
            data36=await charge_point.send_trigger_message(requested_message_value)
            data36=data36.__dict__
            collection62.insert_one(data36)
        
        elif user_input == 37:
            evse_id_value = 122
            connector_id_value=3
            data37=await charge_point.send_unlock_connector(evse_id_value,connector_id_value)
            data37=data37.__dict__
            collection63.insert_one(data37)
        
        elif user_input == 38:
            checksum_value="checksum over the entire"
            data38=await charge_point.send_unpublish_firmware(checksum_value)
            data38=data38.__dict__
            collection64.insert_one(data38)
        
        elif user_input == 39:
            location = "http://localhost:8000/firmware_update.bin"
            retrieve_date_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
            retries_value=3
            request_id_value=7
            firmware_value={
                "location":location,
                "retrieveDateTime":retrieve_date_time
            }
            data39=await charge_point.send_update_firmware(retries_value,request_id_value,firmware_value)
            data39=data39.__dict__
            collection65.insert_one(data39)
        
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
