-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 05, 2017 at 12:13 PM
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

CREATE TABLE `categories` (
  `numero` int(11) NOT NULL,
  `category` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `category_product`
--

CREATE TABLE `category_product` (
  `f_category` int(11) NOT NULL,
  `f_product` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `code` varchar(20) NOT NULL,
  `product_name` varchar(150) NOT NULL,
  `quantity` varchar(80) NOT NULL,
  `brands` varchar(80) NOT NULL,
  `stores` text NOT NULL,
  `specific_category` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `save_product`
--

CREATE TABLE `save_product` (
  `id` int(11) NOT NULL,
  `code_product` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`category`),
  ADD KEY `numero` (`numero`);

--
-- Indexes for table `category_product`
--
ALTER TABLE `category_product`
  ADD KEY `f_category` (`f_category`),
  ADD KEY `f_product` (`f_product`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD KEY `code` (`code`);

--
-- Indexes for table `save_product`
--
ALTER TABLE `save_product`
  ADD KEY `id` (`id`),
  ADD KEY `code_product` (`code_product`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `numero` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100;
--
-- AUTO_INCREMENT for table `save_product`
--
ALTER TABLE `save_product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
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
