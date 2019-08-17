DROP TABLE nyc_jobs;

CREATE TABLE nyc_jobs (
	index INT PRIMARY KEY NOT NULL,
	jobID int,
	agency varchar(255) NOT NULL,
	businessTitle varchar (255) NOT NULL,
	numOfPositions int,
	jobCategory varchar (255) NOT NULL,
	salaryRangeFrom int,
	salaryRangeTo int,
	workLocation1 varchar (255)
	
);



