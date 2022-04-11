create table Movie(MovieId int, Title varchar(20), Duration datetime, Language varchar(20), ReleaseDate datetime, City varchar(20), Genre varchar(20), PRIMARY KEY (MovieId));
create table City(CityId int, Name varchar(20), PRIMARY KEY (CityId));
create table Cinema(CinemaId int, Name varchar(20), TotalCinemaHalls int,CityId int, PRIMARY KEY(CinemaId), FOREIGN KEY (CityId) REFERENCES City(CityId));
create table CinemaHall(CinemaHallId int, Name varchar(20), TotalSeats int,CinemaId int, PRIMARY KEY (CinemaHallId), FOREIGN KEY (CinemaId) REFERENCES Cinema(CinemaId));
create table Shows(ShowId int, Date datetime, StartTime time, Endtime time,CinemaHallId int,MovieId int,  PRIMARY KEY (ShowId), FOREIGN KEY(MovieId) REFERENCES Movie(MovieId), FOREIGN KEY(CinemaHallId) REFERENCES CinemaHall(CinemaHallId));
create table CinemaSeat(CinemaSeatId int, SeatNumber int, type enum('Regular', 'Balcony'), CinemaHallId int, PRIMARY KEY (CinemaSeatId), FOREIGN KEY (CinemaHallId) REFERENCES CinemaHall(CinemaHallId));
create table User(UserId int, Name varchar(64), Password varchar(20), Email varchar(64), Phone varchar(16), PRIMARY KEY (UserId));
create table Booking(BookingId int, NumberOfSeats int, Timestamp datetime, Status enum('Booked','Reserved'),UserId int, ShowId int, PRIMARY KEY (BookingId), FOREIGN KEY (UserId) REFERENCES User(UserId), FOREIGN KEY (ShowId) REFERENCES Shows(ShowId))

