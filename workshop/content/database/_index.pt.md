---
date: 2020-06-01
title: "Banco de dados — Amazon Aurora"  
weight: 300
pre: "<b>3. </b>"
---
  
{{% notice note %}}
Entre as muitas opções de banco de dados disponíveis na AWS, o Amazon RDS (Relational Database Service) é um serviço de banco de dados baseado em nuvem fácil de configurar e operar e é fácil de dimensionar. O Amazon RDS é econômico, fácil de dimensionar a capacidade e reduz tarefas administrativas demoradas, liberando você para se concentrar em seus negócios e aplicativos.  
{{% /notice %}}
  
----
  
## Diagrama meta  
Este laboratório de banco de dados implanta uma instância do RDS Aurora dentro do `vPC-Lab` e configura o Web Service (Apache+PHP) de uma instância dentro de um grupo de Auto Scaling já criado para usar o RDS Aurora (MySQL). Depois de estabelecer sua conexão com seu banco de dados, crie uma nova versão da AMI personalizada existente e atualize-a para usar a nova AMI no seu Grupo de Auto Scaling. Em seguida, através do Web Browser, vamos adicionar, modificar e excluir contatos de um livro de endereços simples armazenado no RDS DB.  
![Architecture Diagram](/images/rds/gid-rds-01.svg)
  
----
  
## Ordem do laboratório  
Este laboratório estará na seguinte ordem:  
  
  
  
  
  
  
