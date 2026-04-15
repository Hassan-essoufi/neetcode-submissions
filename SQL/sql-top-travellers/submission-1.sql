-- Write your query below
select name, coalesce(sum(distance), 0) as travelled_distance from users left join rides on users.id = user_id group by users.id order by travelled_distance desc, name asc;