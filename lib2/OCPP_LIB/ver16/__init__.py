from OCPP_LIB.charging_station import ChargePoint as cp
from OCPP_LIB.ver16 import ocpp_request, ocpp_response


class ChargePoint(cp):
    _call = ocpp_request
    _call_result = ocpp_response
    _ocpp_version = "1.6"
