---
date: 2020-06-01
title: "Implantar um serviço Web de escalonamento automático"  
weight: 220
pre: "<b>2-2. </b>"
---
  
{{% notice note %}}
Vamos implantar um serviço Web que seja escalonado automaticamente para out/in e altamente disponível sob carga sobre a infraestrutura de rede criada no laboratório de rede. Isso usará a AMI do servidor Web que você criou no capítulo anterior e a infraestrutura de rede que você configurou em 'Laboratório VPC'.  
{{% /notice %}}
  
----
  
## Configurar o Balanceador de Carga  
O AWS Elastic Load Balancing oferece suporte a três tipos de balanceadores de carga: Application Load Balancer, Network Load Balancer e Classic Load Balancer. Neste laboratório, você configura e configura um Application Load Balancer para balancear a carga de solicitações HTTP.  
  
# Criar ALB  
1.**Console de gerenciamento do EC2**Entrar. No menu à esquerda, role para baixo até**Balanceamento de Carga**Em Itens**Balanceadores de carga**, e no centro superior, clique em**Criar balanceador de carga**Clique em.  
![gid-ec2-33](/images/compute/gid-ec2-33.png)
  
2. Na janela Selecionar tipo de balanceador de carga, clique em**Balanceador de Carga de**do**Criar**botão.  
![gid-ec2-34](/images/compute/gid-ec2-34.png)
  
3.***[Etapa 1: Configurar o balanceador de carga]***fornece um nome para o balanceador de carga. Aqui,**Nome**com um nome `web-alb`. Deixe as outras configurações em seus valores padrão. A configuração padrão é permitir que os ALBs escutem conexões HTTP recebidas a 80 portas da Internet.  
![gid-ec2-35](/images/compute/gid-ec2-35.png)
  
4. Role um pouco para baixo e você verá uma seção para definir a zona de disponibilidade. Pré-configurada**VPC**é selecionado como `VPC-Lab`, e, em seguida, o**Zonas de disponibilidade**, encontre `ap-northeast-2a` e especifique `sub-rede pública A`. Da mesma forma, selecione `ap-northeast-2c` e especifique `sub-rede pública C`. Parte inferior direita**Seguinte: Configurar configurações de segurança**para prosseguir para o próximo passo.  
![gid-ec2-36](/images/compute/gid-ec2-36.png)
  
5.***[Etapa 2: Configurar configurações de segurança]***avisa para configurar um ouvinte de segurança que usa HTTPS. Para este laboratório, usaremos ouvintes HTTP para sua conveniência. imediatamente**Seguinte: Configurar grupos de segurança**botão para avançar.  
![gid-ec2-37](/images/compute/gid-ec2-37.png)
  
6.***[Etapa 3: Configurar grupos de segurança]***, defina os grupos de segurança que serão aplicados ao primer ALBs**Atribuir um grupo de segurança**, selecione `Criar um novo grupo de segurança`,**nome do grupo de segurança**, digite `web-alb-sg`. E**Tipo**Localize e selecione `HTTP` no menu suspenso. Quando você terminar**Seguinte: Configurar o Roteamento**para prosseguir para a próxima etapa.  
![gid-ec2-38](/images/compute/gid-ec2-38.png)
  
7.***[Etapa 4: Configurar o roteamento]***, defina o grupo de destino para o qual os listeners definidos acima passarão o tráfego. Atualmente, não temos uma instância para receber tráfego e processá-lo. uma vez**Nome**e torná-lo `web-tg`**Seguinte: Registrar alvos**e prossiga para a próxima etapa.  
![gid-ec2-39](/images/compute/gid-ec2-39.png)
  
8.***[Etapa 5: Registrar alvos]***passo. No entanto, como mencionado anteriormente, atualmente não existem metas a serem registadas.**Próximo: Revisão**para avançar.  
![gid-ec2-40](/images/compute/gid-ec2-40.png)
  
9.***[Passo 6: Revisão]***para ver as configurações que você configurou até agora. Depois de confirmar que não há anormalidades, clique em**Criar**para concluir a configuração de criação.  
![gid-ec2-41](/images/compute/gid-ec2-41.png)
  
10. A criação do balanceador de carga está concluída.**Fechar**para sair da tela de criação.  
![gid-ec2-42](/images/compute/gid-ec2-42.png)
  
----
  
## Configurando Modelos de Inicialização  
{{% notice note %}}
Agora que você criou o ALB, é hora de colocar as instâncias atrás do balanceador de carga. Para configurar uma instância do Amazon EC2 para ser executada a partir de um grupo de Auto Scaling**Modelo de inicialização**,**Iniciar configuração**, ou**Instâncias do EC2**pode ser usado. Nesse caso, criaremos um grupo Auto Scaling usando um modelo de inicialização.  
{{% /notice %}}
  
Um modelo de execução foi projetado para configurar todos os parâmetros de execução dentro de um recurso de uma só vez, reduzindo o número de etapas necessárias para criar uma instância. Além disso, os modelos de execução facilitam a implementação de práticas recomendadas com suporte para instâncias Auto Scaling, Frota spot, spot e sob demanda. Isso ajuda você a gerenciar custos com mais facilidade, melhorar a segurança e minimizar o risco de erros de implantação.  
  
O modelo de execução contém informações que o Amazon EC2 precisa para executar uma instância, como AMI e tipo de instância. O grupo Auto Scaling faz referência a isso para adicionar novas instâncias quando ocorre o evento Scaling out. Se você precisar alterar a configuração das instâncias do EC2 para serem executadas em um grupo Auto Scaling, você poderá criar uma nova versão do modelo de inicialização e atribuí-la ao grupo Auto Scaling Opcionalmente, você pode selecionar uma versão específica do modelo de inicialização que o grupo Auto Scaling usa para executar instâncias do EC2. Você pode alterar essa configuração a qualquer momento.  
  
----
  
# Criando Grupos de Segurança  
{{% notice note %}}
Antes de criar um modelo de execução, vamos criar um security group que será usado pelas instâncias criadas pelo modelo de inicialização.  
{{% /notice %}}
  
1. No console do EC2, selecione**Rede e Segurança**Khan**Grupos de Segurança**no canto superior direito, selecione**Criar grupo de segurança**Clique em.  
![gid-ec2-43](/images/compute/gid-ec2-43.png)
  
2. Na tela Criar Grupo de Segurança, preencha o seguinte:  
![gid-ec2-44](/images/compute/gid-ec2-44.png)
  
| Chaves | Valores |  
|—|—|  
| Nome do grupo de segurança | `ASG-WEB-inst-SG` |  
| Descrição | `HTTP Allow` |  
| VPC | `VPC-LAB` |  
  
3. Role para baixo para modificar as regras de entrada.**Adicionar regra**para adicionar a janela Modificar Regras de Entrada e**Tipo**, digite `HTTP`.**Fonte**, digite `ALB` na caixa de pesquisa para procurar o security group criado quando o ALB foi criado. Ao clicar nele,**Configurar um security group para receber somente o tráfego HTTP de entrada dos ALBs**Deixe-me fazer isso.  
![gid-ec2-45](/images/compute/gid-ec2-45.png)
  
| Chaves | Valores |  
|—|—|  
| Tipo | HTTP |  
| Fonte | `Web-ALB-SG` (alterações para o formulário sg-xxxx quando clicado) |  
  
3. As regras de saída deixam as configurações existentes e clique em**Criar grupo de segurança**para criar um grupo de segurança. Isso criou um security group que permite o tráfego somente para conexões HTTP (TCP 80) da Internet para a instância via ALB.  
![gid-ec2-46](/images/compute/gid-ec2-46.png)
  
----
  
# Criando um modelo de inicialização  
1. Conecte-se ao console do EC2, selecione**Modelos de lançamento**, selecione-o e clique em**Criar modelo de lançamento**Clique em.  
![gid-ec2-47](/images/compute/gid-ec2-47.png)
  
2. Vamos prosseguir com a configuração do modelo de inicialização um por um. Primeiro, defina o**Nome do modelo de lançamento** e**Descrição da versão do modelo** como mostrado abaixo e clique em***Marque a caixa***. Marque esta caixa para permitir que o modelo criado seja utilizado pelo Amazon EC2 Auto Scaling.  
![gid-ec2-48](/images/compute/gid-ec2-48.png)
  
| Chaves | Valores |  
|—|—|  
| Nome do modelo de lançamento | `Web` |  
| Descrição da versão do modelo | Modelo de instâncias da Web do Dia da Imersão — somente Web” |  
| Orientação de Auto Scaling |**Forneça orientações para me ajudar a configurar um modelo que eu possa usar com o EC2 Auto Scaling**`Clique na caixa de seleção` |  
  
3. Role para baixo para definir o conteúdo do modelo inicial.**Imagem de máquina da Amazon (AMI)**, localize e defina a AMI (`Web Server v1`) que você criou no laboratório EC2 anterior. Você pode encontrá-lo digitando `Web Server v1` na barra de pesquisa ou role para baixo até a coluna Minha AMI. Em seguida, digite `t2.micro` para o tipo de instância para selecioná-lo. Não teremos acesso SSH porque estamos colocando um servidor web para o serviço. Portanto, você não usa pares de chaves.  
![gid-ec2-49](/images/compute/gid-ec2-49.png)
  
| Chaves | Valores |  
|—|—|  
| AMI | `Servidor Web v1` |  
| Tipo de instância | `t2.micro` |  
  
4. Deixe as outras partes em seus valores padrão, e vamos ver a seção Configurações de Rede. primer**Plataforma de rede**, selecione 'Virtual Private Cloud (VPC) '. Na coluna Security Group, selecionaremos o grupo de segurança que criamos anteriormente digitando `ASG-WEB-inst-SG `na barra de pesquisa.  
![gid-ec2-50](/images/compute/gid-ec2-50.png)
  
| Chaves | Valores |  
|—|—|  
| Plataforma de rede | `Virtual Private Cloud (VPC` |  
| Grupos de segurança | `ASG-WEB-INST-SG` |  
  
5. O armazenamento seguirá os valores padrão sem qualquer configuração. Vamos para baixo e definir tags Instance.**Adicionar tag**e, em seguida, pressione**Chave**para `Name`,**Valor**, digite `Web Instance`. Clique para selecionar “Volume de tag” também.  
![gid-ec2-51](/images/compute/gid-ec2-51.png)
  
| Chaves | Valores |  
|—|—|  
| Chave | `Name` |  
| Valor | `Web Instance` |  
| Tag Volumes | caixa de seleção `click volumes `|  
  
6. Todas as outras configurações são definidas para seus valores padrão e**Criar modelo de lançamento**botão para criar um modelo de inicialização.  
![gid-ec2-52](/images/compute/gid-ec2-52.png)
  
7. Na próxima etapa**Exibir modelo de lançamento**e você verá o modelo de lançamento criado como mostrado abaixo.  
![gid-ec2-53](/images/compute/gid-ec2-53.png)
![gid-ec2-54](/images/compute/gid-ec2-54.png)
  
----
  
## Configurar o grupo de Auto Scaling  
Agora vamos criar um grupo de Auto Scaling.  
  
1. Vá para o console do EC2 e clique em**Grupos de Auto Scaling**Selecione. E**Criar grupo Auto Scaling**botão para*Grupo de Auto Scaling*para criar.  
![gid-ec2-55](/images/compute/gid-ec2-55.png)
  
2.***[Etapa 1: Escolha o modelo de inicialização ou configuração]***, nomeie o grupo Auto Scaling. Vamos especificar `WEB-ASG` aqui. Na coluna Start Template abaixo, selecione `Web`, o modelo que você acabou de criar. As configurações padrão para o modelo inicial são expandidas para baixo. Após a confirmação, canto inferior direito**Próxima**botão.  
![gid-ec2-56](/images/compute/gid-ec2-56.png)
  
| Chaves | Valores |  
|—|—|  
| Nome do grupo de Auto Scaling | `WEB-ASG` |  
| Modelo de inicialização | `Web` |  
  
3.***[Etapa 2: Configurar configurações]***, defina a configuração de rede, deixando as opções e os tipos de instância do Purchasing como seus valores padrão.**VPC**, selecione `VPC-Lab`,**Sub-redes**coluna**`Sub-rede privada A`**com**`Subrede privada C`**Escolha. Quando a configuração estiver concluída**Próxima**botão.  
![gid-ec2-57](/images/compute/gid-ec2-57.png)
  
| Chaves | Valores |  
|—|—|  
| VPC | `VPC-LAB` |  
| Sub-redes | `Subrede privada A`, `Subrede privada C` |  
  
1. Em seguida, prossiga com a configuração do balanceamento de carga. Primeiro, selecione `Anexar a um balanceador de carga existente`. desde**Escolha um grupo-alvo para o balanceador de carga**, selecione o `Web-Tg` que você criou quando criou o ALB. mais baixo**Monitoramento**em**Habilitar a coleta de métricas de grupo no CloudWatch**`caixa de seleção de marcação`. Isso permite que o CloudWatch veja as métricas de grupo (métricas) que permitem ver o status do seu grupo Auto Scaling. No canto inferior direito**Próxima**botão.  
![gid-ec2-58](/images/compute/gid-ec2-58.png)
![gid-ec2-58-1](/images/compute/gid-ec2-58-1.png)
  
| Chaves | Valores |  
|—|—|  
| Ativar balanceamento de carga |**Application Load Balancer ou Network Load Balancer**`Clique na caixa de seleção` |  
| Escolha um grupo-alvo para o seu balanceador de carga | `web-tg` |  
| Monitoramento |**Habilitar a coleta de métricas de grupo no CloudWatch**`Clique na caixa de seleção` |  
  
5. Na etapa Configurar o tamanho do grupo e políticas de escala, você configura a política de escalabilidade para o grupo Auto Scaling.**Tamanho do grupo**Correu**Capacidade desejada**,**Capacidade mínima**como `2`, respectivamente,**Capacidade máxima**é especificado como `4`. Mantenha o número de instâncias como de costume e permita um mínimo de 2 e um máximo de 4 escalonamento por política.  
![gid-ec2-59](/images/compute/gid-ec2-59.png)
  
| Chaves | Valores |  
|—|—|  
| Capacidade desejada | `2` |  
| Capacidade mínima | `2` |  
| Capacidade máxima | `4` |  
  
6. A seção Política de Reconciliação abaixo**Política de escalabilidade de rastreamento de destino**, e selecione**Valor de destino**, digite `30`. Uma política que ajusta o número de instâncias para que a utilização média da CPU seja mantida em 30%. Deixe todas as outras configurações em seu valor padrão e clique no botão**Próxima**botão.  
![gid-ec2-60](/images/compute/gid-ec2-60.png)
  
| Chaves | Valores |  
|—|—|  
| Política de escalonamento de rastreamento de destino | `Selecionar caixa de seleção |  
| Valor alvo | `30` |  
  
7. Deixe a etapa Adicionar notificações no valor padrão.**Próxima**para avançar.  
![gid-ec2-61](/images/compute/gid-ec2-61.png)
  
8. Na etapa Adicionar tags, simplesmente especificaremos a tag de nome.**Adicionar tag**e, em seguida, pressione**Chave**para `Name`,**Valor**, digite `ASG-WEB-instance` e, em seguida, clique em**Próxima**Clique em.  
![gid-ec2-62](/images/compute/gid-ec2-62.png)
  
| Chaves | Valores |  
|—|—|  
| Chave | `Name` |  
| Valor | `ASG-WEB-Instance` |  
  
9. Esta é a etapa final da revisão. Depois de analisar as configurações relevantes, clique em**Criar grupo de Auto Scaling**botão.  
![gid-ec2-63](/images/compute/gid-ec2-63.png)
  
10. O grupo Auto Scaling foi criado. No console Grupos de Auto Scaling, você pode ver os grupos de Auto Scaling criados abaixo.  
![gid-ec2-64](/images/compute/gid-ec2-64.png) 
  
11. Instâncias criadas por meio de grupos de Auto Scaling também podem ser encontradas no menu Instâncias do EC2.  
![gid-ec2-65](/images/compute/gid-ec2-65.png) 
  
----
  
## Arquiteturas até à data  
Agora, construímos um serviço web que é dimensionado automaticamente com base na carga, com alta disponibilidade! O diagrama de configuração dos serviços que criamos é mostrado abaixo.  
![gid-ec2-66](/images/compute/gid-ec2-66.svg) 
  
