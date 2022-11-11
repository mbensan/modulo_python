select * from users
select * from books

insert into users values ()
delete from users where id=7

select * from faves

create table books (
	id int not null auto_increment primary key,
    title varchar(45) not null,
    num_pages int not null default 100,
    created_at datetime not null default now(),
    updated_at datetime not null default now()
)

create table favorites (
    created_at datetime not null default now(),
    updated_at datetime not null default now(),
    user_id int not null,
    book_id int not null,
    primary key (user_id, book_id),
    foreign key (user_id) references users(id),
    foreign key (book_id) references books(id)
)

insert into favorites (user_id, book_id)
values (8, 1), (9, 2), (9, 3)

insert into users (first_name, last_name) values
('Tomas', 'Heilenkotter'), ('Viviana', 'Figueroa');

insert into books (title) values ('Fareinheit 451'), ('La muerte tiene olor a pachulí'),
('El alquimista')

select first_name, last_name, books.title, num_pages
from users
join favorites on users.id = favorites.user_id
join books on favorites.book_id = books.id;


select tweets.id, tweet, concat(first_name, ' ', last_name) as 'Nombre Completo'
from tweets
join users on tweets.user_id = users.id