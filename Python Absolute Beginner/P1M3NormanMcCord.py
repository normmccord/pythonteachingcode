# Norman McCord
# P1M1 assignment

# defining the cheese ordering function to calculate a total based on the weight of cheese the cusomer wants
def cheese_order(order_amount = 0, min_weight = 1, max_weight = 100, price = 7.99):
    if order_amount < min_weight:
        print(f"{order_amount} is below minimum order amount.")
    elif order_amount > max_weight:
        print(f"{order_amount} is more than currently available stock.")
    else:
        total_cost = order_amount * price
        print(f"{order_amount} costs ${total_cost:.2f}.")

full_name = input("What is the full customer name for the order? ")
cust_order = input(f"{full_name}, enter the weight for your cheese order: ")

# since the cheese_order function has defaults for all parameters, we don't have to pass any info.  We give the order amount simply because the order won't be for zero cheese.
cheese_order(order_amount = float(cust_order))

