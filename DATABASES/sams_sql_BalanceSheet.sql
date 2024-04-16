-- MySQL dump 10.13  Distrib 8.0.36, for macos14 (x86_64)
--
-- Host: 127.0.0.1    Database: sams_sql
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `BalanceSheet`
--

DROP TABLE IF EXISTS `BalanceSheet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BalanceSheet` (
  `show_id` varchar(500) DEFAULT NULL,
  `Date` varchar(500) DEFAULT NULL,
  `Amount` double DEFAULT NULL,
  `Type` varchar(50) DEFAULT NULL,
  `sales_id` int DEFAULT NULL,
  `txn_id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`txn_id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BalanceSheet`
--

LOCK TABLES `BalanceSheet` WRITE;
/*!40000 ALTER TABLE `BalanceSheet` DISABLE KEYS */;
INSERT INTO `BalanceSheet` VALUES ('12','2024-03-21',200,'Ticket Booking',134,26),('12','2024-03-21',-185,'Refund',134,27),('12','2024-03-21',200,'Ticket Booking',134,28),('12','2024-03-21',-185,'Refund',134,29),('12','2024-03-21',200,'Ticket Booking',134,30),('12','2024-03-21',-185,'Refund',134,31),('12','2024-03-21',200,'Ticket Booking',134,32),('12','2024-03-21',-185,'Refund',134,33),('12','2024-03-23',-100,'Copyright',NULL,34),('2345','2024-03-22',180,'Ticket Booking',134,36),('2345','2024-03-22',120,'Ticket Booking',134,37),('2345','2024-03-22',180,'Ticket Booking',134,38),('2345','2024-03-22',180,'Ticket Booking',134,39),('2345','2024-03-22',180,'Ticket Booking',134,40),('12','2024-03-25',200,'Ticket Booking',134,41),('2347','2024-03-26',180,'Ticket Booking',134,42),('12','2024-03-26',0,'Refund',134,43),('2345','2024-03-26',-165,'Refund',134,44),('12','2024-03-26',0,'Refund',134,45),('2347','2024-03-26',-165,'Refund',134,46),('2345','2024-03-26',-165,'Refund',134,47),('2345','2024-03-26',-165,'Refund',134,48),('2345','2024-03-26',-110,'Refund',134,49),('2347','2024-03-26',180,'Ticket Booking',134,50);
/*!40000 ALTER TABLE `BalanceSheet` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-26 17:51:41
