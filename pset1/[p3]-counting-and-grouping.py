def item_order(order):
    order_list = order.split(" ")
    return 'salad:' + str(order_list.count("salad")) + ' hamburger:' + str(order_list.count("hamburger")) + ' water:' + str(order_list.count("water"))
