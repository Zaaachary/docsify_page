# Docker 相关





注册了一个 linux 服务器，有root权限。 我准备安装docker，并且想让各个子用户也有访问docker的权限。（例如 work 用户），该如何进行？ linux 是 ubuntu 系统

要在Ubuntu上安装Docker并为子用户提供访问权限，可以按照以下步骤进行操作：

1. 登录到Linux服务器，并使用root权限运行以下命令来安装Docker：

   ```
   apt update
   apt install docker.io
   ```

2. 安装完成后，你需要将用户添加到`docker`用户组中。假设你想要将`work`用户添加到该用户组中，可以运行以下命令：

   ```
   usermod -aG docker work
   ```

   > `usermod -aG docker work` 的含义是将用户 "work" 添加到 "docker" 用户组中。   
   > 具体解释如下：
   >
   >    - `usermod` 是一个用于修改用户属性的命令。
   >    - `-aG` 选项用于将用户添加到一个或多个附加用户组中，而不会影响用户的主组。
   >    - `docker` 是要添加用户到的用户组名称。
   >    - `work` 是要被添加到用户组的用户名。

   这条命令的作用是将用户 "work" 添加到 "docker" 用户组中，允许该用户执行与 Docker 相关的操作，例如运行容器、管理镜像等。

3. 然后，注销当前用户（root），重新登录以使更改生效。

4. 确认Docker是否成功安装并用户是否有访问权限。运行以下命令来检查：

   ```
   docker info
   ```

   如果你能够看到有关Docker的相关信息，并且没有权限错误提示，那么说明Docker已经成功安装并且`work`用户也具有访问权限了。

现在，你的`work`用户应该能够使用Docker了。记住，在使用Docker时需要谨慎操作，以确保服务器的安全性和稳定性。



然而在使用的时候 会存在没有权限访问 docker daemon socket 权限的问题，以下为解决方案：

1. Run the command with `sudo`:

   ```bash
   sudo docker run xxxx
   ```

2. Add your user to the `docker` group and then log out and log back in (or restart the system):

   ```bash
   sudo usermod -aG docker $USER
   ```

3. If you're using a Linux distribution like Ubuntu, you might need to use `sudo` every time you run Docker commands, or you can enable Docker to be used without superuser privileges by executing the following command and then logging out and back in:

   ```bash
   sudo systemctl enable docker
   ```

Please try one of these solutions and let me know if you encounter any issues.