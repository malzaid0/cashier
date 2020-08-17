def main():
    # write code here

    receipt = []
    total = 0
    entered = input("Item (enter \"done\" when finished): ")

    while entered != "done":
        item_details = {}
        item_details["name"] = entered
        item_details["price"] = float(input("Price: "))
        item_details["quantity"] = int(input("Quantity: "))
        receipt.append(item_details)
        entered = input("Item (enter \"done\" when finished): ")

    print("\n-------------------")
    print("receipt")
    print("-------------------")

    for item in receipt:
        item_total = item["quantity"] * item["price"]
        total += item_total
        print(item["quantity"], item["name"], str("{:.3f}".format(item_total)) + "KD")

    print("-------------------")
    print("Total Price: " + str("{:.3f}".format(total)) + "KD")


if __name__ == '__main__':
    main()
