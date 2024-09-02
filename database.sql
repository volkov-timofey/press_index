--noqa: disable=L010
DROP TABLE IF EXISTS hubs_hub, articles;
CREATE TABLE hubs_hub (
	id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	name varchar(255),
	url varchar(255),
	time_delta_check INTERVAL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE articles (
	id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	hub_id bigint REFERENCES hubs_hub (id) ON DELETE CASCADE,
	title varchar(255),
	date_published DATE,
	url varchar(255),
	article text,
	author_full_name varchar(255),
	author_url varchar(255),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO hubs_hub (name, url, time_delta_check)
VALUES ('Interfux', 'https://www.interfax.ru', '00:10:00');
INSERT INTO hubs_hub (name, url, time_delta_check)
VALUES ('66.ru', 'https://www.66.ru', '00:10:00');
INSERT INTO hubs_hub (name, url, time_delta_check)
VALUES ('Russia Today', 'https://russian.rt.com', '00:10:00');
CREATE UNIQUE INDEX url_article ON articles(url);