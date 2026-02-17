class Report:
    def generate(self):
        pass


class SalesReport(Report):
    def generate(self):
        print("Generating Sales Report")


class InventoryReport(Report):
    def generate(self):
        print("Generating Inventory Report")


def generate_report(report):
    report.generate()


generate_report(SalesReport())
generate_report(InventoryReport())
