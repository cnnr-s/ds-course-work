"""Sample order data for the Ch3 project "Records explorer".

84 sales orders from a fictional office-supplies distributor, January to June 2026.
The export system glitched, so a few orders appear more than once (exact copies).

Usage (with this file in the same folder as your script or notebook):
    from orders_data import ORDERS

Fields per record:
    order_id   str    unique order number, e.g. 'SO-1001'
    date       str    order date, ISO format 'YYYY-MM-DD'
    customer   str    customer company name
    region     str    sales region: West, Prairies, Ontario, Quebec, Atlantic
    product    str    product name
    category   str    Office Supplies, Furniture, Technology or Breakroom
    qty        int    units ordered
    unit_price float  price per unit in CAD
    notes      str    free-text note from the sales rep ('' if none)
"""

ORDERS = [
    {'order_id': 'SO-1001', 'date': '2026-01-05', 'customer': 'Laurentian Clinic', 'region': 'Quebec', 'product': 'Ergonomic chair', 'category': 'Furniture', 'qty': 4, 'unit_price': 389.0, 'notes': 'damaged box on arrival, replacement sent'},
    {'order_id': 'SO-1002', 'date': '2026-01-10', 'customer': 'Northern Logistics', 'region': 'Ontario', 'product': 'Coffee beans (5 lb)', 'category': 'Breakroom', 'qty': 8, 'unit_price': 68.0, 'notes': 'new office setup'},
    {'order_id': 'SO-1003', 'date': '2026-01-10', 'customer': 'Vieux-Port Bistro', 'region': 'Quebec', 'product': 'Filing cabinet', 'category': 'Furniture', 'qty': 5, 'unit_price': 229.0, 'notes': 'bulk discount discussed with sales rep'},
    {'order_id': 'SO-1004', 'date': '2026-01-11', 'customer': 'Maple Leaf Dental', 'region': 'Ontario', 'product': 'Paper cups (500)', 'category': 'Breakroom', 'qty': 7, 'unit_price': 32.4, 'notes': 'quote approved by finance'},
    {'order_id': 'SO-1005', 'date': '2026-01-11', 'customer': 'Northern Logistics', 'region': 'Ontario', 'product': 'Paper cups (500)', 'category': 'Breakroom', 'qty': 6, 'unit_price': 32.4, 'notes': 'back order, ship when available'},
    {'order_id': 'SO-1006', 'date': '2026-01-12', 'customer': 'Prairie Grain Co-op', 'region': 'Prairies', 'product': 'Filing cabinet', 'category': 'Furniture', 'qty': 5, 'unit_price': 229.0, 'notes': 'repeat order'},
    {'order_id': 'SO-1007', 'date': '2026-01-17', 'customer': 'Summit Engineering', 'region': 'Prairies', 'product': '27in monitor', 'category': 'Technology', 'qty': 3, 'unit_price': 299.99, 'notes': 'replacement for damaged item'},
    {'order_id': 'SO-1008', 'date': '2026-01-20', 'customer': 'Cascade Outfitters', 'region': 'West', 'product': 'Laser printer', 'category': 'Technology', 'qty': 5, 'unit_price': 449.0, 'notes': 'back order, ship when available'},
    {'order_id': 'SO-1006', 'date': '2026-01-12', 'customer': 'Prairie Grain Co-op', 'region': 'Prairies', 'product': 'Filing cabinet', 'category': 'Furniture', 'qty': 5, 'unit_price': 229.0, 'notes': 'repeat order'},
    {'order_id': 'SO-1009', 'date': '2026-01-20', 'customer': 'Red River Schools', 'region': 'Prairies', 'product': 'Laser printer', 'category': 'Technology', 'qty': 2, 'unit_price': 449.0, 'notes': ''},
    {'order_id': 'SO-1010', 'date': '2026-01-23', 'customer': 'Coastline Realty', 'region': 'West', 'product': '27in monitor', 'category': 'Technology', 'qty': 6, 'unit_price': 299.99, 'notes': 'back order, ship when available'},
    {'order_id': 'SO-1011', 'date': '2026-01-25', 'customer': 'Rideau Accounting', 'region': 'Ontario', 'product': 'Laser printer', 'category': 'Technology', 'qty': 2, 'unit_price': 449.0, 'notes': 'new office setup, rush delivery requested'},
    {'order_id': 'SO-1012', 'date': '2026-02-01', 'customer': 'Vieux-Port Bistro', 'region': 'Quebec', 'product': '27in monitor', 'category': 'Technology', 'qty': 2, 'unit_price': 299.99, 'notes': 'bulk discount discussed with sales rep'},
    {'order_id': 'SO-1013', 'date': '2026-02-03', 'customer': 'Cascade Outfitters', 'region': 'West', 'product': 'Ergonomic chair', 'category': 'Furniture', 'qty': 4, 'unit_price': 389.0, 'notes': 'bulk discount discussed with sales rep'},
    {'order_id': 'SO-1014', 'date': '2026-02-05', 'customer': 'Red River Schools', 'region': 'Prairies', 'product': 'Gel pens (12-pack)', 'category': 'Office Supplies', 'qty': 19, 'unit_price': 14.5, 'notes': 'new office setup'},
    {'order_id': 'SO-1015', 'date': '2026-02-08', 'customer': 'Rideau Accounting', 'region': 'Ontario', 'product': 'USB-C dock', 'category': 'Technology', 'qty': 1, 'unit_price': 179.0, 'notes': 'back order, ship when available'},
    {'order_id': 'SO-1016', 'date': '2026-02-08', 'customer': 'Vieux-Port Bistro', 'region': 'Quebec', 'product': 'Copy paper (case)', 'category': 'Office Supplies', 'qty': 18, 'unit_price': 54.99, 'notes': 'rush delivery requested'},
    {'order_id': 'SO-1017', 'date': '2026-02-09', 'customer': 'Coastline Realty', 'region': 'West', 'product': 'Filing cabinet', 'category': 'Furniture', 'qty': 4, 'unit_price': 229.0, 'notes': ''},
    {'order_id': 'SO-1018', 'date': '2026-02-14', 'customer': 'Prairie Grain Co-op', 'region': 'Prairies', 'product': 'Laser printer', 'category': 'Technology', 'qty': 7, 'unit_price': 449.0, 'notes': 'invoice to head office, not the branch'},
    {'order_id': 'SO-1019', 'date': '2026-02-15', 'customer': 'Northern Logistics', 'region': 'Ontario', 'product': 'Sticky notes (24-pack)', 'category': 'Office Supplies', 'qty': 7, 'unit_price': 21.75, 'notes': 'damaged box on arrival, replacement sent'},
    {'order_id': 'SO-1020', 'date': '2026-02-15', 'customer': 'Cascade Outfitters', 'region': 'West', 'product': 'Filing cabinet', 'category': 'Furniture', 'qty': 3, 'unit_price': 229.0, 'notes': 'repeat order'},
    {'order_id': 'SO-1021', 'date': '2026-02-15', 'customer': 'Okanagan Wines', 'region': 'West', 'product': 'Laser printer', 'category': 'Technology', 'qty': 4, 'unit_price': 449.0, 'notes': 'repeat order'},
    {'order_id': 'SO-1022', 'date': '2026-02-16', 'customer': 'Laurentian Clinic', 'region': 'Quebec', 'product': 'Coffee beans (5 lb)', 'category': 'Breakroom', 'qty': 5, 'unit_price': 68.0, 'notes': 'replacement for damaged item'},
    {'order_id': 'SO-1023', 'date': '2026-02-17', 'customer': 'Red River Schools', 'region': 'Prairies', 'product': 'Ergonomic chair', 'category': 'Furniture', 'qty': 3, 'unit_price': 389.0, 'notes': 'repeat order, same as last month'},
    {'order_id': 'SO-1024', 'date': '2026-02-18', 'customer': 'Granville Studio', 'region': 'West', 'product': 'Wireless keyboard', 'category': 'Technology', 'qty': 6, 'unit_price': 59.99, 'notes': ''},
    {'order_id': 'SO-1025', 'date': '2026-02-19', 'customer': 'Laurentian Clinic', 'region': 'Quebec', 'product': 'Sticky notes (24-pack)', 'category': 'Office Supplies', 'qty': 12, 'unit_price': 21.75, 'notes': ''},
    {'order_id': 'SO-1026', 'date': '2026-03-01', 'customer': 'Red River Schools', 'region': 'Prairies', 'product': 'Copy paper (case)', 'category': 'Office Supplies', 'qty': 7, 'unit_price': 54.99, 'notes': 'back order, ship when available'},
    {'order_id': 'SO-1023', 'date': '2026-02-17', 'customer': 'Red River Schools', 'region': 'Prairies', 'product': 'Ergonomic chair', 'category': 'Furniture', 'qty': 3, 'unit_price': 389.0, 'notes': 'repeat order, same as last month'},
    {'order_id': 'SO-1027', 'date': '2026-03-04', 'customer': 'Okanagan Wines', 'region': 'West', 'product': 'Wireless keyboard', 'category': 'Technology', 'qty': 7, 'unit_price': 59.99, 'notes': ''},
    {'order_id': 'SO-1028', 'date': '2026-03-07', 'customer': 'Northern Logistics', 'region': 'Ontario', 'product': 'Gel pens (12-pack)', 'category': 'Office Supplies', 'qty': 15, 'unit_price': 14.5, 'notes': 'repeat order'},
    {'order_id': 'SO-1029', 'date': '2026-03-08', 'customer': 'Cascade Outfitters', 'region': 'West', 'product': 'Ergonomic chair', 'category': 'Furniture', 'qty': 5, 'unit_price': 389.0, 'notes': 'rush delivery requested'},
    {'order_id': 'SO-1030', 'date': '2026-03-08', 'customer': 'Harbourview Legal', 'region': 'Atlantic', 'product': 'Gel pens (12-pack)', 'category': 'Office Supplies', 'qty': 13, 'unit_price': 14.5, 'notes': 'quote approved by finance'},
    {'order_id': 'SO-1031', 'date': '2026-03-09', 'customer': 'Vieux-Port Bistro', 'region': 'Quebec', 'product': 'Sticky notes (24-pack)', 'category': 'Office Supplies', 'qty': 16, 'unit_price': 21.75, 'notes': 'replacement for damaged item'},
    {'order_id': 'SO-1032', 'date': '2026-03-13', 'customer': 'Rideau Accounting', 'region': 'Ontario', 'product': 'Standing desk', 'category': 'Furniture', 'qty': 1, 'unit_price': 649.0, 'notes': 'rush delivery requested'},
    {'order_id': 'SO-1033', 'date': '2026-03-16', 'customer': 'Prairie Grain Co-op', 'region': 'Prairies', 'product': 'Laser printer', 'category': 'Technology', 'qty': 3, 'unit_price': 449.0, 'notes': ''},
    {'order_id': 'SO-1034', 'date': '2026-03-18', 'customer': 'Red River Schools', 'region': 'Prairies', 'product': 'Wireless keyboard', 'category': 'Technology', 'qty': 5, 'unit_price': 59.99, 'notes': 'call before delivery'},
    {'order_id': 'SO-1035', 'date': '2026-03-25', 'customer': 'Maple Leaf Dental', 'region': 'Ontario', 'product': 'Gel pens (12-pack)', 'category': 'Office Supplies', 'qty': 8, 'unit_price': 14.5, 'notes': 'back order, ship when available'},
    {'order_id': 'SO-1036', 'date': '2026-03-28', 'customer': 'Harbourview Legal', 'region': 'Atlantic', 'product': 'Filing cabinet', 'category': 'Furniture', 'qty': 4, 'unit_price': 229.0, 'notes': 'new office setup, rush delivery requested'},
    {'order_id': 'SO-1037', 'date': '2026-03-28', 'customer': 'Laurentian Clinic', 'region': 'Quebec', 'product': 'Paper cups (500)', 'category': 'Breakroom', 'qty': 10, 'unit_price': 32.4, 'notes': 'repeat order'},
    {'order_id': 'SO-1038', 'date': '2026-03-29', 'customer': 'Cascade Outfitters', 'region': 'West', 'product': 'Ergonomic chair', 'category': 'Furniture', 'qty': 6, 'unit_price': 389.0, 'notes': 'back order, ship when available'},
    {'order_id': 'SO-1039', 'date': '2026-03-31', 'customer': 'Rideau Accounting', 'region': 'Ontario', 'product': 'Laser printer', 'category': 'Technology', 'qty': 8, 'unit_price': 449.0, 'notes': 'rush delivery requested'},
    {'order_id': 'SO-1040', 'date': '2026-04-04', 'customer': 'Summit Engineering', 'region': 'Prairies', 'product': 'Paper cups (500)', 'category': 'Breakroom', 'qty': 9, 'unit_price': 32.4, 'notes': 'bulk discount discussed with sales rep'},
    {'order_id': 'SO-1041', 'date': '2026-04-05', 'customer': 'Coastline Realty', 'region': 'West', 'product': 'Copy paper (case)', 'category': 'Office Supplies', 'qty': 10, 'unit_price': 54.99, 'notes': 'deliver to loading dock at rear'},
    {'order_id': 'SO-1042', 'date': '2026-04-05', 'customer': 'Okanagan Wines', 'region': 'West', 'product': 'Ergonomic chair', 'category': 'Furniture', 'qty': 2, 'unit_price': 389.0, 'notes': ''},
    {'order_id': 'SO-1043', 'date': '2026-04-10', 'customer': 'Red River Schools', 'region': 'Prairies', 'product': 'Sticky notes (24-pack)', 'category': 'Office Supplies', 'qty': 9, 'unit_price': 21.75, 'notes': 'invoice to head office, not the branch'},
    {'order_id': 'SO-1044', 'date': '2026-04-18', 'customer': 'Laurentian Clinic', 'region': 'Quebec', 'product': 'USB-C dock', 'category': 'Technology', 'qty': 4, 'unit_price': 179.0, 'notes': 'replacement for damaged item'},
    {'order_id': 'SO-1045', 'date': '2026-04-18', 'customer': 'Harbourview Legal', 'region': 'Atlantic', 'product': 'Paper cups (500)', 'category': 'Breakroom', 'qty': 4, 'unit_price': 32.4, 'notes': 'bulk discount discussed with sales rep'},
    {'order_id': 'SO-1041', 'date': '2026-04-05', 'customer': 'Coastline Realty', 'region': 'West', 'product': 'Copy paper (case)', 'category': 'Office Supplies', 'qty': 10, 'unit_price': 54.99, 'notes': 'deliver to loading dock at rear'},
    {'order_id': 'SO-1046', 'date': '2026-04-19', 'customer': 'Laurentian Clinic', 'region': 'Quebec', 'product': 'Filing cabinet', 'category': 'Furniture', 'qty': 4, 'unit_price': 229.0, 'notes': ''},
    {'order_id': 'SO-1047', 'date': '2026-04-26', 'customer': 'Summit Engineering', 'region': 'Prairies', 'product': 'Ergonomic chair', 'category': 'Furniture', 'qty': 2, 'unit_price': 389.0, 'notes': 'invoice to head office, not the branch'},
    {'order_id': 'SO-1042', 'date': '2026-04-05', 'customer': 'Okanagan Wines', 'region': 'West', 'product': 'Ergonomic chair', 'category': 'Furniture', 'qty': 2, 'unit_price': 389.0, 'notes': ''},
    {'order_id': 'SO-1048', 'date': '2026-04-26', 'customer': 'Coastline Realty', 'region': 'West', 'product': 'Coffee beans (5 lb)', 'category': 'Breakroom', 'qty': 3, 'unit_price': 68.0, 'notes': 'rush delivery requested'},
    {'order_id': 'SO-1049', 'date': '2026-04-30', 'customer': 'Bluewater Fisheries', 'region': 'Atlantic', 'product': '27in monitor', 'category': 'Technology', 'qty': 8, 'unit_price': 299.99, 'notes': 'new office setup, rush delivery requested'},
    {'order_id': 'SO-1050', 'date': '2026-05-03', 'customer': 'Summit Engineering', 'region': 'Prairies', 'product': 'Standing desk', 'category': 'Furniture', 'qty': 2, 'unit_price': 649.0, 'notes': 'repeat order, same as last month'},
    {'order_id': 'SO-1051', 'date': '2026-05-04', 'customer': 'Vieux-Port Bistro', 'region': 'Quebec', 'product': 'Sticky notes (24-pack)', 'category': 'Office Supplies', 'qty': 16, 'unit_price': 21.75, 'notes': 'damaged box on arrival, replacement sent'},
    {'order_id': 'SO-1052', 'date': '2026-05-06', 'customer': 'Vieux-Port Bistro', 'region': 'Quebec', 'product': 'Coffee beans (5 lb)', 'category': 'Breakroom', 'qty': 1, 'unit_price': 68.0, 'notes': 'new office setup, rush delivery requested'},
    {'order_id': 'SO-1053', 'date': '2026-05-06', 'customer': 'Northern Logistics', 'region': 'Ontario', 'product': 'Laser printer', 'category': 'Technology', 'qty': 3, 'unit_price': 449.0, 'notes': 'bulk discount discussed with sales rep'},
    {'order_id': 'SO-1054', 'date': '2026-05-07', 'customer': 'Okanagan Wines', 'region': 'West', 'product': 'Ergonomic chair', 'category': 'Furniture', 'qty': 1, 'unit_price': 389.0, 'notes': 'quote approved by finance'},
    {'order_id': 'SO-1055', 'date': '2026-05-09', 'customer': 'Maple Leaf Dental', 'region': 'Ontario', 'product': 'Gel pens (12-pack)', 'category': 'Office Supplies', 'qty': 6, 'unit_price': 14.5, 'notes': 'damaged box on arrival, replacement sent'},
    {'order_id': 'SO-1056', 'date': '2026-05-16', 'customer': 'Granville Studio', 'region': 'West', 'product': 'Gel pens (12-pack)', 'category': 'Office Supplies', 'qty': 17, 'unit_price': 14.5, 'notes': 'rush delivery requested'},
    {'order_id': 'SO-1057', 'date': '2026-05-16', 'customer': 'Rideau Accounting', 'region': 'Ontario', 'product': 'Filing cabinet', 'category': 'Furniture', 'qty': 6, 'unit_price': 229.0, 'notes': ''},
    {'order_id': 'SO-1058', 'date': '2026-05-17', 'customer': 'Red River Schools', 'region': 'Prairies', 'product': 'Gel pens (12-pack)', 'category': 'Office Supplies', 'qty': 2, 'unit_price': 14.5, 'notes': 'repeat order'},
    {'order_id': 'SO-1059', 'date': '2026-05-21', 'customer': 'Vieux-Port Bistro', 'region': 'Quebec', 'product': 'Copy paper (case)', 'category': 'Office Supplies', 'qty': 16, 'unit_price': 54.99, 'notes': 'repeat order, same as last month'},
    {'order_id': 'SO-1060', 'date': '2026-05-21', 'customer': 'Red River Schools', 'region': 'Prairies', 'product': 'Standing desk', 'category': 'Furniture', 'qty': 5, 'unit_price': 649.0, 'notes': 'rush delivery requested'},
    {'order_id': 'SO-1061', 'date': '2026-05-22', 'customer': 'Summit Engineering', 'region': 'Prairies', 'product': 'Filing cabinet', 'category': 'Furniture', 'qty': 5, 'unit_price': 229.0, 'notes': 'new office setup'},
    {'order_id': 'SO-1062', 'date': '2026-05-28', 'customer': 'Red River Schools', 'region': 'Prairies', 'product': 'USB-C dock', 'category': 'Technology', 'qty': 2, 'unit_price': 179.0, 'notes': 'deliver to loading dock at rear'},
    {'order_id': 'SO-1063', 'date': '2026-05-29', 'customer': 'Summit Engineering', 'region': 'Prairies', 'product': 'Filing cabinet', 'category': 'Furniture', 'qty': 3, 'unit_price': 229.0, 'notes': ''},
    {'order_id': 'SO-1064', 'date': '2026-05-29', 'customer': 'Okanagan Wines', 'region': 'West', 'product': 'Wireless keyboard', 'category': 'Technology', 'qty': 4, 'unit_price': 59.99, 'notes': 'call before delivery'},
    {'order_id': 'SO-1065', 'date': '2026-05-31', 'customer': 'Summit Engineering', 'region': 'Prairies', 'product': 'USB-C dock', 'category': 'Technology', 'qty': 6, 'unit_price': 179.0, 'notes': 'call before delivery'},
    {'order_id': 'SO-1066', 'date': '2026-05-31', 'customer': 'Okanagan Wines', 'region': 'West', 'product': 'Paper cups (500)', 'category': 'Breakroom', 'qty': 10, 'unit_price': 32.4, 'notes': 'rush delivery, invoice by email'},
    {'order_id': 'SO-1067', 'date': '2026-05-31', 'customer': 'Vieux-Port Bistro', 'region': 'Quebec', 'product': 'Standing desk', 'category': 'Furniture', 'qty': 6, 'unit_price': 649.0, 'notes': ''},
    {'order_id': 'SO-1068', 'date': '2026-06-02', 'customer': 'Vieux-Port Bistro', 'region': 'Quebec', 'product': 'Wireless keyboard', 'category': 'Technology', 'qty': 6, 'unit_price': 59.99, 'notes': 'call before delivery'},
    {'order_id': 'SO-1069', 'date': '2026-06-03', 'customer': 'Granville Studio', 'region': 'West', 'product': 'Standing desk', 'category': 'Furniture', 'qty': 4, 'unit_price': 649.0, 'notes': ''},
    {'order_id': 'SO-1070', 'date': '2026-06-03', 'customer': 'Summit Engineering', 'region': 'Prairies', 'product': 'Wireless keyboard', 'category': 'Technology', 'qty': 1, 'unit_price': 59.99, 'notes': 'damaged box on arrival, replacement sent'},
    {'order_id': 'SO-1071', 'date': '2026-06-05', 'customer': 'Maple Leaf Dental', 'region': 'Ontario', 'product': 'Coffee beans (5 lb)', 'category': 'Breakroom', 'qty': 8, 'unit_price': 68.0, 'notes': 'repeat order, same as last month'},
    {'order_id': 'SO-1072', 'date': '2026-06-08', 'customer': 'Laurentian Clinic', 'region': 'Quebec', 'product': 'Gel pens (12-pack)', 'category': 'Office Supplies', 'qty': 11, 'unit_price': 14.5, 'notes': 'customer asked for invoice by email'},
    {'order_id': 'SO-1073', 'date': '2026-06-10', 'customer': 'Okanagan Wines', 'region': 'West', 'product': '27in monitor', 'category': 'Technology', 'qty': 2, 'unit_price': 299.99, 'notes': 'quote approved by finance'},
    {'order_id': 'SO-1074', 'date': '2026-06-15', 'customer': 'Laurentian Clinic', 'region': 'Quebec', 'product': 'Laser printer', 'category': 'Technology', 'qty': 3, 'unit_price': 449.0, 'notes': 'quote approved by finance'},
    {'order_id': 'SO-1075', 'date': '2026-06-15', 'customer': 'Laurentian Clinic', 'region': 'Quebec', 'product': 'Copy paper (case)', 'category': 'Office Supplies', 'qty': 2, 'unit_price': 54.99, 'notes': 'back order, ship when available'},
    {'order_id': 'SO-1076', 'date': '2026-06-18', 'customer': 'Granville Studio', 'region': 'West', 'product': 'Filing cabinet', 'category': 'Furniture', 'qty': 1, 'unit_price': 229.0, 'notes': 'new office setup, rush delivery requested'},
    {'order_id': 'SO-1077', 'date': '2026-06-21', 'customer': 'Harbourview Legal', 'region': 'Atlantic', 'product': 'Paper cups (500)', 'category': 'Breakroom', 'qty': 8, 'unit_price': 32.4, 'notes': 'quote approved by finance'},
    {'order_id': 'SO-1071', 'date': '2026-06-05', 'customer': 'Maple Leaf Dental', 'region': 'Ontario', 'product': 'Coffee beans (5 lb)', 'category': 'Breakroom', 'qty': 8, 'unit_price': 68.0, 'notes': 'repeat order, same as last month'},
    {'order_id': 'SO-1078', 'date': '2026-06-23', 'customer': 'Maple Leaf Dental', 'region': 'Ontario', 'product': 'Wireless keyboard', 'category': 'Technology', 'qty': 1, 'unit_price': 59.99, 'notes': ''},
    {'order_id': 'SO-1079', 'date': '2026-06-26', 'customer': 'Cascade Outfitters', 'region': 'West', 'product': 'Standing desk', 'category': 'Furniture', 'qty': 3, 'unit_price': 649.0, 'notes': 'repeat order'},
    {'order_id': 'SO-1080', 'date': '2026-06-27', 'customer': 'Coastline Realty', 'region': 'West', 'product': 'USB-C dock', 'category': 'Technology', 'qty': 1, 'unit_price': 179.0, 'notes': 'quote approved by finance'},
    {'order_id': 'SO-1081', 'date': '2026-06-28', 'customer': 'Prairie Grain Co-op', 'region': 'Prairies', 'product': 'Laser printer', 'category': 'Technology', 'qty': 2, 'unit_price': 449.0, 'notes': 'repeat order, same as last month'},
    {'order_id': 'SO-1082', 'date': '2026-06-28', 'customer': 'Granville Studio', 'region': 'West', 'product': 'Ergonomic chair', 'category': 'Furniture', 'qty': 5, 'unit_price': 389.0, 'notes': 'new office setup, rush delivery requested'},
    {'order_id': 'SO-1083', 'date': '2026-06-28', 'customer': 'Summit Engineering', 'region': 'Prairies', 'product': 'Paper cups (500)', 'category': 'Breakroom', 'qty': 3, 'unit_price': 32.4, 'notes': 'deliver to loading dock at rear'},
    {'order_id': 'SO-1084', 'date': '2026-06-29', 'customer': 'Red River Schools', 'region': 'Prairies', 'product': '27in monitor', 'category': 'Technology', 'qty': 1, 'unit_price': 299.99, 'notes': 'new office setup, rush delivery requested'},
]
