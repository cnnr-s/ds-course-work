from orders_data import ORDERS
import copy

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
    o["line_total"] = o["qty"] * o["unit_price"]         # creates the new dict item 'line_total' for each order

# check that ORDERS has no 'line_total' with assert
assert all("line_total" not in r for r in ORDERS)
assert all("line_total" in o for o in orders)


