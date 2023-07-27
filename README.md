# Results of using RISC-V CLINT `mtime` directly instead of `rdtime` in the seL4 kernel

## HiFive Unleashed - MCS kenrel

To reproduce with sel4bench:
```sh
../init-build.sh -DPLATFORM=hifive -DMCS=1
```

|IPC Benchmark|Direction|IPC length|In same VSpace|Mean (before patch)|Stddev (before patch)|Mean (after patch)|Stddev (after patch)|Change|
|-------------|---------|----------|--------------|-------------------|---------------------|-----------------|--------------------|------|
|seL4_Call|client->server|0|True|369.25|26.61|367.375|23.92|-0.51%|
|seL4_ReplyRecv|server->client|0|True|449.5|12.29|447.5625|9.14|-0.43%|
|seL4_Call|client->server|0|False|518.9375|9.35|518.75|8.17|-0.04%|
|seL4_ReplyRecv|server->client|0|False|752.1875|99.58|643.625|103.97|-16.87%|
|seL4_Send|client->server|0|False|3733.125|126.36|3211.1875|128.94|-16.25%|
|seL4_Call|client->server|10|False|4064.4375|133.91|3558.3125|132.92|-14.22%|
|seL4_ReplyRecv|server->client|10|False|4446.4375|99.65|3609.3125|115.91|-23.19%|


|Benchmark|Priority|Mean (before patch)|Stddev (before patch)|Mean (after patch)|Stddev (after patch)|Change|
|---------|--------|-------------------|---------------------|------------------|--------------------|------|
|Signal to thread of higher prio|1|4540.81|98.75|3237.36|124.67|-40.26%|
|Signal to thread of higher prio|65|4615.89|124.45|3221.21|114.02|-43.3%|
|Signal to thread of higher prio|129|4615.76|152.29|3235.5|132.46|-42.66%|
|Signal to thread of higher prio|193|4548.05|107.13|3217.17|104.37|-41.37%|


|Benchmark|Priority|Mean (before patch)|Stddev (before patch)|Mean (after patch)|Stddev (after patch)|Change|
|---------|--------|-------------------|---------------------|------------------|--------------------|------|
|Signal to process of higher prio|1|4594.51|139.36|3215.22|108.85|-42.9%|
|Signal to process of higher prio|65|4506.22|91.49|3214.37|131.18|-40.19%|
|Signal to process of higher prio|129|4528.6|114.34|3230.56|132.68|-40.18%|
|Signal to process of higher prio|193|4560.72|140.52|3177.89|90.1|-43.51%|


## HiFive Unleashed - non-MCS kenrel

To reproduce with sel4bench:
```sh
../init-build.sh -DPLATFORM=hifive
```

|IPC Benchmark|Direction|IPC length|In same VSpace|Mean (before patch)|Stddev (before patch)|Mean (after patch)|Stddev (after patch)|Change|
|-------------|---------|----------|--------------|-------------------|---------------------|-----------------|--------------------|------|
|seL4_Call|client->server|0|True|321.625|5.1|319.1875|2.86|-0.76%|
|seL4_ReplyRecv|server->client|0|True|367.625|1.63|366.875|2.07|-0.2%|
|seL4_Call|client->server|0|False|483.8125|35.31|489.1875|46.04|1.1%|
|seL4_ReplyRecv|server->client|0|False|556.3125|80.07|527.6875|12.74|-5.42%|
|seL4_Send|client->server|0|False|1325.3125|67.12|1290.875|10.79|-2.67%|
|seL4_Call|client->server|10|False|1410.875|74.69|1442.1875|86.73|2.17%|
|seL4_ReplyRecv|server->client|10|False|1358.0625|24.56|1370.625|61.34|0.92%|


|Benchmark|Priority|Mean (before patch)|Stddev (before patch)|Mean (after patch)|Stddev (after patch)|Change|
|---------|--------|-------------------|---------------------|------------------|--------------------|------|
|Signal to thread of higher prio|1|1269.8|9.45|1272.02|9.98|0.17%|
|Signal to thread of higher prio|65|1294.8|88.29|1279.05|87.68|-1.23%|
|Signal to thread of higher prio|129|1280.48|65.96|1267.34|65.72|-1.04%|
|Signal to thread of higher prio|193|1285.48|50.15|1279.6|40.71|-0.46%|


|Benchmark|Priority|Mean (before patch)|Stddev (before patch)|Mean (after patch)|Stddev (after patch)|Change|
|---------|--------|-------------------|---------------------|------------------|--------------------|------|
|Signal to process of higher prio|1|1132.5|43.9|1124.82|42.69|-0.68%|
|Signal to process of higher prio|65|1101.8|8.41|1111.99|3.09|0.92%|
|Signal to process of higher prio|129|1101.47|1.44|1102|0|0.05%|
|Signal to process of higher prio|193|1120.08|5.32|1105|0|-1.36%|
