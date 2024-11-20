from django import template

register = template.Library ()


@register.filter (name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys ()    # {101 : 1}, it means {product_id : quantity}
    for id in keys:
        if int (id) == product.id:
            return True
    return False;


@register.filter (name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys ()
    for id in keys:
        if int (id) == product.id:  # {101 : 1,102 : 3}, its card value
            return cart.get (id)  # card.get(101)  o/p=1,3
    return 0;


@register.filter (name='price_total')
def price_total(product, cart):
    return product.price * cart_quantity (product, cart)
    # 101 product_id which price is 500 and is quantity 1 => 500
    # 102 product_id which price is 800 and is quantity 3 => 2400


@register.filter (name='total_cart_price')
def total_cart_price(products, cart):
    sum = 0;
    for p in products:
        sum += price_total (p, cart)

    return sum
