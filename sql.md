
# SQL Snippets


## Count number of NULL values in each column in SQL

```
DECLARE @t nvarchar(max)
SET @t = N'SELECT '

SELECT @t = @t + 'sum(case when ' + c.name + ' is null then 1 else 0 end) "Null Values for ' + c.name + '",
                sum(case when ' + c.name + ' is null then 0 else 1 end) "Non-Null Values for ' + c.name + '",'
FROM sys.columns c 
WHERE c.object_id = object_id('my_table');

SET @t = SUBSTRING(@t, 1, LEN(@t) - 1) + ' FROM my_table;'

EXEC sp_executesql @t
```

[Source](https://stackoverflow.com/questions/24411159/count-number-of-null-values-in-each-column-in-sql)



