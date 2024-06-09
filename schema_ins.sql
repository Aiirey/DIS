\i schema.sql

DELETE FROM Updates;
DELETE FROM Delivers;
DELETE FROM Users;
DELETE FROM Supplier;
DELETE FROM Item;
DELETE FROM Category;

INSERT INTO Users (name_, password_) VALUES ('4243', '$2y$10$Rcwc60GjOCUpbRBASQBsq.v8BFXysvMfb1.aCqcpnmBX145lY3uBi');

INSERT INTO Supplier (name_) VALUES ('Carlsberg');        --1
INSERT INTO Supplier (name_) VALUES ('Drinx');            --2
INSERT INTO Supplier (name_) VALUES ('Sukkerfabrikken');  --3
INSERT INTO Supplier (name_) VALUES ('KiMs');             --4

INSERT INTO Category (name_) VALUES ('Væske');                              --1
INSERT INTO Category (name_, supercategory_id) VALUES ('Sodavand', 1);      --2
INSERT INTO Category (name_, supercategory_id) VALUES ('Sukkerfri', 2);     --3
INSERT INTO Category (name_, supercategory_id) VALUES ('Alkohol', 1);       --4
INSERT INTO Category (name_, supercategory_id) VALUES ('Likør', 4);         --5
INSERT INTO Category (name_, supercategory_id) VALUES ('Shots', 4);         --6
INSERT INTO Category (name_, supercategory_id) VALUES ('Energidrikke', 1);  --7
INSERT INTO Category (name_) VALUES ('Mad');                                --8
INSERT INTO Category (name_, supercategory_id) VALUES ('Snacks', 8);        --9
INSERT INTO Category (name_, supercategory_id) VALUES ('Saltevarer', 9);    --10
INSERT INTO Category (name_, supercategory_id) VALUES ('Sødevarer', 9);     --11
INSERT INTO Category (name_, supercategory_id) VALUES ('Nudler', 8);        --12
INSERT INTO Category (name_, supercategory_id) VALUES ('Cider', 4);         --13
INSERT INTO Category (name_, supercategory_id) VALUES ('Sukkerfri', 7);     --14

INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Coca Cola', 120, 10, 2);                      --1
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Cola Zero', 90, 10, 3);                       --2
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Fanta', 60, 10, 2);                           --3
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Fanta Zero', 30, 10, 3);                      --4
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Chips', 36, 10, 10);                          --5
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Saltstænger', 20, 5, 10);                     --6
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Chokolade', 30, 10, 11);                      --7
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Vingummier', 50, 5, 11);                      --8
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Grøn Tuborg', 60, 15, 4);                     --9
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Guld Tuborg', 60, 20, 4);                     --10
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Sommersby Blackberry', 60, 15, 13);           --11
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Sommersby Apple', 60, 15, 13);                --12
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Sommersby Elderflower', 60, 15, 13);          --13
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Små Fugle', 120, 10, 6);                      --14
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Små Sure', 120, 10, 6);                       --15
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Små Konger', 120, 10, 6);                     --16
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Cuba Caramel', 90, 10, 5);                    --17
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Smirnoff Vodka', 200, 10, 5);                 --18
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Sapphire Gin', 200, 10, 5);                   --19
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Jägermeister', 100, 10, 5);                   --20
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Red Bull Original', 20, 20, 7);               --21
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Red Bull Granatæble', 20, 20, 7);             --22
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Monster', 24, 20, 7);                         --23
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Rød Kinley', 60, 10, 2);                      --24
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Sport', 60, 10, 2);                           --25
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Sprite', 60, 10, 2);                          --26
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Schweppes Lemon', 120, 10, 2);                --27
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Red Bull Sukkerfri', 20, 20, 14);             --28
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Monster Ultra (Hvid)', 24, 20, 14);           --29
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Instant Nudler med kylling', 36, 15, 12);     --30
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Instant Nudler med oksekød', 36, 15, 12);     --31
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Instant Nudler med grøntsager', 72, 15, 12);  --32

INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (1, 1, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 1, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (1, 2, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 2, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (1, 3, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 3, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (1, 4, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 4, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (4, 5, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (4, 6, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (3, 7, 6);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (3, 8, 3);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (1, 9, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 9, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (1, 10, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 10, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (1, 11, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 11, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (1, 12, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 12, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (1, 13, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 13, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 14, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 15, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 16, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 17, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 18, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 19, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 20, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 21, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 22, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (1, 23, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 23, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (1, 24, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 24, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (1, 25, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 25, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (1, 26, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 26, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (1, 27, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 27, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 28, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (1, 29, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 29, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 30, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 31, 5);
INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (2, 32, 5);
