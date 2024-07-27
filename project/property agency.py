# Design a real estate management system with the following classes and features:
# A Property class with attributes for address, property type, price, and availability status.
# A Client class with attributes for name, client ID, and a list of interested properties.
# An Agent class with attributes for name, agent ID, and a list of listed properties.
# A RealEstateAgency class to manage properties, clients, and agents. Implement methods to add properties, register clients, assign agents, and handle property transactions.

class Property:
    address = ''
    property_type = ''
    price = 0
    available = True
    def __init__(self, address, property_type, price):
        self.address = address
        self.property_type = property_type
        self.price = price
        self.available = True

    def display(self):
        return f"Property(address={self.address}, type={self.property_type}, price={self.price}, available={self.available})"


class Client:
    name = ''
    client_id = ''
    interested_properties = []
    def __init__(self, name, client_id):
        self.name = name
        self.client_id = client_id
        self.interested_properties = []

    def add_interested_property(self, property):
        self.interested_properties.append(property)

    def display(self):
        return f"Client(name={self.name}, id={self.client_id}, interested_properties={len(self.interested_properties)})"


class Agent:
    name = ''
    agent_id = ''
    listed_properties = []
    def __init__(self, name, agent_id):
        self.name = name
        self.agent_id = agent_id
        self.listed_properties = []

    def add_property(self, property):
        self.listed_properties.append(property)

    def display(self):
        return f"Agent(name={self.name}, id={self.agent_id}, listed_properties={len(self.listed_properties)})"


class RealEstateAgency:
    properties = []
    clients = []
    agent = []
    def __init__(self):
        self.properties = []
        self.clients = []
        self.agents = []

    def add_property(self, property):
        self.properties.append(property)
        print(f"Property added: {property}")

    def register_client(self, client):
        self.clients.append(client)
        print(f"Client registered: {client}")

    def assign_agent(self, agent):
        self.agents.append(agent)
        print(f"Agent assigned: {agent}")

    def handle_property_transaction(self, property, client, agent):
        if property in self.properties and property.available:
            property.available = False
            client.add_interested_property(property)
            agent.add_property(property)
            print(f"Transaction completed: {property} sold to {client.name} by {agent.name}")
        else:
            print("Property not available or doesn't exist")


agency = RealEstateAgency()
prop1 = Property("123 Main St", "House", 250000)
prop2 = Property("456 Main st", "Apartment", 150000)
agency.add_property(prop1)
agency.add_property(prop2)

client1 = Client("Ali", 1)
client2 = Client("Bilal", 2)
agency.register_client(client1)
agency.register_client(client2)


agent1 = Agent("Agent1", 101)
agent2 = Agent("Agent2", 102)
agency.assign_agent(agent1)
agency.assign_agent(agent2)


agency.handle_property_transaction(prop1, client1, agent1)
agency.handle_property_transaction(prop2, client2, agent2)

print("\nCurrent state:")
print(f"Properties: {[str(p) for p in agency.properties]}")
print(f"Clients: {[str(c) for c in agency.clients]}")
print(f"Agents: {[str(a) for a in agency.agents]}")





    