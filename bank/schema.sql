\i schema_drop.sql

CREATE TABLE IF NOT EXISTS Users(
	ID serial PRIMARY KEY,
	name_ varchar(100) UNIQUE,
	password_ varchar(100)
);

CREATE TABLE IF NOT EXISTS Supplier(
	ID serial PRIMARY KEY,
	name_ varchar(100) UNIQUE
);

CREATE TABLE IF NOT EXISTS Category(
	ID serial PRIMARY KEY,
	name_ varchar(100),
	supercategory_id integer DEFAULT NULL,
	FOREIGN KEY (supercategory_id) REFERENCES Category(ID)
);

CREATE TABLE IF NOT EXISTS Item(
	ID serial PRIMARY KEY,
	name_ varchar(100) UNIQUE,
	amount integer DEFAULT 0,
	resaleprice integer,
	category_id integer NOT NULL,
	FOREIGN KEY (category_id) REFERENCES Category(ID)
);

CREATE TABLE IF NOT EXISTS Delivers(
	supplier_id integer,
	item_id integer,
	supplierprice integer,
	CONSTRAINT delivers_key PRIMARY KEY (supplier_id, item_id),
	FOREIGN KEY (supplier_id) REFERENCES Supplier(ID),
	FOREIGN KEY (item_id) REFERENCES Item(ID)
);

CREATE TABLE IF NOT EXISTS Updates(
	user_id integer,
	item_id integer,
	change integer,
	timestamp_ TIMESTAMP, -- TODO: hvad fuck er et timestamp??
	CONSTRAINT updates_key PRIMARY KEY (user_id, item_id),
	FOREIGN KEY (user_id) REFERENCES Users(ID),
	FOREIGN KEY (item_id) REFERENCES Item(ID)
);
