-- Ejemplo de creación de tabla, al final de twitter.sql
create table news (
	id int not null auto_increment primary key,
    title varchar(255) not null,
    body text not null,
    image_path varchar(255),
    author_id int not null,
    foreign key (author_id) references users(id)
);

select *
from tweets
where tweet like '%T%'
order by created_at desc
limit 5 offset 2;

-- CRUD
select * from news;

-- podemos insertar 1 registro
insert into news (title, body, author_id)
values ('Buenas Noticias', 'Baja el dolar. Pero durará poco', 1);

-- o varios registros a la vez
insert into news (title, body, image_path, author_id)
values ('Malas Noticias', 'Subió la bencina. A llenar el auto rápido', '/images/bencina.png', 1),
       ('Se cayó un joven en las Malvinas', 'Lo habrían pillado robando', null, 3);

update news
set title='Se cayó un joven en las Maldivas', author_id=4
where id=3;

delete
from news
where id=2;