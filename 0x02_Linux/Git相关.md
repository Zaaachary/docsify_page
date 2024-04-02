# Git 相关



关闭 fast-forward 进行合并 `git merge --no-ff master `





删除分支`git branch -d rc_merge`

强制删除分支 `git branch -D rc_merge`



##### 检出远程分支到本地

1. **获取最新的远程分支列表**

   ```
   git fetch
   ```

   这将更新你的本地远程跟踪分支列表。

2. **检出远程分支**

   ```
   git checkout <branch_name>
   ```

   如果分支不存在于本地，Git 会自动创建一个新的本地分支，名为 `<branch_name>`，并将其设置为跟踪远程分支。


我的git仓库添加了几个不想要的文件/目录，并提交了。而后我将它们 添加到 .gitignore 中了，但是如何从仓库中删除？

使用git rm命令的--cached选项

1. 打开终端或命令行界面，并确保你已经在Git仓库的根目录下。
2. 运行以下命令来删除已经提交的文件或目录：
`git rm -r --cached path/to/unwanted_file_or_directory`
3. 替换path/to/unwanted_file_or_directory为你要删除的文件或目录的路径。
4. 运行以下命令来提交更改：
`git commit -m "Remove unwanted files/directories"`
5. 运行以下命令来推送更改到远程仓库（如果需要）：
`git push origin branch_name`
6. 替换branch_name为你的分支名称。
