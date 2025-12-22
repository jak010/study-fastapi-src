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

INSERT INTO member (email, name, age) VALUES
('only1@test.com', '홍길동', 28),
('only2@test.com', '김철수', 35),
('only3@test.com', '이영희', 22);

/* =========================
   MEMBER + PROFILE
   ========================= */
INSERT INTO member (email, name, age) VALUES
('both1@test.com', '박민수', 30),
('both2@test.com', '최지은', 27),
('both3@test.com', '정우성', 41);

/* profile은 email 기준으로 member_id 조회해서 INSERT */
INSERT INTO member_profile (member_id, phone, hit, birth_date)
SELECT
    m.member_id,
    CASE m.email
        WHEN 'both1@test.com' THEN '010-1111-2222'
        WHEN 'both2@test.com' THEN '010-3333-4444'
        WHEN 'both3@test.com' THEN '010-5555-6666'
    END AS phone,
    CASE m.email
        WHEN 'both1@test.com' THEN 10
        WHEN 'both2@test.com' THEN 3
        WHEN 'both3@test.com' THEN 25
    END AS hit,
    CASE m.email
        WHEN 'both1@test.com' THEN '1995-03-21'
        WHEN 'both2@test.com' THEN '1998-07-11'
        WHEN 'both3@test.com' THEN '1983-01-09'
    END AS birth_date
FROM member m
WHERE m.email IN (
    'both1@test.com',
    'both2@test.com',
    'both3@test.com'
);

