drop table if exists entries;
create tavle entries (
	id integer primary key autoincrement,
	title text not null,
	text text not null
);