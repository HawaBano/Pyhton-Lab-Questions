class User:
    def __init__(self, user_name, user_password, user_email, user_role):
        self.user_name = user_name
        self.user_password = user_password
        self.user_email = user_email
        self.user_role = user_role


class UserManager:
    def __init__(self):
        self.users = []
        self.logged_in_user = None

    def register(self, user_name, user_password, user_email, user_role):
        for user in self.users:
            if user.user_name == user_name:
                return "Username already exists."
        new_user = User(user_name, user_password, user_email, user_role)
        self.users.append(new_user)
        return "User registered successfully."

    def login(self, user_name, user_password):
        for user in self.users:
            if user.user_name == user_name and user.user_password == user_password:
                self.logged_in_user = user
                return "Login successful."
        return "Invalid username or password."

    def authenticate_user(self, user_email, user_password):
        for user in self.users:
            if user.user_email == user_email and user.user_password == user_password:
                print("Authenticate user")
                return True
        print("User email or password is invalid")
        return False

    def update_profile(self, user_name, user_new_role):
        for user in self.users:
            if user.user_name == user_name:
                if user_new_role:
                    user.user_role = user_new_role
                return "Profile updated successfully."
        return "User not found."


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
    
    

user_manager = UserManager()
device_manager = DeviceManager()

print(user_manager.register("admin", "password123", "admin123@gmail.com", "Admin"))
print(user_manager.login("admin", "password123"))
print(user_manager.authenticate_user("admin123@gmail.com", "password123"))
print(user_manager.update_profile("admin", "Admin2"))


print(user_manager.register("user", "user_password123", "user123@gmail.com", "User"))
print(user_manager.login("user", "password123"))
print(user_manager.authenticate_user("user123@gmail.com", "user_password123"))
print(user_manager.update_profile("user", "User1"))

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
