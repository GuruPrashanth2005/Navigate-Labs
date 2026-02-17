class Processor:
    def process(self, data):
        pass


class ImageProcessor(Processor):
    def process(self, data):
        print("Processing Image Data")


class TextProcessor(Processor):
    def process(self, data):
        print("Processing Text Data")


processors = [ImageProcessor(), TextProcessor()]

for p in processors:
    p.process("sample data")
