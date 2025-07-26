import json
from serial import Serial
from pathlib import Path

MSG_GET = 'get'
MSG_SET = 'set'
MSG_ERROR = 'error'
MSG_VALUE = 'value'
MSG_COMMAND = 'command'
MSG_TEMPERATURE = 'temperature'
MSG_CTRL_POWER = 'ctrl_power'
MSG_CTRL_ERROR = 'ctrl_error'
MSG_CTRL_IERROR = 'ctrl_ierror'
MSG_CTRL_PGAIN = 'ctrl_pgain'
MSG_CTRL_IGAIN = 'ctrl_igain'
MSG_CTRL_SETPOINT = 'ctrl_setpoint'
MSG_CTRL_ENABLED = 'ctrl_enabled'
MSG_ALL = 'all'

class PupaeThermalDevice(Serial): # type: ignore

    DEFAULT_TIMEOUT = 2.0

    def __init__(self, port: str|Path , timeout: float=DEFAULT_TIMEOUT):
        params = {'baudrate': 115200, 'timeout': timeout}
        super().__init__(port, **params)

    def get_temperature(self) -> dict:
        cmd_dict = {MSG_COMMAND: MSG_GET, MSG_VALUE: MSG_TEMPERATURE} 
        rsp_dict = self.send_cmd(cmd_dict)
        return rsp_dict[MSG_TEMPERATURE]

    def get_ctrl_power(self) -> dict:
        cmd_dict = {MSG_COMMAND: MSG_GET, MSG_VALUE: MSG_CTRL_POWER} 
        rsp_dict = self.send_cmd(cmd_dict)
        return rsp_dict[MSG_CTRL_POWER]

    def get_ctrl_error(self) -> dict:
        cmd_dict = {MSG_COMMAND: MSG_GET, MSG_VALUE: MSG_CTRL_ERROR} 
        rsp_dict = self.send_cmd(cmd_dict)
        return rsp_dict[MSG_CTRL_ERROR]

    def get_ctrl_ierror(self) -> dict:
        cmd_dict = {MSG_COMMAND: MSG_GET, MSG_VALUE: MSG_CTRL_IERROR} 
        rsp_dict = self.send_cmd(cmd_dict)
        return rsp_dict[MSG_CTRL_IERROR]

    def get_ctrl_pgain(self) -> dict:
        cmd_dict = {MSG_COMMAND: MSG_GET, MSG_VALUE: MSG_CTRL_PGAIN} 
        rsp_dict = self.send_cmd(cmd_dict)
        return rsp_dict[MSG_CTRL_PGAIN]

    def get_ctrl_igain(self) -> dict:
        cmd_dict = {MSG_COMMAND: MSG_GET, MSG_VALUE: MSG_CTRL_IGAIN} 
        rsp_dict = self.send_cmd(cmd_dict)
        return rsp_dict[MSG_CTRL_IGAIN]

    def get_ctrl_setpoint(self) -> dict:
        cmd_dict = {MSG_COMMAND: MSG_GET, MSG_VALUE: MSG_CTRL_SETPOINT} 
        rsp_dict = self.send_cmd(cmd_dict)
        return rsp_dict[MSG_CTRL_SETPOINT]

    def get_ctrl_enabled(self) -> dict:
        cmd_dict = {MSG_COMMAND: MSG_GET, MSG_VALUE: MSG_CTRL_ENABLED} 
        rsp_dict = self.send_cmd(cmd_dict)
        return rsp_dict[MSG_CTRL_ENABLED]

    def get_all(self) -> dict:
        cmd_dict = {MSG_COMMAND: MSG_GET, MSG_VALUE: MSG_ALL} 
        rsp_dict = self.send_cmd(cmd_dict)
        del rsp_dict[MSG_COMMAND]
        return rsp_dict

    def set_ctrl_enabled(self, enabled: bool):
        cmd_dict = {MSG_COMMAND: MSG_SET, MSG_CTRL_ENABLED: enabled}
        rsp_dict = self.send_cmd(cmd_dict)

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
