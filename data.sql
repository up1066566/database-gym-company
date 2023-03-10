CREATE TABLE Gymnastirio (
	KodikosGym integer PRIMARY KEY AUTO_INCREMENT NOT NULL,
	Periochi varchar(30) NOT NULL,
	Arithmos integer(3) NOT NULL,
	Odos varchar(30) NOT NULL,
	T_K varchar(5) NOT NULL
);

CREATE TABLE Aithousa (
	id_aith integer AUTO_INCREMENT NOT NULL,
	tetragonika_metra integer ,
	Gym integer NOT NULL,
	PRIMARY KEY (id_aith, Gym),
	CONSTRAINT `Aithousa_fk0` FOREIGN KEY (`Gym`) REFERENCES `Gymnastirio`(`KodikosGym`)  ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE Ergazomenos (
	onoma varchar(30) NOT NULL,
	eponimo varchar(30) NOT NULL,
	afm varchar(9) UNIQUE NOT NULL,
	tilefono varchar(14) UNIQUE NOT NULL,
	misthos decimal(10,2) NOT NULL,
	arSymv integer NOT NULL,
	super_id integer,
	id integer PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE,
	CONSTRAINT `Ergazomenos_fk0` FOREIGN KEY (`super_id`) REFERENCES `Ergazomenos`(`id`) ON UPDATE CASCADE
);

CREATE TABLE Gymnastis (
	eidos varchar(20) NOT NULL,
	id integer NOT NULL,
	PRIMARY KEY (id),
	CONSTRAINT `Gymnastis_fk0` FOREIGN KEY (`id`) REFERENCES `Ergazomenos`(`id`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Ypallilos (
	idiotita varchar(20) NOT NULL,
	id integer NOT NULL,
	PRIMARY KEY (id),
	CONSTRAINT `Ypallilos_fk0` FOREIGN KEY (`id`) REFERENCES `Ergazomenos`(`id`)  ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Eksoplismos (
	Gym integer NOT NULL,
	id_eks integer AUTO_INCREMENT NOT NULL ,
	posotita integer NOT NULL ,
	eidos varchar(30) NOT NULL,
	aithousa integer NOT NULL,
	PRIMARY KEY(id_eks, Gym),
	CONSTRAINT `Eksoplismos_fk0` FOREIGN KEY (`Gym`) REFERENCES `Gymnastirio`(`KodikosGym`) ON UPDATE CASCADE,
	CONSTRAINT `Eksoplismos_fk1` FOREIGN KEY (`aithousa`) REFERENCES `Aithousa`(`id_aith`) ON UPDATE CASCADE
);

CREATE TABLE Programma (
	timi integer NOT NULL,
	onoma varchar(20) NOT NULL,
	id integer PRIMARY KEY AUTO_INCREMENT NOT NULL
);

CREATE TABLE Eidos_drast (
	eidos varchar(20) NOT NULL,
	typos varchar(7) NOT NULL,
	id integer PRIMARY KEY AUTO_INCREMENT NOT NULL
);

CREATE TABLE Eggegrammenos (
	id integer PRIMARY KEY AUTO_INCREMENT NOT NULL,
	email varchar(255) UNIQUE NOT NULL ,
	onoma varchar(30) NOT NULL,
	eponimo varchar(30) NOT NULL,
	thlefono varchar(14) UNIQUE NOT NULL
);

CREATE TABLE perilambanei (
	id_p integer NOT NULL,
	id_drast integer NOT NULL,
	id integer PRIMARY KEY AUTO_INCREMENT NOT NULL,
 	CONSTRAINT `perilambanei_fk0` FOREIGN KEY (`id_p`) REFERENCES `Programma`(`id`) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT `perilambanei_fk1` FOREIGN KEY (`id_drast`) REFERENCES `Eidos_drast`(`id`) ON UPDATE CASCADE
);

CREATE TABLE eggrafi_pr (
	id_pr integer NOT NULL,
	id_egg integer NOT NULL,
	ekptosi integer NOT NULL,
	hm_eggr date NOT NULL,
	hm_liksis date NOT NULL,
	id integer PRIMARY KEY AUTO_INCREMENT NOT NULL,
	CONSTRAINT `eggrafi_pr_fk0` FOREIGN KEY (`id_pr`) REFERENCES `Programma`(`id`) ON UPDATE CASCADE,
	CONSTRAINT `eggrafi_pr_fk1` FOREIGN KEY (`id_egg`) REFERENCES `Eggegrammenos`(`id`) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE Drastiriotita (
	Ora_enarksis time NOT NULL,
	Ora_liksis time NOT NULL,
	Mera integer NOT NULL,
	e_id integer NOT NULL,
	Gym integer NOT NULL,
	aithousa integer NOT NULL,
	eid_drast_id integer NOT NULL,
	id integer AUTO_INCREMENT,
	PRIMARY KEY (id, eid_drast_id,  Gym),
    CONSTRAINT `Drastiriotita_fk0` FOREIGN KEY (`e_id`) REFERENCES `Gymnastis`(`id`) ON UPDATE CASCADE,
    CONSTRAINT `Drastiriotita_fk1` FOREIGN KEY (`Gym`) REFERENCES `Gymnastirio`(`KodikosGym`)  ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `Drastiriotita_fk2` FOREIGN KEY (`aithousa`) REFERENCES `Aithousa`(`id_aith`) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `Drastiriotita_fk3` FOREIGN KEY (`eid_drast_id`) REFERENCES `Eidos_drast`(`id`) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE simmetexei (
	eggr integer NOT NULL,
	dra integer NOT NULL,
	id integer PRIMARY KEY AUTO_INCREMENT NOT NULL,
	CONSTRAINT `simmetexei_fk0` FOREIGN KEY (`eggr`) REFERENCES `Eggegrammenos`(`id`) ON DELETE CASCADE ,
	CONSTRAINT `simmetexei_fk1` FOREIGN KEY (`dra`) REFERENCES `Drastiriotita`(`id`) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO `Gymnastirio` (`Periochi`,`Arithmos`,`Odos`,`T_K`) VALUES 
	("????????????????",56,"????????????",24100), 
	('??????????', 81, '????????????????', 26223), 
	('??????', 13, '???? ??????????????', 85300),
        ("??????????",6,"??????????????",23131),
        ("????????????",45,"??????????",25601);

INSERT INTO `Eidos_drast`(`eidos`, `typos`) VALUES 
	('YOGA', '??????????????'), 
	('????????????', '??????????????'),
	('PILATES', '??????????????'),
        ("KICK_BOXING","??????????????"),
	('ARIAL ACROBATICS', '??????????????');

INSERT INTO `Aithousa` (`tetragonika_metra`,`gym`) VALUES
	(25, 1),
	(15,1),
	(15,2),
	(18,1),
	(50,2),
	(60,3),
	(40,3),
        (30,3),
        (42,4),
        (80,4),
        (45,5),
        (80,5),
        (60,5);

INSERT INTO `Ergazomenos` (`onoma`,`eponimo`, `afm`, `tilefono`, `misthos`, `arSymv`) VALUES
	('??????????????????', '????????????????', '101010101', '00306987654321', 2400.25, 1),
	("????????????????","????????????????",'123456789','00306973851454',1900.00,1);

INSERT INTO `Ergazomenos` (`onoma`,`eponimo`, `afm`, `tilefono`, `misthos`, `arSymv`, super_id) VALUES
	('??????????????', '??????????????????????', '010101010', '00306945678900', 1300.23,2,1),
	('??????????????', '????????????????????', '110101010', '00306945678991', 1300.23,2,1),
	('????????????', '????????????????????', '110101017', '00306985678991', 1100.23,2,1),
	('????????????????', '??????????????????????????', '810101017', '00306985678992', 1100.23,2,1),
 	("??????????????????????","??????????????????????",'123456779','00306973851694',1000.50,2,2),
 	("????????????????","????????????????????????",'123556789','00306973951454',900.00,2,2);

INSERT INTO `Ypallilos` (idiotita, id) VALUES 
	('????????????????????', 1),
        ('??????????????????????????', 2);
	
INSERT INTO `Gymnastis`	(eidos, id) VALUES
	('YOGA', 3),
	('ARIAL ACROBATICS',4),
	('????????????', 5),
	('????????????', 6),
	("KICK_BOXING",7),
	('????????????',8);

INSERT INTO `Programma` (`timi`,`onoma`) VALUES 
	(30,"????????"),
	(50,"KICK_BOXING"),
	(60,"PREMIUM");

INSERT INTO `perilambanei` (`id_p`,`id_drast`) VALUES
	(1,2),
 	(2,2),
	(2,4),
 	(3,1),
 	(3,2),
	(3,3),
	(3,4),
 	(3,5);

INSERT INTO `Eggegrammenos` (`onoma`,`eponimo`,`email`,`thlefono`) VALUES
	("????????????????","????????????????","nikkar@gmail.com",00306966851454),
	("??????","????????","papaaa@gmail.com",00306973851665),
	("??????????","????????????","markats@gmail.com",00306973851666),
	("????????","??????????????","annkar@gmail.com",00306973851667),
 	("??????????","??????????????","markar@gmail.com",00306973851668);

INSERT INTO `eggrafi_pr` (`id_pr`,`id_egg`,`ekptosi`,`hm_eggr`,`hm_liksis`)VALUES
	(1,1,0,'2022-12-12','2023-1-12'),
 	(1,1,0,'2022-10-10','2022-12-10'),
	(2,2,10,'2022-12-15','2023-1-15'),
	(2,3,0,'2022-12-16','2023-1-16'),
	(3,4,0,'2022-12-17','2023-1-17'),
	(3,5,0,'2022-12-18','2023-1-18');
	
	INSERT INTO `Drastiriotita` (`Gym`,`e_id`,`Ora_enarksis`, `Ora_liksis`, `Mera`, `aithousa`, `eid_drast_id`) VALUES
	(1,3, '12:15', '14:15', 1, 2, 1 ),
	(1,3, '13:15', '14:45', 3, 2, 1 ),
	(1,3, '12:15', '14:15', 3, 2, 1 ),
	(1,3, '11:15', '13:15', 5, 2, 1 ),
	(2,3, '12:15', '14:15', 1, 5, 1 ),
	(2,3, '13:15', '14:45', 2, 5, 1 ),
	(2,3, '12:15', '14:15', 3, 5, 1 ),
	(2,3, '11:15', '13:15', 4, 5, 1 ),
	(1,4, '12:15', '14:45', 1, 4, 4 ),
	(1,4, '12:15', '14:15', 2, 4, 3 ),
	(1,5, '08:30', '15:45', 1, 1, 2 ),
	(1,6, '15:45', '23:00', 2, 1, 2 ),
	(1,5, '08:30', '15:45', 3, 1, 2 ),
	(1,6, '15:45', '23:00', 4, 1, 2 ),
	(1,5, '08:30', '15:45', 5, 1, 2 ),
	(1,6, '15:45', '23:00', 6, 1, 2 ),
	(5,6,'9:00','21:59',1,12,2),
 	(5,6,'9:00','21:59',2,12,2),
 	(5,6,'9:00','21:59',3,12,2),
 	(5,6,'9:00','21:59',4,12,2),
 	(5,8,'9:00','21:59',5,12,2),
 	(5,8,'9:00','20:59',6,12,2),
 	(5,8,'9:00','20:59',7,12,2),
 	(5,7,'19:00','19:59',1,13,4),
 	(5,7,'19:00','19:59',3,13,4),
 	(5,7,'19:00','19:59',5,13,4); 

INSERT INTO `simmetexei` (`eggr`,`dra`)
 VALUES
 (2,25),
 (2,24),
 (3,23),
 (3,24);

INSERT INTO Eksoplismos (Gym,`eidos`,`posotita`,`aithousa`) VALUES
 (1,'??????????????????',4,1),
 (1,'????????????????????',3,1),
 (1,'??????????',3,2),
 (2,'??????????????????',3,3),
 (1,'??????????????',15,2),
 (1,'10KG_????????',10,2);