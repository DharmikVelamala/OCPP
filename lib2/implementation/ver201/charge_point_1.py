"""
@brief Class representing a Charge Point in the OCPP (Open Charge Point Protocol) implementation.

This class handles various OCPP requests and responses between a Charge Point and a central system.

@details
The ChargePoint class manages communication with a central system, processing requests such as
start transaction, stop transaction, status notifications, firmware updates, etc.

Example usage:
@code
charge_point = ChargePoint(...)
charge_point.connect()
...
charge_point.disconnect()
@endcode
"""



import asyncio
import logging
from OCPP_LIB.ocpp_routing import on
import charge_point_responce_handler



from OCPP_LIB.ver201 import ChargePoint as cp
from OCPP_LIB.ver201 import ocpp_request
from OCPP_LIB.ver201 import ocpp_response

logging.basicConfig(level=logging.INFO)


class ChargePoint(cp):
    """! The ChargePoint base class.
    Defines the base class utilized by all OCPP APIS.
    
    @brief Class representing a Charge Point in the OCPP (Open Charge Point Protocol) implementation.
    This class handles various OCPP requests and responses between a Charge Point and a central system.
    
    @details
    The ChargePoint class manages communication with a central system, processing requests such as
    start transaction, stop transaction, status notifications, firmware updates, etc.
    """
    
    async def send_authorize(self,id_token_value):
        """
        @brief Sends an Authorize request to the charge point system.

        This method sends an Authorize request with the specified ID token
        to the charge point system.

        @param id_token_value The ID token for authorization.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates an Authorize request with the provided ID token,
        sends it to the charge point system, and waits for the response.

        Example usage:
        @code
        await charge_point.send_authorize("IDToken123")
        @endcode
        """
        request = ocpp_request.Authorize(
            id_token=id_token_value
        )
        response = await self.call(request)
        if response and hasattr(response, 'id_tag_info') and response.id_tag_info.get('status') == 'Accepted':
            print(f"Authorization accepted for ID token:")
        else:
            print(f"Authorization failed for ID token:. Response: {response}")

    async def send_boot_notification(self,charging_station_value,reason_value):
        """
        @brief Sends a BootNotification request to the charge point system.

        This method sends a BootNotification request with the specified
        charging station and reason to the charge point system.

        @param charging_station_value The identifier of the charging station.
        @param reason_value The reason for the boot notification.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a BootNotification request with the provided
        charging station identifier and reason, sends it to the charge point
        system, and waits for the response.

        Example usage:
        @code
        await charge_point.send_boot_notification("Station001", "PowerUp")
        @endcode
        """
        request = ocpp_request.BootNotification(
            charging_station=charging_station_value,
            reason=reason_value
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to central system 'boot notification'")
        # await self.send_heartbeat(response.interval)
        

    async def send_cleared_charging_limit(self,charging_limit_source_value):
        """
        @brief Sends a ClearedChargingLimit request to the charge point system.

        This method sends a ClearedChargingLimit request with the specified
        charging limit source to the charge point system.

        @param charging_limit_source_value The source of the cleared charging limit.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a ClearedChargingLimit request with the provided
        charging limit source, sends it to the charge point system, and waits
        for the response.

        Example usage:
        @code
        await charge_point.send_cleared_charging_limit("Source123")
        @endcode
        """
        request = ocpp_request.ClearedChargingLimit(
            charging_limit_source=charging_limit_source_value
        )
        response = await self.call(request)
        if response == None:
            print("Connected to central system'ClearedChargingLimit'")

    async def send_data_transfer(self,vendor_id_str_value):
        """
        @brief Sends a DataTransfer request to the charge point system.

        This method sends a DataTransfer request with the specified vendor ID string
        to the charge point system.

        @param vendor_id_str_value The vendor ID string for the data transfer.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a DataTransfer request with the provided vendor ID string,
        sends it to the charge point system, and waits for the response.

        Example usage:
        @code
        await charge_point.send_data_transfer("Vendor123")
        @endcode
        """
        request = ocpp_request.DataTransfer(
            vendor_id=vendor_id_str_value
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to chargepoint system 'Data Transfer'")
        else:
            print("Connected to chargepoint system 'Data Transfer',error")

    async def send_firmware_status_notification(self,status_value):
        """
        @brief Sends a FirmwareStatusNotification to the charge point system.

        This method sends a FirmwareStatusNotification with the specified status value
        to the charge point system.

        @param status_value The status value of the firmware update notification.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a FirmwareStatusNotification request with the provided status value,
        sends it to the charge point system, and waits for the response.

        Example usage:
        @code
        await charge_point.send_firmware_status_notification("Downloaded")
        @endcode
        """
        request = ocpp_request.FirmwareStatusNotification(
            status=status_value
        )
        response = await self.call(request)
        if response == None:
            print("Connected to central system'Firmware Status Notification'")

    async def send_get_15118_ev_certificate(self,iso15118_schema_version_value,action_value,exi_request_value):
        """
        @brief Sends a Get15118EVCertificate request to the charge point system.

        This method sends a Get15118EVCertificate request with the specified ISO 15118 schema version,
        action, and EXI request data to the charge point system.

        @param iso15118_schema_version_value The ISO 15118 schema version for the certificate request.
        @param action_value The action to be performed in relation to the certificate request.
        @param exi_request_value The EXI encoded certificate request data.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a Get15118EVCertificate request with the provided parameters,
        sends it to the charge point system, and waits for the response.

        Example usage:
        @code
        await charge_point.send_get_15118_ev_certificate("ISO15118-2", "request", "EXI request data")
        @endcode
        """
        request = ocpp_request.Get15118EVCertificate(
            iso15118_schema_version=iso15118_schema_version_value,
            action=action_value,
            exi_request=exi_request_value
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to central system'Get 15118 EV Certificaten'")

    async def send_get_certificate_status(self,ocsp_request_data_value):
        """
        @brief Sends a GetCertificateStatus request to the charge point system.

        This method sends a GetCertificateStatus request with the provided OCSP request data
        to retrieve the status of a certificate from the charge point system.

        @param ocsp_request_data_value The OCSP request data used to verify the certificate status.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a GetCertificateStatus request with the specified OCSP request data,
        sends it to the charge point system, and waits for the response.

        Example usage:
        @code
        await charge_point.send_get_certificate_status("OCSP request data")
        @endcode
        """
        request = ocpp_request.GetCertificateStatus(
            ocsp_request_data=ocsp_request_data_value
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to central system'GetCertificateStatus'")

    async def send_get_display_messages(self,request_id_value):
        """
        @brief Sends a GetDisplayMessages request to the charge point system.

        This method sends a GetDisplayMessages request with the provided request ID to
        retrieve display messages from the charge point system.

        @param request_id_value The ID of the request for retrieving display messages.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a GetDisplayMessages request with the specified request ID,
        sends it to the charge point system, and waits for the response.

        Example usage:
        @code
        await charge_point.send_get_display_messages(12345)
        @endcode
        """
        request = ocpp_request.GetDisplayMessages(
            request_id=request_id_value
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("Connected to central system'Get Display Messages'")

    async def send_heartbeat(self, interval):
        """
        @brief Sends periodic Heartbeat requests to the charge point system.

        This method sends Heartbeat requests at regular intervals to the charge point system.

        @param interval The interval (in seconds) between successive Heartbeat requests.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a Heartbeat request and sends it to the charge point system
        periodically with the specified interval. It uses asyncio's sleep function to control
        the timing between requests.

        Example usage:
        @code
        await charge_point.send_heartbeat(30)  # Sends Heartbeat requests every 30 seconds
        @endcode
        """
        request = ocpp_request.Heartbeat()
        while True:
            await self.call(request)
            await asyncio.sleep(interval)  

    async def send_log_status_notification(self,status_value):
        """
        @brief Sends a LogStatusNotification request to the charge point system.

        This method sends a LogStatusNotification request with the provided status.
        It waits for a response from the charge point system.

        @param status_value The status to be logged.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a LogStatusNotification request with the given status,
        sends it to the charge point system, and waits for the response.

        Example usage:
        @code
        await charge_point.send_log_status_notification("Uploaded")
        @endcode
        """
        request = ocpp_request.LogStatusNotification(
            status=status_value
        )
        response = await self.call(request)
        if response == None:
            print("Connected to central system'send_log_status_notification'")

    async def send_meter_values(self,evse_id_value,meter_value_value):
        """
        @brief Sends a MeterValues request to the charge point system.

        This method sends a MeterValues request with the specified EVSE ID and meter values
        to the charge point system.

        @param evse_id_value The ID of the EVSE (Electric Vehicle Supply Equipment).
        @param meter_value_value The meter values to be sent.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a MeterValues request with the provided EVSE ID and meter values,
        sends it to the charge point system, and waits for the response.

        Example usage:
        @code
        await charge_point.send_meter_values(evse_id, meter_values)
        @endcode
        """
        request = ocpp_request.MeterValues(
            evse_id=evse_id_value,
            meter_value=meter_value_value
        )
        response = await self.call(request)
        if response == None:
            print("Connected to central system'send_meter_values'")

    async def send_notify_charging_limit(self,charging_limit_value):
        """
        @brief Sends a NotifyChargingLimit request to the charge point system.

        This method sends a NotifyChargingLimit request with the specified charging limit
        to the charge point system.

        @param charging_limit_value The charging limit to be set.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a NotifyChargingLimit request with the provided charging limit,
        sends it to the charge point system, and waits for the response.

        Example usage:
        @code
        await charge_point.send_notify_charging_limit(charging_limit)
        @endcode
        """
        request = ocpp_request.NotifyChargingLimit(
            charging_limit=charging_limit_value
        )
        response = await self.call(request)
        if response == None:
            print("Connected to central system'NotifyChargingLimit'")

    async def send_notify_customer_information(self,data_value,seq_no_value,generated_at_value,request_id_value):
        """
        @brief Sends a NotifyCustomerInformation request to the charge point system.

        This method sends a NotifyCustomerInformation request with the specified data,
        sequence number, generated timestamp, and request ID to the charge point system.

        @param data_value The customer information data to be sent.
        @param seq_no_value The sequence number of the information.
        @param generated_at_value The timestamp when the information was generated.
        @param request_id_value The ID of the request.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a NotifyCustomerInformation request with the provided data,
        sequence number, generated timestamp, and request ID, sends it to the charge point
        system, and waits for the response.

        Example usage:
        @code
        await charge_point.send_notify_customer_information(data, seq_no, generated_at, request_id)
        @endcode
        """
        request = ocpp_request.NotifyCustomerInformation(
            data=data_value,
            seq_no=seq_no_value,
            generated_at=generated_at_value,
            request_id=request_id_value
        )
        response = await self.call(request)
        if response == None:
            print("Connected to central system'NotifyCustomerInformation'")

    async def send_notify_display_messages(self,request_id_value):
        """
        @brief Sends a NotifyDisplayMessages request to the charge point system.

        This method sends a NotifyDisplayMessages request with the specified request ID
        to the charge point system.

        @param request_id_value The ID of the request.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a NotifyDisplayMessages request with the provided request ID,
        sends it to the charge point system, and waits for the response.

        Example usage:
        @code
        await charge_point.send_notify_display_messages(1)
        @endcode
        """
        request = ocpp_request.NotifyDisplayMessages(
            request_id=request_id_value
        )
        response = await self.call(request)
        if response == None:
            print("connected to central system'NotifyDisplayMessages'")

    async def send_notify_ev_charging_needs(self,evse_id_value,charging_needs_value):
        """
        @brief Sends a NotifyEVChargingNeeds request to the charge point system.

        This method sends a NotifyEVChargingNeeds request with the specified EVSE ID
        and charging needs to the charge point system.

        @param evse_id_value The ID of the EVSE.
        @param charging_needs_value The charging needs of the electric vehicle.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a NotifyEVChargingNeeds request with the provided EVSE ID and
        charging needs, sends it to the charge point system, and waits for the response.

        Example usage:
        @code
        await charge_point.send_notify_ev_charging_needs(1, charging_needs)
        @endcode
        """
        request = ocpp_request.NotifyEVChargingNeeds(
            evse_id=evse_id_value,
            charging_needs=charging_needs_value
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("connected to central system'NotifyEVChargingNeeds'")

    async def send_notify_ev_charging_schedule(self,time_base_value,evse_id_value,charging_schedule_value):
        """
        @brief Sends a NotifyEVChargingSchedule request to the charge point system.

        This method sends a NotifyEVChargingSchedule request with the specified time base,
        EVSE ID, and charging schedule to the charge point system.

        @param time_base_value: The time base for the charging schedule notification.
        @param evse_id_value: The identifier of the EVSE for which the charging schedule applies.
        @param charging_schedule_value: The charging schedule data to be notified.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a NotifyEVChargingSchedule request with the provided parameters,
        sends it to the charge point system, and waits for the response.

        Example usage:
        @code
        await charge_point.send_notify_ev_charging_schedule("TimeBaseValue", "EVSEIdValue", "ChargingScheduleValue")
        @endcode
        """
        request = ocpp_request.NotifyEVChargingSchedule(
            time_base=time_base_value,
            evse_id=evse_id_value,
            charging_schedule=charging_schedule_value
        )
        response = await self.call(request)
        if response.status == "Accepted":
            print("connected to central system'NotifyEVChargingSchedule'")

    async def send_notify_event(self,generated_at_value,seq_no_value,event_data_value):
        """
        @brief Sends a NotifyEvent request to the charge point system.

        This method sends a NotifyEvent request with the specified generated at time,
        sequence number, and event data to the charge point system.

        @param generated_at_value: The timestamp indicating when the event was generated.
        @param seq_no_value: The sequence number of the event.
        @param event_data_value: Data associated with the event.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a NotifyEvent request with the provided parameters, sends it
        to the charge point system, and waits for the response.

        Example usage:
        @code
        await charge_point.send_notify_event("GeneratedAtValue", "SeqNoValue", "EventDataValue")
        @endcode
        """
        request = ocpp_request.NotifyEvent(
            generated_at=generated_at_value,
            seq_no=seq_no_value,
            event_data=event_data_value
        )
        response = await self.call(request)
        if response == None:
            print("connected to central system'NotifyEvent'")

    async def send_notify_monitoring_report(self,generated_at_value,seq_no_value,request_id_value):
        """
        @brief Sends a NotifyMonitoringReport request to the charge point system.

        This method sends a NotifyMonitoringReport request with the specified generated at time,
        sequence number, and request ID to the charge point system.

        @param generated_at_value: The timestamp indicating when the report was generated.
        @param seq_no_value: The sequence number of the report.
        @param request_id_value: The ID of the request.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a NotifyMonitoringReport request with the provided parameters, sends it
        to the charge point system, and waits for the response.

        Example usage:
        @code
        await charge_point.send_notify_monitoring_report("GeneratedAtValue", "SeqNoValue", "RequestIdValue")
        @endcode
        """
        request = ocpp_request.NotifyMonitoringReport(
            generated_at=generated_at_value,
            seq_no=seq_no_value,
            request_id=request_id_value
        )
        response = await self.call(request)
        if response == None:
            print("connected to central system'NotifyMonitoringReport'")

    async def send_notify_report(self,generated_at_value,seq_no_value,request_id_value):
        """
        @brief Sends a NotifyReport request to the charge point system.

        This method sends a NotifyReport request with the specified generated at time,
        sequence number, and request ID to the charge point system.

        @param generated_at_value: The timestamp indicating when the report was generated.
        @param seq_no_value: The sequence number of the report.
        @param request_id_value: The ID of the request.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a NotifyReport request with the provided parameters, sends it
        to the charge point system, and waits for the response.

        Example usage:
        @code
        await charge_point.send_notify_report("GeneratedAtValue", "SeqNoValue", "RequestIdValue")
        @endcode
        """
        request = ocpp_request.NotifyReport(
            generated_at=generated_at_value,
            seq_no=seq_no_value,
            request_id=request_id_value
        )
        response = await self.call(request)
        if response == None:
            print("connected to central system'NotifyReport'")

    async def send_publish_firmware_status_notification(self,status_value):
        """
        @brief Sends a PublishFirmwareStatusNotification request to the charge point system.

        This method sends a PublishFirmwareStatusNotification request with the specified status
        to the charge point system.

        @param status_value: The status of the firmware publication.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a PublishFirmwareStatusNotification request with the provided status,
        sends it to the charge point system, and waits for the response.

        Example usage:
        @code
        await charge_point.send_publish_firmware_status_notification("StatusValue")
        @endcode
        """
        request = ocpp_request.PublishFirmwareStatusNotification(
            status=status_value
        )
        response = await self.call(request)
        if response == None:
            print("connected to central system'publish_firmware_status_notification'")

    async def send_report_charging_profiles(self,request_id_value,charging_limit_source_value,charging_profile_value,evse_id_value):
        """
        @brief Sends a ReportChargingProfiles request to the charge point system.

        This method sends a ReportChargingProfiles request with specified request ID, 
        charging limit source, charging profile, and EVSE ID to the charge point system.

        @param request_id_value: The ID of the request.
        @param charging_limit_source_value: The source of the charging limit.
        @param charging_profile_value: The charging profile to report.
        @param evse_id_value: The ID of the EVSE associated with the charging profile.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a ReportChargingProfiles request with the provided request ID, 
        charging limit source, charging profile, and EVSE ID, sends it to the charge point system, 
        and waits for the response.

        Example usage:
        @code
        await charge_point.send_report_charging_profiles("RequestIDValue", "ChargingLimitSourceValue", "ChargingProfileValue", "EVSEIDValue")
        @endcode
        """
        request = ocpp_request.ReportChargingProfiles(
            request_id=request_id_value,
            charging_limit_source=charging_limit_source_value,
            charging_profile=charging_profile_value,
            evse_id=evse_id_value
        )
        response = await self.call(request)
        if response == None:
            print("connected to central system'report_charging_profiles'")

    async def send_reservation_status_update(self,reservation_id_value,reservation_update_status_value):
        """
        @brief Sends a ReservationStatusUpdate request to the charge point system.

        This method sends a ReservationStatusUpdate request with a specified reservation ID 
        and update status to the charge point system.

        @param reservation_id_value: The ID of the reservation being updated.
        @param reservation_update_status_value: The updated status of the reservation.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a ReservationStatusUpdate request with the provided reservation ID 
        and update status, sends it to the charge point system, and waits for the response.

        Example usage:
        @code
        await charge_point.send_reservation_status_update("ReservationIDValue", "UpdateStatusValue")
        @endcode
        """
        request = ocpp_request.ReservationStatusUpdate(
            reservation_id = reservation_id_value,
            reservation_update_status= reservation_update_status_value
        )
        response = await self.call(request)
        if response == None:
            print("connected to central system'send_reservation_status_update'")

    async def send_security_event_notification(self,type_value,timestamp_value):
        """
        @brief Sends a SecurityEventNotification request to the charge point system.

        This method sends a SecurityEventNotification request with a specified type and timestamp 
        to the charge point system.

        @param type_value: The type of security event being reported.
        @param timestamp_value: The timestamp when the security event occurred.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a SecurityEventNotification request with the provided type and timestamp, 
        sends it to the charge point system, and waits for the response.

        Example usage:
        @code
        await charge_point.send_security_event_notification("TypeValue", "TimestampValue")
        @endcode
        """
        request = ocpp_request.SecurityEventNotification(
        type = type_value,
        timestamp = timestamp_value
            )
        response = await self.call(request)
        if response == None:
            print("connected to central system on Security event notification")

    async def send_sign_certificate(self):
        """
        @brief Sends a SignCertificate request to the charge point system.

        This method sends a SignCertificate request with a Certificate Signing Request (CSR) 
        to the charge point system.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a SignCertificate request with a provided CSR, sends it to the charge point 
        system, and waits for the response.

        Example usage:
        @code
        await charge_point.send_sign_certificate()
        @endcode
        """
        request = ocpp_request.SignCertificate(
            csr = "bjcverhvijejbvbnktejbcjf"
            )
        response = await self.call(request)
        if response.status == "Accepted":
            print("connected to central system on sign certificate ")

    async def send_status_notification(self,timestamp_value,connector_status_value,evse_id_value,connector_id_value):
        """
        @brief Sends a StatusNotification request to the charge point system.

        This method sends a StatusNotification request with the specified parameters to the
        charge point system.

        @param timestamp_value The timestamp of the status notification.
        @param connector_status_value The status of the connector (e.g., Available, Occupied).
        @param evse_id_value The ID of the EVSE.
        @param connector_id_value The ID of the connector.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a StatusNotification request with the provided timestamp, connector status,
        EVSE ID, and connector ID, sends it to the charge point system, and waits for the response.

        Example usage:
        @code
        await charge_point.send_status_notification(timestamp, connector_status, evse_id, connector_id)
        @endcode
        """
        request = ocpp_request.StatusNotification(
            timestamp =timestamp_value,
            connector_status = connector_status_value,
            evse_id = evse_id_value,
            connector_id = connector_id_value
    )
        response = await self.call(request)
        if response==None:
            print("Connected to chargepoint system ' send_status_notification '")

    async def send_transaction_event(self,event_type_value,timestamp_value,trigger_reason_value,seq_no_value,transaction_info_value):
        """
        @brief Sends a TransactionEvent request to the charge point system.

        This method sends a TransactionEvent request with the specified parameters to the
        charge point system.

        @param event_type_value The type of the event (e.g., Started, Updated, Ended).
        @param timestamp_value The timestamp of the event.
        @param trigger_reason_value The reason for triggering the event.
        @param seq_no_value The sequence number of the event.
        @param transaction_info_value The information about the transaction.

        @return None

        @exception ocpp.v201.exceptions.OCPPError If there is an error in the OCPP call.

        @details
        The method creates a TransactionEvent request with the provided event type, timestamp,
        trigger reason, sequence number, and transaction information, sends it to the charge point system, and waits for the response.

        Example usage:
        @code
        await charge_point.send_transaction_event(event_type, timestamp, trigger_reason, seq_no, transaction_info)
        @endcode
        """
        request = ocpp_request.TransactionEvent(
            event_type = event_type_value,
            timestamp= timestamp_value,
            trigger_reason=trigger_reason_value,
            seq_no = seq_no_value,
            transaction_info=transaction_info_value
            )
        response = await self.call(request)
        if response==None:
            print("Connected to chargepoint system ' send_transaction_event '")






    @on("CancelReservation")
    def on_cancel_reservation(self,reservation_id, **kwargs):
        """
        @brief Handles the CancelReservation request from the central system.

        This method is triggered when a CancelReservation request is received from the central system.
        It processes the reservation cancellation using the charge point response handler.

        @param reservation_id: The ID of the reservation to be canceled.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.CancelReservation: The response to the CancelReservation request.

        @details
        The method invokes the charge point response handler to process the CancelReservation request
        with the provided reservation ID and any additional keyword arguments. It then returns a 
        CancelReservation response with the status of the cancellation.

        Example usage:
        @code
        charge_point.on_cancel_reservation(reservation_id)
        @endcode
        """
        status_value=charge_point_responce_handler.cancel_reservation(reservation_id, **kwargs)
        return ocpp_response.CancelReservation(
            status=status_value
        )

    @on("CertificateSigned")
    def on_certificate_signed(self,certificate_chain, **kwargs):
        """
        @brief Handles the CertificateSigned request from the central system.

        This method is triggered when a CertificateSigned request is received from the central system.
        It processes the signed certificate chain using the charge point response handler.

        @param certificate_chain: The chain of signed certificates.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.CertificateSigned: The response to the CertificateSigned request.

        @details
        The method invokes the charge point response handler to process the CertificateSigned request
        with the provided certificate chain and any additional keyword arguments. It then returns a 
        CertificateSigned response with the status of the certificate signing process.

        Example usage:
        @code
        charge_point.on_certificate_signed(certificate_chain)
        @endcode
        """
        status_value=charge_point_responce_handler.certificate_signed(certificate_chain, **kwargs)
        return ocpp_response.CertificateSigned(
            status=status_value
        )

    @on("ChangeAvailability")
    def on_change_availability(self,operational_status, **kwargs):
        """
        @brief Handles the ChangeAvailability request from the central system.

        This method is triggered when a ChangeAvailability request is received from the central system.
        It processes the change in operational status using the charge point response handler.

        @param operational_status: The new operational status of the charge point (e.g., Operative, Inoperative).
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.ChangeAvailability: The response to the ChangeAvailability request.

        @details
        The method invokes the charge point response handler to process the ChangeAvailability request
        with the provided operational status and any additional keyword arguments. It then returns a 
        ChangeAvailability response with the status of the availability change process.

        Example usage:
        @code
        charge_point.on_change_availability(operational_status)
        @endcode
        """
        status_value=charge_point_responce_handler.change_availability(operational_status, **kwargs)
        return ocpp_response.ChangeAvailability(
            status=status_value
        )

    @on("ClearCache")
    def on_clear_cache(self, **kwargs):
        """
        @brief Handles the ClearCache request from the central system.

        This method is triggered when a ClearCache request is received from the central system.
        It processes the request to clear the cache using the charge point response handler.

        @param kwargs: Additional keyword arguments.
        @return ocpp_response.ClearCache: The response to the ClearCache request.

        @details
        The method invokes the charge point response handler to process the ClearCache request
        with any additional keyword arguments. It then returns a ClearCache response with the status
        of the cache clearing process.

        Example usage:
        @code
        charge_point.on_clear_cache()
        @endcode
        """
        status_value=charge_point_responce_handler.clear_cache(**kwargs)
        return ocpp_response.ClearCache(
            status=status_value
        )

    @on("ClearChargingProfile")
    def on_clear_charging_profile(self, **kwargs):
        """
        @brief Handles the ClearChargingProfile request from the central system.

        This method is triggered when a ClearChargingProfile request is received from the central system.
        It processes the request to clear the charging profile using the charge point response handler.

        @param kwargs: Additional keyword arguments.
        @return ocpp_response.ClearChargingProfile: The response to the ClearChargingProfile request.

        @details
        The method invokes the charge point response handler to process the ClearChargingProfile request
        with any additional keyword arguments. It then returns a ClearChargingProfile response with the 
        status of the charging profile clearing process.

        Example usage:
        @code
        charge_point.on_clear_charging_profile()
        @endcode
        """
        status_value=charge_point_responce_handler.clear_charging_profile(**kwargs)
        return ocpp_response.ClearChargingProfile(
            status=status_value
        )

    @on("ClearDisplayMessage")
    def on_clear_display_message(self,id, **kwargs):
        """
        @brief Handles the ClearDisplayMessage request from the central system.

        This method is triggered when a ClearDisplayMessage request is received from the central system.
        It processes the request to clear a display message using the charge point response handler.

        @param id: The ID of the display message to be cleared.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.ClearDisplayMessage: The response to the ClearDisplayMessage request.

        @details
        The method invokes the charge point response handler to process the ClearDisplayMessage request
        with the provided display message ID and any additional keyword arguments. It then returns a 
        ClearDisplayMessage response with the status of the display message clearing process.

        Example usage:
        @code
        charge_point.on_clear_display_message(id)
        @endcode
        """
        status_value=charge_point_responce_handler.clear_display_message(id,**kwargs)
        return ocpp_response.ClearDisplayMessage(
            status=status_value
        )

    @on("ClearVariableMonitoring")
    def on_clear_variable_monitoring(self,id, **kwargs):
        """
        @brief Handles the ClearVariableMonitoring request from the central system.

        This method is triggered when a ClearVariableMonitoring request is received from the central system.
        It processes the request to clear variable monitoring using the charge point response handler.

        @param id: The ID of the variable monitoring to be cleared.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.ClearVariableMonitoring: The response to the ClearVariableMonitoring request.

        @details
        The method invokes the charge point response handler to process the ClearVariableMonitoring request
        with the provided variable monitoring ID and any additional keyword arguments. It then returns a 
        ClearVariableMonitoring response with the result of the variable monitoring clearing process.

        Example usage:
        @code
        charge_point.on_clear_variable_monitoring(id)
        @endcode
        """
        clear_monitoring_result_value=charge_point_responce_handler.clear_variable_monitoring(id,**kwargs)
        return ocpp_response.ClearVariableMonitoring(
            clear_monitoring_result=clear_monitoring_result_value
        )

    @on("CostUpdated")
    def on_cost_update(self,total_cost,transaction_id, **kwargs):
        """
        @brief Handles the CostUpdated event from the central system.

        This method is triggered when a CostUpdated event is received from the central system.
        It processes the updated cost information using the charge point response handler.

        @param id: The ID associated with the cost update event.
        @param total_cost: The total cost after the update.
        @param transaction_id: The ID of the transaction associated with the cost update.
        @param kwargs: Additional keyword arguments.

        @details
        The method invokes the charge point response handler to process the CostUpdated event
        with the provided parameters. It does not return any specific response object directly.

        Example usage:
        @code
        charge_point.on_cost_update(id, total_cost, transaction_id)
        @endcode
        """
        charge_point_responce_handler.cost_update(total_cost,transaction_id, **kwargs)
        return ocpp_response.CostUpdated(
        )

    @on("CustomerInformation")
    def on_customer_information(self,request_id,report,clear, **kwargs):
        """
        @brief Handles the CustomerInformation request from the central system.

        This method is triggered when a CustomerInformation request is received from the central system.
        It processes the customer information request using the charge point response handler.

        @param request_id: The ID of the customer information request.
        @param report: A flag indicating whether to report customer information.
        @param clear: A flag indicating whether to clear customer information.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.CustomerInformation: The response to the CustomerInformation request.

        @details
        The method invokes the charge point response handler to process the CustomerInformation request
        with the provided request ID, report flag, clear flag, and any additional keyword arguments. It then
        returns a CustomerInformation response with the status of the customer information processing.

        Example usage:
        @code
        charge_point.on_customer_information(request_id, report, clear)
        @endcode
        """
        status_value=charge_point_responce_handler.customer_information(request_id,report,clear, **kwargs)
        return ocpp_response.CustomerInformation(
            status=status_value
        )

    @on("DataTransfer")
    def on_data_transfer(self,vendor_id, **kwargs):
        """
        @brief Handles the DataTransfer request from the central system.

        This method is triggered when a DataTransfer request is received from the central system.
        It processes the data transfer request using the charge point response handler.

        @param vendor_id: The vendor ID associated with the data transfer request.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.DataTransfer: The response to the DataTransfer request.

        @details
        The method invokes the charge point response handler to process the DataTransfer request
        with the provided vendor ID and any additional keyword arguments. It then returns a 
        DataTransfer response with the status of the data transfer process.

        Example usage:
        @code
        charge_point.on_data_transfer(vendor_id)
        @endcode
        """
        status_value=charge_point_responce_handler.data_transfer(vendor_id,**kwargs)
        return ocpp_response.DataTransfer(
            status=status_value
        )

    @on("DeleteCertificate")
    def on_delete_certificate(self,certificate_hash_data, **kwargs):
        """
        @brief Handles the DeleteCertificate request from the central system.

        This method is triggered when a DeleteCertificate request is received from the central system.
        It processes the request to delete a certificate using the charge point response handler.

        @param certificate_hash_data: The hash data of the certificate to be deleted.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.DeleteCertificate: The response to the DeleteCertificate request.

        @details
        The method invokes the charge point response handler to process the DeleteCertificate request
        with the provided certificate hash data and any additional keyword arguments. It then returns a 
        DeleteCertificate response with the status of the certificate deletion process.

        Example usage:
        @code
        charge_point.on_delete_certificate(certificate_hash_data)
        @endcode
        """
        status_value=charge_point_responce_handler.delete_certificate(certificate_hash_data,**kwargs)
        return ocpp_response.DeleteCertificate(
            status=status_value
        )

    @on("GetBaseReport")
    def on_get_base_report(self, request_id, report_base, **kwargs):
        """
        @brief Handles the GetBaseReport request from the central system.

        This method is triggered when a GetBaseReport request is received from the central system.
        It processes the request to generate a base report using the charge point response handler.

        @param request_id: The ID of the report request.
        @param report_base: The base of the report to be generated.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.GetBaseReport: The response to the GetBaseReport request.

        @details
        The method invokes the charge point response handler to process the GetBaseReport request
        with the provided request ID, report base, and any additional keyword arguments. It then
        returns a GetBaseReport response with the status of the base report generation process.

        Example usage:
        @code
        charge_point.on_get_base_report(request_id, report_base)
        @endcode
        """
        status_value=charge_point_responce_handler.get_base_report(request_id, report_base, **kwargs)
        return ocpp_response.GetBaseReport(
            status=status_value
        )

    @on("GetChargingProfiles")
    def on_get_charging_profiles(self, request_id, charging_profile, **kwargs):
        """
        @brief Handles the GetChargingProfiles request from the central system.

        This method is triggered when a GetChargingProfiles request is received from the central system.
        It processes the request to retrieve charging profiles using the charge point response handler.

        @param request_id: The ID of the charging profiles request.
        @param charging_profile: The charging profile information to be retrieved.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.GetChargingProfiles: The response to the GetChargingProfiles request.

        @details
        The method invokes the charge point response handler to process the GetChargingProfiles request
        with the provided request ID, charging profile information, and any additional keyword arguments.
        It then returns a GetChargingProfiles response with the status of the charging profiles retrieval process.

        Example usage:
        @code
        charge_point.on_get_charging_profiles(request_id, charging_profile)
        @endcode
        """
        status_value=charge_point_responce_handler.get_charging_profiles(request_id, charging_profile, **kwargs)
        return ocpp_response.GetChargingProfiles(
            status=status_value
        )

    @on("GetCompositeSchedule")
    def on_get_composite_schedule(self, duration, evse_id, **kwargs):
        """
        @brief Handles the GetCompositeSchedule request from the central system.

        This method is triggered when a GetCompositeSchedule request is received from the central system.
        It processes the request to retrieve a composite schedule using the charge point response handler.

        @param duration: The duration for which the composite schedule is requested.
        @param evse_id: The ID of the Electric Vehicle Supply Equipment (EVSE) for which the schedule is requested.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.GetCompositeSchedule: The response to the GetCompositeSchedule request.

        @details
        The method invokes the charge point response handler to process the GetCompositeSchedule request
        with the provided duration, EVSE ID, and any additional keyword arguments. It then returns a
        GetCompositeSchedule response with the status of the composite schedule retrieval process.

        Example usage:
        @code
        charge_point.on_get_composite_schedule(duration, evse_id)
        @endcode
        """
        status_value=charge_point_responce_handler.get_composite_schedule( duration, evse_id, **kwargs)
        return ocpp_response.GetCompositeSchedule(
            status=status_value
        )

    @on("GetInstalledCertificateIds")
    def on_get_installed_certificate_ids(self,**kwargs):
        """
        @brief Handles the GetInstalledCertificateIds request from the central system.

        This method is triggered when a GetInstalledCertificateIds request is received from the central system.
        It processes the request to retrieve installed certificate IDs using the charge point response handler.

        @param kwargs: Additional keyword arguments.
        @return ocpp_response.GetInstalledCertificateIds: The response to the GetInstalledCertificateIds request.

        @details
        The method invokes the charge point response handler to process the GetInstalledCertificateIds request
        with any additional keyword arguments. It then returns a GetInstalledCertificateIds response with the status
        of the installed certificate IDs retrieval process.

        Example usage:
        @code
        charge_point.on_get_installed_certificate_ids()
        @endcode
        """
        status_value=charge_point_responce_handler.get_installed_certificate_ids(**kwargs)
        return ocpp_response.GetInstalledCertificateIds(
            status=status_value
        )

    @on("GetLocalListVersion")
    def on_get_local_list_version(self,**kwargs):
        """
        @brief Handles the GetLocalListVersion request from the central system.

        This method is triggered when a GetLocalListVersion request is received from the central system.
        It processes the request to retrieve the local list version using the charge point response handler.

        @param kwargs: Additional keyword arguments.
        @return ocpp_response.GetLocalListVersion: The response to the GetLocalListVersion request, including the version number.

        @details
        The method invokes the charge point response handler to process the GetLocalListVersion request
        with any additional keyword arguments. It then returns a GetLocalListVersion response with the 
        version number of the local list.

        Example usage:
        @code
        charge_point.on_get_local_list_version()
        @endcode
        """
        version_number_value=charge_point_responce_handler.get_local_list_version(**kwargs)
        return ocpp_response.GetLocalListVersion(
            version_number=version_number_value
        )

    @on("GetLog")
    def on_get_log(self,**kwargs):
        """
        @brief Handles the GetLog request from the central system.

        This method is triggered when a GetLog request is received from the central system.
        It processes the request to retrieve logs using the charge point response handler.

        @param kwargs: Additional keyword arguments.
        @return ocpp_response.GetLog: The response to the GetLog request, including the status of the log retrieval process.

        @details
        The method invokes the charge point response handler to process the GetLog request
        with any additional keyword arguments. It then returns a GetLog response with the 
        status of the log retrieval process.

        Example usage:
        @code
        charge_point.on_get_log()
        @endcode
        """
        status_value=charge_point_responce_handler.get_log(**kwargs)
        return ocpp_response.GetLog(
            status=status_value
        )

    @on("GetMonitoringReport")
    def on_get_monitoring_report(self, request_id,**kwargs):
        """
        @brief Handles the GetMonitoringReport request from the central system.

        This method is triggered when a GetMonitoringReport request is received from the central system.
        It processes the request to retrieve a monitoring report using the charge point response handler.

        @param request_id: The ID of the monitoring report request.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.GetMonitoringReport: The response to the GetMonitoringReport request.

        @details
        The method invokes the charge point response handler to process the GetMonitoringReport request
        with the provided request ID and any additional keyword arguments. It then returns a GetMonitoringReport
        response with the status of the monitoring report retrieval process.

        Example usage:
        @code
        charge_point.on_get_monitoring_report(request_id)
        @endcode
        """
        status_value=charge_point_responce_handler.get_monitoring_report( request_id,**kwargs)
        return ocpp_response.GetMonitoringReport(
            status=status_value
        )

    @on("GetReport")
    def on_get_report(self,request_id,**kwargs):
        """
        @brief Handles the GetReport request from the central system.

        This method is triggered when a GetReport request is received from the central system.
        It processes the request to retrieve a report using the charge point response handler.

        @param request_id: The ID of the report request.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.GetReport: The response to the GetReport request.

        @details
        The method invokes the charge point response handler to process the GetReport request
        with the provided request ID and any additional keyword arguments. It then returns a GetReport
        response with the status of the report retrieval process.

        Example usage:
        @code
        charge_point.on_get_report(request_id)
        @endcode
        """
        status_value=charge_point_responce_handler.get_report( request_id,**kwargs)
        return ocpp_response.GetReport(
            status=status_value
        )

    @on("GetTransactionStatus")
    def on_get_transaction_status(self,**kwargs):
        """
        @brief Handles the GetTransactionStatus request from the central system.

        This method is triggered when a GetTransactionStatus request is received from the central system.
        It processes the request to retrieve transaction status information using the charge point response handler.

        @param kwargs: Additional keyword arguments.
        @return ocpp_response.GetTransactionStatus: The response to the GetTransactionStatus request.

        @details
        The method invokes the charge point response handler to process the GetTransactionStatus request
        with any additional keyword arguments. It then returns a GetTransactionStatus response with the
        transaction status information.

        Example usage:
        @code
        charge_point.on_get_transaction_status()
        @endcode
        """
        messages_in_queue_value=charge_point_responce_handler.get_transaction_status(**kwargs)
        return ocpp_response.GetTransactionStatus(
            messages_in_queue=messages_in_queue_value
        )

    @on("GetVariables")
    def on_get_variables(self, get_variable_data, **kwargs):
        """
        @brief Handles the GetVariables request from the central system.

        This method is triggered when a GetVariables request is received from the central system.
        It processes the request to retrieve variables using the charge point response handler.

        @param get_variable_data: The data specifying which variables to retrieve.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.GetVariables: The response to the GetVariables request.

        @details
        The method invokes the charge point response handler to process the GetVariables request
        with the specified get_variable_data and any additional keyword arguments. It then returns a GetVariables
        response with the result of the variable retrieval process.

        Example usage:
        @code
        charge_point.on_get_variables(get_variable_data)
        @endcode
        """
        get_variable_result_value=charge_point_responce_handler.get_variables(get_variable_data,**kwargs)
        return ocpp_response.GetVariables(
            get_variable_result=get_variable_result_value
        )

    @on("InstallCertificate")
    def on_install_certificate(self, certificate,certificate_type, **kwargs):
        """
        @brief Handles the InstallCertificate request from the central system.

        This method is triggered when an InstallCertificate request is received from the central system.
        It processes the request to install a certificate using the charge point response handler.

        @param certificate: The certificate data to be installed.
        @param certificate_type: The type of certificate being installed.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.InstallCertificate: The response to the InstallCertificate request.

        @details
        The method invokes the charge point response handler to process the InstallCertificate request
        with the provided certificate, certificate_type, and any additional keyword arguments. It then returns
        an InstallCertificate response with the status of the certificate installation process.

        Example usage:
        @code
        charge_point.on_install_certificate(certificate, certificate_type)
        @endcode
        """
        status_value=charge_point_responce_handler.install_certificate(certificate,certificate_type, **kwargs)
        return ocpp_response.InstallCertificate(
            status=status_value
        )

    @on("PublishFirmware")
    def on_publish_firmware(self, location,checksum,request_id, **kwargs):
        """
        @brief Handles the PublishFirmware request from the central system.

        This method is triggered when a PublishFirmware request is received from the central system.
        It processes the request to publish firmware using the charge point response handler.

        @param location: The location URI of the firmware package to be published.
        @param checksum: The checksum of the firmware package.
        @param request_id: The ID of the firmware publication request.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.PublishFirmware: The response to the PublishFirmware request.

        @details
        The method invokes the charge point response handler to process the PublishFirmware request
        with the provided location URI, checksum, request ID, and any additional keyword arguments. It then returns
        a PublishFirmware response with the status of the firmware publication process.

        Example usage:
        @code
        charge_point.on_publish_firmware(location, checksum, request_id)
        @endcode
        """
        status_value=charge_point_responce_handler.publish_firmware(location,checksum,request_id, **kwargs)
        return ocpp_response.PublishFirmware(
            status=status_value
        )

    @on("RequestStartTransaction")
    def on_request_start_transaction(self, id_token,remote_start_id, **kwargs):
        """
        @brief Handles the RequestStartTransaction request from the central system.

        This method is triggered when a RequestStartTransaction request is received from the central system.
        It processes the request to start a transaction using the charge point response handler.

        @param id_token: The identifier token for authentication or authorization.
        @param remote_start_id: The ID provided by the central system for remote start.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.RequestStartTransaction: The response to the RequestStartTransaction request.

        @details
        The method invokes the charge point response handler to process the RequestStartTransaction request
        with the provided ID token, remote start ID, and any additional keyword arguments. It then returns
        a RequestStartTransaction response with the status of the transaction start process.

        Example usage:
        @code
        charge_point.on_request_start_transaction(id_token, remote_start_id)
        @endcode
        """
        status_value=charge_point_responce_handler.request_start_transaction(id_token,remote_start_id, **kwargs)
        return ocpp_response.RequestStartTransaction(
            status=status_value
        )

    @on("RequestStopTransaction")
    def on_request_stop_transaction(self, transaction_id,**kwargs):
        """
        @brief Handles the RequestStopTransaction request from the central system.

        This method is triggered when a RequestStopTransaction request is received from the central system.
        It processes the request to stop a transaction using the charge point response handler.

        @param transaction_id: The ID of the transaction to be stopped.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.RequestStopTransaction: The response to the RequestStopTransaction request.

        @details
        The method invokes the charge point response handler to process the RequestStopTransaction request
        with the provided transaction ID and any additional keyword arguments. It then returns
        a RequestStopTransaction response with the status of the transaction stop process.

        Example usage:
        @code
        charge_point.on_request_stop_transaction(transaction_id)
        @endcode
        """
        status_value=charge_point_responce_handler.request_stop_transaction(transaction_id,**kwargs)
        return ocpp_response.RequestStopTransaction(
            status=status_value
        )

    @on("ReserveNow")
    def on_reserve_now(self, id,expiry_date_time,id_token,**kwargs):
        """
        @brief Handles the ReserveNow request from the central system.

        This method is triggered when a ReserveNow request is received from the central system.
        It processes the request to reserve a charging station using the charge point response handler.

        @param id: The reservation ID.
        @param expiry_date_time: The date and time when the reservation expires.
        @param id_token: The identifier token for authentication or authorization.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.ReserveNow: The response to the ReserveNow request.

        @details
        The method invokes the charge point response handler to process the ReserveNow request
        with the provided reservation ID, expiry date and time, ID token, and any additional keyword arguments.
        It then returns a ReserveNow response with the status of the reservation process.

        Example usage:
        @code
        charge_point.on_reserve_now(id, expiry_date_time, id_token)
        @endcode
        """
        status_value=charge_point_responce_handler.reserve_now(id,expiry_date_time,id_token,**kwargs)
        return ocpp_response.ReserveNow(
            status=status_value
        )

    @on("Reset")
    def on_reset_request(self,type,**kwargs):
        """
        @brief Handles the Reset request from the central system.

        This method is triggered when a Reset request is received from the central system.
        It processes the request to reset the charge point using the charge point response handler.

        @param type: The type of reset requested (e.g., Soft, Hard).
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.Reset: The response to the Reset request.

        @details
        The method invokes the charge point response handler to process the Reset request
        with the provided reset type and any additional keyword arguments.
        It then returns a Reset response with the status of the reset process.

        Example usage:
        @code
        charge_point.on_reset_request(type)
        @endcode
        """
        status_value=charge_point_responce_handler.reset_request(type,**kwargs)
        return ocpp_response.Reset(
            status=status_value
        )    

    @on("SendLocalList")
    def on_send_local_list(self,version_number,update_type,**kwargs):
        status_value=charge_point_responce_handler.send_local_list(version_number,update_type,**kwargs)
        return ocpp_response.SendLocalList(
            status=status_value
        )

    @on("SetChargingProfile")
    def on_set_charging_profile(self,evse_id,charging_profile,**kwargs):
        """
        @brief Handles the SendLocalList request from the central system.

        This method is triggered when a SendLocalList request is received from the central system.
        It processes the request to send a local authorization list using the charge point response handler.

        @param version_number: The version number of the local authorization list.
        @param update_type: The type of update requested for the local authorization list.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.SendLocalList: The response to the SendLocalList request.

        @details
        The method invokes the charge point response handler to process the SendLocalList request
        with the provided version number, update type, and any additional keyword arguments.
        It then returns a SendLocalList response with the status of the local list sending process.

        Example usage:
        @code
        charge_point.on_send_local_list(version_number, update_type)
        @endcode
        """
        status_value=charge_point_responce_handler.set_charging_profile(evse_id,charging_profile,**kwargs)
        return ocpp_response.SetChargingProfile(
            status=status_value
        )

    @on("SetDisplayMessage")
    def on_set_display_message(self,message,**kwargs):
        status_value=charge_point_responce_handler.set_display_message(message,**kwargs)
        return ocpp_response.SetDisplayMessage(
            status=status_value
        )

    @on("SetMonitoringBase")
    def on_set_monitoring_base(self,monitoring_base ,**kwargs):
        """
        @brief Handles the SetDisplayMessage request from the central system.

        This method is triggered when a SetDisplayMessage request is received from the central system.
        It processes the request to set a display message using the charge point response handler.

        @param message: The message to be displayed on the charge point.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.SetDisplayMessage: The response to the SetDisplayMessage request.

        @details
        The method invokes the charge point response handler to process the SetDisplayMessage request
        with the provided message and any additional keyword arguments.
        It then returns a SetDisplayMessage response with the status of the display message setting process.

        Example usage:
        @code
        charge_point.on_set_display_message(message)
        @endcode
        """
        status_value=charge_point_responce_handler.set_monitoring_base(monitoring_base ,**kwargs)
        return ocpp_response.SetMonitoringBase(
            status=status_value
        )
        
    @on("SetMonitoringLevel")
    def on_set_monitoring_level(self,severity,**kwargs):
        """
        @brief Handles the SetMonitoringLevel request from the central system.

        This method is triggered when a SetMonitoringLevel request is received from the central system.
        It processes the request to set the monitoring level using the charge point response handler.

        @param severity: The severity level for monitoring (e.g., Debug, Information).
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.SetMonitoringLevel: The response to the SetMonitoringLevel request.

        @details
        The method invokes the charge point response handler to process the SetMonitoringLevel request
        with the provided severity level and any additional keyword arguments.
        It then returns a SetMonitoringLevel response with the status of the monitoring level setting process.

        Example usage:
        @code
        charge_point.on_set_monitoring_level(severity)
        @endcode
        """
        status_value=charge_point_responce_handler.set_monitoring_level(severity,**kwargs)
        return ocpp_response.SetMonitoringLevel(
            status=status_value
        )

    @on("SetNetworkProfile")
    def on_set_network_profile(self,configuration_slot,connection_data,**kwargs):
        """
        @brief Handles the SetNetworkProfile request from the central system.

        This method is triggered when a SetNetworkProfile request is received from the central system.
        It processes the request to set a network profile using the charge point response handler.

        @param configuration_slot: The slot number for the network configuration.
        @param connection_data: The data for establishing the network connection.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.SetNetworkProfile: The response to the SetNetworkProfile request.

        @details
        The method invokes the charge point response handler to process the SetNetworkProfile request
        with the provided configuration slot, connection data, and any additional keyword arguments.
        It then returns a SetNetworkProfile response with the status of the network profile setting process.

        Example usage:
        @code
        charge_point.on_set_network_profile(configuration_slot, connection_data)
        @endcode
        """
        status_value=charge_point_responce_handler.set_network_profile(configuration_slot,connection_data,**kwargs)
        return ocpp_response.SetNetworkProfile(
            status=status_value
        )

    @on("SetVariableMonitoring")
    def on_set_variable_monitoring(self, set_monitoring_data, **kwargs):
        """
        @brief Handles the SetVariableMonitoring request from the central system.

        This method is triggered when a SetVariableMonitoring request is received from the central system.
        It processes the request to set variable monitoring using the charge point response handler.

        @param set_monitoring_data: Data specifying the variables to monitor.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.SetVariableMonitoring: The response to the SetVariableMonitoring request.

        @details
        The method invokes the charge point response handler to process the SetVariableMonitoring request
        with the provided monitoring data and any additional keyword arguments.
        It then returns a SetVariableMonitoring response with the status of the variable monitoring setting process.

        Example usage:
        @code
        charge_point.on_set_variable_monitoring(set_monitoring_data)
        @endcode
        """
        set_monitoring_result_value=charge_point_responce_handler.set_variable_monitoring(set_monitoring_data, **kwargs)
        return ocpp_response.SetVariableMonitoring(
            set_monitoring_result=set_monitoring_result_value
        )

    @on("SetVariables")
    def on_set_variables(self, set_variable_data, **kwargs):
        """
        @brief Handles the SetVariables request from the central system.

        This method is triggered when a SetVariables request is received from the central system.
        It processes the request to set variables using the charge point response handler.

        @param set_variable_data: Data specifying the variables to set.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.SetVariables: The response to the SetVariables request.

        @details
        The method invokes the charge point response handler to process the SetVariables request
        with the provided variable setting data and any additional keyword arguments.
        It then returns a SetVariables response with the status of the variable setting process.

        Example usage:
        @code
        charge_point.on_set_variables(set_variable_data)
        @endcode
        """
        set_variable_results=charge_point_responce_handler.set_variables(set_variable_data,**kwargs)
        return ocpp_response.SetVariables(
            set_variable_result=set_variable_results
        )

    @on("TriggerMessage")
    def on_trigger_message(self,requested_message, **kwargs):
        """
        @brief Handles the TriggerMessage request from the central system.

        This method is triggered when a TriggerMessage request is received from the central system.
        It processes the request to trigger a message using the charge point response handler.

        @param requested_message: The message to be triggered.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.TriggerMessage: The response to the TriggerMessage request.

        @details
        The method invokes the charge point response handler to process the TriggerMessage request
        with the provided message and any additional keyword arguments.
        It then returns a TriggerMessage response with the status of the message triggering process.

        Example usage:
        @code
        charge_point.on_trigger_message(requested_message)
        @endcode
        """
        status_value=charge_point_responce_handler.trigger_message(requested_message,**kwargs)
        return ocpp_response.TriggerMessage(
            status=status_value
        )

    @on("UnlockConnector")
    def on_unlock_connector(self,evse_id,connector_id,**kwargs):
        """
        @brief Handles the UnlockConnector request from the central system.

        This method is triggered when an UnlockConnector request is received from the central system.
        It processes the request to unlock a connector using the charge point response handler.

        @param evse_id: Identifier of the Electric Vehicle Supply Equipment (EVSE) where the connector is located.
        @param connector_id: Identifier of the connector to unlock.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.UnlockConnector: The response to the UnlockConnector request.

        @details
        The method invokes the charge point response handler to process the UnlockConnector request
        with the provided EVSE ID, connector ID, and any additional keyword arguments.
        It then returns an UnlockConnector response with the status of the connector unlocking process.

        Example usage:
        @code
        charge_point.on_unlock_connector(evse_id, connector_id)
        @endcode
        """
        status_value=charge_point_responce_handler.unlock_connector(evse_id,connector_id,**kwargs)
        return ocpp_response.UnlockConnector(
            status=status_value
        )

    @on("UnpublishFirmware")
    def on_unpublish_firmware(self,checksum, **kwargs):
        """
        @brief Handles the UnpublishFirmware request from the central system.

        This method is triggered when an UnpublishFirmware request is received from the central system.
        It processes the request to unpublish firmware using the charge point response handler.

        @param checksum: The checksum of the firmware to be unpublished.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.UnpublishFirmware: The response to the UnpublishFirmware request.

        @details
        The method invokes the charge point response handler to process the UnpublishFirmware request
        with the provided firmware checksum and any additional keyword arguments.
        It then returns an UnpublishFirmware response with the status of the firmware unpublishing process.

        Example usage:
        @code
        charge_point.on_unpublish_firmware(checksum)
        @endcode
        """
        status_value=charge_point_responce_handler.unpublish_firmware(checksum, **kwargs)
        return ocpp_response.UnpublishFirmware(
            status=status_value
        )

    @on("UpdateFirmware")
    def on_update_firmware(self,request_id,firmware,retries,**kwargs):
        """
        @brief Handles the UpdateFirmware request from the central system.

        This method is triggered when an UpdateFirmware request is received from the central system.
        It processes the request to update firmware using the charge point response handler.

        @param request_id: Identifier of the firmware update request.
        @param firmware: Details of the firmware to be updated, such as location.
        @param retries: Number of retry attempts allowed for the firmware update.
        @param kwargs: Additional keyword arguments.
        @return ocpp_response.UpdateFirmware: The response to the UpdateFirmware request.

        @details
        The method invokes the charge point response handler to process the UpdateFirmware request
        with the provided request ID, firmware details, retries, and any additional keyword arguments.
        It then returns an UpdateFirmware response with the status of the firmware update process.

        Example usage:
        @code
        charge_point.on_update_firmware(request_id, firmware, retries)
        @endcode
        """
        # print("Firmware update request received. Download from:",firmware("location"))
        # Here you would add the logic to download and apply the firmware
        status_value=charge_point_responce_handler.update_firmware(request_id,firmware,retries,**kwargs)
        return ocpp_response.UpdateFirmware(
            status=status_value
        )

# async def api_handle(charge_point):
#     loop = asyncio.get_running_loop()
#     while True:
#         user_input = int(await loop.run_in_executor(None, input, "Enter a valid number (1: Boot Notification, 2: Heartbeat): "))
#         if user_input == 1:
#             await charge_point.send_authorize()
            
#         elif user_input == 2:
#             await charge_point.send_boot_notification()
            
#         elif user_input == 3:
#             await charge_point.send_cleared_charging_limit()
            
#         elif user_input == 4:
#             await charge_point.send_data_transfer()
            
#         elif user_input == 5:
#             await charge_point.send_firmware_status_notification()
            
#         elif user_input == 6:
#             await charge_point.send_get_15118_ev_certificate()
            
#         elif user_input == 7:
#             await charge_point.send_get_certificate_status()
            
#         elif user_input == 8:
#             await charge_point.send_get_display_messages()
            
#         elif user_input == 9:
#             await charge_point.send_heartbeat(5)
            
#         elif user_input == 10:
#             await charge_point.send_log_status_notification()
            
#         elif user_input == 11:
#             await charge_point.send_meter_values()
            
#         elif user_input == 12:
#             await charge_point.send_notify_charging_limit()
            
#         elif user_input == 13:
#             await charge_point.send_notify_customer_information()
            
#         elif user_input == 14:
#             await charge_point.send_notify_display_messages()
            
#         elif user_input == 15:
#             await charge_point.send_notify_ev_charging_needs()
            
#         elif user_input == 16:
#             await charge_point.send_notify_ev_charging_schedule()
            
#         elif user_input == 17:
#             await charge_point.send_notify_event()
            
#         elif user_input == 18:
#             await charge_point.send_notify_monitoring_report()
            
#         elif user_input == 19:
#             await charge_point.send_notify_report()
            
#         elif user_input == 20:
#             await charge_point.send_publish_firmware_status_notification()
            
#         elif user_input == 21:
#             await charge_point.send_report_charging_profiles()
            
#         elif user_input == 22:
#             await charge_point.send_reservation_status_update()
            
#         elif user_input == 23:
#             await charge_point.send_security_event_notification()
            
#         elif user_input == 24:
#             await charge_point.send_sign_certificate()
            
#         elif user_input == 25:
#             await charge_point.send_status_notification()
            
#         elif user_input == 26:
#             await charge_point.send_transaction_event()
            
#         else:
#             logging.warning("Invalid number entered. Please try again.")

    
# async def main():
#     async with websockets.connect(
#         "ws://10.10.0.221:9876/CP_1", subprotocols=["ocpp2.0.1"]
#     ) as ws:
#         print(ws)
#         charge_point = ChargePoint("CP_1", ws)
#         api_event=asyncio.ensure_future(api_handle(charge_point))
#         await asyncio.gather(
#             charge_point.start(),api_event
#         )

# if __name__ == "__main__":
#     # asyncio.run() is used when running this example with Python >= 3.7v
#     asyncio.run(main())
