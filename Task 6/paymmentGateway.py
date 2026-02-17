class PaymentGateway:
    def process(self, amount):
        pass


class Razorpay(PaymentGateway):
    def process(self, amount):
        print("Processed", amount, "via Razorpay")


class Stripe(PaymentGateway):
    def process(self, amount):
        print("Processed", amount, "via Stripe")


for gateway in [Razorpay(), Stripe()]:
    gateway.process(1000)
