from datetime import datetime
from OCPP_LIB.ver201 import ocpp_response


#("CancelReservation")
def cancel_reservation(reservation_id, **kwargs):
    status="Accepted"
    return (
        status
    )

#("CertificateSigned")
def certificate_signed(certificate_chain, **kwargs):
    status="Accepted"
    return (
        status
    )

#("ChangeAvailability")
def change_availability(operational_status, **kwargs):
    status="Accepted"
    return(
        status
    )

#("ClearCache")
def clear_cache( **kwargs):
    status="Accepted"
    return (
        status
    )

#("ClearChargingProfile")
def clear_charging_profile( **kwargs):
    status="Accepted"
    return (
        status
    )

#("ClearDisplayMessage")
def clear_display_message(id, **kwargs):
    status="Accepted"
    return (
        status
    )

#("ClearVariableMonitoring")
def clear_variable_monitoring(id, **kwargs):
    clear_monitoring_result=[
            {
                "status":"Accepted",
                "id" : 5
            }
        ]
    return (
        clear_monitoring_result
    )

#("CostUpdated")
def cost_update(total_cost,transaction_id, **kwargs):
    return (
    )

#("CustomerInformation")
def customer_information(request_id,report,clear, **kwargs):
    status="Accepted"
    return (
        status
    )

#("DataTransfer")
def data_transfer(vendor_id, **kwargs):
    status="Accepted"
    return (
        status
    )

#("DeleteCertificate")
def delete_certificate(certificate_hash_data, **kwargs):
    status="Accepted"
    return (
        status
    )

#("GetBaseReport")
def get_base_report( request_id, report_base, **kwargs):
    status="Accepted"
    return (
        status
    )

#("GetChargingProfiles")
def get_charging_profiles( request_id, charging_profile, **kwargs):
    status="Accepted"
    return(
        status
    )

#("GetCompositeSchedule")
def get_composite_schedule( duration, evse_id, **kwargs):
    status="Accepted"
    return (
        status
    )

#("GetInstalledCertificateIds")
def get_installed_certificate_ids(**kwargs):
    status="Accepted"
    return (
        status
    )

#("GetLocalListVersion")
def get_local_list_version(**kwargs):
    version_number_value=201
    return (
        version_number_value
    )

#("GetLog")
def get_log(**kwargs):
    status="Accepted"
    return (
        status
    )

#("GetMonitoringReport")
def get_monitoring_report( request_id,**kwargs):
    status="Accepted"
    return (
        status
    )

#("GetReport")
def get_report(request_id,**kwargs):
    status="Accepted"
    return (
        status
    )

#("GetTransactionStatus")
def get_transaction_status(**kwargs):
    messages_in_queue=True
    return (
        messages_in_queue
    )

#("GetVariables")
def get_variables( get_variable_data, **kwargs):
    get_variable_result=[
            {
                "attributeStatus": "Accepted",
                "component": {"name": "EVSE"},
                "variable": {"name": "VariableName"}
            }
        ]
    return (
        get_variable_result
    )

#("InstallCertificate")
def install_certificate( certificate,certificate_type, **kwargs):
    status="Accepted"
    return (
        status
    )

#("PublishFirmware")
def publish_firmware( location,checksum,request_id, **kwargs):
    status="Accepted"
    return (
        status
    )

#("RequestStartTransaction")
def request_start_transaction( id_token,remote_start_id, **kwargs):
    status="Accepted"
    return (
        status
    )

#("RequestStopTransaction")
def request_stop_transaction( transactiid,**kwargs):
    status="Accepted"
    return (
        status
    )

#("ReserveNow")
def reserve_now( id,expiry_date_time,id_token,**kwargs):
    status="Accepted"
    return (
        status
    )

#("Reset")
def reset_request(type,**kwargs):
    status="Accepted"
    return (
        status
    )    

#("SendLocalList")
def send_local_list(versinumber,update_type,**kwargs):
    status="Accepted"
    return(
        status
    )

#("SetChargingProfile")
def set_charging_profile(evse_id,charging_profile,**kwargs):
    status="Accepted"
    return (
        status
    )

#("SetDisplayMessage")
def set_display_message(message,**kwargs):
    status="Accepted"
    return (
        status
    )

#("SetMonitoringBase")
def set_monitoring_base(monitoring_base ,**kwargs):
    status="Accepted"
    return (
        status
    )
    
#("SetMonitoringLevel")
def set_monitoring_level(severity,**kwargs):
    status="Accepted"
    return (
        status
    )

#("SetNetworkProfile")
def set_network_profile(configuratislot,connectidata,**kwargs):
    status="Accepted"
    return (
        status
    )

#("SetVariableMonitoring")
def set_variable_monitoring( set_monitoring_data, **kwargs):
    set_monitoring_result=[
            {
            "status":"Accepted",
            "type": "UpperThreshold",
            "severity": 9,
            "component": {"name": "ChargingStation"},
            "variable": {"name": "VariableName"}
            }
        ]
    return (
        set_monitoring_result
    )

#("SetVariables")
def set_variables( set_variable_data, **kwargs):
    set_variable_results = []
    for variable in set_variable_data:
        # Process each variable and determine the result status
        result_status = "Accepted"  # This should be determined based on your logic
        set_variable_results.append({
            "attributeStatus": result_status,
            "component": variable["component"],
            "variable": variable["variable"]
        })
        set_variable_result=set_variable_results
    return (
        set_variable_result
    )

#("TriggerMessage")
def trigger_message(requested_message, **kwargs):
    status="Accepted"
    return(
        status
    )

#("UnlockConnector")
def unlock_connector(evse_id,connector_id,**kwargs):
    status="Unlocked"
    return(
        status
    )

#("UnpublishFirmware")
def unpublish_firmware(checksum, **kwargs):
    status="DownloadOngoing"
    return (
        status
    )

#("UpdateFirmware")
def update_firmware(request_id,firmware,retries,**kwargs):
    status="Accepted"
    # print("Firmware update request received. Download from:",firmware("location"))
    # Here you would add the logic to download and apply the firmware
    return(
        status
    )
