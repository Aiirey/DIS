DELETE FROM User;

INSERT INTO User () VALUES ();

INSERT INTO Category (name_) VALUES ('Sodavand');

INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Coca Cola', 3000, 10, 1);
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Squash', 1000, 10, 1);


INSERT INTO Supplier (name_) ("Carlsberg");
INSERT INTO Supplier (name_) ("Drinx");

INSERT INTO User (name_, password_) ("Admin", "1235");


INSERT INTO Delivers (supplier, item, supplierprice) VALUES (1, 1, 7);
