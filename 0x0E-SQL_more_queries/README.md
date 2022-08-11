# 0x0E. SQL - More queries

## Description
This Directory covers
- How To Create a New User and Grant Permissions in MySQL
- How To Use MySQL GRANT Statement To Grant Privileges To a User
- MySQL constraints
- SQL technique: subqueries
- Basic query operation: the join
- SQL technique: multiple joins and the distinct keyword
- SQL technique: join types
- SQL technique: union and minus
- MySQL Cheat Sheet
- The Seven Types of SQL Joins
- MySQL Tutorial
- SQL Style Guide
- MySQL 8.0 SQL Statement Syntax


## Table of contents

Files | Description
----------- | -----------
[0-privileges.sql](./0-privileges.sql) | A script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
[1-create_user.sql](./1-create_user.sql) | A script that creates the MySQL server user user_0d_1
[2-create_read_user.sql](./2-create_read_user.sql) | A script that creates the database hbtn_0d_2 and the user user_0d_2.
[3-force_name.sql](./3-force_name.sql) | A script that creates the table force_name on your MySQL server.
[4-never_empty.sql](./4-never_empty.sql) | A script that creates the table id_not_null on your MySQL server
[5-unique_id.sql](./5-unique_id.sql) | A script that creates the table unique_id on your MySQL server.
[6-states.sql](./6-states.sql) | A script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
[7-cities.sql](./7-cities.sql) | A script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server
[8-cities_of_california_subquery.sql](./8-cities_of_california_subquery.sql) | A script that lists all the cities of California that can be found in the database hbtn_0d_usa
[9-cities_by_state_join.sql](./9-cities_by_state_join.sql) | A script that lists all cities contained in the database hbtn_0d_usa
[10-genre_id_by_show.sql](./10-genre_id_by_show.sql) | A script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked. Import the database dump from hbtn_0d_tvshows to your MySQL server: [hbtn_0d_tvshows.sql](./hbtn_0d_tvshows.sql) or [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)
[11-genre_id_all_shows.sql](./11-genre_id_all_shows.sql) | A script that lists all shows contained in the database hbtn_0d_tvshows. Import the database dump of hbtn_0d_tvshows to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as [10-genre_id_by_show.sql](./10-genre_id_by_show.sql))
[12-no_genre.sql](./12-no_genre.sql) | A script that lists all shows contained in hbtn_0d_tvshows without a genre linked. Import the database dump from hbtn_0d_tvshows to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as [11-genre_id_all_shows.sql](./10-genre_id_by_show.sql))
[13-count_shows_by_genre.sql](./13-count_shows_by_genre.sql) | A script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each. Import the database dump from hbtn_0d_tvshows to your MySQL server: [hbtn_0d_tvshows.sql](./hbtn_0d_tvshows.sql) or [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as [12-no_genre.sql](./12-no_genre.sql))
[14-my_genres.sql](./14-my_genres.sql) | A script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter. Import the database dump from hbtn_0d_tvshows to your MySQL server: [hbtn_0d_tvshows.sql](./hbtn_0d_tvshows.sql) or [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as [13-count_shows_by_genre.sql](./13-count_shows_by_genre.sql))
[15-comedy_only.sql](./15-comedy_only.sql) | A script that lists all Comedy shows in the database hbtn_0d_tvshows. Import the database dump from hbtn_0d_tvshows to your MySQL server: [hbtn_0d_tvshows.sql](./hbtn_0d_tvshows.sql) or [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as [14-my_genres.sql](./14-my_genres.sql))
[16-shows_by_genre.sql](./16-shows_by_genre.sql) | A script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows. Import the database dump from hbtn_0d_tvshows to your MySQL server: [hbtn_0d_tvshows.sql](./hbtn_0d_tvshows.sql) or [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as [15-comedy_only.sql](./15-comedy_only.sql))
[100-not_my_genres.sql](./100-not_my_genres.sql) | A script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter. Import the database dump from hbtn_0d_tvshows to your MySQL server: [hbtn_0d_tvshows.sql](./hbtn_0d_tvshows.sql) or [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as [16-shows_by_genre.sql](./16-shows_by_genre.sql))
[101-not_a_comedy.sql](./101-not_a_comedy.sql) | A script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows. Import the database dump from hbtn_0d_tvshows to your MySQL server: [hbtn_0d_tvshows.sql](./hbtn_0d_tvshows.sql) or [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as [100-not_my_genres.sql](./100-not_my_genres.sql))
[102-rating_shows.sql](./102-rating_shows.sql) | A script that lists all shows from hbtn_0d_tvshows_rate by their rating. Import the database hbtn_0d_tvshows_rate dump to your MySQL server: [hbtn_0d_tvshows_rate.sql](./hbtn_0d_tvshows_rate.sql) or [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/)
[103-rating_genres.sql](./103-rating_genres.sql) | A script that lists all genres in the database hbtn_0d_tvshows_rate by their rating. Import the database dump from hbtn_0d_tvshows_rate to your MySQL server: [hbtn_0d_tvshows_rate.sql](./hbtn_0d_tvshows_rate.sql) or [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/)
