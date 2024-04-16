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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add shows',7,'add_shows'),(26,'Can change shows',7,'change_shows'),(27,'Can delete shows',7,'delete_shows'),(28,'Can view shows',7,'view_shows'),(29,'Can add spectators',8,'add_spectators'),(30,'Can change spectators',8,'change_spectators'),(31,'Can delete spectators',8,'delete_spectators'),(32,'Can view spectators',8,'view_spectators'),(33,'Can add sales person',9,'add_salesperson'),(34,'Can change sales person',9,'change_salesperson'),(35,'Can delete sales person',9,'delete_salesperson'),(36,'Can view sales person',9,'view_salesperson'),(37,'Can add manager',10,'add_manager'),(38,'Can change manager',10,'change_manager'),(39,'Can delete manager',10,'delete_manager'),(40,'Can view manager',10,'view_manager'),(41,'Can add sales person',11,'add_salesperson'),(42,'Can change sales person',11,'change_salesperson'),(43,'Can delete sales person',11,'delete_salesperson'),(44,'Can view sales person',11,'view_salesperson'),(45,'Can add account clerk',12,'add_accountclerk'),(46,'Can change account clerk',12,'change_accountclerk'),(47,'Can delete account clerk',12,'delete_accountclerk'),(48,'Can view account clerk',12,'view_accountclerk'),(49,'Can add spectators',13,'add_spectators'),(50,'Can change spectators',13,'change_spectators'),(51,'Can delete spectators',13,'delete_spectators'),(52,'Can view spectators',13,'view_spectators'),(53,'Can add user',14,'add_customuser'),(54,'Can change user',14,'change_customuser'),(55,'Can delete user',14,'delete_customuser'),(56,'Can view user',14,'view_customuser'),(57,'Can add user',15,'add_users'),(58,'Can change user',15,'change_users'),(59,'Can delete user',15,'delete_users'),(60,'Can view user',15,'view_users'),(61,'Can add seats',16,'add_seats'),(62,'Can change seats',16,'change_seats'),(63,'Can delete seats',16,'delete_seats'),(64,'Can view seats',16,'view_seats'),(65,'Can add tickets_ info',17,'add_tickets_info'),(66,'Can change tickets_ info',17,'change_tickets_info'),(67,'Can delete tickets_ info',17,'delete_tickets_info'),(68,'Can view tickets_ info',17,'view_tickets_info');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
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
