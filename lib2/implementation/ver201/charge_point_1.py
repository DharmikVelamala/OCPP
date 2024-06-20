import asyncio
import logging
from OCPP_LIB.ocpp_routing import on
from datetime import datetime

try:
    import websockets
except ModuleNotFoundError:
    print("This example relies on the 'websockets' package.")
    print("Please install it by running: ")
    print()
    print(" $ pip install websockets")
    import sys

    sys.exit(1)


from OCPP_LIB.ver201 import ChargePoint as cp
from OCPP_LIB.ver201 import ocpp_request
from OCPP_LIB.ver201 import ocpp_response

logging.basicConfig(level=logging.INFO)


class ChargePoint(cp):
    async def send_authorize(self):
        request = ocpp_request.Authorize(
            id_token={"idToken": "75", "type": "Central"},
        
        )
        response = await self.call(request)
        if response and hasattr(response, 'id_tag_info') and response.id_tag_info.get('status') == 'Accepted':
            print(f"Authorization accepted for ID token:")
        else:
            print(f"Authorization failed for ID token:. Response: {response}")

    async def send_boot_notification(self):
        request = ocpp_request.BootNotification(
            charging_station={"model": "SingleSocketCharger", "vendor_name": "Pisquare"},
            reason="PowerUp",
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to central system 'boot notification'")
        # await self.send_heartbeat(response.interval)
        

    async def send_cleared_charging_limit(self):
        request = ocpp_request.ClearedChargingLimit(
            charging_limit_source="EMS"
        )
        response = await self.call(request)
        if response == None:
            print("Connected to central system'ClearedChargingLimit'")

    async def send_data_transfer(self):
        request = ocpp_request.DataTransfer(
            vendor_id="This identifies the Vendor specific implementation",
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'Data Transfer'")
        else:
            print("Connected to chargepoint system 'Data Transfer',error")

    async def send_firmware_status_notification(self):
        request = ocpp_request.FirmwareStatusNotification(
            status="Downloaded"
        )
        response = await self.call(request)
        if response == None:
            print("Connected to central system'Firmware Status Notification'")

    async def send_get_15118_ev_certificate(self):
        request = ocpp_request.Get15118EVCertificate(
            iso15118_schema_version="version_201",
            action="Install",
            exi_request="Raw CertificateInstallationReq request from EV, Base64"
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to central system'Get 15118 EV Certificaten'")

    async def send_get_certificate_status(self):
        request = ocpp_request.GetCertificateStatus(
            ocsp_request_data={
                "hashAlgorithm":"SHA256",
                "issuerNameHash":"Admin",
                "issuerKeyHash":"Admin@123",
                "serialNumber":"20",
                "responderURL":"ANY URL SHOULD BE TYPED HEREY"
                }
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to central system'GetCertificateStatus'")

    async def send_get_display_messages(self):
        request = ocpp_request.GetDisplayMessages(
            request_id=7
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to central system'Get Display Messages'")

    async def send_heartbeat(self, interval):
        request = ocpp_request.Heartbeat()
        while True:
            await self.call(request)
            await asyncio.sleep(interval)  

    async def send_log_status_notification(self):
        request = ocpp_request.LogStatusNotification(
            status="BadMessage"
        )
        response = await self.call(request)
        if response == None:
            print("Connected to central system'send_log_status_notification'")

    async def send_meter_values(self):
        request = ocpp_request.MeterValues(
            evse_id=123,
            meter_value=[
                {
                "timestamp":datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S"),
                "sampledValue":[{"value":9}]
            }
            ]
        )
        response = await self.call(request)
        if response == None:
            print("Connected to central system'send_meter_values'")

    async def send_notify_charging_limit(self):
        request = ocpp_request.NotifyChargingLimit(
            charging_limit={
                "chargingLimitSource":"EMS"
            }
        )
        response = await self.call(request)
        if response == None:
            print("Connected to central system'NotifyChargingLimit'")

    async def send_notify_customer_information(self):
        request = ocpp_request.NotifyCustomerInformation(
            data="(Part of) the requested data. No format specified in which the data is returned. Should be human readable",
            seq_no=5,
            generated_at=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S"),
            request_id=7
        )
        response = await self.call(request)
        if response == None:
            print("Connected to central system'NotifyCustomerInformation'")

    async def send_notify_display_messages(self):
        request = ocpp_request.NotifyDisplayMessages(
            request_id=7
        )
        response = await self.call(request)
        if response == None:
            print("connected to central system'NotifyDisplayMessages'")

    async def send_notify_ev_charging_needs(self):
        request = ocpp_request.NotifyEVChargingNeeds(
            evse_id=123,
            charging_needs={"requestedEnergyTransfer":"DC"}
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("connected to central system'NotifyEVChargingNeeds'")

    async def send_notify_ev_charging_schedule(self):
        request = ocpp_request.NotifyEVChargingSchedule(
            time_base=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S"),
            evse_id=123,
            charging_schedule={
                "id":5,
                "chargingRateUnit":"W",
                "chargingSchedulePeriod":[{
                    "startPeriod":4800,
                    "limit":9000
                }]
            }
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("connected to central system'NotifyEVChargingSchedule'")

    async def send_notify_event(self):
        request = ocpp_request.NotifyEvent(
            generated_at=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S"),
            seq_no=0,
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
        if response == None:
            print("connected to central system'NotifyEvent'")

    async def send_notify_monitoring_report(self):
        request = ocpp_request.NotifyMonitoringReport(
            generated_at=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S"),
            seq_no=0,
            request_id=7
        )
        response = await self.call(request)
        if response == None:
            print("connected to central system'NotifyMonitoringReport'")

    async def send_notify_report(self):
        request = ocpp_request.NotifyReport(
            generated_at=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S"),
            seq_no=0,
            request_id=7
        )
        response = await self.call(request)
        if response == None:
            print("connected to central system'NotifyReport'")

    async def send_publish_firmware_status_notification(self):
        request = ocpp_request.PublishFirmwareStatusNotification(
            status="DownloadScheduled"
        )
        response = await self.call(request)
        if response == None:
            print("connected to central system'publish_firmware_status_notification'")

    async def send_report_charging_profiles(self):
        request = ocpp_request.ReportChargingProfiles(
            request_id=7,
            charging_limit_source="EMS",
            charging_profile=[{
                "id":5,
                "stackLevel":2,
                "chargingProfilePurpose":"ChargingStationExternalConstraints",
                "chargingProfileKind":"Absolute",
                "chargingSchedule":[{"id":5,
                                    "chargingRateUnit":"W",
                                    "chargingSchedulePeriod":[{"startPeriod":4800,
                                                                "limit":90}]
                                                            }]
            }],
            evse_id=5
        )
        response = await self.call(request)
        if response == None:
            print("connected to central system'report_charging_profiles'")

    async def send_reservation_status_update(self):
        request = ocpp_request.ReservationStatusUpdate(
            reservation_id = 1234 ,
            reservation_update_status= "Expired"
        )
        response = await self.call(request)
        if response == None:
            print("connected to central system'send_reservation_status_update'")

    async def send_security_event_notification(self):
        request = ocpp_request.SecurityEventNotification(
        type = "Ritika",
        timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
            )
        response = await self.call(request)
        if response == None:
            print("connected to central system on Security event notification")

    async def send_sign_certificate(self):
        request = ocpp_request.SignCertificate(
            csr = "bjcverhvijejbvbnktejbcjf"
            )
        response = await self.call(request)
        if response.status == "Accepted":
            print("connected to central system on sign certificate ")

    async def send_status_notification(self):
        request = ocpp_request.StatusNotification(
            timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S"),
            connector_status = "Available",
            evse_id = 13,
            connector_id = 56
    )
        response = await self.call(request)
        if response==None:
            print("Connected to chargepoint system ' send_status_notification '")

    async def send_transaction_event(self):
        request = ocpp_request.TransactionEvent(
            event_type = "Started" ,
            timestamp= datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S"),
            trigger_reason="Authorized",
            seq_no = 1,
            transaction_info={
                "transactionId":"123123123123"
                
            }
            )
        response = await self.call(request)
        if response==None:
            print("Connected to chargepoint system ' send_transaction_event '")






    @on("CancelReservation")
    def on_cancel_reservation(self,reservation_id, **kwargs):
        return ocpp_response.CancelReservation(
            status="Accepted"
        )

    @on("CertificateSigned")
    def on_certificate_signed(self,certificate_chain, **kwargs):
        return ocpp_response.CertificateSigned(
            status="Accepted"
        )

    @on("ChangeAvailability")
    def on_change_availability(self,operational_status, **kwargs):
        return ocpp_response.ChangeAvailability(
            status="Accepted"
        )

    @on("ClearCache")
    def on_clear_cache(self, **kwargs):
        return ocpp_response.ClearCache(
            status="Accepted"
        )

    @on("ClearChargingProfile")
    def on_clear_charging_profile(self, **kwargs):
        return ocpp_response.ClearChargingProfile(
            status="Accepted"
        )

    @on("ClearDisplayMessage")
    def on_clear_display_message(self,id, **kwargs):
        return ocpp_response.ClearDisplayMessage(
            status="Accepted"
        )

    @on("ClearVariableMonitoring")
    def on_clear_variable_monitoring(self,id, **kwargs):
        return ocpp_response.ClearVariableMonitoring(
            clear_monitoring_result=[
                {
                    "status":"Accepted",
                    "id" : 5
                }
            ]
        )

    @on("CostUpdated")
    def on_cost_update(self,id,total_cost,transaction_id, **kwargs):
        return ocpp_response.CostUpdated(
        )

    @on("CustomerInformation")
    def on_customer_information(self,request_id,report,clear, **kwargs):
        return ocpp_response.CustomerInformation(
            status="Accepted"
        )

    @on("DataTransfer")
    def on_data_transfer(self,vendor_id, **kwargs):
        return ocpp_response.DataTransfer(
            status="Accepted"
        )

    @on("DeleteCertificate")
    def on_delete_certificate(self,certificate_hash_data, **kwargs):
        return ocpp_response.DeleteCertificate(
            status="Accepted"
        )

    @on("GetBaseReport")
    def on_get_base_report(self, request_id, report_base, **kwargs):
        return ocpp_response.GetBaseReport(
            status="Accepted"
        )

    @on("GetChargingProfiles")
    def on_get_charging_profiles(self, request_id, charging_profile, **kwargs):
        return ocpp_response.GetChargingProfiles(
            status="Accepted"
        )

    @on("GetCompositeSchedule")
    def on_get_composite_schedule(self, duration, evse_id, **kwargs):
        return ocpp_response.GetCompositeSchedule(
            status="Accepted"
        )

    @on("GetInstalledCertificateIds")
    def on_get_installed_certificate_ids(self,**kwargs):
        return ocpp_response.GetInstalledCertificateIds(
            status="Accepted"
        )

    @on("GetLocalListVersion")
    def on_get_local_list_version(self,**kwargs):
        return ocpp_response.GetLocalListVersion(
            version_number=201
        )

    @on("GetLog")
    def on_get_log(self,**kwargs):
        return ocpp_response.GetLog(
            status="Accepted"
        )

    @on("GetMonitoringReport")
    def on_get_monitoring_report(self, request_id,**kwargs):
        return ocpp_response.GetMonitoringReport(
            status="Accepted"
        )

    @on("GetReport")
    def on_get_report(self,request_id,**kwargs):
        return ocpp_response.GetReport(
            status="Accepted"
        )

    @on("GetTransactionStatus")
    def on_get_transaction_status(self,**kwargs):
        return ocpp_response.GetTransactionStatus(
            messages_in_queue=True
        )

    @on("GetVariables")
    def on_get_variables(self, get_variable_data, **kwargs):
        return ocpp_response.GetVariables(
            
            get_variable_result=[
                {
                    "attributeStatus": "Accepted",
                    "component": {"name": "EVSE"},
                    "variable": {"name": "VariableName"}
                }
            ]
        )

    @on("InstallCertificate")
    def on_install_certificate(self, certificate,certificate_type, **kwargs):
        return ocpp_response.InstallCertificate(
            status="Accepted"
        )

    @on("PublishFirmware")
    def on_publish_firmware(self, location,checksum,request_id, **kwargs):
        return ocpp_response.PublishFirmware(
            status="Accepted"
        )

    @on("RequestStartTransaction")
    def on_request_start_transaction(self, id_token,remote_start_id, **kwargs):
        return ocpp_response.RequestStartTransaction(
            status="Accepted"
        )

    @on("RequestStopTransaction")
    def on_request_stop_transaction(self, transaction_id,**kwargs):
        return ocpp_response.RequestStopTransaction(
            status="Accepted"
        )

    @on("ReserveNow")
    def on_reserve_now(self, id,expiry_date_time,id_token,**kwargs):
        return ocpp_response.ReserveNow(
            status="Accepted"
        )

    @on("Reset")
    def on_reset_request(self,type,**kwargs):
        return ocpp_response.Reset(
            status="Accepted"
        )    

    @on("SendLocalList")
    def on_send_local_list(self,version_number,update_type,**kwargs):
        return ocpp_response.SendLocalList(
            status="Accepted"
        )

    @on("SetChargingProfile")
    def on_send_set_charging_profile(self,evse_id,charging_profile,**kwargs):
        return ocpp_response.SetChargingProfile(
            status="Accepted"
        )

    @on("SetDisplayMessage")
    def on_send_set_display_message(self,message,**kwargs):
        return ocpp_response.SetDisplayMessage(
            status="Accepted"
        )

    @on("SetMonitoringBase")
    def on_set_monitoring_base(self,monitoring_base ,**kwargs):
        return ocpp_response.SetMonitoringBase(
            status="Accepted"
        )
        
    @on("SetMonitoringLevel")
    def on_set_monitoring_level(self,severity,**kwargs):
        return ocpp_response.SetMonitoringLevel(
            status="Accepted"
        )

    @on("SetNetworkProfile")
    def on_set_network_profile(self,configuration_slot,connection_data,**kwargs):
        return ocpp_response.SetNetworkProfile(
            status="Accepted"
        )

    @on("SetVariableMonitoring")
    def on_set_variable_monitoring(self, set_monitoring_data, **kwargs):
        return ocpp_response.SetVariableMonitoring(
            
            set_monitoring_result=[
                {
                "status":"Accepted",
                "type": "UpperThreshold",
                "severity": 9,
                "component": {"name": "ChargingStation"},
                "variable": {"name": "VariableName"}
                }
            ]
        )

    @on("SetVariables")
    def on_set_variables(self, set_variable_data, **kwargs):
        set_variable_results = []
        for variable in set_variable_data:
            # Process each variable and determine the result status
            result_status = "Accepted"  # This should be determined based on your logic
            set_variable_results.append({
                "attributeStatus": result_status,
                "component": variable["component"],
                "variable": variable["variable"]
            })
        return ocpp_response.SetVariables(
            set_variable_result=set_variable_results
        )

    @on("TriggerMessage")
    def on_trigger_message(self,requested_message, **kwargs):
        return ocpp_response.TriggerMessage(
            status="Accepted"
        )

    @on("UnlockConnector")
    def on_unlock_connector(self,evse_id,connector_id,**kwargs):
        return ocpp_response.UnlockConnector(
            status="Unlocked"
        )

    @on("UnpublishFirmware")
    def on_unpublish_firmware(self,checksum, **kwargs):
        return ocpp_response.UnpublishFirmware(
            status="DownloadOngoing"
        )

    @on("UpdateFirmware")
    def on_update_firmware(self,request_id,firmware,retries,**kwargs):
        # print("Firmware update request received. Download from:",firmware("location"))
        # Here you would add the logic to download and apply the firmware
        return ocpp_response.UpdateFirmware(
            status="Accepted"
        )

async def api_handle(charge_point):
    loop = asyncio.get_running_loop()
    while True:
        user_input = int(await loop.run_in_executor(None, input, "Enter a valid number (1: Boot Notification, 2: Heartbeat): "))
        if user_input == 1:
            await charge_point.send_authorize()
            
        elif user_input == 2:
            await charge_point.send_boot_notification()
            
        elif user_input == 3:
            await charge_point.send_cleared_charging_limit()
            
        elif user_input == 4:
            await charge_point.send_data_transfer()
            
        elif user_input == 5:
            await charge_point.send_firmware_status_notification()
            
        elif user_input == 6:
            await charge_point.send_get_15118_ev_certificate()
            
        elif user_input == 7:
            await charge_point.send_get_certificate_status()
            
        elif user_input == 8:
            await charge_point.send_get_display_messages()
            
        elif user_input == 9:
            await charge_point.send_heartbeat(5)
            
        elif user_input == 10:
            await charge_point.send_log_status_notification()
            
        elif user_input == 11:
            await charge_point.send_meter_values()
            
        elif user_input == 12:
            await charge_point.send_notify_charging_limit()
            
        elif user_input == 13:
            await charge_point.send_notify_customer_information()
            
        elif user_input == 14:
            await charge_point.send_notify_display_messages()
            
        elif user_input == 15:
            await charge_point.send_notify_ev_charging_needs()
            
        elif user_input == 16:
            await charge_point.send_notify_ev_charging_schedule()
            
        elif user_input == 17:
            await charge_point.send_notify_event()
            
        elif user_input == 18:
            await charge_point.send_notify_monitoring_report()
            
        elif user_input == 19:
            await charge_point.send_notify_report()
            
        elif user_input == 20:
            await charge_point.send_publish_firmware_status_notification()
            
        elif user_input == 21:
            await charge_point.send_report_charging_profiles()
            
        elif user_input == 22:
            await charge_point.send_reservation_status_update()
            
        elif user_input == 23:
            await charge_point.send_security_event_notification()
            
        elif user_input == 24:
            await charge_point.send_sign_certificate()
            
        elif user_input == 25:
            await charge_point.send_status_notification()
            
        elif user_input == 26:
            await charge_point.send_transaction_event()
            
        else:
            logging.warning("Invalid number entered. Please try again.")

    
async def main():
    async with websockets.connect(
        "ws://10.10.0.221:8765/CP_1", subprotocols=["ocpp2.0.1"]
    ) as ws:
        print(ws)
        charge_point = ChargePoint("CP_1", ws)
        api_event=asyncio.ensure_future(api_handle(charge_point))
        await asyncio.gather(
            charge_point.start(),api_event
        )

if __name__ == "__main__":
    # asyncio.run() is used when running this example with Python >= 3.7v
    asyncio.run(main())
