from orders_data import ORDERS
import copy
from collections import Counter, defaultdict
import math

# task 1 - inspect
    # number of raw records
no_raw_records = len(ORDERS)
# there are 89 raw records
    
    # field names of the first record
field_names_first = ORDERS[0].keys()
# dict_keys(['order_id', 'date', 'customer', 'region', 'product', 'category', 'qty', 'unit_price', 'notes'])

    # sorted distinct values of region and catgeory
        # distinct region names & total unique
distinct_regions = set(r["region"] for r in ORDERS)
len(distinct_regions)
        # {'Quebec', 'Ontario', 'Prairies', 'Atlantic', 'West'}
        # 5

        # distinct category names & total unique
distinct_category = set(r["category"] for r in ORDERS)
len(distinct_category)
        # {'Furniture', 'Office Supplies', 'Breakroom', 'Technology'}
        # 4


# task 2 - de-duplicate
orders = []
duplicates = []
seen = set()    # empty set for unique order id signatures
for o in ORDERS:
    sig = (o["order_id"])
    if sig not in seen:
        seen.add(sig)
        orders.append(o)
    else:
        duplicates.append(o.get('order_id'))

    # unique count
unique_count = len(orders) # = 84
len(ORDERS) # = 89


    # duplicated ids
# print(duplicates) = ['SO-1006', 'SO-1023', 'SO-1041', 'SO-1042', 'SO-1071']

    # verify
first_by_id = {o["order_id"]: o for o in orders}   # creates a set with each order id as the key for the corresponding row

all_exact = all(o == first_by_id[o["order_id"]] for o in ORDERS)   # comprehension checking for all rows in ORDERS eq rows in orders with the same order id

# print("Duplicates are exact copies:", all_exact) = True



# task 3 - add a derived field without touching raw data

orders = copy.deepcopy(orders)          # deepcopy copies the list, and the values inside the list as independent
for o in orders:
    o["line_total"] = round(o["qty"]*o["unit_price"], 2) # creates the new dict item 'line_total' for each order

# check that ORDERS has no 'line_total' with assert
assert all("line_total" not in r for r in ORDERS)
assert all("line_total" in o for o in orders)


# task 4 - revenue by region
                # creates a grouped dict by region totalling the revenues (calculated column) using defaultdict
region_revenue = defaultdict(float)
for o in orders:
    region_revenue[o["region"]] += o["line_total"]


region_revenue = dict(region_revenue)
highest_revenue = sorted(region_revenue.items(), key = lambda r: r[1], reverse=True)


                # tuple list to dict list
highest_revenue = [{'region': reg, 'revenue': rev} for reg, rev in highest_revenue]


                # path B: sum of revenues for each region in the grouped dict
total_revenue = sum(region_revenue.values())


                # derive revenue share proportion column and running revenue share total
share_percentage_total = 0
highest_revenue = copy.deepcopy(highest_revenue)            # copies internal values of highest_revenue
for h in highest_revenue:
    h['revenue_share'] = h['revenue'] / total_revenue       # calculated column -> regional revenue as a percent of totals
    share_percentage_total += h['revenue_share']            


                # regional totals table construction
print(f"{'Region':<12}{'Revenue':^10}{'Share':>8}")             # creates table headers
print('-'*30)           # underline formatting separating values and headers
for item in highest_revenue:
    print(f"{item['region']:<12}{item['revenue']:>10,.2f}{item['revenue_share']:>10,.1%}") # value inputs from dict

print(f"{'Total':<12}{total_revenue:>10,.2f}{share_percentage_total:>10,.1%}")        # prints 'totals' row

                # path A: sum of revenues for each order in orders -> from the raw data
overall_total = sum(o["line_total"] for o in orders)

                # checking if path A and path B provide equal revenue totals -> confirms accurate grouping sums
assert math.isclose(total_revenue, overall_total)



# task 5 - top products

    # grouped orders dict by product
product_revenue = defaultdict(float)
product_qty = defaultdict(int)
for o in orders:
    product_revenue[o["product"]] += o["line_total"]
    product_qty[o["product"]] += o["qty"]

    # each sorted dict split into top 5
top_revenue = sorted(product_revenue.items(), key = lambda r: (-r[1], r[0]))[:5]
top_qty = sorted(product_qty.items(), key = lambda r: (-r[1], r[0]))[:5]

    # top 5 products sold (by revenue)
print("\nTop 5 Revenue Drivers By Product")
for i, (prod,rev) in enumerate(top_revenue, start = 1):
    print(f"{i}. {prod:<16} ${rev:>10,.2f}")

    # top 5 products sold (by volume)
print("\nTop 5 Products by Quantity Sold")
for i, (prod, quantity) in enumerate(top_qty, start = 1):
    print(f"{i}. {prod:<25} {quantity:>3}")



# task 6 - monthly trends

    # count orders per month
monthly_counts = Counter(o["date"][:7] for o in orders).items()


    # printed months in calendar order with bar graph
print("\nMonthly Order Volumes")
for month, count in monthly_counts:
    print(f"{month} {'#' * count} {count}")



# task 7 - cross-sell targets
    # dict -> {customer1: {category 1, category 2, ...}, customer2: {category 1, category 2, ...}...}

customer_categories = defaultdict(set)      # creates an empty set for order rows to fall in
for o in orders:        # each o in orders is a dictionary
    customer_categories[o["customer"]].add(o["category"])
# o['customer'] references the customer key in row o
# .add(o['catgeory']) makes the customer key values a set of all unique categories associated with that key


    # customers who bought from 2 or more categories
print("\nCustomers Who Bought From 2 or More Categories")
for customer, cats in sorted(customer_categories.items()):
    if len(cats) >= 2:
        print(f"{customer:<20}{len(cats):>4}")

    # customers who bought from every category that appears in the data
print("\nCustomers Who Bought From All Categories")
for customer, cats in sorted(customer_categories.items()):
    if distinct_category <= cats:
        print(customer)


    # customers who bought technology but never furniture
tech_customers = {customer for customer, cats in customer_categories.items() if "Technology" in cats}
furniture_customers = {customer for customer, cats in customer_categories.items() if "Furniture" in cats}

print("\nCustomers That Bought Technology But Never Furniture")
for customer in sorted(tech_customers - furniture_customers):           # set operator A not B
    print(customer)





