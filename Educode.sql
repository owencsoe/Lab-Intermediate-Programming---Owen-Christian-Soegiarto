-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Jun 24, 2024 at 12:37 PM
-- Server version: 5.7.39
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Educode`
--

-- --------------------------------------------------------

--
-- Table structure for table `Classes`
--

CREATE TABLE `Classes` (
  `ClassID` int(11) NOT NULL,
  `ClassType` varchar(100) DEFAULT NULL,
  `TutorsName` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Classes`
--

INSERT INTO `Classes` (`ClassID`, `ClassType`, `TutorsName`) VALUES
(1, 'Counseling', 'Alice Brown'),
(2, 'Live Classes', 'Bob Johnson'),
(3, 'Offline Classes', 'Charlie Wilson'),
(4, 'Private Classes', 'David Lee'),
(5, 'Private Classes', 'Eva Green');

-- --------------------------------------------------------

--
-- Table structure for table `Classes_Tutors`
--

CREATE TABLE `Classes_Tutors` (
  `ClassID` int(11) NOT NULL,
  `TutorID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Classes_Tutors`
--

INSERT INTO `Classes_Tutors` (`ClassID`, `TutorID`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

-- --------------------------------------------------------

--
-- Table structure for table `Courses`
--

CREATE TABLE `Courses` (
  `CourseID` int(11) NOT NULL,
  `CourseName` varchar(100) DEFAULT NULL,
  `CourseVideo` varchar(100) DEFAULT NULL,
  `CourseLesson` varchar(100) DEFAULT NULL,
  `MemberID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Courses`
--

INSERT INTO `Courses` (`CourseID`, `CourseName`, `CourseVideo`, `CourseLesson`, `MemberID`) VALUES
(1, 'Phyton', 'intro_to_phyton.mp4', 'Intro to Phyton', 1),
(2, 'C++', 'intro_to_c++.mp4', 'Intro to C++', 2),
(3, 'JavaScript', 'data_types.mp4', 'Data Types', 3),
(4, 'Phyton', 'variable_names.mp4', 'Variable Names', 4),
(5, 'C++', 'string_methods.mp4', 'String Methods', 5);

-- --------------------------------------------------------

--
-- Table structure for table `Member`
--

CREATE TABLE `Member` (
  `MemberID` int(11) NOT NULL,
  `Name` varchar(100) DEFAULT NULL,
  `MembershipDate` date DEFAULT NULL,
  `SubscriptionID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Member`
--

INSERT INTO `Member` (`MemberID`, `Name`, `MembershipDate`, `SubscriptionID`) VALUES
(1, 'Steven Valerian', '2024-06-22', 1),
(2, 'Allegra Wijaya', '2024-06-30', 2),
(3, 'Samuel L Jackson', '2024-09-15', 3),
(4, 'Lionel Messi', '2024-06-01', 4),
(5, 'Cristiano Ronaldo', '2024-06-20', 5);

-- --------------------------------------------------------

--
-- Table structure for table `Payment`
--

CREATE TABLE `Payment` (
  `PaymentID` int(11) NOT NULL,
  `PaymentMethod` varchar(50) DEFAULT NULL,
  `Amount` decimal(10,2) DEFAULT NULL,
  `Verification` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Payment`
--

INSERT INTO `Payment` (`PaymentID`, `PaymentMethod`, `Amount`, `Verification`) VALUES
(1, 'BCA', '9.99', 'Verified'),
(2, 'Visa', '29.99', 'Verified'),
(3, 'Gopay', '169.99', 'Pending'),
(4, 'OVO', '29.99', 'Verified'),
(5, 'BCA', '169.99', 'Verified');

-- --------------------------------------------------------

--
-- Table structure for table `Subscription`
--

CREATE TABLE `Subscription` (
  `SubscriptionID` int(11) NOT NULL,
  `Plans` varchar(100) DEFAULT NULL,
  `ExpiryDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Subscription`
--

INSERT INTO `Subscription` (`SubscriptionID`, `Plans`, `ExpiryDate`) VALUES
(1, 'Weekly', '2024-06-29'),
(2, 'Monthly', '2024-07-30'),
(3, 'Yearly', '2025-09-15'),
(4, 'Monthly', '2024-07-01'),
(5, 'Yearly', '2025-06-20');

-- --------------------------------------------------------

--
-- Table structure for table `Tutors`
--

CREATE TABLE `Tutors` (
  `TutorID` int(11) NOT NULL,
  `Name` varchar(100) DEFAULT NULL,
  `Occupation` varchar(100) DEFAULT NULL,
  `ClassType` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Tutors`
--

INSERT INTO `Tutors` (`TutorID`, `Name`, `Occupation`, `ClassType`) VALUES
(1, 'Alice Brown', 'Database Expert', 'Counseling'),
(2, 'Bob Johnson', 'Data Scientist', 'Live Classes'),
(3, 'Charlie Wilson', 'IT Operator', 'Offline Classes'),
(4, 'David Lee', 'Software Engineer', 'Private Classes'),
(5, 'Eva Green', 'Statistician', 'Private Classes');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Classes`
--
ALTER TABLE `Classes`
  ADD PRIMARY KEY (`ClassID`);

--
-- Indexes for table `Classes_Tutors`
--
ALTER TABLE `Classes_Tutors`
  ADD PRIMARY KEY (`ClassID`,`TutorID`),
  ADD KEY `TutorID` (`TutorID`);

--
-- Indexes for table `Courses`
--
ALTER TABLE `Courses`
  ADD PRIMARY KEY (`CourseID`),
  ADD KEY `MemberID` (`MemberID`);

--
-- Indexes for table `Member`
--
ALTER TABLE `Member`
  ADD PRIMARY KEY (`MemberID`),
  ADD KEY `SubscriptionID` (`SubscriptionID`);

--
-- Indexes for table `Payment`
--
ALTER TABLE `Payment`
  ADD PRIMARY KEY (`PaymentID`);

--
-- Indexes for table `Subscription`
--
ALTER TABLE `Subscription`
  ADD PRIMARY KEY (`SubscriptionID`);

--
-- Indexes for table `Tutors`
--
ALTER TABLE `Tutors`
  ADD PRIMARY KEY (`TutorID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Classes_Tutors`
--
ALTER TABLE `Classes_Tutors`
  ADD CONSTRAINT `classes_tutors_ibfk_1` FOREIGN KEY (`ClassID`) REFERENCES `Classes` (`ClassID`),
  ADD CONSTRAINT `classes_tutors_ibfk_2` FOREIGN KEY (`TutorID`) REFERENCES `Tutors` (`TutorID`);

--
-- Constraints for table `Courses`
--
ALTER TABLE `Courses`
  ADD CONSTRAINT `courses_ibfk_1` FOREIGN KEY (`MemberID`) REFERENCES `Member` (`MemberID`);

--
-- Constraints for table `Member`
--
ALTER TABLE `Member`
  ADD CONSTRAINT `member_ibfk_1` FOREIGN KEY (`SubscriptionID`) REFERENCES `Subscription` (`SubscriptionID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
