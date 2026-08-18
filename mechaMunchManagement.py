"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """

    for i in items_to_add:
        if i in current_cart.keys():
            current_cart[i]+=1
        else:
            current_cart[i]=1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """
    d=dict()
    for i in notes:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    return d


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """

    newDict= sorted(cart.items())
    return newDict


def send_to_store(cart, aisle_mapping):
    """Combine cart quantity with aisle and refrigeration information."""
    fulfillment_cart = {}
    
    for item, quantity in cart.items():
        # Get aisle and refrigeration data from the mapping dictionary
        aisle, refrigeration = aisle_mapping[item]
        
        # Combine everything into a nested list format
        fulfillment_cart[item] = [quantity, aisle, refrigeration]
        
    # Return sorted by item name in reverse alphabetical order
    return dict(sorted(fulfillment_cart.items(), reverse=True))


    


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order."""
    for item, details in fulfillment_cart.items():
        ordered_quantity = details[0]
        store_inventory[item][0] -= ordered_quantity
        
        # Check if the new stock level is 0
        if store_inventory[item][0] == 0:
            store_inventory[item][0] = "Out of Stock"
            
    return store_inventory

