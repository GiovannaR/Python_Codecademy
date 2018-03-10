"""
*Author: Giovanna Avila Riqueti
*Version 1 02/26/2018
"""

class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""
  
  #Global variable
  items_in_cart = {}


  def __init__(self, customer_name):
    self.customer_name = customer_name

  #Add product to the cart.
  def add_item(self, product, price):
    if not product in self.items_in_cart:

      self.items_in_cart[product] = price
      print product + " added."
    
    else:
      print product + " is already in the cart."

  #Remove product from the cart.
  def remove_item(self, product):
    
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print product + " removed."
    else:
      print product + " is not in the cart."

     
    
my_cart = ShoppingCart("Siovanna")
my_cart.add_item("shampoo", 5.00)