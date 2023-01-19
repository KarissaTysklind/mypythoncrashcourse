prompt = "Hello,\nhow many people are in your dinner group?"
guests = int(input(prompt))

if guests > 8:
    print("There is a waiting list, you will have to wait.")
else:
    print("Your table is ready.")
    
