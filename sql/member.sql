CREATE TABLE member (
	reference_id int(1) unsigned AUTO_INCREMENT,
	name varchar(12) NOT NULL,
	age smallint(1) unsigned default '0',
	PRIMARY KEY(`reference_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

