header= """ BOOK STORE RECEIPT """

Book1 = "Python Basics"
Price1 = 450
Book2 =  "Data Science Intro"
Price2 = 600
print("\n\t" + header.upper())

line1 = f"BOOK :\t{Book1}\t\t₹{Price1}"

line2 = f"BOOK :\t{Book2}\t₹{Price2}"

print(line1.upper())
print(line2.upper())
total = Price1 + Price2
print("TOTAL AMOUNT :\t\t₹", total)

thank_you = "\n\tTHANK YOU FOR SHOPPING WITH US!"
print(thank_you.upper())
