class Shipment:
    def delivery_time(self):
        pass


class AirShipment(Shipment):
    def delivery_time(self):
        return "2 Days"


class GroundShipment(Shipment):
    def delivery_time(self):
        return "5 Days"


shipments = [AirShipment(), GroundShipment()]

for s in shipments:
    print("Delivery Time:", s.delivery_time())
