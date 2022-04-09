#create database
create database Exercise18;
#use database
use Exercise18;

#create table for users
CREATE TABLE USER_INFO(
ID INT AUTO_INCREMENT NOT NULL,
FIRSTNAME VARCHAR(50),
LASTNAME VARCHAR(50),
EMAIL VARCHAR(50),
ADDRESS VARCHAR(50),
POSTCODE VARCHAR (10),
PRIMARY KEY (ID)
);

CREATE TABLE BOOK_INFO(
BOOK_ID INT AUTO_INCREMENT NOT NULL,
TITLE VARCHAR (20),
AUTHOR VARCHAR (20),
GENRE VARCHAR(10),
PRIMARY KEY (BOOK_ID)
);

CREATE TABLE LOAN_LOG(
BOOK_ID INT,
CUST_ID INT, 
DUE_DATE VARCHAR(20),
RETURNED VARCHAR (3),
PRIMARY KEY (DUE_DATE),
FOREIGN KEY (BOOK_ID) REFERENCES BOOK_INFO(BOOK_ID),
FOREIGN KEY (CUST_ID) REFERENCES USER_INFO(ID)
);


INSERT INTO USER_INFO VALUES (1, "POTTER", "HARRY", "H.POTTER@HOGWARTS.COM", "4 PRIVET DRIVE", "HW98 7T");
INSERT INTO USER_INFO VALUES (2, "GRANGER", "HERMIONE", "H.GRANGER@HOGWARTS.COM", "6 ROSE CLOSE", "HW05 8H");
INSERT INTO USER_INFO VALUES (3, "WEASLEY",	"RON", "R.WEASLEY@HOGWARTS.COM", "15 GODRICKS HOLLOW","HW09 7H");
INSERT INTO USER_INFO VALUES (4,"MALFOY","DRACO","D.MALFOY@HOTMAIL.COM","19 DIAGON ALLEY","HW22 7H");
INSERT INTO BOOK_INFO VALUES (1, "FANTASTICAL BEASTS","S.JONES","FICTION");
INSERT INTO BOOK_INFO VALUES (2,"POTION MAKING","K.LEWIS","FICTION");
INSERT INTO BOOK_INFO VALUES (3,"THE DARK ARTS","G.LOCKHEART","FICTION");
INSERT INTO BOOK_INFO VALUES (4, "HERBOLOGY  101","P.SPROUT","FICTION");
INSERT INTO LOAN_LOG VALUES (4, 2, "2022-03-26", "no");
INSERT INTO LOAN_LOG VALUES (3, 1, "2022-03-29", "no");
USE LIBRARY;


#showing existing tables
show tables;

DROP database Exercise18;

SELECT * FROM Exercise18.BOOK_INFO;

SELECT * FROM Exercise18.BOOK_INFO where GENRE="FICTION";

SELECT * FROM Exercise18.LOAN_LOG WHERE DUE_DATE="2022-03-26";

SELECT CUST_ID, TITLE, DUE_DATE FROM BOOK_INFO, LOAN_LOG WHERE CUST_ID="2";


INSERT INTO BOOK_INFO(BOOK_ID, TITLE, AUTHOR, GENRE) VALUES (5,"MERPEOPLE: A COMPREHENSIVE GUIDE TO THEIR LANGUAGE AND CUSTOMS", "D.MARWOOD", "NON-FICTION")


        
        



        