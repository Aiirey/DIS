\i schema.sql

DELETE FROM Updates;
DELETE FROM Delivers;
DELETE FROM Users;
DELETE FROM Supplier;
DELETE FROM Item;
DELETE FROM Category;

INSERT INTO Category (name_) VALUES ('Væske');
INSERT INTO Category (name_, supercategory_id) VALUES ('Sodavand', 1);
INSERT INTO Category (name_, supercategory_id) VALUES ('Alkohol', 1);
INSERT INTO Category (name_, supercategory_id) VALUES ('Sukkerfri', 2);
INSERT INTO Category (name_) VALUES ('Mad');

INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Pip', 20, 10, 1);
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Pap', 20, 10, 1);
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Coca Cola', 20, 10, 2);
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Fanta', 20, 10, 2);
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Cola Zero', 20, 10, 4);
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Fanta Zero', 20, 10, 4);

