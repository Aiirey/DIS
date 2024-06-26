from flask_login import UserMixin
from pob import conn, login_manager


@login_manager.user_loader
def load_user(username):
    user = create_user(username)
    if user is None:
        return None
    user.active = True
    return user


class Users(UserMixin):
    def __init__(self, ID, name, password):
        self.id = ID
        self.name = name
        self.password = password
        self.active = False

    @property
    def is_active(self):
        return self.active

    def get_id(self):
        return self.name


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
    def __init__(self, supplier_id, item_id, supplierprice,
                 suppliername=None):
        self.ID = ()
        self.supplier_id = supplier_id
        self.item_id = item_id
        self.supplierprice = supplierprice
        self.suppliername = suppliername


class Updates():
    def __init__(self, user_name, item_name, change, timestamp):
        self.ID = ()
        self.user_name = user_name
        self.item_name = item_name
        self.change = change
        self.timestamp = timestamp


def insert_user(name, password):
    cur = conn.cursor()
    sql = """
    INSERT INTO Users(name_, password_)
    VALUES (%s, %s)
    """
    cur.execute(sql, (name, password))
    conn.commit()


def insert_supplier(name):
    cur = conn.cursor()
    sql = """
    INSERT INTO Supplier(name_)
    VALUES (%s)
    """
    cur.execute(sql, (name,))
    conn.commit()


def insert_category(name, supercategory_id=None):
    cur = conn.cursor()
    if supercategory_id == None:
        sql = """
        INSERT INTO Supplier(name_)
        VALUES (%s)
        """
        cur.execute(sql, (name,))
    else:
        sql = """
        INSERT INTO Supplier(name_, supercategory_id)
        VALUES (%s, %s)
        """
        cur.execute(sql, (name, supercategory_id))
    conn.commit()


def insert_item(name, resaleprice, category_id):
    cur = conn.cursor()
    sql = """
    INSERT INTO Item(name_, resaleprice, category_id)
    VALUES (%s, %s, %s)
    """
    cur.execute(sql, (name, resaleprice, category_id))
    conn.commit()


def insert_delivers(supplier_id, item_id, supplierprice):
    cur = conn.cursor()
    sql = """
    INSERT INTO Delivers(supplier_id, item_id, supplierprice)
    VALUES (%s, %s, %s)
    """
    cur.execute(sql, (supplier_id, item_id, supplierprice))
    conn.commit()


def insert_updates(user_id, item_id, change, timestamp_):
    cur = conn.cursor()
    sql = """
    INSERT INTO Updates(user_id, item_id, change, timestamp_)
    VALUES (%s, %s, %s, %s)
    """
    cur.execute(sql, (user_id, item_id, change, timestamp_))
    conn.commit()


def create_user(name):
    cur = conn.cursor()
    sql = """
    SELECT ID, name_, password_ FROM Users WHERE name_ = %s
    """
    cur.execute(sql, (name,))
    potential_user = cur.fetchone()
    cur.close()
    if potential_user == None:
        return potential_user
    else:
        return Users(*potential_user)


def create_supplier(name):
    cur = conn.cursor()
    sql = """
    SELECT ID, name_ FROM Supplier WHERE name_ = %s
    """
    cur.execute(sql, (name,))
    potential_supplier = cur.fetchone()
    cur.close()
    if potential_supplier == None:
        return potential_supplier
    else:
        return Supplier(*potential_supplier)


def create_category(id):
    cur = conn.cursor()
    sql = """
    SELECT ID, name_, supercategory_id FROM Category WHERE ID = %s
    """
    cur.execute(sql, (id,))
    potential_category = cur.fetchone()
    cur.close()
    if potential_category == None:
        return potential_category
    else:
        return Category(*potential_category)


def create_item(name):
    cur = conn.cursor()
    sql = """
    SELECT ID, name_, amount, resaleprice, category_id FROM Item
    WHERE name_ = %s
    """
    cur.execute(sql, (name,))
    potential_item = cur.fetchone()
    cur.close()
    if potential_item == None:
        return potential_item
    else:
        return Item(*potential_item)


def create_delivers_by_item_ID(ID):
    cur = conn.cursor()
    sql = """
    SELECT supplier_id, item_id, supplierprice, suppliername FROM Delivers
    JOIN (SELECT ID, name_ as suppliername FROM Supplier) AS Supplier
    ON Delivers.supplier_id = Supplier.ID
    WHERE item_id = %s
    """
    cur.execute(sql, (ID,))
    delivers = cur.fetchall()
    cur.close()

    return list(map(lambda deliverer: Delivers(*deliverer), delivers))


def add_item_to_item(id, amount):
    cur = conn.cursor()
    sql = """
    UPDATE Item SET amount = amount + %s WHERE ID = %s
    """
    cur.execute(sql, (amount, id))
    conn.commit()


def user_adds_item(user_id, item_id, change):
    if change == "":
        return
    add_item_to_item(item_id, change)

    cur = conn.cursor()
    sql = """
    INSERT INTO Updates (user_id, item_id, change, timestamp_)
    VALUES (%s, %s, %s, CURRENT_TIMESTAMP)
    """

    cur.execute(sql, (user_id, item_id, change))
    conn.commit()


def search_item_by_item(name):
    cur = conn.cursor()
    sql = """
    SELECT ID, name_, amount, resaleprice, category_id FROM Item
        WHERE LOWER(name_) LIKE LOWER(%s) ORDER BY name_
    """
    cur.execute(sql, ("%" + name + "%",))
    items = cur.fetchall()
    cur.close()

    return list(map(lambda item: Item(*item), items))


def search_item_by_supplier(name):
    cur = conn.cursor()
    sql = """
    SELECT ID, name_, amount, resaleprice, category_id FROM Item
        WHERE ID IN (SELECT item_id FROM Delivers
                        WHERE supplier_id IN
                            (SELECT ID from Supplier
                                WHERE LOWER(name_) LIKE LOWER(%s)))
    ORDER BY name_
    """
    cur.execute(sql, ("%" + name + "%",))
    items = cur.fetchall()
    cur.close()

    return list(map(lambda item: Item(*item), items))


def search_item_by_category(name):
    cur = conn.cursor()
    sql = """
    SELECT ID, name_, amount, resaleprice, category_id FROM Item
        WHERE category_id
            IN (WITH RECURSIVE CTE_name AS
                (
                SELECT ID, supercategory_id FROM Category
                WHERE LOWER(name_) LIKE LOWER(%s)
                UNION ALL
                SELECT c.ID, c.supercategory_id
                FROM Category c
                INNER JOIN CTE_name ON c.supercategory_id = CTE_name.ID
                )
                SELECT ID FROM CTE_name) ORDER BY name_
    """
    cur.execute(sql, ("%" + name + "%",))
    items = cur.fetchall()
    cur.close()

    return list(map(lambda item: Item(*item), items))


def search_item_by_any(name):
    return (search_item_by_item(name) + search_item_by_supplier(name) +
            search_item_by_category(name))


def find_all_items():
    cur = conn.cursor()
    sql = """
    SELECT * FROM Item ORDER BY name_
    """
    cur.execute(sql)
    lstOfItems = cur.fetchall()
    cur.close()

    return list(map(lambda item: Item(*item), lstOfItems))


def find_all_suppliers():
    cur = conn.cursor()
    sql = """
    SELECT * FROM Supplier ORDER BY name_
    """
    cur.execute(sql)
    lstOfSuppliers = cur.fetchall()
    cur.close()

    return list(map(lambda supplier: Supplier(*supplier), lstOfSuppliers))


def find_all_categories():
    cur = conn.cursor()
    sql = """
    SELECT * FROM Category ORDER BY name_
    """
    cur.execute(sql)
    lstOfCategories = cur.fetchall()
    cur.close()

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


def find_items_by_category(items):
    categories = []
    category_ids = []
    root_categories = []

    for item in items:
        if item.category_id not in category_ids:
            categories += [create_category(item.category_id)]
            category_ids += [item.category_id]

    for category in categories:
        if category.supercategory_id not in category_ids:
            root_categories += [category]
        else:
            for category_ in categories:
                if category.supercategory_id == category_.ID:
                    category_.subcategories += [category]

        for item in items:
            if item.category_id == category.ID:
                category.items += [item]

    return root_categories


def create_history():
    cur = conn.cursor()
    sql = """
    SELECT user_name, item_name, change, timestamp_ FROM
    Updates
    JOIN
    (SELECT name_ AS item_name, ID FROM Item) AS Item
    ON Updates.item_id = Item.ID
    JOIN
    (SELECT name_ AS user_name, ID FROM Users) AS Users
    ON Updates.user_id = Users.ID
    ORDER BY timestamp_ DESC
    """
    cur.execute(sql)
    lstOfUpdates = cur.fetchall()
    cur.close()

    return list(map(lambda update: Updates(*update), lstOfUpdates))
