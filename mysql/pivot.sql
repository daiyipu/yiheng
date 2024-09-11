drop table if exists dwt_fdds.tax_credit_grade_roll_rate_analysis_pivot;
create table if not exists dwt_fdds.tax_credit_grade_roll_rate_analysis_pivot as
select * from dwt fdds.tax credit grade roll rate analysis
pivot  -- 从一个列字段中拆出
(max(grade)for year in(2023,2022,2021,2020,2019,2018,2017,2016)
)
-- 通过窗口函数rank的使用，将某一个样本下多记录的情况，按照要求进行排序，从中可以挑选出我们需要的前几个记录。
select *, rank() over(partition by need_groupby_column_name order by need_orderby_column_name)
from table_name;
