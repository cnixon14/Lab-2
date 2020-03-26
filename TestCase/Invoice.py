class Invoice:

    def __init__(self):
        self.items = {}
        self.delivery_type = 0

    def addProduct(self, qnt, price, discount, delivery_type):
        self.items['qnt'] = qnt
        self.items['unit_price'] = price
        self.items['discount'] = discount
        self.items['delivery_type'] = delivery_type
        return self.items

    def totalImpurePrice(self, products):
        total_impure_price = 0
        for k, v in products.items():
            total_impure_price += float(v['unit_price']) * int(v['qnt'])
        total_impure_price = round(total_impure_price, 2)
        return total_impure_price

    def totalDiscount(self, products):
        total_discount = 0
        for k, v in products.items():
            total_discount += (int(v['qnt']) * float(v['unit_price'])) * float(v['discount']) / 100
        total_discount = round(total_discount, 2)
        self.total_discount = total_discount
        return total_discount

    def totalPurePrice(self, products):
        total_pure_price = self.totalImpurePrice(products) - self.totalDiscount(products)
        return total_pure_price

    def inputAnswer(self, input_value):
        while True:
            userInput = input(input_value)
            if userInput in ['v', 'n']:
                return userInput
            print("y or n! Try again.")

    def inputNumber(self, input_value):
        while True:
            try:
                userInput = float(input(input_value))
            except ValueError:
                print("Not a number! Try again.")
                continue
            else:
                return userInput

    def deliveryType(self, input_value):
        if input_value == 1:
            delivery_type = 1
        elif input_value == 2:
            delivery_type = 2
        else:
            delivery_type = 3
        return delivery_type

    def totalTime(self, products):
        total_time = 0
        time_per_unit = deliveryType(self.delivery_type)
        for k, v in products.items():
            total_time += (int(v['qnt'])) * time_per_unit
        self.total_time = total_time
        return total_time