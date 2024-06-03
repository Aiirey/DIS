from datetime import datetime
from bank import conn, login_manager
from flask_login import UserMixin
from psycopg2 import sql


@login_manager.user_loader
def load_user(user_id):
    user = Users(user_id, "HELLO")
    if user_id != -1:
        user.active = True
    return user

    # TODO: Fix
    cur = conn.cursor()

    schema = 'customers'
    id = 'cpr_number'
    if str(user_id).startswith('60'):
        schema = 'employees'
        id = 'id'

    user_sql = sql.SQL("""
    SELECT * FROM {}
    WHERE {} = %s
    """).format(sql.Identifier(schema),  sql.Identifier(id))

    cur.execute(user_sql, (int(user_id),))
    if cur.rowcount > 0:
        return None


class Users(UserMixin):
    def __init__(self, ID, name):
        self.id = ID
        self.name = name
        self.active = False

    @property
    def is_active(self):
        return self.active


class Supplier():
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name

class Category():
    def __init__(self, ID, name, supercategory_id):
        self.ID = ID
        self.name = name
        self.supercategory_id = supercategory_id
        self.items = []
        self.subcategories = []

class Item():
    def __init__(self, ID, name, amount, resaleprice, category_id):
        self.ID = ID
        self.name = name
        self.amount = amount
        self.resaleprice = resaleprice
        self.category_id = category_id

class Delivers():
    def __init__(self, supplier_id, item_id, supplierprice):
        self.ID = ()
        self.supplier_id = supplier_id
        self.item_id = item_id
        self.supplierprice = supplierprice

class Updates():
    def __init__(self, user_id, item_id, change, timestamp):
        self.ID = ()
        self.user_id = user_id
        self.item_id = item_id
        self.change = change
        self.timestamp = timestamp

# TODO: Make functions for all SQL operations.
def insert_user(name, password):
    cur = conn.cursor()
    sql = """
    INSERT INTO Users(name)
    VALUES (%s, %s)
    """
    cur.execute(sql, (name, password))
    conn.commit()
    cur.close()

def insert_supplier(name):
    cur = conn.cursor()
    sql = """
    INSERT INTO Supplier(name)
    VALUES (%s)
    """
    cur.execute(sql, (name))
    conn.commit()
    cur.close()

def insert_updates(user_id, item_id, change, timestamp_):
    cur = conn.cursor()
    sql = """
    INSERT INTO Updates(user_id, item_id, change, timestamp_)
    VALUES (%s, %s, %s, %s)
    """
    cur.execute(sql, (user_id, item_id, change, timestamp_))
    conn.commit()
    cur.close()

def create_user(name):
    cur = conn.cursor()
    sql = """"
    SELECT ID FROM Users WHERE name_ = %s
    """
    cur.execute(sql, (name))
    ID = cur.fetchone()[0]
    conn.commit()
    cur.close()
    
    return Users(ID, name)

def create_supplier(name):
    cur = conn.cursor()
    sql = """"
    SELECT ID FROM Supplier WHERE name_ = %s
    """
    cur.execute(sql, (name))
    ID = cur.fetchone()[0]
    conn.commit()
    cur.close()
    
    return Supplier(ID, name)

def update_item(name, amount):
    cur = conn.cursor()
    sql = """"
    UPDATE Item SET amount = amount + %i WHERE name_ = %s
    """
    cur.execute(sql, (amount, name))
    ID = cur.fetchone()[0]
    conn.commit()
    cur.close()

def search_item_by_item(name):
    cur = conn.cursor()
    sql = """
    SELECT ID, name_, amount, resaleprice, category_id FROM Item
        WHERE name_ = %s
    """
    cur.execute(sql, (name))
    lstOfItems = cur.fetchall()

    return list(map(lambda item: Item(*item), lstOfItems))

def search_item_by_supplier(name):
    cur = conn.cursor()
    sql = """
    SELECT ID, name_, amount, resaleprice, category_id FROM Item
        WHERE ID IN (SELECT item_id FROM Delivers
                        WHERE supplier_id IN (SELECT ID from Supplier WHERE name_ = %s))
    """
    cur.execute(sql, (name))
    lstOfItems = cur.fetchall()

    return list(map(lambda item: Item(*item), lstOfItems))

def search_item_by_category(name):
    cur = conn.cursor()
    sql = """
    SELECT ID, name_, amount, resaleprice, category_id FROM Item
        WHERE category_id
            IN (WITH RECURSIVE CTE_name AS
                (
                SELECT ID, supercategory_id FROM Category
                WHERE name_ = 'Sukkerfri'
                UNION ALL
                SELECT c.ID, c.supercategory_id
                FROM Category c
                INNER JOIN CTE_name ON c.supercategory_id = CTE_name.ID
                )
                SELECT ID FROM CTE_name)
    """
    cur.execute(sql, (name))
    lstOfItems = cur.fetchall()

    return list(map(lambda item: Item(*item), lstOfItems))

def search_item_by(name):
    return search_item_by_item(name) + search_item_by_supplier(name) + search_item_by_category(name)

def find_all_items():
    cur = conn.cursor()
    sql = """
    SELECT * FROM Item
    """
    cur.execute(sql,)
    lstOfItems = cur.fetchall()

    return list(map(lambda item: Item(*item), lstOfItems))

def find_all_categories():
    cur = conn.cursor()
    sql = """
    SELECT * FROM Category
    """
    cur.execute(sql,)
    lstOfCategories = cur.fetchall()

    return list(map(lambda category: Category(*category), lstOfCategories))

def find_all_items_by_category():
    items = find_all_items()
    categories = find_all_categories()
    root_categories = []

    for category in categories:
        if category.supercategory_id == None:
            root_categories += [category]
        else:
            for category_ in categories:
                if category.supercategory_id == category_.ID:
                    category_.subcategories += [category]
        
        for item in items:
            if item.category_id == category.ID:
                category.items += [item]
    
    return root_categories
