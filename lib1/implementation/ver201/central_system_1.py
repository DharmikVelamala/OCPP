import asyncio
import logging
from datetime import datetime

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

from OCPP_LIB.ocpp_routing import on
from OCPP_LIB.ver201 import ChargePoint as cp
from OCPP_LIB.ver201 import ocpp_response
from OCPP_LIB.ver201 import ocpp_request

logging.basicConfig(level=logging.INFO)







class ChargePoint(cp):
    @on("Authorize")
    def on_authorize(self, id_token, **kwargs):
        return ocpp_response.Authorize(
            id_token_info={"status":"Accepted"}
        )

    @on("BootNotification")
    def on_boot_notification(self, charging_station, reason, **kwargs):
        return ocpp_response.BootNotification(
            current_time=datetime.utcnow().isoformat(),
            interval=10,
            status="Accepted"
        )

    @on("ClearedChargingLimit")
    def on_cleared_charging_limit(self, charging_limit_source, **kwargs):
        return ocpp_response.ClearedChargingLimit(
        )

    @on("FirmwareStatusNotification")
    def on_firmware_status_notification(self, status, **kwargs):
        return ocpp_response.FirmwareStatusNotification(
        )

    @on("Get15118EVCertificate")
    def on_get_15118_ev_certificate(self, iso15118_schema_version,action,exi_request, **kwargs):
        return ocpp_response.Get15118EVCertificate(
            status="Accepted",
            exi_response="Raw CertificateInstallationRes response for the EV, Base64 encoded."
        )

    @on("GetCertificateStatus")
    def on_get_certificate_status(self, ocsp_request_data,**kwargs):
        return ocpp_response.GetCertificateStatus(
            status="Accepted",
        )

    @on("GetDisplayMessages")
    def on_get_display_messages(self, request_id,**kwargs):
        return ocpp_response.GetDisplayMessages(
            status="Accepted",
        )

    @on("Heartbeat")
    def on_heartbeat(self):
        print("Got a Heartbeat!")
        return ocpp_response.Heartbeat(
            current_time=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S") + "Z"
        )

    @on("LogStatusNotification")
    def on_log_status_notification(self,**kwargs):
        return ocpp_response.LogStatusNotification(
        )

    @on("MeterValues")
    def on_meter_values(self,**kwargs):
        return ocpp_response.MeterValues(
            
        )

    @on("NotifyChargingLimit")
    def on_notify_charging_limit(self,**kwargs):
        return ocpp_response.NotifyChargingLimit(
            
        )

    @on("NotifyCustomerInformation")
    def on_notify_customer_information(self,data,seq_no,generated_at,request_id,**kwargs):
        return ocpp_response.NotifyCustomerInformation(
            
        )
        
    @on("NotifyDisplayMessages")
    def on_notify_display_messages(self,request_id,**kwargs):
        return ocpp_response.NotifyDisplayMessages(
            
        )

    @on("NotifyEVChargingNeeds")
    def on_notify_ev_charging_needs(self,evse_id,charging_needs,**kwargs):
        return ocpp_response.NotifyEVChargingNeeds(
            status="Accepted"
        )

    @on("NotifyEvent")
    def on_notify_event(self,generated_at,seq_no,event_data,**kwargs):
        return ocpp_response.NotifyEvent(
        )

    @on("NotifyMonitoringReport")
    def on_notify_monitoring_report(self,generated_at,seq_no,request_id,**kwargs):
        return ocpp_response.NotifyMonitoringReport(
        )

    @on("NotifyReport")
    def on_notify_report(self,generated_at,seq_no,request_id,**kwargs):
        return ocpp_response.NotifyReport(
        )












    async def send_cancel_reservation(self):
        request = ocpp_request.CancelReservation(
            reservation_id = 123
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'cancelReservation' ")

    async def send_certificate_signed(self):
        request = ocpp_request.CertificateSigned(
            certificate_chain = "PI Square"
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'certificate signed' ")

    async def send_change_availability(self):
        request = ocpp_request.ChangeAvailability(
            operational_status = "Inoperative"
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'Change available' ")

    async def send_clear_cache(self):
        request = ocpp_request.ClearCache(
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'clear cache' ")

    async def send_clear_charging_profile(self):
        request = ocpp_request.ClearChargingProfile(
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'Clear Charging Profile' ")

    async def send_clear_display_message(self):
        request = ocpp_request.ClearDisplayMessage(
            id=5
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'Clear Display Message' ")

    async def send_clear_variable_monitoring(self):
        request = ocpp_request.ClearVariableMonitoring(
            id = [5]
        )
        response = await self.call(request)
        if response.clear_monitoring_result[0].get("status") == "Accepted":
            print("Connected to chargepoint system 'Clear Variable Monitoringt")
        else:
            print("Connected to chargepoint system 'Clear Variable Monitoringt,error")

    async def send_cost_updated(self):
        request = ocpp_request.CostUpdated(
            total_cost= 100.45,
            transaction_id="123123"
        )
        response = await self.call(request)
        if response == None:
            print("Connected to chargepoint system 'cost update'")
        else:
            print("Connected to chargepoint system 'cost update',error")

    async def send_customer_information(self):
        request = ocpp_request.CustomerInformation(
            request_id=7,
            report=True,
            clear=True
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'Customer Information'")
        else:
            print("Connected to chargepoint system 'Customer Information',error")

    async def send_delete_certificate(self):
        request = ocpp_request.DeleteCertificate(
            certificate_hash_data={
                "hashAlgorithm":"SHA256",
                "issuerNameHash":"Admin",
                "issuerKeyHash":"Admin@123",
                "serialNumber":"20"}
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'Delete Certificate'")
        else:
            print("Connected to chargepoint system 'Delete Certificate',error")

    async def send_get_base_report(self):
        request = ocpp_request.GetBaseReport(
            request_id= 7,
            report_base= "SummaryInventory",
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'get base report")
            

    async def send_get_charging_profiles(self):
        request = ocpp_request.GetChargingProfiles(
            request_id=7,
            charging_profile={
                "customData": {"vendorId": "VendorName"},
                "chargingProfilePurpose": "ChargingStationExternalConstraints",
                "stackLevel": 1,
                "chargingProfileId": [789],
                "chargingLimitSource": ["EMS"]
            }
        )
        
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'Get Charging Profiles' ")

    async def send_get_composite_schedule(self):
        request = ocpp_request.GetCompositeSchedule(
            duration=70,
            evse_id=123
        )
        
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'GetCompositeSchedule'")

    async def send_get_installed_certificate_ids(self):
        request = ocpp_request.GetInstalledCertificateIds(
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'Get Installed Certificate Ids'")

    async def send_get_local_list_version(self):
        request = ocpp_request.GetLocalListVersion(
        )
        response = await self.call(request)
        if response.version_number == 201:
            print("Connected to chargepoint system 'Get Local List Version'")

    async def send_get_log(self):
        request = ocpp_request.GetLog(
            log={"remoteLocation":"Remote_ Location"},
            log_type="DiagnosticsLog",
            request_id=7
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'Get Log'")

    async def send_get_monitoring_report(self):
        request = ocpp_request.GetMonitoringReport(
            request_id=7
        )
        response = await self.call(request) 
        if response.status == "Accepted":
            print("Connected to chargepoint system 'get monitoring report' ")

    async def send_get_report(self):
        request = ocpp_request.GetReport(
            request_id=7
        )
        response = await self.call(request) 
        if response.status == "Accepted":
            print("Connected to chargepoint system 'get monitoring report' ")

    async def send_get_transaction_status(self):
        request = ocpp_request.GetTransactionStatus(
        )
        response = await self.call(request) 
        if response.messages_in_queue == True:
            print("Connected to chargepoint system 'Get Transaction Status' ")

    async def send_get_variables(self):
        request = ocpp_request.GetVariables(
            get_variable_data=[
                {
                    "component": {"name": "ChargingStation"},
                    "variable": {"name": "VariableName"}
                }
            ]
            # custom_data= {"string": 5}
        )
        response = await self.call(request)
        
        if response.get_variable_result[0].get("attributeStatus") == "Accepted":
            print("Connected to chargepoint system 'get variables'")
        else:
            
            print("dharmik"+"response.get_variable_result[0].get('attributeStatus')")

    async def send_install_certificate(self):
        request = ocpp_request.InstallCertificate(
            certificate="A PEM encoded X.509 certificate",
            certificate_type="V2GRootCertificate"
        )
        response = await self.call(request)
        
        if response.status == "Accepted":
            print("Connected to chargepoint system 'InstallCertificate'")

    async def send_publish_firmware(self):
        request = ocpp_request.PublishFirmware(
            location="HTTTP//pisquare.co.in",
            checksum="123123123",
            request_id=7
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'PublishFirmware'")








    async def send_set_monitoring_base(self):
        request = ocpp_request.SetMonitoringBase(
            monitoring_base="FactoryDefault"
        )
        response = await self.call(request) 
        if response.status == "Accepted":
            print("Connected to chargepoint system 'set monitoring base' ")

    async def send_notify_event(self):
        request = ocpp_request.NotifyEvent(
            
            generated_at=(datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S") + "Z"),
            seq_no = 0,
            event_data=[
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
            )
        response = await self.call(request)
        
        custom_data = getattr(response, 'custom_data', None)
        if custom_data and isinstance(custom_data, dict):
            vendor_id = custom_data.get("vendorId")
            if vendor_id == "notification received by notify event":
                print("Connected to chargepoint system 'notify event'")
            else:
                print("dharmik")
        else:
            print("Error: Response does not contain valid custom_data")

    async def send_set_monitoring_level(self):
        request = ocpp_request.SetMonitoringLevel(
            severity = 9
        )
        response = await self.call(request) 
        if response.status == "Accepted":
            print("Connected to chargepoint system 'set monitoring level' ")

    async def send_set_variable_monitoring(self):
        request = ocpp_request.SetVariableMonitoring(
            set_monitoring_data=[
                {"value":9,
                "type": "UpperThreshold",
                "severity": 9,
                "component": {"name": "ChargingStation"},
                "variable": {"name": "VariableName"}}
            ]
            # custom_data= {"string": 5}
        )
        response = await self.call(request)
        
        if response.set_monitoring_result[0].get("status") == "Accepted":
            print("Connected to chargepoint 'set variable monitoring' ")
        else:
            
            print("dharmik",response.get_variable_result[0].get("attributeStatus"))
        # await request

    async def send_set_variables(self):
        request = ocpp_request.SetVariables(
            set_variable_data=[
                {
                    "component": {"name": "componentName"},
                    "variable": {"name": "variableName"},
                    "attributeValue": "newValue"
                }
            ]
        )
        response = await self.call(request)
        print(response)









async def api_handle(charge_point):
    loop = asyncio.get_running_loop()
    while True:
        user_input = int(await loop.run_in_executor(None, input, "Enter a valid number (1: Boot Notification, 2: Heartbeat): "))
        if user_input == 1:
            await charge_point.send_cancel_reservation()
            
        elif user_input == 2:
            await charge_point.send_certificate_signed()
            
        elif user_input == 3:
            await charge_point.send_change_availability()
            
        elif user_input == 4:
            await charge_point.send_clear_cache()
            
        elif user_input == 5:
            await charge_point.send_clear_charging_profile()
            
        elif user_input == 6:
            await charge_point.send_clear_display_message()
            
        elif user_input == 7:
            await charge_point.send_clear_variable_monitoring()
            
        elif user_input == 8:
            await charge_point.send_cost_updated()
            
        elif user_input == 9:
            await charge_point.send_customer_information()
            
        elif user_input == 11:
            await charge_point.send_delete_certificate()
            
        elif user_input == 12:
            await charge_point.send_get_base_report()
            
        elif user_input == 13:
            await charge_point.send_get_charging_profiles()
            
        elif user_input == 14:
            await charge_point.send_get_composite_schedule()
            
        elif user_input == 15:
            await charge_point.send_get_composite_schedule()
            
        elif user_input == 16:
            await charge_point.send_get_installed_certificate_ids()
            
        elif user_input == 17:
            await charge_point.send_get_local_list_version()
            
        elif user_input == 18:
            await charge_point.send_get_log()
            
        elif user_input == 19:
            await charge_point.send_get_monitoring_report()
            
        elif user_input == 20:
            await charge_point.send_get_report()
            
        elif user_input == 21:
            await charge_point.send_get_transaction_status()
            
        elif user_input == 22:
            await charge_point.send_install_certificate()
            
        elif user_input == 23:
            await charge_point.send_publish_firmware()
            
        elif user_input == 113:
            await charge_point.send_get_variables()
            
        elif user_input == 114:
            await charge_point.send_set_monitoring_base()
            
        elif user_input == 115:
            await charge_point.send_notify_event()
            
        elif user_input == 116:
            await charge_point.send_set_monitoring_level()
            
        elif user_input == 117:
            await charge_point.send_set_variable_monitoring()
            
        elif user_input == 118:
            await charge_point.send_set_variables()
            
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
    charge_point = ChargePoint(charge_point_id, websocket)
    logging.info(f"New connection from {charge_point_id}")
    api_event=asyncio.ensure_future(api_handle(charge_point))
    await asyncio.gather(
            charge_point.start(),api_event
        )
    


async def main():
    #  deepcode ignore BindToAllNetworkInterfaces: <Example Purposes>
    server = await websockets.serve(
        on_connect, "10.10.0.221", 8765, subprotocols=["ocpp2.0.1"]
    )
    logging.info("Server Started listening to new connections...")
    
    await server.wait_closed()


if __name__ == "__main__":
    # asyncio.run() is used when running this example with Python >= 3.7v
    asyncio.run(main())
