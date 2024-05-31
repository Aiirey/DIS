\i schema_drop.sql

CREATE TABLE IF NOT EXISTS User(
	ID integer IDENTITY[(1,1)] PRIMARY KEY,
	_name varchar(100) UNIQUE,
	_password varchar(100)
);

CREATE TABLE IF NOT EXISTS Supplier(
	ID integer IDENTITY[(1,1)] PRIMARY KEY,
	_name varchar(100) UNIQUE
);

CREATE TABLE IF NOT EXISTS Item(
	ID integer IDENTITY[(1,1)] PRIMARY KEY,
	_name varchar(100) UNIQUE,
	amount integer,
	resaleprice integer,
	category_id integer NOT NULL,
	FOREIGN KEY (category_id) REFERENCES Category(ID)
);

CREATE TABLE IF NOT EXISTS Category(
	ID integer IDENTITY[(1,1)] PRIMARY KEY,
	_name varchar(100)
	supercategory_id integer,
	FOREIGN KEY (supercategory_id) REFERENCES Category(ID)
);

CREATE TABLE IF NOT EXISTS Delivers(
	supplier integer,
	item integer,
	supplierprice integer,
	CONSTRAINT delivers_key PRIMARY KEY (supplier, item),
	FOREIGN KEY (supplier) REFERENCES Supplier(ID),
	FOREIGN KEY (item) REFERENCES Item(ID)
);

CREATE TABLE IF NOT EXISTS Updates(
	ID integer IDENTITY[(1,1)] PRIMARY KEY,
	user integer,
	item integer,
	_timestamp TIMESTAMP, -- TODO: hvad fuck er et timestamp??
	change integer,
	CONSTRAINT updates_key PRIMARY KEY (user, item),
	FOREIGN KEY (user) REFERENCES User(ID),
	FOREIGN KEY (item) REFERENCES Item(ID)
);
