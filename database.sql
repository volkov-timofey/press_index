--noqa: disable=L010
DROP TABLE IF EXISTS urls, url_checks;
CREATE TABLE urls (
	id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	name varchar(255),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE url_checks (
	id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	url_id bigint ,
	status_code bigint,
	h1 varchar(255),
	title varchar(255),
	description varchar(255),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);