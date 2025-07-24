import json
from serial import Serial
from pathlib import Path

MSG_GET = 'get'
MSG_SET = 'set'
MSG_ERROR = 'error'
MSG_VALUE = 'value'
MSG_COMMAND = 'command'
MSG_TEMPERATURE = 'temperature'
MSG_CTRL_ERROR = "ctrl_error"
MSG_CTRL_IERROR = "ctrl_ierror"
MSG_PGAIN = "pgain"
MSG_IGAIN = "igain"
MSG_SETPOINT = "setpoint"

class PupaeThermalDevice(Serial): # type: ignore

    DEFAULT_TIMEOUT = 2.0

    def __init__(self, port: str|Path , timeout: float=DEFAULT_TIMEOUT):
        params = {'baudrate': 115200, 'timeout': timeout}
        super().__init__(port, **params)

    def get_temperature(self):
        cmd_dict = {MSG_COMMAND: MSG_GET, MSG_VALUE: MSG_TEMPERATURE} 
        rsp_dict = self.send_cmd(cmd_dict)
        return rsp_dict[MSG_TEMPERATURE]

    def send_cmd(self, cmd_dict: dict) -> dict:
        cmd_json = f'{json.dumps(cmd_dict)}\n'
        self.write(cmd_json.encode())
        rsp_json = self.readline()
        rsp_json = rsp_json.strip()
        rsp_dict = json.loads(rsp_json.decode())
        if 'error' in rsp_dict:
            raise PupaeThermalDeviceException(rsp_dict[MSG_ERROR])
        try:
            rsp_command = rsp_dict[MSG_COMMAND]
        except KeyError:
            error_msg = 'command key not found in response form device'
            raise PupaeThermalDeviceException(error_msg)
        if cmd_dict[MSG_COMMAND] != rsp_command:
            error_msg = 'response command does not match that sent to device'
            raise PupaeThermalDeviceException(error_msg)
        return rsp_dict



class PupaeThermalDeviceException(Exception):
    pass
