---
date: 2020-06-01
title: "Iniciando uma instância de servidor Web"  
weight: 210
pre: "<b>2-1. </b>"
---
  
{{% notice note %}}
Esse processo executará uma instância padrão do Amazon Linux e configurará automaticamente o Servidor Web Apache/PHP durante a inicialização.  
{{% /notice %}}
  
----
  
## Ir para os Serviços do EC2  
1. No canto superior esquerdo do Console de Gerenciamento da AWS***Serviços***Clique no menu e selecione EC2.  
![gid-ec2-03](/images/compute/gid-ec2-03.png)
  
----
  
## Criar uma instância  
1. Na parte superior do menu à esquerda clique em **Painel do EC2**.  
![gid-ec2-04](/images/compute/gid-ec2-04.png)
  
2.Clique no botão **Iniciar instância** e selecione **Iniciar instância** no menu.
![gid-ec2-05](/images/compute/gid-ec2-05.png)
  
3.**[Passo 1. Selecione AMI]** Na guia Início rápido, escolha `Amazon Linux 2 AMI`. Este é o `Amazon Linux 2 AMI`, não o Amazon Linux AMI. 
![gid-ec2-06](/images/compute/gid-ec2-06.png)
  
4.**[Passo 2. Selecionar tipo de instância]**, selecione `t2.micro` e clique em **Seguinte: Configurar detalhes da instância**
![gid-ec2-07](/images/compute/gid-ec2-07.png)
  
5.**[Passo 3. Configurar instância]**, defina-o da seguinte forma:  
![gid-ec2-08](/images/compute/gid-ec2-08.png)
  
| Chaves | Valores |  
|—|—|  
| Rede | Selecione a VPC que tem a tag `VPC-Lab`. |  
| Sub-rede | Localize e selecione `Public sub-net A` no menu suspenso. |  
| Atribuir IP público automaticamente | `Ativar` |  
  
1. Todos os valores restantes usam valores padrão e clique em**Detalhes Avançados**para expandi-lo.  
**Dados do usuário** campo contém os dois métodos a seguir:***Selecione 1***e, em seguida, digite**Seguinte: Adicionar armazenamento**Por favor, selecione.  
-**Método 1.**Digite o URL onde o script shell é descrito  
```  
#include https://go.aws/38GIqcB  
```  
      ![gid-ec2-09](/images/compute/gid-ec2-09.png)
  
-**Método 2.**Digite o script shell diretamente  
```  
#! /bin/sh  
yum -y instalar httpd php mysql php-mysql  
chkconfig httpd em  
systemctl iniciar httpd  
se [! -f /var/www/html/bootcamp-app.tar.gz]; então  
cd /var/www/html  
wget https://s3.amazonaws.com/awstechbootcamp/GettingStarted/bootcamp-app.tar.gz  
tar xvfz bootcamp-app.tar.gz  
chown apache:root /var/www/html/rds.conf.php  
fi  
yum -y atualização  
```  
      ![gid-ec2-10](/images/compute/gid-ec2-10.png)
  
{{% notice tip %}}
Dados do usuário é um script de inicialização personalizado que é executado quando a primeira instância é criada.  
{{% /notice %}}
  
7.**[Passo 4. Adicionar armazenamento]**atribui o Volume do SO (Volume do EBS) à instância. Aceite o valor padrão de 8GB (tipo SSD).**Seguinte: Adicionar Tags**para prosseguir para o próximo passo.  
![gid-ec2-11](/images/compute/gid-ec2-11.png)
  
8.**[Passo 5: Adicionar etiquetas]**, você pode adicionar uma variedade de informações para identificar sua instância. As informações sobre tags facilitam para os usuários verem a finalidade, a finalidade e as informações relacionadas ao custo de uma instância.**Adicionar Tag**e digite a chave e o valor como mostrado abaixo. Quando feito**Seguinte: Configurar o Security Group**Clique em.  
![gid-ec2-12](/images/compute/gid-ec2-12.png)
  
| Chaves | Valores |  
|—|—|  
| Chave | `Name` |  
| Valor | `Servidor Web para AMI` personalizado |  
  
9.**[Etapa 6: Configurar o grupo de segurança]**, você pode criar um novo security group ou selecionar um security group existente.  
O security group especifica os protocolos e endereços que você deseja permitir com a política de firewall. Crie e nomeie um grupo de segurança novo para o laboratório.  
Digite `Dia da Imersão - Servidor Web` para o nome do grupo de segurança** e **Descrição**, em seguida, selecione Adicionar regra** para selecionar***HTTP***para permitir TCP/80 para serviços Web também. do endereço de origem**0.0.0.0/0**significa acesso a partir de qualquer rede. No canto inferior direito**Revisão e lançamento**Clique em.  
![gid-ec2-13](/images/compute/gid-ec2-13.png)
  
10.**[Passo 7. Revisão]**, verifique as informações que você configurou anteriormente e clique em**Lançamento**para executar a instância.  
![gid-ec2-14](/images/compute/gid-ec2-14.png)
  
11. Neste laboratório, você não aprenderá como acessar sua instância com um par de chaves. Então, na tela Selecionar par de chaves**Prossiga sem um par de chaves**Selecione. Marque as caixas de seleção abaixo e clique em**Iniciar Instâncias**Clique em.  
![gid-ec2-15](/images/compute/gid-ec2-15.png)
  
12. Você verá informações na tela de que a instanciação está em andamento. No canto inferior direito**Exibir Instâncias**para ver uma lista de instâncias do EC2.  
![gid-ec2-16](/images/compute/gid-ec2-16.png)
  
13. Depois que sua instância for executada, você poderá determinar a zona de disponibilidade na qual sua instância está sendo executada, IP acessível externamente e informações de DNS.  
![gid-ec2-17](/images/compute/gid-ec2-17.png)
  
----
  
## Acesso ao serviço Web  
  
1. instância**Verificação de status**resultado**2/2 cheques passados**Aguarde até que se torne. Quando a inicialização estiver concluída**2/2 cheques passados**vai mudar para.  
![gid-ec2-18](/images/compute/gid-ec2-18.png)
  
2. Abra uma nova guia do navegador da Web e, na área onde você insere um endereço URL, selecione**Digite DNS público ou IPv4 IP público**Por favor. Se você vir a página como mostrado abaixo, sua instância do servidor web é configurada normalmente.  
![gid-ec2-20](/images/compute/gid-ec2-20.png)
  
----
  
## Conexões de instância  
  
1. Insira o console da instância do EC2. Selecione a instância à qual você deseja se conectar e selecione o meio**Conectar**botão.  
![gid-ec2-21](/images/compute/gid-ec2-21.png)
  
1.**Conecte sua instância**, selecione a guia Conexão de Instância do EC2 e, em seguida, clique em**Conectar**botão.  
![gid-ec2-22](/images/compute/gid-ec2-22.png)
  
3. Depois de esperar por um tempo, você pode usar o console SSH baseado em navegador, como mostrado abaixo. Basta fechar a janela depois de testar.  
![gid-ec2-23](/images/compute/gid-ec2-23.png)
  
----
  
## Criar uma AMI personalizada  
{{% notice note %}}
No console do AWS EC2, você pode usar a instância criada para criar uma imagem e usá-la para criação futura de instâncias. Isso é chamado de AMI personalizada.  
Nesse caso, criaremos uma AMI usando a instância do servidor web que criamos anteriormente.  
{{% /notice %}}
  
1. No console do EC2, selecione a instância que você criou anteriormente e**Ações**->**Imagem e modelos**->**Criar imagem**Selecione.  
![gid-ec2-24](/images/compute/gid-ec2-24.png)
  
2. Na janela Criar imagem, digite**Criar imagem**para criar a imagem.  
![gid-ec2-25](/images/compute/gid-ec2-25.png)
  
| Chaves | Valores |  
|—|—|  
| Nome da imagem | `Servidor Web v1` |  
| Descrição da imagem | `LAMP web server AMI` |  
  
3. Observe a janela informando que a solicitação de criação de imagem foi concluída.  
  
4. No menu do console esquerdo, clique em**Imagens**por baixo**AMIS**botão e clique nele. A AMI que acabei de pedir**Status**está criando (**Pendente**), ou disponível quando concluído (**Disponível**) e você pode ver que está em um estado.  
![gid-ec2-27](/images/compute/gid-ec2-27.png)
  
----
  
## Encerrar a instância  
{{% notice info %}}
{{% notice info %}}
{{% /notice %}}
  
1. A partir do painel do EC2**Instâncias**guia. Em seguida, selecione a instância que você deseja excluir. desde**Estado da instância**->**Encerrar instância**Clique em.  
![gid-ec2-28](/images/compute/gid-ec2-28.png)
  
2. Se uma janela de aviso for exibida, clique em**Terminar**para excluí-lo.  
![gid-ec2-29](/images/compute/gid-ec2-29.png)
  
3. Estado da instância**Desligamento**vai mudar para.  
![gid-ec2-30](/images/compute/gid-ec2-30.png)
  
4. Em breve**encerrado**vai mudar para. Exclusão concluída. Você pode ver um período de tempo para o registro de exclusão de exemplo.  
![gid-ec2-31](/images/compute/gid-ec2-31.png)
  
----
  
## Arquiteturas até à data  
Conceitualmente, os recursos que você configurou até o momento são exibidos no desenho como mostrado abaixo.  
![gid-ec2-32](/images/compute/gid-ec2-32.svg)
