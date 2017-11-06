-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 06, 2017 at 09:03 PM
-- Server version: 10.1.26-MariaDB-0+deb9u1
-- PHP Version: 7.0.19-1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `oui`
--
CREATE DATABASE IF NOT EXISTS `oui` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `oui`;

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE IF NOT EXISTS `categories` (
  `numero` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(80) NOT NULL,
  PRIMARY KEY (`category`),
  KEY `numero` (`numero`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `category_product`
--

CREATE TABLE IF NOT EXISTS `category_product` (
  `f_category` int(11) NOT NULL,
  `f_product` varchar(50) NOT NULL,
  KEY `f_category` (`f_category`),
  KEY `f_product` (`f_product`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE IF NOT EXISTS `products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(20) NOT NULL,
  `product_name` varchar(150) NOT NULL,
  `quantity` varchar(80) NOT NULL,
  `brands` varchar(80) NOT NULL,
  `stores` text NOT NULL,
  `specific_category` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `save_product`
--

CREATE TABLE IF NOT EXISTS `save_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code_product` varchar(20) NOT NULL,
  KEY `id` (`id`),
  KEY `code_product` (`code_product`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `category_product`
--
ALTER TABLE `category_product`
  ADD CONSTRAINT `category_product_ibfk_1` FOREIGN KEY (`f_category`) REFERENCES `categories` (`numero`),
  ADD CONSTRAINT `category_product_ibfk_2` FOREIGN KEY (`f_product`) REFERENCES `products` (`code`);

--
-- Constraints for table `save_product`
--
ALTER TABLE `save_product`
  ADD CONSTRAINT `save_product_ibfk_1` FOREIGN KEY (`code_product`) REFERENCES `products` (`code`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
