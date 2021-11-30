# Результаты тестирования Apache Benchmark

## Запрос https://localhost:443/api/v1/Products/ без балансировки
```
dr_starland@user76887:~$ ab -c 10 -n 5000 https://localhost:443/api/v1/Products/
This is ApacheBench, Version 2.3 <$Revision: 1843412 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 500 requests
Completed 1000 requests
Completed 1500 requests
Completed 2000 requests
Completed 2500 requests
Completed 3000 requests
Completed 3500 requests
Completed 4000 requests
Completed 4500 requests
Completed 5000 requests
Finished 5000 requests


Server Software:        artshop
Server Hostname:        localhost
Server Port:            443
SSL/TLS Protocol:       TLSv1.2,ECDHE-RSA-AES256-GCM-SHA384,2048,256
Server Temp Key:        X25519 253 bits
TLS Server Name:        localhost

Document Path:          /api/v1/Products/
Document Length:        82 bytes

Concurrency Level:      10
Time taken for tests:   10.140 seconds
Complete requests:      5000
Failed requests:        0
Non-2xx responses:      5000
Total transferred:      2075000 bytes
HTML transferred:       410000 bytes
Requests per second:    493.10 [#/sec] (mean)
Time per request:       20.280 [ms] (mean)
Time per request:       2.028 [ms] (mean, across all concurrent requests)
Transfer rate:          199.84 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        1    2   0.3      2       6
Processing:     3   13  15.7     11     329
Waiting:        2   13  15.7     11     329
Total:          4   15  15.7     13     331

Percentage of the requests served within a certain time (ms)
  50%     13
  66%     15
  75%     16
  80%     17
  90%     19
  95%     21
  98%     24
  99%     78
 100%    331 (longest request)
 ```
 ## Запрос https://localhost:443/api/v1/Products/ с балансировкой
 ```
dr_starland@user76887:~$ ab -c 10 -n 5000 https://localhost:443/api/v1/Products/
This is ApacheBench, Version 2.3 <$Revision: 1843412 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 500 requests
Completed 1000 requests
Completed 1500 requests
Completed 2000 requests
Completed 2500 requests
Completed 3000 requests
Completed 3500 requests
Completed 4000 requests
Completed 4500 requests
Completed 5000 requests
Finished 5000 requests


Server Software:        artshop
Server Hostname:        localhost
Server Port:            443
SSL/TLS Protocol:       TLSv1.2,ECDHE-RSA-AES256-GCM-SHA384,2048,256
Server Temp Key:        X25519 253 bits
TLS Server Name:        localhost

Document Path:          /api/v1/Products/
Document Length:        82 bytes

Concurrency Level:      10
Time taken for tests:   6.653 seconds
Complete requests:      5000
Failed requests:        0
Non-2xx responses:      5000
Total transferred:      2075000 bytes
HTML transferred:       410000 bytes
Requests per second:    751.57 [#/sec] (mean)
Time per request:       13.305 [ms] (mean)
Time per request:       1.331 [ms] (mean, across all concurrent requests)
Transfer rate:          304.59 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        1    2   0.6      2       8
Processing:     2    8  14.8      6     326
Waiting:        2    7  14.8      5     326
Total:          3   10  14.8      8     328

Percentage of the requests served within a certain time (ms)
  50%      8
  66%     10
  75%     11
  80%     12
  90%     14
  95%     17
  98%     20
  99%     21
 100%    328 (longest request)
 ```
 ## Запрос https://localhost:443/api/v1/Products/1/ без балансировки
 ```
dr_starland@user76887:~$ ab -c 10 -n 5000 https://localhost:443/api/v1/Products/1/
This is ApacheBench, Version 2.3 <$Revision: 1843412 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 500 requests
Completed 1000 requests
Completed 1500 requests
Completed 2000 requests
Completed 2500 requests
Completed 3000 requests
Completed 3500 requests
Completed 4000 requests
Completed 4500 requests
Completed 5000 requests
Finished 5000 requests


Server Software:        artshop
Server Hostname:        localhost
Server Port:            443
SSL/TLS Protocol:       TLSv1.2,ECDHE-RSA-AES256-GCM-SHA384,2048,256
Server Temp Key:        X25519 253 bits
TLS Server Name:        localhost

Document Path:          /api/v1/Products/1/
Document Length:        82 bytes

Concurrency Level:      10
Time taken for tests:   10.608 seconds
Complete requests:      5000
Failed requests:        0
Non-2xx responses:      5000
Total transferred:      2145000 bytes
HTML transferred:       410000 bytes
Requests per second:    471.34 [#/sec] (mean)
Time per request:       21.216 [ms] (mean)
Time per request:       2.122 [ms] (mean, across all concurrent requests)
Transfer rate:          197.47 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        1    2   0.8      2      25
Processing:     2   13  19.3     10     325
Waiting:        2   13  19.3     10     324
Total:          4   14  19.4     11     327

Percentage of the requests served within a certain time (ms)
  50%     11
  66%     14
  75%     16
  80%     17
  90%     20
  95%     22
  98%     25
  99%     94
 100%    327 (longest request)
 ```

 
## Запрос https://localhost:443/api/v1/Products/1/ с балансировкой
 ```
dr_starland@user76887:~$ ab -c 10 -n 5000 https://localhost:443/api/v1/Products/1/
This is ApacheBench, Version 2.3 <$Revision: 1843412 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 500 requests
Completed 1000 requests
Completed 1500 requests
Completed 2000 requests
Completed 2500 requests
Completed 3000 requests
Completed 3500 requests
Completed 4000 requests
Completed 4500 requests
Completed 5000 requests
Finished 5000 requests


Server Software:        artshop
Server Hostname:        localhost
Server Port:            443
SSL/TLS Protocol:       TLSv1.2,ECDHE-RSA-AES256-GCM-SHA384,2048,256
Server Temp Key:        X25519 253 bits
TLS Server Name:        localhost

Document Path:          /api/v1/Products/1/
Document Length:        82 bytes

Concurrency Level:      10
Time taken for tests:   6.680 seconds
Complete requests:      5000
Failed requests:        0
Non-2xx responses:      5000
Total transferred:      2145000 bytes
HTML transferred:       410000 bytes
Requests per second:    748.51 [#/sec] (mean)
Time per request:       13.360 [ms] (mean)
Time per request:       1.336 [ms] (mean, across all concurrent requests)
Transfer rate:          313.58 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        1    2   1.0      2      18
Processing:     2   10  12.5      7     321
Waiting:        2    9  12.5      7     320
Total:          3   12  12.6     10     323

Percentage of the requests served within a certain time (ms)
  50%     10
  66%     14
  75%     16
  80%     17
  90%     19
  95%     21
  98%     24
  99%     28
 100%    323 (longest request)
 ```