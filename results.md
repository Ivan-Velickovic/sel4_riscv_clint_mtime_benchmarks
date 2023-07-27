|IPC Benchmark|Direction|IPC length|In same VSpace|Mean (before patch)|Stddev (before patch)|Mean(after patch)|Stddev (after patch)|Change|
|-------------|---------|----------|--------------|-------------------|---------------------|-----------------|--------------------|------|
|seL4_Call|client->server|0|True|371.4375|40.980483159670044|363.5625|26.861372513952695|-2.17%|
|seL4_ReplyRecv|server->client|0|True|446.4375|9.476286192385707|447.375|10.40512694140089|0.21%|
|seL4_Call|client->server|0|False|537.125|75.50187635637496|520.0625|9.132360045464699|-3.28%|
|seL4_ReplyRecv|server->client|0|False|758.4375|97.56399609145443|615.75|13.759844960366863|-23.17%|
|seL4_Send|client->server|0|False|3738.5|146.30105946301276|3164.625|111.66019881766287|-18.13%|
|seL4_Call|client->server|10|False|3997.0|87.69720634090918|3551.4375|148.66091169728062|-12.55%|
|seL4_ReplyRecv|server->client|10|False|4439.3125|115.65264084029094|3578.5|42.82522621072771|-24.06%|


|Benchmark|Priority|Mean (before patch)|Mean (after patch)|Change|
|---------|----|-----------------|----------------|------|
|Signal to thread of higher prio|1|4567.5|3233.2|-41.27%|
|Signal to thread of higher prio|65|4591.19|3233.68|-41.98%|
|Signal to thread of higher prio|129|4617.99|3232.89|-42.84%|
|Signal to thread of higher prio|193|4583.91|3220.58|-42.33%|


|Benchmark|Priority|Mean (before patch)|Mean (after patch)|Change|
|---------|----|-----------------|----------------|------|
|Signal to process of higher prio|1|4540.47|3208.24|-41.53%|
|Signal to process of higher prio|65|4526.32|3213.99|-40.83%|
|Signal to process of higher prio|129|4531.29|3232.0|-40.2%|
|Signal to process of higher prio|193|4590.72|3217.36|-42.69%|


