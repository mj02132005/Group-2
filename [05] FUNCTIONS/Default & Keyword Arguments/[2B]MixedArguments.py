def shipping_cost(weight, express=False, remote_area=False):
    cost = weight * 50
    if express: cost += 100
    if remote_area: cost += 75
    return cost

print(shipping_cost(2, express=True, remote_area=True))
