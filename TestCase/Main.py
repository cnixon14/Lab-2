from Invoice import Invoice

products = {}
total_amount = 0
repeat = ''
total_time = 0
delivery_type = 0
while True:
    print("Select delivery ")
    delivery_type = Invoice().inputNumber("Please enter your selection : ")
    if delivery_type > 0 or delivery_type <= 3:
        break
while True:
    product = input('What is your product : ')
    unit_price = Invoice().inputNumber("Please enter unit price : ")
    qnt = Invoice().inputNumber("Please enter quantity of product : ")
    discount = Invoice().inputNumber("Discount percent (%) : ")
    repeat = Invoice().inputAnswer("Another product? (y, n) : ")
    result = Invoice().addProduct(qnt, unit_price, discount, delivery_type)
    products[product] = result
    if repeat == "n":
        break


total_amount = Invoice().totalPurePrice(products)
total_time = Invoice().totalTime(products)

print("Your total pure price is: ", total_amount)
print("Total time for delivery is {0} day(s)".format(total_time))
