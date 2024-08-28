> DATE_FORMAT
1. SELECT DATE_FORMAT('2022-08-15', '%Y-%m') from  your_table;--取年月日数据为年月
2. SELECT DATE_FORMAT('2022-08-15', '%Y-%m-%d') from  your_table;--取年月日数据为年月日

>months_between 
1. 求间隔月份数
```
SELECT  months_between(end_date,start_date) AS months_diff  
FROM your_table;

SELECT  
  (YEAR(end_date) - YEAR(start_date)) * 12 + (MONTH(end_date) - MONTH(start_date)) AS months_diff  
FROM  
  your_table;
  ```