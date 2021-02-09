---
date: 2020-06-01
title: "Conectando seu servidor de aplicativos da Web ao RDS"  
weight: 330
pre: "<b>3-3. </b>"
---
  
{{% notice note %}}
A instância do Servidor Web que você criou no laboratório de computação anterior contém código que cria um catálogo de endereços simples para uso do RDS. Para usar o RDS com o EC2 Web Server, você deve primeiro verificar o URL do endpoint (DNS FQDN) do RDS.  
{{% /notice %}}
  
----
  
## Conectando servidores de aplicativos Web ao RDS  
  
1. No console do Amazon RDS, no menu à esquerda, clique em**bancos de dados**, selecione o nome do cluster do RDS Aurora criado e clique em**rdscluster**Por favor selecione**Conectividade e segurança**, você pode visualizar os endpoints do RDS Aurora.**Tipo**dente**Escritor**, o nome do Endpoint.  
![gid-rds-17](/images/rds/gid-rds-17.png) 
  
3. Resolve o nome DNS do ALB que você criou no laboratório da VPC e se conecta ao navegador da Web.  
![gid-ec2-67](/images/compute/gid-ec2-67.png) 
  
3. Selecione**RDS** no menu acima para inserir as informações necessárias para a conexão RDS. A partir das informações da instância do RDS,***URL do endpoint do gravador***e você inseriu ao criar instâncias do RDS.***Banco de dados***Pousada `immersionday`,***Nome de usuário***é `awsuser` e***Senha***, digite `awspassword` e, em seguida, clique em**Enviar**Selecione.  
![gid-rds-18](/images/rds/gid-rds-18.png) 
  
| Chaves | Valores |  
|—|—|  
| Endpoint | `Nome do ponto final do escritor` (ex. rdscluster.cluster-.ap-northeast-2.rds.amazonaws.com<임의의 번호>) |  
| Banco de dados | `immersionday` |  
| Nome de usuário | `awsuser` |  
| Senha | `awspassword` |  
  
4. Se as informações inseridas estiverem corretas, você pode***Criar um arquivo de configuração para conexão de banco de dados usando PHP***. No futuro, ao se conectar ao menu RDS, as informações de conexão são referenciadas, portanto, você não precisa passar pelo processo de login do banco de dados.  
![gid-rds-18-1](/images/rds/gid-rds-18-1.png) 
  
5. E define automaticamente o banco de dados especificado (immersionday) para um simples**abordar**, e dois Registro de Amostra (Linha) são adicionados. Aguarde 10 segundos para alternar entre as telas automaticamente. Verifique se o registro de amostra adicionado está exibido corretamente.  
![gid-rds-20](/images/rds/gid-rds-20.png) 
  
6. O Servidor de Aplicativos Web e o RDS Aurora agora estão conectados corretamente. Em uma página web configurada com PHP**Editar**,**Remover**ou**Adicionar contato**Use Link para verificar se os dados podem ser modificados/excluídos e adicionados ao banco de dados do RDS. Neste caso, adicionamos o seguinte usuário como uma amostra:  
![gid-rds-21](/images/rds/gid-rds-21.png) 
  
7. Você pode ver que o usuário foi adicionado normalmente.  
![gid-rds-22](/images/rds/gid-rds-22.png) 
  
----
  
## Arquiteturas até à data  
![gid-rds-101](/images/rds/gid-rds-101.svg)
