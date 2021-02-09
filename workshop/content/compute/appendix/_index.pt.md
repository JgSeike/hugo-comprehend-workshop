---
date: 2020-06-01
title: "Apêndice - Conceitos adicionais do EC2"  
weight: 240
pre: "<b>2-4. </b>"
---
  
{{% notice warning %}}
Para manter o nível gratuito, você pode usar o tipo de instância***t2.micro***, não mude.  
{{% /notice %}}
  
----
  
## Criar um novo par de chaves  
A fim SSH acessar EC2, você precisa de criar um par de chaves. O procedimento a seguir descreve o processo de criação de uma chave SSH Air.  
  
{{% notice info %}}
Os pares de chaves são gerenciados independentemente para cada região.  
{{% /notice %}}
  
  
  
2. No tópico Rede e Segurança,**Pares de chaves**Selecione Você verá uma página onde você pode gerenciar seu SSH Key Air. Para criar um novo SSH Key Air**Criar par de chaves**botão.  
![gid-ec2-102](/images/compute/gid-ec2-102.png) 
  
3. Na janela Criar par de chaves,**Laboratório de Imersão da AWS**Especifique o nome do par de chaves na**Criando um par de chaves**. Clique no botão O nome do par de chaves pode ser especificado de acordo com sua finalidade e finalidade para facilitar a identificação do usuário.  
{{% notice info %}}
Se você estiver usando PuTTY, selecione o ppk inferior do tipo de arquivo (Windows) e, se você estiver usando ssh (Mac ou Linux), selecione o tipo de arquivo como pem.  
{{% /notice %}}
![gid-ec2-103](/images/compute/gid-ec2-103.png) 
  
4. Um novo par de chaves é criado e baixado para o seu PC apenas uma vez pela primeira vez. Se você escolheu o formato de arquivo pem, o nome do arquivo baixado será***aws-immersionday-lab.pem***. Se você selecionou o formato de arquivo ppk, clique em***AWS-Imersionday-lab.ppk***será baixado.  
![gid-ec2-104](/images/compute/gid-ec2-104.png) 
  
5. Por favor, mantenha o arquivo de par de chaves baixado em um local seguro.  
  
{{% notice warning %}}
O arquivo de par de chaves baixado será usado para atribuir às instâncias do EC2 criadas no próximo laboratório. Também é necessário fazer login na instância do EC2 no futuro.  
{{% /notice %}}
  
----
  
## Acesso ao sistema operacional Linux via SSH  
{{% notice info %}}
As instâncias Linux executadas na AWS usam um método de autenticação diferente da abordagem normal do Linux local. Estou usando a autenticação de chave privada identidade+chave privada/chave pública em vez de identidade normal + autenticação de usuário do sistema operacional de senha.  
{{% /notice %}}
  
Atualmente, existem três maneiras de se conectar a uma instância do EC2:  
1. Como usar um par de chaves para SSH  
2. Como se conectar usando o Gerenciador de Sessão no Systems Manager  
3. Conectando-se a instâncias usando conexões SSH baseadas em navegador  
![gid-ec2-105](/images/compute/gid-ec2-105.png) 
  
Neste módulo, você aprenderá como fazer o SSH para uma instância do EC2 que você criou anteriormente usando o par de chaves especificado no EC2.  
  
Sua Chave Privada só pode ser baixada uma vez pelo usuário durante a criação do par de chaves, e a instância do EC2 Linux instalará a Chave Pública correspondente ao par de chaves especificado durante o processo de implantação. Os usuários poderão então autenticar SSH e se conectar às instâncias do Linux do EC2 usando sua própria Chave Privada.  
  
{{% notice info %}}
Dependendo do sistema operacional e do tipo de Ferramenta de Cliente SSH usada pelo usuário que conecta, a preparação preliminar pode ser necessária. Seu sistema operacional terminal é baseado no Windows, e a Ferramenta de cliente SSH que você usa é**Massa**, é conveniente baixar e usar o formato.ppk ao gerar o par de chaves inicial.  
{{% /notice %}}
  
----
  
# Como usar o PuTTY para usuários de laptop do Windows  
{{% notice info %}}
A AWS está disponível no formato de certificado padrão, Privacy-Enhanced Electronic Mail (PEM), mas o PuTTY, o cliente Freeware SSH representativo usado principalmente por usuários de laptop Windows, não suporta diretamente certificados de formato PEM. (A maioria dos outros clientes SSH apoia certificados PEM à revelia.)  
{{% /notice %}}
  
Portanto, se você estiver usando PuTTY no computador portátil Windows, você deve baixar a chave privada em um formato de arquivo PPK (.ppk, PuTTY Private Key Files) compatível com PuTTY para conectividade SSH com sua instância do EC2.  
  
----
  
# Especificando e conectando um certificado PPK no PuTTY  
  
1. Execute massa de vidraceiro, e***ec2-usuário @EC2_PUBLIC_IP_ADDRESS /FQDN***no formato de  
![gid-ec2-106](/images/compute/gid-ec2-106.png) 
  
2.**Conexão > SSH > Auth**cardápio**Arquivo de chave privada para autenticação:**item**Navegar**para especificar um arquivo de certificado (Chave privada) no formato PPK. No futuro, se você fizer o SSH da instância do EC2 conectada para outra instância do EC2 na VPC, poderá usar o**Permitir o encaminhamento**Por favor, selecione um recurso  
![gid-ec2-107](/images/compute/gid-ec2-107.png) 
  
3.**Abrir**, faça perguntas sobre se o certificado está armazenado em cache e, em seguida, a sessão SSH será conectada.  
![gid-ec2-108](/images/compute/gid-ec2-108.png) 
  
4. Agora você pode conexões SSH especificando um certificado privado (Chave privada). Use comandos básicos do Linux para verificar a configuração do sistema operacional e assim por diante.  
  
----
  
## Alterando o tipo de instância  
{{% notice note %}}
As instâncias do EC2 que usam o EBS Volume podem alterar o tipo de instância (dependendo da capacidade da CPU/memória e da área de uso principal) por meio de um procedimento simples. Não é necessário neste laboratório, mas você pode alterar o tipo de instância para o tipo desejado seguindo as etapas abaixo.  
{{% /notice %}}
  
1. No Console de Gerenciamento da AWS, selecione a instância que você deseja alterar.**Estado da instância**sub**Parar instância**(Note que este não é o fim!) Selecione.  
![gid-ec2-109](/images/compute/gid-ec2-109.png) 
  
2. Identifique as instâncias a serem interrompidas e clique em**Pare**botão.  
![gid-ec2-110](/images/compute/gid-ec2-110.png) 
  
1. Quando a instância é interrompida**Ação**->**Configurações da instância**e selecione o**Alterar tipo de instância (alterar o tipo de instância)**Por favor selecione  
![gid-ec2-111](/images/compute/gid-ec2-111.png)  
  
4. Selecione o tipo de instância que você deseja alterar e clique em**se candidatando**. Clique no Neste laboratório,**t2.small**Altere o valor para.  
![gid-ec2-112](/images/compute/gid-ec2-112.png) 
  
5. Quando as alterações estiverem concluídas,**Status da instância**sub**startup**para começar com o tipo de instância alterado.  
  
  
  
