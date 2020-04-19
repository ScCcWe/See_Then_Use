- 安装
```bash
$ pip install tqdm
``` 
- 入门例
```python
from tqdm import tqdm
import time

for i in tqdm(["a", "b", "c", "d"]):
    time.sleep(0.5)
    pass
```  
延伸：这里的`["a", "b", "c", "d"]`可以代表四个任务，每个任务的功能是`time.sleep(0.5)`。

- 实际使用使用  
    你可以把它加在你的脚本中，以此来监控，完成情况。例子如下：
    
    假如说现在有1000个任务：task_list = [1, 2, ..., 1001], 代码如下：
```python
from tqdm import tqdm

for i in tqdm(task_list):
    ...
```
