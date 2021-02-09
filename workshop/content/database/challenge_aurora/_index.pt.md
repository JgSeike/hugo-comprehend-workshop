---
date: 2020-06-01
title: "Desafios - Conexões RDS Aurora"  
weight: 360
pre: "<b>3-6. </b>"
---
  
{{% notice note %}}
Vamos fazer uma conexão RDS através da CLI MySQL, que é usada para administração e operação de banco de dados normais.  
{{% /notice %}}
  
----
  
Para fazer isso,  
  
1. Crie uma instância do EC2 a partir da AMI criada na sub-rede pública em `VPC-Lab. Neste ponto, você deve permitir IP público em suas opções de rede.  
  
2. Permite que você altere as configurações do security group para o RDS Aurora. Configure a instância do EC2 recém-criada para aceitar o security group como origem.  
  
3. SSH na instância do EC2 que você acabou de criar e conectar-se ao RDS Aurora por meio do cliente MySQL. O EC2 Web Server já tem o MySQL Client instalado durante a implantação do EC2.  
  
O desafio é configurar os itens acima para si mesmo. Se as configurações estiverem corretas, você pode conectar ao CLI e executar o comando mysql como mostrado abaixo.  
  
```ssh
$ ssh -i AWS-ImmersionDay-Lab.pem ec2-user@”EC2 Host FQDN or IP”
Last login: Sun Feb 18 14:41:59 2018 from 112.148.83.236

       __|  __|_  )
       _|  (     /   Amazon Linux AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-ami/2017.09-release-notes/


$ mysql -u awsuser -pawspassword -h awsdb.ccjlcjlrtga1.ap-northeast-2.rds.amazonaws.com

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 34
Server version: 5.6.10 MySQL Community Server (GPL)


Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| immersionday       |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.01 sec)

mysql> use immersionday;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+------------------------+
| Tables_in_immersionday |
+------------------------+
| address                |
+------------------------+
1 row in set (0.01 sec)

mysql> select * from address;
+----+-------+--------------+---------------------+
| id | name  | phone        | email               |
+----+-------+--------------+---------------------+
|  1 | Bob   | 630-555-1254 | bob@fakeaddress.com |
|  2 | Alice | 571-555-4875 | alice@address2.us   |
+----+-------+--------------+---------------------+
2 rows in set (0.00 sec)

mysql>
```