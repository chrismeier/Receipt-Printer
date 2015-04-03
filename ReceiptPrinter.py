tax = float(raw_input("What is the tax rate in your county? \n"))
tip = float(raw_input("How much do you want to tip this sucker? \n"))

def find_subtotal():
    items_ordered = int(raw_input("How many items did you order? \n")) 
    prices_of_items = []

    
    i = 1
    for items in range(1, items_ordered +1) :
        prices_of_items.append(raw_input("How much did item %d cost? " % items))

        i += 1
        bill = 0.0

    i = 1
    print "\n\nTOTAL BILL" 
    print "---------------------------"

    for items in prices_of_items:
        print "Item #%d: \t" % i + items
        i += 1
    print "---------------------------"

    for items in prices_of_items:
        bill  = bill + float(items)

    return bill

bill = find_subtotal()


def tax_calculator(bill, tax_rate):
    total_tax = bill * tax_rate / 100
    return total_tax

def tip_calculator(bill, tip_rate):
    total_tip = bill * tip_rate / 100
    return total_tip

def total_bill(bill, tax, tip):
    total_tax = tax_calculator(bill, tax)
    total_tip = tip_calculator(bill, tip)
    total_bill = bill + total_tax + total_tip
    print "Subtotal: \t$%r"  % bill
    print "Tax: \t\t$%r" % total_tax
    print "Tip Rate \t%r"  % tip + "%" 
    print "Total \t\t$%r " % total_bill

total_bill(bill, tax, tip)
print "\n\n"