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
-- Table structure for table `Shows`
--

DROP TABLE IF EXISTS `Shows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Shows` (
  `show_id` int NOT NULL AUTO_INCREMENT,
  `show_name` varchar(20) DEFAULT NULL,
  `date` varchar(10) DEFAULT NULL,
  `timing` time DEFAULT NULL,
  `no_of_balcony_seats` int DEFAULT '70',
  `no_of_ordinary_seats` int DEFAULT '190',
  `balcony_rate` int DEFAULT '180',
  `ordinary_rate` int DEFAULT '120',
  `end_time` time DEFAULT '00:00:00',
  PRIMARY KEY (`show_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2349 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Shows`
--

LOCK TABLES `Shows` WRITE;
/*!40000 ALTER TABLE `Shows` DISABLE KEYS */;
INSERT INTO `Shows` VALUES (12,'Dune','2024-03-23','21:34:00',10,20,200,100,'00:00:00'),(2345,'Panda','2024-03-28','17:35:00',30,50,180,120,'00:00:00'),(2347,'Music Day','2024-03-28','09:00:00',3,4,180,120,'10:00:00'),(2348,'Music Day','2024-03-28','15:00:00',3,4,180,120,'16:00:00');
/*!40000 ALTER TABLE `Shows` ENABLE KEYS */;
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
