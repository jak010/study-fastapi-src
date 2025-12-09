CREATE TABLE `member` (
  `member_id` int(1) unsigned NOT NULL AUTO_INCREMENT,
  `email` varchar(36) NOT NULL,
  `name` varchar(12) NOT NULL,
  `age` smallint(1) unsigned DEFAULT '0',
  PRIMARY KEY (`member_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8