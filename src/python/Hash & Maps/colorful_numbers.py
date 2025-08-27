
def get_color(arr):
    products = set()

    for i in range(len(arr)):
        product = 1
        for j in range(i, len(arr)):
            product *= int(arr[j])
            if product in products:
                return False
            products.add(product)
    return True
        
print(get_color("3245"))
print(get_color("326"))