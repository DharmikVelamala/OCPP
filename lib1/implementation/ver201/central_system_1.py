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
    @on("BootNotification")
    def on_boot_notification(self, charging_station, reason, **kwargs):
        return ocpp_response.BootNotification(
            current_time=datetime.utcnow().isoformat(),
            interval=10,
            status="Accepted"
        )

    @on("Heartbeat")
    def on_heartbeat(self):
        print("Got a Heartbeat!")
        return ocpp_response.Heartbeat(
            current_time=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S") + "Z"
        )
    
    
    async def send_clear_variable_monitoring(self):
        request = ocpp_request.ClearVariableMonitoring(
            id = [5]
        )
        response = await self.call(request)

        if response.clear_monitoring_result[0].get("status") == "Accepted":
            print("Connected to chargepoint system 'Clear Variable Monitoringt")
        else:
               print("Connected to chargepoint system 'Clear Variable Monitoringt,error")
    
    async def send_get_base_report(self):
        request = ocpp_request.GetBaseReport(
            request_id= 7,
            report_base= "SummaryInventory",
        )
        response = await self.call(request)

        if response.status == "Accepted":
            print("Connected to chargepoint system 'get base report")
            
            
    async def send_get_monitoring_report(self):
        request = ocpp_request.GetMonitoringReport(
            request_id=7
        )
        response = await self.call(request) 
        if response.status == "Accepted":
            print("Connected to chargepoint system 'get monitoring report' ")
            
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
        if user_input == 0:
            await charge_point.send_clear_variable_monitoring()
            
        elif user_input == 1:
            await charge_point.send_get_base_report()
            
        elif user_input == 2:
            await charge_point.send_get_monitoring_report()
            
        elif user_input == 3:
            await charge_point.send_get_variables()
            
        elif user_input == 4:
            await charge_point.send_set_monitoring_base()
            
        elif user_input == 5:
            await charge_point.send_notify_event()
            
        elif user_input == 6:
            await charge_point.send_set_monitoring_level()
            
        elif user_input == 7:
            await charge_point.send_set_variable_monitoring()
            
        elif user_input == 8:
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
