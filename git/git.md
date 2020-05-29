- 查看当前项目仓库中包含的所有标签
    ```shell
    $ git tag -n
    ```
    
- 签出对应标签版本的代码
    ```shell
    git checkout foo
    ```

- 撤销改动
    ```shell
    git reset --hard
    ```

- 查看两个版本之间的变化
    ```shell
    git diff foo bar
    ```

- 更加直观的查看版本变化
    ```shell
    gitk
    ```

- 更新本地仓库
    ```shell
    git fetch --all
    git fetch --tags
    git reset --hard origin/master
    ```

