class Device:
    def __init__(self, name, status='off'):
        self.name = name
        self.status = status


class Light(Device):
    def __init__(self, name, status='off', brightness=100):
        super().__init__(name, status)
        self.brightness = brightness


class Thermostat(Device):
    def __init__(self, name, status='off', temperature=22):
        super().__init__(name, status)
        self.temperature = temperature


class SecurityCamera(Device):
    def __init__(self, name, status='off', recording=False):
        super().__init__(name, status)
        self.recording = recording


class DeviceManager:
    def __init__(self):
        self.devices = []
        self.device_groups = {}

    def add_device(self, device):
        self.devices.append(device)
        return "Device added successfully"

    def remove_device(self, name):
        for device in self.devices:
            if device.name == name:
                self.devices.remove(device)
                return "Device removed successfully"
        return "Device not found"

    def update_device(self, name, new_device):
        for device in self.devices:
            if device.name == name:
                device.status = new_device.status
                return "Device updated successfully"
        return "Device not found"
    
    def list_devices(self):
        device_list = []
        for device in self.devices:
            device_list.append(device)
        return (device_list)
          
    def create_device_group(self, group_name, device_names):
        self.device_groups[group_name] = [device for device in self.devices if device.name in device_names]
        return f"Group '{group_name}' created successfully."

    def control_device_group(self, group_name, status):
        if group_name not in self.device_groups:
            return "Group not found."
        for device in self.device_groups[group_name]:
            device.status = status
        return f"All devices in group {group_name} is set {status}"
    



device_manager = DeviceManager()
light = Light("Living Room Light", "off", 75)
thermostat = Thermostat("Living Room Thermostat", "off", 20)
camera = SecurityCamera("Front Door Camera", "off", True)

print(device_manager.add_device(light))
print(device_manager.add_device(thermostat))
print(device_manager.add_device(camera))

print(device_manager.update_device("Living Room Light", Light("Living Room Light", "on", 100)))
print(device_manager.update_device("Living Room Thermostat", Thermostat("Living Room Thermostat", "on", 25)))
print(device_manager.update_device("Front Door Camera", SecurityCamera("Front Door Camera", "on", False)))

print(device_manager.remove_device("Front Door Camera"))
print(device_manager.list_devices())

print(device_manager.create_device_group("Living Room", ["Living Room Light", "Living Room Thermostat"]))
print(device_manager.control_device_group("Living Room", "on"))
