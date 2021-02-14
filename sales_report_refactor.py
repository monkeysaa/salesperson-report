"""Read sales file and print out sales report."""

melon_sales = {}

with open('sales-report.txt') as file: 
    for line in file:
        salesperson, sales, melons = line.rstrip().split('|')

        if salesperson in melon_sales:
            melons_sold = melon_sales[salesperson] + int(melons)
            melon_sales[salesperson] = melons_sold

        else: 
            melon_sales[salesperson] = int(melons)


for person in sorted(melon_sales):
     print(f"{person} sold {melon_sales[person]} melons.")