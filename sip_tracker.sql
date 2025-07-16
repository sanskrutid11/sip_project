-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 09, 2025 at 07:05 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sip_tracker`
--

-- --------------------------------------------------------

--
-- Table structure for table `investments`
--

CREATE TABLE `investments` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `mutual_fund_id` int(11) DEFAULT NULL,
  `investment_amount` float DEFAULT NULL,
  `start_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `investments`
--

INSERT INTO `investments` (`id`, `user_id`, `mutual_fund_id`, `investment_amount`, `start_date`) VALUES
(1, 1, 1, 500, '2024-12-12'),
(2, 1, 1, 5000, '2025-12-12'),
(3, 1, 1, 5000, '2025-12-12'),
(4, 1, 1, 500, '2024-12-12');

-- --------------------------------------------------------

--
-- Table structure for table `mutual_funds`
--

CREATE TABLE `mutual_funds` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `risk` varchar(50) NOT NULL,
  `expected_return` varchar(50) NOT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mutual_funds`
--

INSERT INTO `mutual_funds` (`id`, `name`, `price`, `risk`, `expected_return`, `description`) VALUES
(1, 'Equity Growth Fund', 200.00, 'Moderate', '12%', 'This fund focuses on high-growth companies with stable potential.'),
(2, 'ABC Balanced Fund', 150.00, 'Low', '8%', 'A balanced fund for moderate risk and steady returns.'),
(3, 'DEF Equity Fund', 300.00, 'High', '15%', 'An equity-focused fund targeting aggressive growth.'),
(4, 'PQR Debt Fund', 120.00, 'Low', '7%', 'A debt fund that invests in fixed-income securities for low risk.'),
(5, 'LMN Midcap Fund', 250.00, 'Moderate', '13%', 'A fund investing in midcap companies for steady growth.'),
(6, 'UVW Smallcap Fund', 350.00, 'High', '18%', 'A small-cap fund focused on high-growth potential companies.'),
(7, 'JKL Index Fund', 180.00, 'Low', '10%', 'An index fund tracking market indices for passive investment.'),
(8, 'MNO Hybrid Fund', 160.00, 'Moderate', '11%', 'A hybrid fund combining equity and debt for balanced returns.'),
(9, 'STU Dividend Fund', 220.00, 'Moderate', '9%', 'This fund aims to provide regular dividends and stable returns.'),
(10, 'EFG ESG Fund', 280.00, 'Moderate', '12%', 'An ESG fund focusing on companies with strong environmental practices.'),
(11, 'HIJ Infrastructure Fund', 310.00, 'High', '14%', 'Invests in infrastructure projects and companies for high returns.'),
(12, 'VWX Global Fund', 400.00, 'High', '20%', 'A global fund investing in international markets for diversified growth.'),
(13, 'RST Technology Fund', 330.00, 'High', '16%', 'Invests in technology companies for high growth potential.'),
(14, 'NOP Healthcare Fund', 270.00, 'Moderate', '13%', 'A healthcare sector fund focusing on medical and biotech companies.'),
(15, 'QRS Bluechip Fund', 190.00, 'Low', '9%', 'Invests in large-cap blue-chip companies for steady growth.');

-- --------------------------------------------------------

--
-- Table structure for table `registrations`
--

CREATE TABLE `registrations` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `pan_card` varchar(255) DEFAULT NULL,
  `address_proof` varchar(255) DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `investment_amount` decimal(10,2) DEFAULT NULL,
  `frequency` varchar(50) DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `bank_account` varchar(50) DEFAULT NULL,
  `bank_ifsc` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `registrations`
--

INSERT INTO `registrations` (`id`, `user_id`, `pan_card`, `address_proof`, `photo`, `investment_amount`, `frequency`, `duration`, `start_date`, `bank_account`, `bank_ifsc`) VALUES
(1, 1, 'sec4.pdf', 'sec4.pdf', 'sec4.pdf', -5.00, 'Monthly', 2, '2024-12-12', '9787897', '97878'),
(2, 1, 'sec4.pdf', 'sec6.pdf', 'sec6.pdf', 5000.00, 'Monthly', 3, '2025-12-12', '9798787686', '987878767'),
(3, 1, 'sec5.pdf', 'sec3.pdf', 'second.pdf', 5000.00, 'Monthly', 5, '2025-12-12', '787888', '897877987'),
(4, 1, 'second.pdf', 'second.pdf', 'second.pdf', 500.00, 'Monthly', 3, '2024-12-12', '97767666666', '866666');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(20) NOT NULL,
  `pan_number` text NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `pan_number`, `password`) VALUES
(1, '1234', ''),
(2, '1234', ''),
(10, '1234', ''),
(11, '1234', ''),
(12, '1234', ''),
(13, '1234', ''),
(14, '88788877878887', ''),
(15, '12345678', ''),
(16, '9876', '$2b$12$wl2o/R72wpYf9.BDtRnlp.ryMFE7j/droUwjjfE95w5EqNuQ6Nyi2'),
(17, '123456', '$2b$12$esDjiaZYadjEEjf7krYVtuVjERj9fgwKygWaF7rzSp6gRkz9OQ6Pi'),
(18, '112334', '$2b$12$3Bi.Q0CmH0zCoHoZ.c1rd.gf8xPRrUBynJV7rUMM7Mb4UgJGCcztG'),
(19, '1234', '$2b$12$ug6qZUJiRdZfbVeqNeRAVOcg0.HebJ9FFktxMiIuxRnLB/R.mCMvS'),
(20, '1234', '$2b$12$VGyVVjszUnYQfZ61cRIuiu084eBklwwZlmdtFYBeXq9H3s13Mib3m');

-- --------------------------------------------------------

--
-- Table structure for table `withdrawals`
--

CREATE TABLE `withdrawals` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `mutual_fund_id` int(11) DEFAULT NULL,
  `withdrawal_amount` float DEFAULT NULL,
  `withdrawal_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `withdrawals`
--

INSERT INTO `withdrawals` (`id`, `user_id`, `mutual_fund_id`, `withdrawal_amount`, `withdrawal_date`) VALUES
(1, 1, 1, 5, '2025-01-06 13:41:21'),
(2, 1, 1, 500, '2025-01-06 13:41:57');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `investments`
--
ALTER TABLE `investments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `mutual_fund_id` (`mutual_fund_id`);

--
-- Indexes for table `mutual_funds`
--
ALTER TABLE `mutual_funds`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `registrations`
--
ALTER TABLE `registrations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `withdrawals`
--
ALTER TABLE `withdrawals`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `mutual_fund_id` (`mutual_fund_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `investments`
--
ALTER TABLE `investments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `mutual_funds`
--
ALTER TABLE `mutual_funds`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `registrations`
--
ALTER TABLE `registrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `withdrawals`
--
ALTER TABLE `withdrawals`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `investments`
--
ALTER TABLE `investments`
  ADD CONSTRAINT `investments_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `investments_ibfk_2` FOREIGN KEY (`mutual_fund_id`) REFERENCES `mutual_funds` (`id`);

--
-- Constraints for table `registrations`
--
ALTER TABLE `registrations`
  ADD CONSTRAINT `registrations_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `withdrawals`
--
ALTER TABLE `withdrawals`
  ADD CONSTRAINT `withdrawals_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `withdrawals_ibfk_2` FOREIGN KEY (`mutual_fund_id`) REFERENCES `mutual_funds` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
