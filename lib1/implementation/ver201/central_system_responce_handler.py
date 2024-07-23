from datetime import datetime
from pymongo import MongoClient


# client = MongoClient("mongodb://localhost:27017/")
# db = client.ocpp_database

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# client = MongoClient("mongodb://localhost:27017/")
uri = "mongodb+srv://Ritika:Ritz123@cluster0.ftwsd1h.mongodb.net/?appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'),tlsAllowInvalidCertificates=True)
db = client.ocpp_database

collection1 = db.Authorize
collection2 = db.BootNotification
collection3 = db.ClearedChargingLimit
collection4 = db.DataTransfer_chargepoint
collection5 = db.FirmwareStatusNotification
collection6 = db.Get15118EVCertificate
collection7 = db.GetCertificateStatus
collection8 = db.GetDisplayMessages
collection9 = db.Heartbeat
collection10 = db.LogStatusNotification
collection11 = db.MeterValues
collection12 = db.NotifyChargingLimit
collection13 = db.NotifyCustomerInformation
collection14 = db.NotifyDisplayMessages
collection15 = db.NotifyEVChargingNeeds
collection16 = db.NotifyEVChargingSchedule
collection17 = db.NotifyEvent
collection18 = db.NotifyMonitoringReport
collection19 = db.NotifyReport
collection20 = db.PublishFirmwareStatusNotification
collection21 = db.ReportChargingProfiles
collection22 = db.ReservationStatusUpdate
collection23 = db.SecurityEventNotification
collection24 = db.SignCertificate
collection25 = db.StatusNotification
collection26 = db.TransactionEvent





def authorize(id_token_v, **kwargs):
    Authorize={
        "id_token":id_token_v
    }
    collection1.insert_one( Authorize)

    return (
        {"status":"Accepted"}
    )

def boot_notification(charging_station_v, reason_v, **kwargs):
    # pushing
    boot={
        "charging_station":charging_station_v,
        "reason":reason_v
    }
    collection2.insert_one(boot)
    # fetch
    current_time_v=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S") + "Z"
    interval_v=10
    status_v="Accepted"
    # returning
    return (
        current_time_v,interval_v,status_v
        )

#("ClearedChargingLimit")
def cleared_charging_limit(charging_limit_source_v, **kwargs):

    clearcharlimit={
        "charging_limit_source":charging_limit_source_v
    }
    collection3.insert_one(clearcharlimit)
    return (
    )

#("DataTransfer")
def data_transfer(vendor_id_v, **kwargs):
    datatransfer={
        "vendor_id":vendor_id_v
    }
    collection4.insert_one(datatransfer)
    status="Accepted"
    return (
        status
    )

#("FirmwareStatusNotification")
def firmware_status_notification( status_v, **kwargs):
    Firmwarenotification={
        "status":status_v
    }
    collection5.insert_one(Firmwarenotification)
    return (
    )

#("Get15118EVCertificate")
def get_15118_ev_certificate( iso15118_schema_version_v,action_v,exi_request_v, **kwargs):
    status="Accepted"
    exi_response="Raw CertificateInstallationRes response for the EV, Base64 encoded."
    Get15118={
        "iso15118_schema_version":iso15118_schema_version_v,
        "action":action_v,
        "exi_request":exi_request_v  
    }
    collection6.insert_one(Get15118)
    return(
    status,exi_response
    )

#("GetCertificateStatus")
def get_certificate_status( ocsp_request_data_v,**kwargs):
    status_value="Accepted"
    Getcertificate={
        "ocsp_request_data":ocsp_request_data_v
    }
    collection7.insert_one(Getcertificate)
    return (
        status_value
    )

#("GetDisplayMessages")
def get_display_messages( request_id_v,**kwargs):
    status="Accepted"
    Getdisplay={
        "request_id": request_id_v  
    }
    collection8.insert_one(Getdisplay)

    return (
        status
    )

#("Heartbeat")
def heartbeat(self):
    current_time=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S") + "Z"
    print("Got a Heartbeat!")

    Heart={
    }
    collection9.insert_one(Heart)
    return (
        current_time
    )

#("LogStatusNotification")
def log_status_notification(**kwargs):

    Logstatus={
    }
    collection10.insert_one(Logstatus)
    return (
    )

#("MeterValues")
def meter_values(**kwargs):
    Metervalue={
    }
    collection11.insert_one(Metervalue)
    return (
    )

#("NotifyChargingLimit")
def notify_charging_limit(**kwargs):
    Notifycharging={  
    }
    collection12.insert_one(Notifycharging)
    return (
    )

#("NotifyCustomerInformation")
def notify_customer_information(data_v,seq_no_v,generated_at_v,request_id_v,**kwargs):
    Notifycustomerinfo={
        "data":data_v,
        "seq_no":seq_no_v,
        "generated_at":generated_at_v,
        "request_id":request_id_v        
    }
    collection13.insert_one(Notifycustomerinfo)
    return(
    )

#("NotifyDisplayMessages")
def notify_display_messages(request_id_v,**kwargs):
    Notifydisplay={
        "request_id": request_id_v
    }
    collection14.insert_one(Notifydisplay)
    return (
    )

#("NotifyEVChargingNeeds")
def notify_ev_charging_needs(evse_id_v,charging_needs_v,**kwargs):
    status="Accepted"
    Notifyevcharging={
        "evse_id":evse_id_v,
        "charging_needs":charging_needs_v
    }
    collection15.insert_one(Notifyevcharging)
    return (
        status
    )
    
#("NotifyEVChargingSchedule")
def notify_ev_charging_schedule(time_base_v,evse_id_v,charging_schedule_v,**kwargs):
    Notifyevchargingschedule={
        "time_base" : time_base_v,
        "evse_id":evse_id_v,
        "charging_schedule":charging_schedule_v
    }
    collection16.insert_one(Notifyevchargingschedule)  
    status="Accepted"
    return (
        status
    )
    
#("NotifyEvent")
def notify_event(generated_at_v,seq_no_v,event_data_v,**kwargs):
    Notifyevent={
        "generated_at":generated_at_v,
        "seq_no" : seq_no_v,
        "event_data":event_data_v
    }
    collection17.insert_one( Notifyevent)
    return (
    )
    
#("NotifyMonitoringReport")
def notify_monitoring_report(generated_at_v,seq_no_v,request_id_v,**kwargs):
    Notifymonitoring={
        "generated_at":generated_at_v,
        "seq_no" : seq_no_v,
        "request_id": request_id_v  
    }
    collection18.insert_one(Notifymonitoring)
    return (
    )
    
#("NotifyReport")
def notify_report(generated_at_v,seq_no_v,request_id_v,**kwargs):
    Notifyreport={
        "generated_at":generated_at_v,
        "seq_no" : seq_no_v,
        "request_id": request_id_v  
    }
    collection19.insert_one(Notifyreport)
    return (
    )

#("PublishFirmwareStatusNotification")
def publish_firmware_status_notification(status_v,**kwargs):
    Publishfirmware={
        "status" : status_v  
    }
    collection20.insert_one(Publishfirmware)
    return (
    )
    
#("ReportChargingProfiles")
def report_charging_profiles(request_id_v,charging_limit_source_v,charging_profile_v,evse_id_v,**kwargs):
    Reportchargingprofile={
        "request_id": request_id_v,
        "charging_limit_source":charging_limit_source_v,
        "charging_profile" : charging_profile_v,
        "evse_id":evse_id_v
    }
    collection21.insert_one(Reportchargingprofile)
    return (
    )
    

#("ReservationStatusUpdate")
def reservation_status_update(reservation_id_v,reservation_update_status_v):
    Reservationstatus={
        "reservation_id":reservation_id_v,
        "reservation_update_status":reservation_update_status_v
    }
    collection22.insert_one(Reservationstatus)
    return (
    )

#("SecurityEventNotification")
def security_event_notification(type_v,timestamp_v,**kwargs):
    SecurityEventNotification={
    "type":type_v,
    "timestamp":timestamp_v
    }
    collection23.insert_one(SecurityEventNotification)
    return (
    )

#("SignCertificate")
def sign_certificate(csr_v,**kwargs):
    status="Accepted"
    Signcertificate={
    "csr":csr_v
    }
    collection24.insert_one( Signcertificate)
    return (
        status
    )

#("StatusNotification")
def status_notification(timestamp_v,connector_status_v,evse_id_v,connector_id_v,**kwargs):
    Statusnotification={
    "timestamp":timestamp_v,
    "connector_status":connector_status_v,
    "evse_id":evse_id_v,
    "connector_id":connector_id_v  
    }
    collection25.insert_one( Statusnotification)
    return (
    )

#("TransactionEvent")
def transaction_event( Transactionevent_v,timestamp_v,trigger_reason_v,seq_no_v,transaction_info_v,**kwargs):
    Transactionevent={
        "Transactionevent": Transactionevent_v,
        "timestamp": timestamp_v,
        "trigger_reason":trigger_reason_v,
        "seq_no":seq_no_v,
        "transaction_info":transaction_info_v    
    }
    collection26.insert_one(Transactionevent)
    return (
    )
