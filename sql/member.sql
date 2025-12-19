CREATE TABLE `member` (
  `member_id` int(1) unsigned NOT NULL AUTO_INCREMENT,
  `email` varchar(36) NOT NULL,
  `name` varchar(12) NOT NULL,
  `age` smallint(1) unsigned DEFAULT '0',
  PRIMARY KEY (`member_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `member_profile` (
  `member_id` int(1) unsigned NOT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `hit` int(1) unsigned DEFAULT 0,
  `birth_date` date DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO member (email, name, age) VALUES ('testuser@example.com', '홍길동', 30);
INSERT INTO member_profile (member_id, phone, birth_date) VALUES (1, '010-1234-5678', '1995-05-10');
