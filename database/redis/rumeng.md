### redis-cli
```bash
C:\Users\ScCcWe>redis-cli
127.0.0.1:6379>
```

### exit
```bash
127.0.0.1:6379> exit
C:\Users\ScCcWe>
```

### set [key] [value]
```bash
127.0.0.1:6379> set id nihao
OK
127.0.0.1:6379> get id
"nihao"
```

### expire [key] [seconds]
给key设定一个寿命(seconds)（key原先的寿命是无限）
```shell
127.0.0.1:6379> set name beishang
OK
127.0.0.1:6379> get name
"beishang"
127.0.0.1:6379> expire name 10
(integer) 1
127.0.0.1:6379> get name
"beishang"
-- 等待10秒后输入 -- 
127.0.0.1:6379> get name
(nil)
```
### del [key]
删除key
```bash
127.0.0.1:6379> set num 1
OK
127.0.0.1:6379> get num
"1"
127.0.0.1:6379> del num
(integer) 1
127.0.0.1:6379> get num
(nil)
```
### keys * 
获取当前全部的keys
```bash
127.0.0.1:6379> keys *
1) "id"
127.0.0.1:6379> set name "beishang"
OK
127.0.0.1:6379> set num 1
OK
127.0.0.1:6379> keys *
1) "num"
2) "name"
3) "id"
```
### ttl [key]
查询key的剩余寿命
```bash
127.0.0.1:6379> set name "mingtianshi520"
OK
127.0.0.1:6379> get name
"mingtianshi520"
127.0.0.1:6379> expire name 10
(integer) 1
-- 等待5秒后的结果 --
127.0.0.1:6379> ttl name
(integer) 5
-- 又等待7秒后的结果 --
127.0.0.1:6379> ttl name
(integer) -2
127.0.0.1:6379> get name
(nil)
```
### persist [key]
将key的寿命延长至无限
```bash
127.0.0.1:6379> set beauty zhang
OK
127.0.0.1:6379> get beauty
"zhang"
127.0.0.1:6379> ttl beauty
(integer) -1
127.0.0.1:6379> expire beauty 20
(integer) 1
127.0.0.1:6379> ttl beauty
(integer) 15
127.0.0.1:6379> persist beauty
(integer) 1
127.0.0.1:6379> ttl beauty
(integer) -1
```
### select [index]
选择一个redis库（redis默认使用第一个库，也就是index：0）
```bash
127.0.0.1:6379> select 1
OK
127.0.0.1:6379[1]> keys *
(empty list or set)
127.0.0.1:6379[1]> select 0
OK
127.0.0.1:6379> keys *
1) "beauty"
2) "num"
3) "id"
```
