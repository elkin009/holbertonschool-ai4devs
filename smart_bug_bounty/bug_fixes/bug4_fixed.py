def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

if __name__ == '__main__':
    cart1 = add_item('apple')
    cart2 = add_item('banana')
    assert cart1 == ['apple'], f'Test 1 failed: {cart1}'
    print('Test 1 passed')
    assert cart2 == ['banana'], f'Test 2 failed: {cart2}'
    print('Test 2 passed')
    my_cart = []
    add_item('milk', my_cart)
    add_item('eggs', my_cart)
    assert my_cart == ['milk', 'eggs'], f'Test 3 failed: {my_cart}'
    print('Test 3 passed')
    print('All tests passed for bug4_fixed.py')
