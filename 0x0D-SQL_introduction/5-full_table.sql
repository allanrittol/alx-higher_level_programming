-- A script that prints the fulldescripiton of the first_table
SELECT COLUMN_NAME, DATA_TYPE,
IS_NULLABLE, COLUMN_DEFAULT
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'first_table';
