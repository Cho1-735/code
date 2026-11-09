requested_toppings = ['mushrooms','extra cheese','green peppers']
for requested_topping in requested_toppings:
#    print(f"Adding {requested_topping}")
    if requested_topping =='green peppers':
        print("Sorry,we are out of green peppers right now>")
    else:
        print(f"Adding {requested_topping}")
print("\nFinished making your pizza!")
available_toppings=['mushrooms','olives','green pepers','pepperonis','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry,we don't have {requested_topping}")
print("\nFinished making your pizza!")