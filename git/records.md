## git 命令记录

### git init
```shell
$ git init
```

### git config
```shell
$ git config user.name                              # 查看当前用户名
$ git config user.email                             # 查看当前用户邮箱
$ git config --global user.name "ScCcWe"            # 设置当前用户名
$ git config --global user.email "xxxxxxxx@xx.com"  # 设置当前邮箱
```

### git commit（提交备注）
```bash
$ git commit -m "最新一次提交的备注"
```

### git status（状态）
```shell
$ git status
```

### git log（日志）
```shell
$ git log
$ git log --pretty=oneline
```

### git remote（链接仓库）
```shell
$ git remote add origin https://github.com/ScCcWe/ajiansc_flask_w
eb.git
```

### git add
```bash
$ git add .  # 用这个即可
$ git add -u
$ git add -A
```

### git branch
```bash
$ git branch  
$ git branch -D master  # 删除master
$ git branch -m master  # 将当前分支重命名为master，通常与上个命令一起使用
```

### git pull
```bash
$ git pull origin master
```

### git push
```bash
$ git push
$ git push -f origin master
$ git push -u origin master
```
---
## 使用流程
- 第一次
```bash
$ git init
$ git remote add origin https://github.com/xxx/xxx.git
$ git add .
$ git commit -m "备注"
$ git push -u origin master
```
- 日常push
```bash
$ git add .
$ git status
$ git commit -m "备注"
$ git push
```

---
## 问题汇总

### 1).gitignore文件不起作用
```bash
$ git rm -r --cached .  # 删除所有缓存
$ git add .
$ git commit -m "update .gitignore"
$ git push
```

### 2)清除以前的commits记录
```bash
$ git checkout --orphan new_branch    # 迁出一个new_branch分支
$ git add .
$ git commit -m "create a new branch"
$ git branch -D master                # 删除master分支
$ git branch -m master                # 将new_branch分支命名为master
$ git push -f origin master  
```

### 3)fatal: remote origin already exists.  
说明：出现这个错误，说明之前链接过一个仓库了，将之前的仓库链接删除即可，命令如下：
```bash
$ git remote rm origin
$ git remote add origin [new_url]
```
