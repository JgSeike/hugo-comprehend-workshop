---
date: 2020-06-01
title: "Criando um Security Group da VPC"  
weight: 310
pre: "<b>3-1. </b>"
---
  
{{% notice note %}}
Os serviços RDS usam o mesmo modelo de segurança que o EC2. O formulário de uso mais comum é fornecer dados como um servidor de banco de dados para uma instância do EC2 em execução como um servidor de aplicativos dentro da mesma VPC ou configurá-lo para ser acessível a um cliente de aplicativo de banco de dados fora da VPC. Para um controle de acesso adequado, você deve aproveitar os security groups da VPC.  
{{% /notice %}}
  
----
  
  
  
1. No lado esquerdo do painel da VPC,**Grupos de Segurança**e, em seguida, selecione**Criar grupo de segurança**Por favor selecione  
 ![gid-rds-02](/images/rds/gid-rds-02.png)
  
2. Como mostrado abaixo**nome do grupo de segurança**,**Descrição**para usar esse grupo e, em seguida, digite**VPC**Especifica o. (Verifique a atribuição de VPC com a tag `VPC-Lab`)  
 ![gid-rds-03](/images/rds/gid-rds-03.png)
  
| Chaves | Valores |  
|—|—|  
| Nome do grupo de segurança | `DB-SG `|  
| Descripyion | `Banco de Dados Security Group` |  
| VPC | `VPC-LAB` |  
  
  
![gid-rds-04](/images/rds/gid-rds-04.png)
  
4. Quando a atribuição estiver concluída, a parte inferior**Criar grupo de segurança**para criar um grupo de segurança.  
![gid-rds-04-1](/images/compute/gid-ec2-46.png)
  
5. Verifique os grupos de segurança que foram criados.  
![gid-rds-05](/images/rds/gid-rds-05.png)