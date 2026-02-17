class ResponseStrategy:
    def respond(self):
        pass


class FriendlyResponse(ResponseStrategy):
    def respond(self):
        print("Hello! How can I help you?")


class FormalResponse(ResponseStrategy):
    def respond(self):
        print("Good day. How may I assist you?")


strategies = [FriendlyResponse(), FormalResponse()]

for s in strategies:
    s.respond()
