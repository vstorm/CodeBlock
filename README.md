###CodeBlock
=========

python+Django搭建在SAE上的个人网站，以翻译国外编程文章为主

地址：http://codeblock.sinaapp.com

###安装
1. 在SAE上创建你的应用和启用MySql服务
2. 在本地Mysql创建数据库app_你的应用名
3. 在本地运行python manger.py syncdb创建表,并将数据库导出
4. 线上PhpAdmin导入前面导出的数据库文件
5. 使用SVN上传代码


###注意
+ settting.py中的 MySQL_DB变量修改成 app_你的应用名
+ 后台修改site为你的域名
