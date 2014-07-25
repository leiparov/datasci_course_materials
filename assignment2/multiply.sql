select c.value from (select a.row_num, b.col_num, sum(a.value * b.value) as value 
from a join b on a.col_num = b.row_num group by a.row_num, b.col_num) c
where c.row_num = 2 and c.col_num = 3;

