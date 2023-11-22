class Smartphone:
    def __init__(self, price, model, phone_number, memory, battery):
        self.price = price
        self.model = model
        self.phone_number = phone_number
        self.memory = memory
        self.battery = battery

    def __str__(self):
        return f"{self.price}, {self.model}, {self.phone_number}, {self.memory}, {self.battery}"

class PhoneStore:
    inventory = []

    @staticmethod
    def add_phone(smartphone):
        PhoneStore.inventory.append(smartphone)

    @staticmethod
    def find_best_phone(max_budget):
        best_phone = None
        for phone in PhoneStore.inventory:
            if phone.price <= max_budget and (best_phone is None or phone.price > best_phone.price):
                best_phone = phone
        return best_phone

    @staticmethod
    def get_phone_numbers():
        return [phone.phone_number for phone in PhoneStore.inventory]

    @staticmethod
    def list_phones_sorted_by_price():
        sorted_phones = sorted(PhoneStore.inventory, key=lambda p: p.price)
        for phone in sorted_phones:
            print(f"Smartphone {phone}")
