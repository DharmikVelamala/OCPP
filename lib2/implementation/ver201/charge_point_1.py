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
