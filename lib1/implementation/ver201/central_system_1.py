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
    
    """! The ChargePoint base class.
    Defines the base class utilized by all OCPP APIS.
    """
    
    
    
    
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

    @on("DataTransfer")
    def on_data_transfer(self,vendor_id, **kwargs):
        return ocpp_response.DataTransfer(
            status="Accepted"
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

    @on("NotifyEVChargingSchedule")
    def on_notify_ev_charging_schedule(self,time_base,evse_id,charging_schedule,**kwargs):
        return ocpp_response.NotifyEVChargingSchedule(
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

    @on("PublishFirmwareStatusNotification")
    def on_publish_firmware_status_notification(self,status,**kwargs):
        return ocpp_response.PublishFirmwareStatusNotification(
        )

    @on("ReportChargingProfiles")
    def on_report_charging_profiles(self,request_id,charging_limit_source,charging_profile,evse_id,**kwargs):
        return ocpp_response.ReportChargingProfiles(
        )

    @on("ReservationStatusUpdate")
    def on_reservation_status_update(self,reservation_id,reservation_update_status):
        return ocpp_response.ReservationStatusUpdate(
        )

    @on("SecurityEventNotification")
    def on_security_event_notification(self,type,timestamp,**kwargs):
        return ocpp_response.SecurityEventNotification(
        )

    @on("SignCertificate")
    def on_sign_certificate(self,csr,**kwargs):
        return ocpp_response.SignCertificate(
            status="Accepted"
        )

    @on("StatusNotification")
    def on_status_notification(self,timestamp,connector_status,evse_id,connector_id,**kwargs):
        return ocpp_response.StatusNotification(
        )

    @on("TransactionEvent")
    def on_transaction_event(self,event_type,timestamp,trigger_reason,seq_no,transaction_info,**kwargs):
        return ocpp_response.TransactionEvent(
        )










    async def send_cancel_reservation(self,reservation_id_value):
        """
        @brief Sends a CancelReservation request to the charge point system.
        
        This method sends a CancelReservation request using the provided
        reservation ID. It waits for a response from the charge point system
        and prints the response status.
        
        @param reservation_id_value The ID of the reservation to be canceled.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a CancelReservation request with the given reservation
        ID and sends it to the charge point system. It then waits for the response.
        If the response status is "Accepted", it prints a success message.
        
        Example usage:
        @code
        await your_instance.send_cancel_reservation(12345)
        @endcode
        """
        request = ocpp_request.CancelReservation(
            reservation_id = reservation_id_value
        )
        print(request)
        response = await self.call(request)
        print(response)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'cancelReservation' ")

    async def send_certificate_signed(self,certificate_chain_value):
        """
        @brief Sends a CertificateSigned request to the charge point system.
        
        This method sends a CertificateSigned request using the provided
        certificate chain. It waits for a response from the charge point system
        and prints a message if the response status is "Accepted".
        
        @param certificate_chain_value The certificate chain to be signed.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a CertificateSigned request with the given certificate
        chain, sends it to the charge point system, and waits for the response. If
        the response status is "Accepted", it prints a success message.
        
        Example usage:
        @code
        await charge_point.send_certificate_signed("YourCertificateChain")
        @endcode
        """
        request = ocpp_request.CertificateSigned(
            certificate_chain = certificate_chain_value
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'certificate signed' ")

    async def send_change_availability(self,operational_status_value):
        """
        @brief Sends a ChangeAvailability request to the charge point system.
        
        This method sends a ChangeAvailability request using the provided
        operational status. It waits for a response from the charge point system.
        
        @param operational_status_value The desired operational status for the charge point.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a ChangeAvailability request with the given operational status,
        sends it to the charge point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_change_availability("Inoperative")
        @endcode
        """
        request = ocpp_request.ChangeAvailability(
            operational_status = operational_status_value
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'Change available' ")

    async def send_clear_cache(self):
        """
        @brief Sends a ClearCache request to the charge point system.
        
        This method sends a ClearCache request. It waits for a response
        from the charge point system.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a ClearCache request, sends it to the charge
        point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_clear_cache()
        @endcode
        """
        request = ocpp_request.ClearCache(
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'clear cache' ")

    async def send_clear_charging_profile(self):
        """
        @brief Sends a ClearChargingProfile request to the charge point system.
        
        This method sends a ClearChargingProfile request. It waits for a response
        from the charge point system.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a ClearChargingProfile request, sends it to the charge
        point system, and waits for the response.
        
        Example usage:
        @code
        await your_instance.send_clear_charging_profile()
        @endcode
        """
        request = ocpp_request.ClearChargingProfile(
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'Clear Charging Profile' ")

    async def send_clear_display_message(self,id_value):
        """
        @brief Sends a ClearDisplayMessage request to the charge point system.
        
        This method sends a ClearDisplayMessage request using the provided
        ID. It waits for a response from the charge point system.
        
        @param id_value The ID of the display message to be cleared.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a ClearDisplayMessage request with the given ID,
        sends it to the charge point system, and waits for the response.
        
        Example usage:
        @code
        await your_instance.send_clear_display_message(123)
        @endcode
        """
        request = ocpp_request.ClearDisplayMessage(
            id=id_value
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'Clear Display Message' ")

    async def send_clear_variable_monitoring(self,id_list_value):
        """
        @brief Sends a ClearVariableMonitoring request to the charge point system.
        
        This method sends a ClearVariableMonitoring request using the provided
        list of IDs. It waits for a response from the charge point system.
        
        @param id_list_value A list of IDs to clear variable monitoring for.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a ClearVariableMonitoring request with the given list
        of IDs, sends it to the charge point system, and waits for the response.
        
        Example usage:
        @code
        await your_instance.send_clear_variable_monitoring([1, 2, 3])
        @endcode
        """
        request = ocpp_request.ClearVariableMonitoring(
            id = id_list_value
        )
        response = await self.call(request)
        if response.clear_monitoring_result[0].get("status") == "Accepted":
            print("Connected to chargepoint system 'Clear Variable Monitoringt")
        else:
            print("Connected to chargepoint system 'Clear Variable Monitoringt,error")

    async def send_cost_updated(self,total_cost_value,transaction_id_value):
        """
        @brief Sends a CostUpdated request to the charge point system.
        
        This method sends a CostUpdated request using the provided total cost and
        transaction ID. It waits for a response from the charge point system.
        
        @param total_cost_value The updated total cost.
        @param transaction_id_value The ID of the transaction.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a CostUpdated request with the given total cost and
        transaction ID, sends it to the charge point system, and waits for the response.
        
        Example usage:
        @code
        await your_instance.send_cost_updated(15.75, "12345")
        @endcode
        """
        request = ocpp_request.CostUpdated(
            total_cost= total_cost_value,
            transaction_id=transaction_id_value
        )
        response = await self.call(request)
        if response == None:
            print("Connected to chargepoint system 'cost update'")
        else:
            print("Connected to chargepoint system 'cost update',error")

    async def send_customer_information(self,request_id_value,report_value,clear_value):
        """
        @brief Sends a CustomerInformation request to the charge point system.
        
        This method sends a CustomerInformation request using the provided
        request ID, report, and clear values. It waits for a response from the
        charge point system.
        
        @param request_id_value The ID of the customer information request.
        @param report_value Indicates whether to report customer information.
        @param clear_value Indicates whether to clear the customer information.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a CustomerInformation request with the given request ID,
        report, and clear values, sends it to the charge point system, and waits for
        the response.
        
        Example usage:
        @code
        await your_instance.send_customer_information(1, True, False)
        @endcode
        """
        request = ocpp_request.CustomerInformation(
            request_id=request_id_value,
            report=report_value,
            clear=clear_value
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'Customer Information'")
        else:
            print("Connected to chargepoint system 'Customer Information',error")

    async def send_data_transfer(self,vendor_id_value):
        """
        @brief Sends a DataTransfer request to the charge point system.
        
        This method sends a DataTransfer request using the provided vendor ID.
        It waits for a response from the charge point system.
        
        @param vendor_id_value The vendor ID for the data transfer.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a DataTransfer request with the given vendor ID, sends
        it to the charge point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_data_transfer("Vendor123")
        @endcode
        """
        request = ocpp_request.DataTransfer(
            vendor_id=vendor_id_value
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'Data Transfer'")
        else:
            print("Connected to chargepoint system 'Data Transfer',error")

    async def send_delete_certificate(self,certificate_hash_data_value):
        """
        @brief Sends a DeleteCertificate request to the charge point system.
        
        This method sends a DeleteCertificate request using the provided
        certificate hash data. It waits for a response from the charge point system.
        
        @param certificate_hash_data_value The hash data of the certificate to be deleted.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a DeleteCertificate request with the given certificate hash data,
        sends it to the charge point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_delete_certificate("YourCertificateHashData")
        @endcode
        """
        request = ocpp_request.DeleteCertificate(
            certificate_hash_data=certificate_hash_data_value
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'Delete Certificate'")
        else:
            print("Connected to chargepoint system 'Delete Certificate',error")

    async def send_get_base_report(self,request_id_value,report_base_value):
        """
        @brief Sends a GetBaseReport request to the charge point system.
        
        This method sends a GetBaseReport request using the provided
        request ID and report base. It waits for a response from the charge point system.
        
        @param request_id_value The ID of the request.
        @param report_base_value The base of the report to be retrieved.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a GetBaseReport request with the given request ID and report base,
        sends it to the charge point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_get_base_report(123, "ConfigurationInventory")
        @endcode
        """
        request = ocpp_request.GetBaseReport(
            request_id= request_id_value,
            report_base= report_base_value
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'get base report")
            

    async def send_get_charging_profiles(self,request_id_value,charging_profile_value):
        """
        @brief Sends a GetChargingProfiles request to the charge point system.
        
        This method sends a GetChargingProfiles request using the provided
        request ID and charging profile. It waits for a response from the charge point system.
        
        @param request_id_value The ID of the request.
        @param charging_profile_value The charging profile to be retrieved.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a GetChargingProfiles request with the given request ID and
        charging profile, sends it to the charge point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_get_charging_profiles(123, "YourChargingProfile")
        @endcode
        """
        request = ocpp_request.GetChargingProfiles(
            request_id=request_id_value,
            charging_profile=charging_profile_value
        )
        
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'Get Charging Profiles' ")

    async def send_get_composite_schedule(self,duration_value,evse_id_value):
        """
        @brief Sends a GetCompositeSchedule request to the charge point system.
        
        This method sends a GetCompositeSchedule request using the provided
        duration and EVSE ID. It waits for a response from the charge point system.
        
        @param duration_value The duration for which to get the composite schedule.
        @param evse_id_value The ID of the EVSE for which to get the composite schedule.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a GetCompositeSchedule request with the given duration and
        EVSE ID, sends it to the charge point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_get_composite_schedule(60, 1)
        @endcode
        """
        request = ocpp_request.GetCompositeSchedule(
            duration=duration_value,
            evse_id=evse_id_value
        )
        
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'GetCompositeSchedule'")

    async def send_get_installed_certificate_ids(self):
        """
        @brief Sends a GetInstalledCertificateIds request to the charge point system.
        
        This method sends a GetInstalledCertificateIds request. It waits for a response
        from the charge point system.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a GetInstalledCertificateIds request, sends it to the charge
        point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_get_installed_certificate_ids()
        @endcode
        """
        request = ocpp_request.GetInstalledCertificateIds(
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'Get Installed Certificate Ids'")

    async def send_get_local_list_version(self):
        """
        @brief Sends a GetLocalListVersion request to the charge point system.
        
        This method sends a GetLocalListVersion request. It waits for a response
        from the charge point system.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a GetLocalListVersion request, sends it to the charge
        point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_get_local_list_version()
        @endcode
        """
        request = ocpp_request.GetLocalListVersion(
        )
        response = await self.call(request)
        if response.version_number == 201:
            print("Connected to chargepoint system 'Get Local List Version'")

    async def send_get_log(self,log_value,log_type_value,request_id_value):
        """
        @brief Sends a GetLog request to the charge point system.
        
        This method sends a GetLog request using the provided log, log type,
        and request ID. It waits for a response from the charge point system.
        
        @param log_value The log data to be requested.
        @param log_type_value The type of log to be requested.
        @param request_id_value The ID of the request.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a GetLog request with the given log data, log type, and
        request ID, and sends it to the charge point system. It then waits for the response.
        
        Example usage:
        @code
        await charge_point.send_get_log("log_data", "log_type", 12345)
        @endcode
        """
        request = ocpp_request.GetLog(
            log=log_value,
            log_type=log_type_value,
            request_id=request_id_value
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'Get Log'")

    async def send_get_monitoring_report(self,request_id_value):
        """
        @brief Sends a GetMonitoringReport request to the charge point system.
        
        This method sends a GetMonitoringReport request with a predefined request ID.
        It waits for a response from the charge point system.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a GetMonitoringReport request with a request ID of 7, sends it to 
        the charge point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_get_monitoring_report()
        @endcode
        """
        request = ocpp_request.GetMonitoringReport(
            request_id=request_id_value
        )
        response = await self.call(request) 
        if response.status == "Accepted":
            print("Connected to chargepoint system 'get monitoring report' ")

    async def send_get_report(self,request_id_value):
        """
        @brief Sends a GetReport request to the charge point system.
        
        This method sends a GetReport request using the provided request ID. 
        It waits for a response from the charge point system.
        
        @param request_id_value The ID of the request.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a GetReport request with the given request ID, sends it to 
        the charge point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_get_report(12345)
        @endcode
        """
        request = ocpp_request.GetReport(
            request_id=request_id_value
        )
        response = await self.call(request) 
        if response.status == "Accepted":
            print("Connected to chargepoint system 'get monitoring report' ")

    async def send_get_transaction_status(self):
        """
        @brief Sends a GetTransactionStatus request to the charge point system.
        
        This method sends a GetTransactionStatus request. It waits for a response
        from the charge point system.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a GetTransactionStatus request, sends it to the charge
        point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_get_transaction_status()
        @endcode
        """
        request = ocpp_request.GetTransactionStatus(
        )
        response = await self.call(request) 
        if response.messages_in_queue == True:
            print("Connected to chargepoint system 'Get Transaction Status' ")
        

    async def send_get_variables(self,get_variable_data_value):
        """
        @brief Sends a GetVariables request to the charge point system.
        
        This method sends a GetVariables request. It waits for a response from the
        charge point system.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a GetVariables request with predefined variable data,
        sends it to the charge point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_get_variables([
                {
                    "component": {"name": "ChargingStation"},
                    "variable": {"name": "VariableName"}
                }
            ])
        @endcode
        """
        request = ocpp_request.GetVariables(
            get_variable_data=get_variable_data_value
            # custom_data= {"string": 5}
        )
        response = await self.call(request)
        
        if response.get_variable_result[0].get("attributeStatus") == "Accepted":
            print("Connected to chargepoint system 'get variables'")
        else:
            
            print("dharmik"+"response.get_variable_result[0].get('attributeStatus')")

    async def send_install_certificate(self,certificate_value,certificate_type_value):
        """
        @brief Sends an InstallCertificate request to the charge point system.
        
        This method sends an InstallCertificate request with a PEM encoded X.509 
        certificate and the specified certificate type. It waits for a response 
        from the charge point system.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates an InstallCertificate request with the provided certificate
        and certificate type, sends it to the charge point system, and waits for 
        the response.
        
        Example usage:
        @code
        await charge_point.send_install_certificate()
        @endcode
        """
        request = ocpp_request.InstallCertificate(
            certificate=certificate_value,
            certificate_type=certificate_type_value
        )
        response = await self.call(request)
        
        if response.status == "Accepted":
            print("Connected to chargepoint system 'InstallCertificate'")

    async def send_publish_firmware(self,location_value,checksum_value,request_id_value):
        """
        @brief Sends a PublishFirmware request to the charge point system.
        
        This method sends a PublishFirmware request with the provided location, 
        checksum, and request ID. It waits for a response from the charge point system.
        
        @param location_value The location of the firmware.
        @param checksum_value The checksum of the firmware.
        @param request_id_value The ID of the request.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a PublishFirmware request with the provided location,
        checksum, and request ID, sends it to the charge point system, and waits 
        for the response.
        
        Example usage:
        @code
        await charge_point.send_publish_firmware("http://example.com/firmware", "checksum123", 1)
        @endcode
        """
        request = ocpp_request.PublishFirmware(
            location=location_value,
            checksum=checksum_value,
            request_id=request_id_value
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'PublishFirmware'")

    async def send_request_start_transaction(self,id_token_value,remote_start_id_value):
        """
        @brief Sends a RequestStartTransaction request to the charge point system.
        
        This method sends a RequestStartTransaction request with the provided ID token
        and remote start ID. It waits for a response from the charge point system.
        
        @param id_token_value The ID token used for authorization.
        @param remote_start_id_value The ID used to remotely start the transaction.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a RequestStartTransaction request with the given ID token
        and remote start ID, sends it to the charge point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_request_start_transaction("token12345", 9876)
        @endcode
        """
        request = ocpp_request.RequestStartTransaction(
            id_token=id_token_value,
            remote_start_id=remote_start_id_value
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'RequestStartTransaction'")

    async def  send_request_stop_transaction(self,transaction_id_value):
        """
        @brief Sends a RequestStopTransaction request to the charge point system.
        
        This method sends a RequestStopTransaction request with the provided transaction ID.
        It waits for a response from the charge point system.
        
        @param transaction_id_value The ID of the transaction to be stopped.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a RequestStopTransaction request with the specified transaction ID,
        sends it to the charge point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_request_stop_transaction(12345)
        @endcode
        """
        request = ocpp_request.RequestStopTransaction(
            transaction_id = transaction_id_value
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Stop Transaction")

    async def  send_reserve_now(self,id_value,expiry_date_time_value,id_token_value):
        """
        @brief Sends a ReserveNow request to the charge point system.
        
        This method sends a ReserveNow request with the provided ID, expiry date/time,
        and ID token. It waits for a response from the charge point system.
        
        @param id_value The ID of the reservation.
        @param expiry_date_time_value The date and time when the reservation expires.
        @param id_token_value The ID token used for authorization.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a ReserveNow request with the provided parameters,
        sends it to the charge point system, and waits for the response.
        If the response status is "Accepted", it indicates that the reservation was successfully made.
        
        Example usage:
        @code
        await charge_point.send_reserve_now(1234, "2024-06-30T12:00:00Z", "token12345")
        @endcode
        """
        request = ocpp_request.ReserveNow(
            id = id_value,
            expiry_date_time = expiry_date_time_value,
            id_token=id_token_value
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'ReserveNow")

    async def send_reset_request(self,type_value):
        """
        @brief Sends a Reset request to the charge point system.
        
        This method sends a Reset request with the specified type. It waits for a
        response from the charge point system.
        
        @param type_value The type of reset to be performed (e.g., Hard, Soft, etc.).
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a Reset request with the provided type, sends it to the
        charge point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_reset_request("Hard")
        @endcode
        """
        request = ocpp_request.Reset(
            type=type_value      
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint reset request")

    async def send_send_local_list(self,version_number_value,update_type_value):
        """
        @brief Sends a SendLocalList request to the charge point system.
        
        This method sends a SendLocalList request with the provided version number
        and update type. It waits for a response from the charge point system.
        
        @param version_number_value The version number of the local list to be sent.
        @param update_type_value The type of update (Full, Differential, etc.) for the local list.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a SendLocalList request with the provided version number
        and update type, sends it to the charge point system, and waits for the response.
        If the response status is "Accepted", it indicates that the local list was successfully sent.
        
        Example usage:
        @code
        await charge_point.send_send_local_list(1, "Full")
        @endcode
        """
        request = ocpp_request.SendLocalList(
        version_number=version_number_value,
        update_type=update_type_value
            )
        response = await self.call(request)
        if response.status == "Accepted":
            print("connected to charge point on Send Local List Request")

    async def send_set_charging_profile(self,evse_id_value,charging_profile_value):
        """
        @brief Sends a SetChargingProfile request to the charge point system.
        
        This method sends a SetChargingProfile request with the provided EVSE ID
        and charging profile. It waits for a response from the charge point system.
        
        @param evse_id_value The ID of the EVSE for which the charging profile is to be set.
        @param charging_profile_value The charging profile to be set.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a SetChargingProfile request with the provided EVSE ID and
        charging profile, sends it to the charge point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_set_charging_profile(1, charging_profile)
        @endcode
        """
        request = ocpp_request.SetChargingProfile(
        evse_id = evse_id_value ,
        charging_profile = charging_profile_value
            )
        response = await self.call(request)
        if response.status == "Accepted":
            print("connected to charging point on Set charging profile")

    async def send_set_display_message(self,message_value):
        """
        @brief Sends a SetDisplayMessage request to the charge point system.
        
        This method sends a SetDisplayMessage request with the provided message.
        It waits for a response from the charge point system and checks if the 
        response status is "Accepted".
        
        @param message_value The message to be displayed.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a SetDisplayMessage request with the provided message,
        sends it to the charge point system, and waits for the response. If the
        response status is "Accepted", it proceeds accordingly.
        
        Example usage:
        @code
        await charge_point.send_set_display_message("Welcome to the charging station")
        @endcode
        """
        request = ocpp_request.SetDisplayMessage(
        message = message_value
            )
        response = await self.call(request)
        if response.status == "Accepted":
            print("connected to charging point on set display message")

    async def send_set_monitoring_base(self,monitoring_base_value):
        """
        @brief Sends a SetMonitoringBase request to the charge point system.
        
        This method sends a SetMonitoringBase request with the provided monitoring base.
        It waits for a response from the charge point system.
        
        @param monitoring_base_value The monitoring base to be set.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a SetMonitoringBase request with the given monitoring base,
        sends it to the charge point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_set_monitoring_base("ALL")
        @endcode
        """
        request = ocpp_request.SetMonitoringBase(
            monitoring_base=monitoring_base_value
        )
        response = await self.call(request) 
        if response.status == "Accepted":
            print("Connected to chargepoint system 'set monitoring base' ")
            
    async def send_set_monitoring_level(self,severity_value):
        """
        @brief Sends a SetMonitoringLevel request to the charge point system.
        
        This method sends a SetMonitoringLevel request with the provided severity level.
        It waits for a response from the charge point system and prints a message if the
        response status is "Accepted".
        
        @param severity_value The severity level to be set for monitoring.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a SetMonitoringLevel request with the given severity level,
        sends it to the charge point system, and waits for the response. If the response
        status is "Accepted", it prints a success message.
        
        Example usage:
        @code
        await charge_point.send_set_monitoring_level(3)
        @endcode
        """
        request = ocpp_request.SetMonitoringLevel(
            severity = severity_value
        )
        response = await self.call(request) 
        if response.status == "Accepted":
            print("Connected to chargepoint system 'set monitoring level' ")

    async def send_set_network_profile(self,configuration_slot_value,connection_data_value):
        """
        @brief Sends a SetNetworkProfile request to the charge point system.
        
        This method sends a SetNetworkProfile request with the provided configuration slot
        and connection data. It waits for a response from the charge point system.
        
        @param configuration_slot_value The slot for the network configuration.
        @param connection_data_value The data for the network connection.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a SetNetworkProfile request with the given configuration slot and
        connection data, sends it to the charge point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_set_network_profile(1, {
            "ocsp_requestor_url": "https://example.com/ocsp",
            "fqdn": "chargepoint.example.com",
            "username": "user",
            "password": "password"
        })
        @endcode
        """
        request = ocpp_request.SetNetworkProfile(
            configuration_slot = configuration_slot_value,
            connection_data = connection_data_value
            )
        response = await self.call(request)
        if response.status == "Accepted":
            print("connected to charging point on set network profile")

    async def send_set_variable_monitoring(self,set_monitoring_data_value):
        """
        @brief Sends a SetVariableMonitoring request to the charge point system.
        
        This method sends a SetVariableMonitoring request with the provided monitoring data.
        It waits for a response from the charge point system.
        
        @param set_monitoring_data_value The data for the variables to be monitored.
        
        @return Non
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a SetVariableMonitoring request with the given monitoring data,
        sends it to the charge point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_set_variable_monitoring([
            {
                "component": {"name": "ChargingStation"},
                "variable": {"name": "VariableName"},
                "monitoring_level": "Critical"
            }
        ])
        @endcode
        """
        request = ocpp_request.SetVariableMonitoring(
            set_monitoring_data=set_monitoring_data_value
            # custom_data= {"string": 5}
        )
        response = await self.call(request)
        
        if response.set_monitoring_result[0].get("status") == "Accepted":
            print("Connected to chargepoint 'set variable monitoring' ")
        else:
            
            print("dharmik",response.get_variable_result[0].get("attributeStatus"))
        # await request

    async def send_set_variables(self,set_variable_data_value):
        """
        @brief Sends a SetVariables request to the charge point system.
        
        This method sends a SetVariables request with the provided set variable data.
        It waits for a response from the charge point system.
        
        @param set_variable_data_value The data for the variables to be set.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a SetVariables request with the given set variable data,
        sends it to the charge point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_set_variables([
            {
                "component": {"name": "ChargingStation"},
                "variable": {"name": "VariableName"},
                "value": "NewValue"
            }
        ])
        @endcode
        """
        request = ocpp_request.SetVariables(
            set_variable_data=set_variable_data_value
        )
        response = await self.call(request)
        print(response)

    async def send_trigger_message(self,requested_message_value):
        """
        @brief Sends a TriggerMessage request to the charge point system.
        
        This method sends a TriggerMessage request with the provided requested message.
        It waits for a response from the charge point system.
        
        @param requested_message_value The requested message to be triggered.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates a TriggerMessage request with the given requested message,
        sends it to the charge point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_trigger_message("BootNotification")
        @endcode
        """
        request = ocpp_request.TriggerMessage(
            requested_message = requested_message_value
            )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Trigger message request accepted")
        else:
            print("Tigger message request rejected.")

    async def send_unlock_connector(self,evse_id_value,connector_id_value):
        """
        @brief Sends an UnlockConnector request to the charge point system.
        
        This method sends an UnlockConnector request with the provided EVSE ID
        and connector ID. It waits for a response from the charge point system.
        
        @param evse_id_value The EVSE ID of the connector to be unlocked.
        @param connector_id_value The connector ID to be unlocked.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates an UnlockConnector request with the given EVSE ID and
        connector ID, sends it to the charge point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_unlock_connector(1, 2)
        @endcode
        """
        request = ocpp_request.UnlockConnector(
            evse_id = evse_id_value,
            connector_id=connector_id_value
            )
        response = await self.call(request)
        if response.status == "Unlocked":
            print("Connector successfully unlocked.")
        elif response.status == "UnlockFailed":
            print("Failed to unlock connector.")
        elif response.status == "OngoingAuthorizedTransaction":
            print("Unlock failed due to ongoing authorized transaction.")
        elif response.status == "UnknownConnector":
            print("Unknown connector.")
        else:
            print("Unknown status received:", response.status)

    async def send_unpublish_firmware(self,checksum_value):
        """
        @brief Sends an UnpublishFirmware request to the charge point system.
        
        This method sends an UnpublishFirmware request with the provided checksum.
        It waits for a response from the charge point system.
        
        @param checksum_value The checksum of the firmware to be unpublished.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates an UnpublishFirmware request with the given checksum,
        sends it to the charge point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_unpublish_firmware("checksum12345")
        @endcode
        """
        request = ocpp_request.UnpublishFirmware(
            checksum=checksum_value
        )
        response = await self.call(request)
        if response.status=="Accepted" :
            print("UpdateFirmwareRequest")


    async def send_update_firmware(self,retries_value,request_id_value,firmware_value):
        """
        @brief Sends an UpdateFirmware request to the charge point system.
        
        This method sends an UpdateFirmware request with the provided retries, request ID,
        and firmware details. It waits for a response from the charge point system.
        
        @param retries_value The number of retries allowed for the firmware update.
        @param request_id_value The ID of the update firmware request.
        @param firmware_value The firmware details to be updated.
        
        @return None
        
        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.
        
        @details
        The method creates an UpdateFirmware request with the given retries, request ID,
        and firmware details, sends it to the charge point system, and waits for the response.
        
        Example usage:
        @code
        await charge_point.send_update_firmware(3, 12345, "firmware_v1.0")
        @endcode
        """
        request = ocpp_request.UpdateFirmware(
            retries=retries_value,
            request_id=request_id_value,
            firmware=firmware_value
        )
        response = await self.call(request)
        if response.status=="DownloadOngoing" :
            print("UpdateFirmwareRequest")








# async def api_handle(charge_point):
#     loop = asyncio.get_running_loop()
#     while True:
#         user_input = int(await loop.run_in_executor(None, input, "Enter a valid number (1: Boot Notification, 2: Heartbeat): "))
#         if user_input == 1:
            
#             await charge_point.send_cancel_reservation()
            
#         elif user_input == 2:
#             await charge_point.send_certificate_signed()
            
#         elif user_input == 3:
#             await charge_point.send_change_availability()
            
#         elif user_input == 4:
#             await charge_point.send_clear_cache()
            
#         elif user_input == 5:
#             await charge_point.send_clear_charging_profile()
            
#         elif user_input == 6:
#             await charge_point.send_clear_display_message()
            
#         elif user_input == 7:
#             await charge_point.send_clear_variable_monitoring()
            
#         elif user_input == 8:
#             await charge_point.send_cost_updated()
            
#         elif user_input == 9:
#             await charge_point.send_customer_information()
            
#         elif user_input == 10:
#             await charge_point.send_data_transfer()
            
#         elif user_input == 11:
#             await charge_point.send_delete_certificate()
            
#         elif user_input == 12:
#             await charge_point.send_get_base_report()
            
#         elif user_input == 13:
#             await charge_point.send_get_charging_profiles()
            
#         elif user_input == 14:
#             await charge_point.send_get_composite_schedule()
            
#         elif user_input == 15:
#             await charge_point.send_get_installed_certificate_ids()
            
#         elif user_input == 16:
#             await charge_point.send_get_local_list_version()
            
#         elif user_input == 17:
#             await charge_point.send_get_log()
            
#         elif user_input == 18:
#             await charge_point.send_get_monitoring_report()
            
#         elif user_input == 19:
#             await charge_point.send_get_report()
            
#         elif user_input == 20:
#             await charge_point.send_get_transaction_status()
            
#         elif user_input == 21:
#             await charge_point.send_get_variables()
            
#         elif user_input == 22:
#             await charge_point.send_install_certificate()
            
#         elif user_input == 23:
#             await charge_point.send_publish_firmware()
            
#         elif user_input == 24:
#             await charge_point.send_request_start_transaction()
            
#         elif user_input == 25:
#             await charge_point.send_request_stop_transaction()
            
#         elif user_input == 26:
#             await charge_point.send_reserve_now()
            
#         elif user_input == 27:
#             await charge_point.send_reset_request()
            
#         elif user_input == 28:
#             await charge_point.send_send_local_list()
            
#         elif user_input == 29:
#             await charge_point.send_set_charging_profile()
            
#         elif user_input == 30:
#             await charge_point.send_set_display_message()
            
#         elif user_input == 31:
#             await charge_point.send_set_monitoring_base()
            
#         elif user_input == 32:
#             await charge_point.send_set_monitoring_level()
            
#         elif user_input == 33:
#             await charge_point.send_set_network_profile()
            
#         elif user_input == 34:
#             await charge_point.send_set_variable_monitoring()
            
#         elif user_input == 35:
#             await charge_point.send_set_variables()
            
#         elif user_input == 36:
#             await charge_point.send_trigger_message()
            
#         elif user_input == 37:
#             await charge_point.send_unlock_connector()
            
#         elif user_input == 38:
#             await charge_point.send_unpublish_firmware()
            
#         elif user_input == 39:
#             await charge_point.send_update_firmware()
            
#         else:
#             logging.warning("Invalid number entered. Please try again.")



# async def on_connect(websocket, path):
#     """For every new charge point that connects, create a ChargePoint
#     instance and start listening for messages.
#     """
#     try:
#         requested_protocols = websocket.request_headers["Sec-WebSocket-Protocol"]
#     except KeyError:
#         logging.error("Client hasn't requested any Subprotocol. Closing Connection")
#         return await websocket.close()
#     if websocket.subprotocol:
#         logging.info("Protocols Matched: %s", websocket.subprotocol)
#     else:
#         # In the websockets lib if no subprotocols are supported by the
#         # client and the server, it proceeds without a subprotocol,
#         # so we have to manually close the connection.
#         logging.warning(
#             "Protocols Mismatched | Expected Subprotocols: %s,"
#             " but client supports %s | Closing connection",
#             websocket.available_subprotocols,
#             requested_protocols,
#         )
#         return await websocket.close()
#     charge_point_id = path.strip("/")
#     charge_point = ChargePoint(charge_point_id, websocket)
#     logging.info(f"New connection from {charge_point_id}")
#     api_event=asyncio.ensure_future(api_handle(charge_point))
#     await asyncio.gather(
#             charge_point.start(),api_event
#         )
    


# async def main():
#     #  deepcode ignore BindToAllNetworkInterfaces: <Example Purposes>
#     server = await websockets.serve(
#         on_connect, "10.10.0.221", 8765, subprotocols=["ocpp2.0.1"]
#     )
#     logging.info("Server Started listening to new connections...")
    
#     await server.wait_closed()


# if __name__ == "__main__":
#     # asyncio.run() is used when running this example with Python >= 3.7v
#     asyncio.run(main())
