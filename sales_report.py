"""Generate sales report showing total melons each salesperson sold.

    Data in two related but disconnected lists is inefficient and in danger of
    data confusion / misalignment. Better to refactor as a dictionary with
    salespeople as keys and a list of melons and money as values. """

# initialize two empty lists
salespeople = []
melons_sold = []

# Read each line in the sales report
f = open('sales-report.txt')
for line in f:
    line = line.rstrip()
    entries = line.split('|') 

    # assign variables
    salesperson = entries[0]
    melons = int(entries[2])

    # if salesperson is recorded, note index and increment melons sold.
    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        melons_sold[position] += melons
    # else add to the list and add the melons to their list
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# Print summary of the sales report, showing melons sold per salesperson. 
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
