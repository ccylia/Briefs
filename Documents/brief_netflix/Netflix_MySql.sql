#lancer mysql
mysql -u root -p --local-infile=1

#creer la database
CREATE DATABASE netflix;

#creer les tables
CREATE TABLE netflix_titles( 
  show_id INT NOT NULL,
  type VARCHAR(10),
  title VARCHAR(110),
  director VARCHAR(210),
  cast VARCHAR(780),
  country VARCHAR(130),
  date_added VARCHAR(20),
  release_year INT NOT NULL,
  rating VARCHAR(10),
  duration VARCHAR(10),
  listed_in VARCHAR(80),
  description VARCHAR(280),
  PRIMARY KEY(show_id)
  );

  CREATE TABLE netflix_shows (
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(64),
    rating VARCHAR(9),
    ratingLevel VARCHAR(126),
    ratingDescription INT NOT NULL,
    release year INT NOT NULL,
    user rating score VARCHAR(4),
    user rating size INT NOT NULL,
    PRIMARY KEY(id)
);

#charger les fichiers csv pour remplir les tables
LOAD DATA LOCAL INFILE 'netflix_titles.csv'
INTO TABLE netflix_titles 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE 'Netflix\ Shows.csv' 
INTO TABLE netflix_shows
CHARACTER SET latin1
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r'
IGNORE 1 LINES(title, rating, ratingLevel, ratingDescription,release year, user rating score, user rating size);



#6- Afficher les titres de films de la table netflix_titles dont l’ID est inférieur strict à 80000000 
SELECT show_id FROM netflix_titles WHERE show_id<80000000;


#7-Afficher toutes les durée des TV Show (colonne duration)
SELECT duration FROM  netflix_titlesWHERE type ='TV Show' ;

#9-Afficher tous les noms de films communs aux 2 tables (netflix_titles et netflix_shows) 
SELECT * FROM netflix_titles INNER JOIN netflix_shows ON netflix_titles.title = netflix_shows.title 

#10

#11Compter le nombre de TV Shows de votre table ‘netflix_shows’ dont le ‘ratingLevel’ est renseigné. 
SELECT COUNT(ratingLevel) from netflix_shows WHERE ratingLevel >='$ratingLevel';

#12-Compter les films et TV Shows pour lesquels les noms (title) sont les mêmes sur les 2 tables et dont le ‘release year’ est supérieur à 2016. 
SELECT COUNT(netflix_titles.title) 
FROM netflix_titles INNER JOIN netflix_shows 
ON netflix_titles.title = netflix_shows.title 
WHERE netflix_titles.title = netflix_shows.title
AND netflix_shows.release_year>2016 AND netflix_titles.release_year >2016;

#13-Supprimer la colonne ‘rating’ de votre table ‘netflix_shows’ 
ALTER TABLE netflix_shows
DROP COLUMN 'rating';