from .cart import Cart

def cart(request):
    return {'cart': Cart(request) }
# we instantiate the cart using request object and make it available to the templates as a variable named 'cart'.

# A context processor is a python function that takes the request object as an argument and returns a dictionary that gets added to the request context.
#You use context processor when you want to make something available to all the templates.