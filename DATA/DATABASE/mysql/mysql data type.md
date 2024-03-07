---
file-created: 2023 11 21
last-modified: 2023 11 29
---

整数类型：包括 TINYINT、SMALLINT、MEDIUMINT、INT、BIGINT 五种类型。
TINYINT：占用 1 个字节，取值范围为 -128 到 127。
SMALLINT：占用 2 个字节，取值范围为 -32768 到 32767。
MEDIUMINT：占用 3 个字节，取值范围为 -8388608 到 8388607。
INT：占用 4 个字节，取值范围为 -2147483648 到 2147483647。
BIGINT：占用 8 个字节，取值范围为 -9223372036854775808 到 9223372036854775807。
浮点数类型：包括 FLOAT、DOUBLE 和 DECIMAL 三种类型。
FLOAT：占用 4 个字节，精度为 7 位小数。
DOUBLE：占用 8 个字节，精度为 15 位小数。
DECIMAL：精度可由用户指定，范围为 1 到 65 位小数。
字符串类型

CHAR：固定长度字符串，占用固定的存储空间。
CHAR(n)：表示字符串长度为 n 个字符。
VARCHAR：可变长度字符串，占用实际字符数的存储空间。
VARCHAR(n)：表示字符串长度最大为 n 个字符。
BINARY：固定长度二进制字符串，与 CHAR 类似。
VARBINARY：可变长度二进制字符串，与 VARCHAR 类似。
BLOB：大字符串，用于存储大量的数据。
TINYBLOB：占用 255 个字节。
BLOB：占用 65535 个字节。
MEDIUMBLOB：占用 16777215 个字节。
LONGBLOB：占用 4294967295 个字节。
TEXT：大字符串，与 BLOB 类似。
TINYTEXT：占用 255 个字节。
TEXT：占用 65535 个字节。
MEDIUMTEXT：占用 16777215 个字节。
LONGTEXT：占用 4294967295 个字节。
日期和时间类型

YEAR：存储年份，占用 1 个字节。
DATE：存储日期，占用 3 个字节。
TIME：存储时间，占用 3 个字节。
DATETIME：存储日期和时间，占用 8 个字节。
TIMESTAMP：存储日期和时间，占用 4 个字节。