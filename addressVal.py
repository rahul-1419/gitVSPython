def addressVal(address):
    dot = address.find(".")
    at = address.find("@")

    if (dot == -1):
        print("Address is invalid")

    elif (at == -1):
        print("Address is invalid")

    else:
        print(" Address is Valid")

while(True):
    x=input("Enter the Address: ")
    
    addressVal(x)