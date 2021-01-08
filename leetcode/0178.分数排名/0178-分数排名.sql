# Write your MySQL query statement below
select Score ,
(select count(distinct Score) from Scores  where Score>=a.Score) as `Rank`
from Scores a
order by Score 
desc