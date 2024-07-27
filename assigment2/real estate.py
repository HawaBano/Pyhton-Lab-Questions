class Property:
    def __init__(self, address, property_type, price, availability_status=True):
        self.address = address
        self.property_type = property_type
        self.price = price
        self.availability_status = availability_status

    def update_availability(self, status):
        self.availability_status = status

    def get_details(self):
        return {
            "Address": self.address,
            "Property Type": self.property_type,
            "Price": self.price,
            "Available": self.availability_status
        }

class Client:
    def __init__(self, name, client_id):
        self.name = name
        self.client_id = client_id
        self.interested_properties = []

    def add_interested_property(self, property):
        if property not in self.interested_properties:
            self.interested_properties.append(property)
            print(f"Added property at {property.address} to client {self.name}'s interests.")
        else:
            print(f"Property at {property.address} is already in the client's interest list.")

    def get_interested_properties(self):
        return [prop.get_details() for prop in self.interested_properties]

class Agent:
    def __init__(self, name, agent_id):
        self.name = name
        self.agent_id = agent_id
        self.listed_properties = []

    def list_property(self, property):
        if property not in self.listed_properties:
            self.listed_properties.append(property)
            print(f"Property at {property.address} listed by agent {self.name}.")
        else:
            print(f"Property at {property.address} is already listed by this agent.")

    def get_listed_properties(self):
        return [prop.get_details() for prop in self.listed_properties]

class RealEstateAgency:
    def __init__(self):
        self.properties = []
        self.clients = {}
        self.agents = {}

    def add_property(self, address, property_type, price):
        property = Property(address, property_type, price)
        self.properties.append(property)
        print(f"Property at {address} added to the agency's listings.")

    def register_client(self, name, client_id):
        if client_id not in self.clients:
            self.clients[client_id] = Client(name, client_id)
            print(f"Client {name} registered with ID {client_id}.")
        else:
            print("Client ID already exists.")

    def assign_agent(self, name, agent_id):
        if agent_id not in self.agents:
            self.agents[agent_id] = Agent(name, agent_id)
            print(f"Agent {name} assigned with ID {agent_id}.")
        else:
            print("Agent ID already exists.")

    def handle_transaction(self, client_id, property_address):
        if client_id in self.clients:
            client = self.clients[client_id]
            for prop in self.properties:
                if prop.address == property_address and prop.availability_status:
                    client.add_interested_property(prop)
                    prop.update_availability(False)
                    print(f"Property at {property_address} has been marked as sold and is no longer available.")
                    return
            print("Property is either not available or not found.")
        else:
            print("Client ID does not exist.")

    def get_property_details(self, address):
        for prop in self.properties:
            if prop.address == address:
                return prop.get_details()
        return "Property not found."

    def get_client_interests(self, client_id):
        if client_id in self.clients:
            return self.clients[client_id].get_interested_properties()
        return "Client not found."

    def get_agent_listings(self, agent_id):
        if agent_id in self.agents:
            return self.agents[agent_id].get_listed_properties()
        return "Agent not found."

# Example usage
def main():
    agency = RealEstateAgency()

    # Add properties
    agency.add_property("123 Maple St", "House", 300000)
    agency.add_property("456 Oak St", "Apartment", 150000)

    # Register clients
    agency.register_client("John Doe", "C001")
    agency.register_client("Jane Smith", "C002")

    # Assign agents
    agency.assign_agent("Alice", "A001")
    agency.assign_agent("Bob", "A002")

    # List properties by agents
    agent1 = agency.agents["A001"]
    prop1 = agency.properties[0]  # 123 Maple St
    agent1.list_property(prop1)

    agent2 = agency.agents["A002"]
    prop2 = agency.properties[1]  # 456 Oak St
    agent2.list_property(prop2)

    # Handle transactions
    agency.handle_transaction("C001", "123 Maple St")

    # Get property details
    print(agency.get_property_details("123 Maple St"))
    print(agency.get_property_details("456 Oak St"))

    # Get client interests
    print(agency.get_client_interests("C001"))

    # Get agent listings
    print(agency.get_agent_listings("A001"))
    print(agency.get_agent_listings("A002"))

if __name__ == "__main__":
    main()
