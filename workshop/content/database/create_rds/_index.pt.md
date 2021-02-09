---
date: 2020-06-01
title: "Criando uma Instância do RDS"  
weight: 320
pre: "<b>3-2. </b>"
---
  
{{% notice note %}}
Agora que você criou um security group para uso com RDS,**RDS Aurora (compatível com MySQL)**Vamos criar uma instância.  
{{% /notice %}}
  
----
  
  
![gid-rds-06](/images/rds/gid-rds-06.png)
  
2. A partir do painel**Criar banco de dados**para começar a criar uma instância do RDS.  
![gid-rds-07](/images/rds/gid-rds-07.png)
  
3. Selecione o mecanismo de banco de dados para a instância do RDS que você deseja usar. O Amazon RDS oferece uma opção de mecanismo de banco de dados baseado em código aberto e um mecanismo de banco de dados comercial. Este laboratório usa a Amazon**Amazon Aurora, um mecanismo de banco de dados compatível com MySQL**será usado. Na caixa Selecionar método de criação de banco de dados, clique em**Criação padrão**Selecione.  
![gid-rds-08](/images/rds/gid-rds-08.png) 
  
4.***Tipo de motor***para o Amazon Aurora**,***Edição***Selecione**Amazon Aurora com capacidade compatível com MySQL**,***Versão***Prata**Aurora (MySQL 5.7) 2.07.2**Selecione.  
![gid-rds-09](/images/rds/gid-rds-09.png) 
  
5.***Modelo***em**Produção**Selecione.  
![gid-rds-10](/images/rds/gid-rds-10.png) 
  
6.**Configurações**especifica informações para identificar uma instância do RDS e informações do administrador. Insira as informações abaixo.  
![gid-rds-11](/images/rds/gid-rds-11.png) 
  
| Chaves | Valores |  
|—|—|  
| Identificador de cluster de banco de dados | `rdscluster` |  
| Nome de usuário mestre | `awsuser` |  
| Senha mestra | `awspassword` |  
  
7.**Tamanho da instância de banco de**com**Disponibilidade e Durabilidade**Certifique-se de que a entrada é a seguinte:**Configurando um nó de replicação de leitura em uma zona de disponibilidade diferente da classe de instância otimizada para memória**é definido como o valor padrão.  
![gid-rds-12](/images/rds/gid-rds-12.png) 
  
1.**Conectividade**, configure sua rede e segurança. No campo Nuvem privada virtual, selecione o VPC-Lab que você criou e especifique a VPC, a sub-rede, se o acesso de fora da VPC e o security group no qual a instância do RDS operará. Basta configurá-lo como mostrado abaixo.  
![gid-rds-13](/images/rds/gid-rds-13.png) 
  
| Chaves | Valores |  
|—|—|  
| Nuvem privada virtual (VPC) | `VPC-Lab` |  
| Grupo de sub-redes | `Criar novo grupo de sub-rede de banco de dados` |  
| Publly acessível | `Não `|  
| security group da VPC | Escolha existente: `DB SG` (***Em Padrão, clique na marca X ao lado dela para excluir***) |  
| Porta de Banco de Dados | `3306` |  
  
9. Role para baixo e vá para baixo,**Configuração adicional**Clique em. Defina as opções de banco de dados como mostrado abaixo.  
![gid-rds-14](/images/rds/gid-rds-14.png) 
  
| Chaves | Valores |  
|—|—|  
| Nome inicial do banco de dados | `immersionday` |  
| grupo de parâmetros do cluster de banco de dados | `default.aurora5.7` |  
| grupo de parâmetros banco de dados | `default.aurora5.7` |  
  
10. Depois,**Backup**,**Criptografia**,**Backtrack**,**Monitoramento**,**Registrar exportações**, aceite todos os valores padrão e assim por diante.**Criar banco de dados**para criar o banco de dados.  
![gid-rds-15](/images/rds/gid-rds-15.png) 
  
11. Uma nova instância do RDS agora é criada. Isso pode levar mais de 5 minutos. O status da instância de banco de dados***Disponível***, você pode usar a instância do RDS.  
![gid-rds-16](/images/rds/gid-rds-16.png) 
  
12. No console do RDS**, selecione o menu **Databases** à esquerda e o status da instância de banco de dados do RDS que você criou é***Disponível***.  
![gid-rds-17](/images/rds/gid-rds-17.png) 
  
----
  
## Arquiteturas até à data  
Conceitualmente, os recursos que você configurou até o momento são exibidos no desenho como mostrado abaixo.  
![gid-rds-100](/images/rds/gid-rds-100.svg)
