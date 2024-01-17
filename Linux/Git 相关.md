# Git 相关

[TOC]





关闭 fast-forward 进行合并 `git merge --no-ff master `





删除分支`git branch -d rc_merge`

强制删除分支 `git branch -D rc_merge`



### 检出远程分支到本地

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





### Git 强制同步远程 master 到本地 master

#### 1. 切换到本地 master 分支
首先，确保你在本地的 `master` 分支上。可以使用以下命令来切换分支：

```sh
git checkout master
```

#### 2. 拉取远程 master 分支
接着，你需要拉取远程仓库的 `master` 分支。可以使用 `git fetch` 命令来获取最新的远程仓库数据：

```sh
git fetch origin master
```

#### 3. 强制同步远程 master 到本地
最后，你可以使用 `git reset` 命令来强制同步远程的 `master` 分支到你的本地分支。这将重置你的本地 `master` 分支，使其与远程的 `master` 分支完全一致：

```sh
git reset --hard origin/master
```

使用该命令会导致本地所有未提交的更改和提交丢失，因为它会将本地 `master` 分支的状态强制更新为远程 `master` 分支的状态。

#### 注意事项
在执行这些操作之前，请确保你已经保存了所有重要的更改，并且理解强制同步可能会导致数据丢失的风险。如果你不确定，可以先备份当前的 `master` 分支：

```sh
git branch backup-master
```

这样你就有了一个名为 `backup-master` 的分支，其中包含了强制同步之前的所有提交。



#### 1. 显示出branch1和branch2中差异的部分

```
git diff branch1 branch2 --stat
```

#### 2. 显示指定文件的详细差异

```
git diff branch1 branch2 具体文件路径
```

#### 3. 显示出所有有差异的文件的详细差异

```
git diff branch1 branch2
```

#### 4. 查看branch1分支有，而branch2中没有的log

```
git log branch1 ^branch2
```

#### 5. 查看branch2中比branch1中多提交了哪些内容

`git log branch1..branch2`
**注意，列出来的是两个点后边（此处即dev）多提交的内容。**

#### 6. 不知道谁提交的多谁提交的少，单纯想知道有是吗不一样

```
git log branch1...branch2
```

#### 7. 在上述情况下，在显示出没个提交是在哪个分支上

`git log --lefg-right branch1...branch2`
**注意 commit 后面的箭头，根据我们在 –left-right branch1…branch2 的顺序，左箭头 < 表示是 branch1 的，右箭头 > 表示是branch2的。**