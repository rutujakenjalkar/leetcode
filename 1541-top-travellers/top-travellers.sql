# Write your MySQL query statement below
with riders as(
select Rides.user_id, COALESCE(SUM(Rides.distance),0) as travelled_distance,name from Users left join Rides on Users.id=Rides.user_id group by Rides.user_id)
select name , travelled_distance from riders order by travelled_distance desc , name asc