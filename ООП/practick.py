# class House:
#     def info(self):
#         print(self.number, self.street)
#
#
# home1 = House()
# home1.number = 47
# home1.street = 'Черняховского'
# print(home1.info())

# class House:
#     def __init__(self):
#         self.interfaces = None
#
#     def generate_interfaces(self, intf_type, number_of_intf):
#         interfaces = [f"{intf_type}{number}" for number in range(1, number_of_intf + 1)]
#         self.interfaces = interfaces
#
#
# home1 = House()
# home1.generate_interfaces('fa', 10)
# print(home1.interfaces)
