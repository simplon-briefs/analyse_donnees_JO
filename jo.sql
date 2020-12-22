-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8081
-- Generation Time: Dec 21, 2020 at 03:07 PM
-- Server version: 5.7.24
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jo`
--

-- --------------------------------------------------------

--
-- Table structure for table `athletes`
--

CREATE TABLE `athletes` (
  `id_athlete` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `sexe` char(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `athletes_epreuves`
--

CREATE TABLE `athletes_epreuves` (
  `id_athlete` int(11) NOT NULL,
  `id_epreuve` int(11) NOT NULL,
  `medaille` varchar(26) DEFAULT 'aucune',
  `age` int(11) NOT NULL,
  `poids` int(11) NOT NULL,
  `taille` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `athletes_sports`
--

CREATE TABLE `athletes_sports` (
  `id_athlete` int(11) NOT NULL,
  `id_sport` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `epreuves`
--

CREATE TABLE `epreuves` (
  `id_epreuve` int(11) NOT NULL,
  `id_sport` int(11) NOT NULL,
  `epreuve` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `epreuves_jeux`
--

CREATE TABLE `epreuves_jeux` (
  `id_epreuve` int(11) NOT NULL,
  `id_jeu` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `equipes`
--

CREATE TABLE `equipes` (
  `id_equipe` int(11) NOT NULL,
  `equipe` varchar(255) NOT NULL,
  `id_noc` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `equipes_athletes`
--

CREATE TABLE `equipes_athletes` (
  `id_equipe` int(11) DEFAULT NULL,
  `id_athlete` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `jeux`
--

CREATE TABLE `jeux` (
  `id_jeu` int(11) NOT NULL,
  `jeu` varchar(255) NOT NULL,
  `annee` smallint(6) NOT NULL,
  `saison` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `jeux_villes`
--

CREATE TABLE `jeux_villes` (
  `id_jeu` int(11) NOT NULL,
  `id_ville` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `nocs`
--

CREATE TABLE `nocs` (
  `id_noc` int(11) NOT NULL,
  `NOC` char(3) NOT NULL,
  `region` varchar(255) NOT NULL,
  `note` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `sports`
--

CREATE TABLE `sports` (
  `id_sport` int(11) NOT NULL,
  `sport` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `villes`
--

CREATE TABLE `villes` (
  `id_ville` int(11) NOT NULL,
  `ville` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `athletes`
--
ALTER TABLE `athletes`
  ADD PRIMARY KEY (`id_athlete`);

--
-- Indexes for table `athletes_epreuves`
--
ALTER TABLE `athletes_epreuves`
  ADD KEY `id_athlete` (`id_athlete`),
  ADD KEY `id_epreuve` (`id_epreuve`);

--
-- Indexes for table `athletes_sports`
--
ALTER TABLE `athletes_sports`
  ADD KEY `id_sport` (`id_sport`),
  ADD KEY `id_athlete` (`id_athlete`);

--
-- Indexes for table `epreuves`
--
ALTER TABLE `epreuves`
  ADD PRIMARY KEY (`id_epreuve`),
  ADD KEY `id_sport` (`id_sport`);

--
-- Indexes for table `epreuves_jeux`
--
ALTER TABLE `epreuves_jeux`
  ADD KEY `id_epreuve` (`id_epreuve`),
  ADD KEY `id_jeu` (`id_jeu`);

--
-- Indexes for table `equipes`
--
ALTER TABLE `equipes`
  ADD PRIMARY KEY (`id_equipe`),
  ADD KEY `id_noc` (`id_noc`);

--
-- Indexes for table `equipes_athletes`
--
ALTER TABLE `equipes_athletes`
  ADD KEY `id_equipe` (`id_equipe`),
  ADD KEY `id_athlete` (`id_athlete`);

--
-- Indexes for table `jeux`
--
ALTER TABLE `jeux`
  ADD PRIMARY KEY (`id_jeu`);

--
-- Indexes for table `jeux_villes`
--
ALTER TABLE `jeux_villes`
  ADD KEY `id_jeu` (`id_jeu`),
  ADD KEY `id_ville` (`id_ville`);

--
-- Indexes for table `nocs`
--
ALTER TABLE `nocs`
  ADD PRIMARY KEY (`id_noc`);

--
-- Indexes for table `sports`
--
ALTER TABLE `sports`
  ADD PRIMARY KEY (`id_sport`);

--
-- Indexes for table `villes`
--
ALTER TABLE `villes`
  ADD PRIMARY KEY (`id_ville`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `athletes`
--
ALTER TABLE `athletes`
  MODIFY `id_athlete` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `epreuves`
--
ALTER TABLE `epreuves`
  MODIFY `id_epreuve` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `equipes`
--
ALTER TABLE `equipes`
  MODIFY `id_equipe` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `jeux`
--
ALTER TABLE `jeux`
  MODIFY `id_jeu` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `nocs`
--
ALTER TABLE `nocs`
  MODIFY `id_noc` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sports`
--
ALTER TABLE `sports`
  MODIFY `id_sport` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `villes`
--
ALTER TABLE `villes`
  MODIFY `id_ville` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `athletes_epreuves`
--
ALTER TABLE `athletes_epreuves`
  ADD CONSTRAINT `athletes_epreuves_ibfk_1` FOREIGN KEY (`id_athlete`) REFERENCES `athletes` (`id_athlete`),
  ADD CONSTRAINT `athletes_epreuves_ibfk_2` FOREIGN KEY (`id_epreuve`) REFERENCES `epreuves` (`id_epreuve`);

--
-- Constraints for table `athletes_sports`
--
ALTER TABLE `athletes_sports`
  ADD CONSTRAINT `athletes_sports_ibfk_1` FOREIGN KEY (`id_sport`) REFERENCES `sports` (`id_sport`),
  ADD CONSTRAINT `athletes_sports_ibfk_2` FOREIGN KEY (`id_athlete`) REFERENCES `athletes` (`id_athlete`);

--
-- Constraints for table `epreuves`
--
ALTER TABLE `epreuves`
  ADD CONSTRAINT `epreuves_ibfk_2` FOREIGN KEY (`id_sport`) REFERENCES `sports` (`id_sport`);

--
-- Constraints for table `epreuves_jeux`
--
ALTER TABLE `epreuves_jeux`
  ADD CONSTRAINT `epreuves_jeux_ibfk_1` FOREIGN KEY (`id_epreuve`) REFERENCES `epreuves` (`id_epreuve`),
  ADD CONSTRAINT `epreuves_jeux_ibfk_2` FOREIGN KEY (`id_jeu`) REFERENCES `jeux` (`id_jeu`);

--
-- Constraints for table `equipes`
--
ALTER TABLE `equipes`
  ADD CONSTRAINT `equipes_ibfk_1` FOREIGN KEY (`id_noc`) REFERENCES `nocs` (`id_noc`);

--
-- Constraints for table `equipes_athletes`
--
ALTER TABLE `equipes_athletes`
  ADD CONSTRAINT `equipes_athletes_ibfk_1` FOREIGN KEY (`id_equipe`) REFERENCES `equipes` (`id_equipe`),
  ADD CONSTRAINT `equipes_athletes_ibfk_2` FOREIGN KEY (`id_athlete`) REFERENCES `athletes` (`id_athlete`);

--
-- Constraints for table `jeux_villes`
--
ALTER TABLE `jeux_villes`
  ADD CONSTRAINT `jeux_villes_ibfk_1` FOREIGN KEY (`id_jeu`) REFERENCES `jeux` (`id_jeu`),
  ADD CONSTRAINT `jeux_villes_ibfk_2` FOREIGN KEY (`id_ville`) REFERENCES `villes` (`id_ville`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
