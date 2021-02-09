---
date: 2020-06-01
title: "Atualizando grupos de Auto Scaling"  
weight: 340
pre: "<b>3-4. </b>"
---
  
{{% notice note %}}
Crie uma nova AMI personalizada usando uma instância da Web configurada para usar o Aurora. Atualize o modelo de execução com essa AMI personalizada recém-criada e use o Auto Scaling Group para implantar novas versões de instâncias com informações de conexão do RDS.  
{{% /notice %}}
  
----
  
## Criar uma nova AMI personalizada  
1.***Console EC2***, e no menu à esquerda, clique em**Instâncias**e marque a caixa de seleção `ASG-WEB-Instance` instância. Depois disso, selecione Ações -> Imagem e modelos -> Criar imagem sequencialmente.  
![gid-rds-23](/images/rds/gid-rds-23.png) 
  
2.***Nome da imagem***, digite `Servidor Web v2`,***Descrição da imagem***, digite `LAMP web server AMI com configuração de conexão RDS”. E**Criar imagem**botão.  
![gid-rds-24](/images/rds/gid-rds-24.png) 
  
3. Localize e clique em AMIs no menu esquerdo do console do EC2. Se você esperar um momento, a nova AMI personalizada***pendente***estado***disponível***status.  
![gid-rds-26](/images/rds/gid-rds-26.png) 
![gid-rds-27](/images/rds/gid-rds-27.png)
  
4. A arquitetura até o momento é a seguinte:  
![gid-rds-102](/images/rds/gid-rds-102.svg)
  
----
  
## Atualizar modelo de lançamento  
1. No console do EC2, selecione Launch Modelos** no menu à esquerda e***Nome do modelo de lançamento***Depois de marcar a caixa de seleção que é `Web`,**Ações**botão, clique**Modificar modelo (Criar nova versão)**Clique em.  
![gid-rds-28](/images/rds/gid-rds-28.png)
  
2. No Modificar modelo, clique em***Descrição da versão do modelo***na orientação Auto Scaling, conforme mostrado abaixo, e, em seguida, digite***Fornecer...***sobre**Marque a caixa**.  
![gid-rds-29](/images/rds/gid-rds-29.png)
- Descrição da versão do modelo: `Immersion Day Web Instances Template - com conexão RDS String`  
  
3. Role para baixo***Lançar conteúdo do modelo***Na coluna Imagem de máquina da Amazon (AMI), selecione sua AMI personalizada recém-criada. Na barra de pesquisa***Servidor Web v2***para encontrá-lo mais fácil.  
![gid-rds-30](/images/rds/gid-rds-30.png) 
  
4. Em seguida, role para baixo até a parte inferior, deixando as outras configurações como elas estão.**Criar versão do modelo**Clique em.  
![gid-rds-31](/images/rds/gid-rds-31.png) 
  
5.**Exibir modelo de lançamento**Toque em.  
![gid-rds-32](/images/rds/gid-rds-32.png) 
  
6. Selecione a guia Versões no meio. Você deve ver a seguinte tela.  
![gid-rds-33](/images/rds/gid-rds-33.png) 
  
7. Dentre as duas versões, selecione Versão 2 que você acabou de criar e pressione Ações -> Definir versão padrão.  
![gid-rds-34](/images/rds/gid-rds-34.png) 
  
8. Depois de verificar se a versão do modelo é 2, clique em**Definir como versão padrão**botão.  
![gid-rds-35](/images/rds/gid-rds-35.png) 
  
9. Agora vejo que a versão padrão do modelo Launch mudou.  
![gid-rds-36](/images/rds/gid-rds-36.png) 
  
----
  
## Atualizar grupo de Auto Scaling  
Agora é hora de atualizar o Grupo Auto Scaling.  
  
1. No menu esquerdo do console EC2, selecione a parte inferior**Grupos de Auto Scaling**Selecione. Selecione o `WEB-ASG` que você criou e, em seguida, clique em**Editar**botão.  
![gid-rds-37](/images/rds/gid-rds-37.png) 
  
2. Na tela Editar WEB-ASG***Capacidade desejada***com***Capacidade mínima***é `2`,***Capacidade máxima***Coloque `4`**Atualizar**botão.  
![gid-rds-38](/images/rds/gid-rds-38.png) 
  
3. Verifique a versão do modelo Launch abaixo. Certifique-se de que está definido como `Default (2) `,**Atualizar**botão.  
![gid-rds-39](/images/rds/gid-rds-39.png) 
![gid-rds-40](/images/rds/gid-rds-40.png) 
  
  
4. Role para baixo até a parte inferior***Avançado***coluna, e**Editar**botão.  
![gid-rds-41](/images/rds/gid-rds-41.png) 
  
5.***Recarga padrão***para `30 segundos` e no canto inferior direito**Atualizar**botão. Se você esperar um momento, verá que o Auto Scaling Group usa o novo modelo de execução para criar uma nova instância.  
![gid-rds-42](/images/rds/gid-rds-42.png) 
  
6. Observe que as duas instâncias são InService. Mas quando olhamos para a versão, um é o antigo modelo de lançamento***Versão (Versão 1)***Uma instância criada pelo. Vamos encerrar manualmente esta instância de versão antiga.**ID da instância (i-xxxxx)**Clique em.  
    ![gid-rds-44](/images/rds/gid-rds-44.png) 
  
A arquitetura que configuramos até o momento é a seguinte:  
    ![gid-rds-103](/images/rds/gid-rds-103.svg)
  
7. Você pode verificar a especificação da instância que deseja encerrar.**Estado da instância**->**Encerrar instância**Pressione.  
![gid-rds-45](/images/rds/gid-rds-45.png) 
  
8. Se você vir um pop-up de aviso que você realmente quer desistir,**Terminar**Pressione.  
![gid-rds-46](/images/rds/gid-rds-46.png) 
  
9. Volte para o menu “Auto Scaling Group**. **Selecione WEB-ASG e pressione a guia Gerenciamento de instância** no meio, o atual***Você verá 3 instâncias.***Se você olhar para isso, você deve sair manualmente do***A instância da versão 1 está encerrando***estado, e o novo***O que uma instância de versão 2 está chegando***Você pode ver o  
![gid-rds-47](/images/rds/gid-rds-47.png) 
Este é o diagrama imediatamente após a instância ter sido encerrada.  
    ![gid-rds-104](/images/rds/gid-rds-104.svg)
  
10. Se você usar o DNS do ALB para acessar o serviço da Web enquanto a alteração estiver ocorrendo, você verá que o acesso é normal.  
![gid-rds-47-1](/images/compute/gid-ec2-68.png) 
  
  
Volte para a página da web demo e acesse o banco de dados**RDS**Vamos pressionar o botão.  
![gid-rds-48](/images/rds/gid-rds-48.png) 
  
12. Ele será acessado da seguinte forma, e você verá que as alterações feitas anteriormente também são refletidas.  
![gid-rds-49](/images/rds/gid-rds-49.png) 
  
----
  
## Arquiteturas até à data  
Agora, ao fazê-lo, você construiu um serviço web altamente disponível. A arquitetura de infraestrutura que configuramos até agora é a seguinte:  
![gid-rds-105](/images/rds/gid-rds-105.svg)
  
