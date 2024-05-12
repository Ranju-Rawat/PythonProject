IteminCart = 0

# if IteminCart != 2:
#     raise Exception("Product count not matching")
#
# assert(IteminCart == 0)

try:
    with open("test.txt") as file:
        file.read()
except Exception as e:
    print("not found", e)

finally:
    print("finally")