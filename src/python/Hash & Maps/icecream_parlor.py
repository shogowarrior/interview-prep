
def get_flavors(money, costs):
    prices = {}

    for i, price in enumerate(costs):
        complement = money - price
        if complement in prices:
            return sorted([prices[complement], i+1])
        prices[price] = i+1
    return None


if __name__ == "__main__":
    money = 4
    costs = [1, 4, 5, 3, 2]
    print(get_flavors(money, costs))

    money = 4
    costs = [2, 2, 4, 3]
    print(get_flavors(money, costs))
