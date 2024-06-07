\i schema.sql

DELETE FROM Updates;
DELETE FROM Delivers;
DELETE FROM Users;
DELETE FROM Supplier;
DELETE FROM Item;
DELETE FROM Category;

INSERT INTO Users (name_, password_) VALUES ('4243', '$2y$10$Rcwc60GjOCUpbRBASQBsq.v8BFXysvMfb1.aCqcpnmBX145lY3uBi');

INSERT INTO Category (name_) VALUES ('Væske');                                                      --1
INSERT INTO Category (name_, supercategory_id) VALUES ('Sodavand', 1);                              --2
INSERT INTO Category (name_, supercategory_id) VALUES ('Sukkerfri', 2);                             --3
INSERT INTO Category (name_, supercategory_id) VALUES ('Alkohol', 1);                               --4
INSERT INTO Category (name_, supercategory_id) VALUES ('Likør', 4);                                 --5
INSERT INTO Category (name_, supercategory_id) VALUES ('Shots', 4);                                 --6
INSERT INTO Category (name_, supercategory_id) VALUES ('Energidrikke', 1);                          --7
INSERT INTO Category (name_) VALUES ('Mad');                                                        --8
INSERT INTO Category (name_, supercategory_id) VALUES ('Snacks', 8);                                --9
INSERT INTO Category (name_, supercategory_id) VALUES ('Saltevarer', 9);                            --10
INSERT INTO Category (name_, supercategory_id) VALUES ('Sødevarer', 9);                             --11
INSERT INTO Category (name_, supercategory_id) VALUES ('Nudler', 8);                                --12
INSERT INTO Category (name_, supercategory_id) VALUES ('Cider', 4);                                 --13
INSERT INTO Category (name_, supercategory_id) VALUES ('Sukkerfri', 7);                             --14

INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Coca Cola', 120, 10, 2);        --1
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Cola Zero', 90, 10, 3);         --2
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Fanta', 60, 10, 2);             --3
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Fanta Zero', 30, 10, 3);        --4
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Chips', 36, 10, 10);            --5
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Saltstænger', 20, 5, 10);       --6
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Chokolade', 30, 10, 11);        --7
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Vingummier', 50, 5, 11);        --8
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Grøn Tuborg', 60, 15, 4);       --9
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Guld Tuborg', 60, 20, 4);       --10
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Sommersby Blackberry', 60, 15, 13);     --11
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Sommersby Apple', 60, 15, 13);          --12
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Sommersby Elderflower', 60, 15, 13);    --12
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Små Fugle', 120, 10, 6);        --12
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Små Sure', 120, 10, 6);         --12
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Små Konger', 120, 10, 6);       --12
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Cuba Caramel', 90, 10, 5);      --12
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Smirnoff Vodka', 200, 10, 5);   --12
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Sapphire Gin', 200, 10, 5);     --12
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Jägermeister', 100, 10, 5);     --12
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Red Bull Original', 20, 20, 7); --12
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Red Bull Granatæble', 20, 20, 7); --12
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Monster', 24, 20, 7);           --12
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Rød Kinley', 60, 10, 2);        --1
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Sport', 60, 10, 2);             --1
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Sprite', 60, 10, 2);            --1
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Schweppes Lemon', 120, 10, 2);  --1
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Red Bull Sukkerfri', 20, 20, 14);       --12
INSERT INTO Item (name_, amount, resaleprice, category_id) VALUES ('Monster Ultra (Hvid)', 24, 20, 14);     --12


INSERT INTO Supplier (name_) VALUES ('Carlsberg');
INSERT INTO Supplier (name_) VALUES ('Drinx');
INSERT INTO Supplier (name_) VALUES ('Sukkerfabrikken');
INSERT INTO Supplier (name_) VALUES ('KiMs');


INSERT INTO Delivers (supplier_id, item_id, supplierprice) VALUES (1, 3, 6);
