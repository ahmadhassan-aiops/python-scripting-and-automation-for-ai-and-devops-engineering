create table my_df_data
(
file_id int NOT NULL AUTO_INCREMENT,
filesystem varchar(255),
size varchar(255),
used varchar(255),
avail varchar(255),
usage_with_per int,
mounted_on varchar(255),
datetime datetime,
ip_address varchar(255),
hostname varchar(255),
PRIMARY KEY (file_id)
);
