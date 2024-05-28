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
    

    async def send_boot_notification(self):
        request = ocpp_request.BootNotification(
            charging_station={"model": "SingleSocketCharger", "vendor_name": "Pisquare"},
            reason="PowerUp",
        )
        response = await self.call(request)

        if response.status == "Accepted":
            print("Connected to central system.")
        # await self.send_heartbeat(response.interval)
        
        
    async def send_heartbeat(self, interval):
        request = ocpp_request.Heartbeat()
        while True:
            await self.call(request)
            await asyncio.sleep(interval)  

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

    @on("GetBaseReport")
    def on_get_base_report(self, request_id, report_base, **kwargs):
        return ocpp_response.GetBaseReport(
            status="Accepted"
        )
        
    @on("GetMonitoringReport")
    def on_get_monitoring_report(self, request_id,**kwargs):
        return ocpp_response.GetMonitoringReport(
            status="Accepted"
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

    @on("NotifyEvent")
    def on_notify_event(self, generated_at,seq_no,event_data, **kwargs):
        return ocpp_response.NotifyEvent(
            custom_data=[{"vendorId":"5"}]
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

async def api_handle(charge_point):
    loop = asyncio.get_running_loop()
    while True:
        user_input = int(await loop.run_in_executor(None, input, "Enter a valid number (1: Boot Notification, 2: Heartbeat): "))
        if user_input == 1:
            # asyncio.create_task(charge_point.send_boot_notification())
            await charge_point.send_boot_notification()
        elif user_input == 2:
            # asyncio.create_task(charge_point.send_heartbeat(5))
            await charge_point.send_heartbeat(5)
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
