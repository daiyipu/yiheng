drop table if exists dwt_fdds.tax_credit_grade_roll_rate_analysis_pivot;
create table if not exists dwt_fdds.tax_credit_grade_roll_rate_analysis_pivot as
select * from dwt fdds.tax credit grade roll rate analysis
pivot  -- 从一个列字段中拆出
(max(grade)for year in(2023,2022,2021,2020,2019,2018,2017,2016)
)