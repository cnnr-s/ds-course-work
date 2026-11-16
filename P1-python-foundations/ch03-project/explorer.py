from orders_data import ORDERS

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


