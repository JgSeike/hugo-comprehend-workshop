---
date: 2020-06-30
title: "Criando uma VPC"  
weight: 110
pre: "<b>1-1. </b>"
---
  
{{% notice note %}}
**O Amazon Virtual Private Cloud (Amazon VPC) usa uma rede virtual que você define** para começar a usar seus recursos da AWS.  
Essa rede virtual é muito semelhante a uma rede tradicional operando em seu próprio data center, com os benefícios de usar a infraestrutura escalável da AWS.  
{{% /notice %}}
  
----
  
## Ir para o serviço VPC  
1. Faça login no Console de Gerenciamento da AWS e selecione **VPC**.  
![GID-VPC-service](/images/network/gid-network-02.png)
  
{{% notice tip %}}
 **Se a tela abaixo estiver diferente da sua**, clique no canto superior esquerdo da tela para **Ativar a nova experiência da VPC**.  
![gid-VPC-new-experience](/images/network/gid-network-03.png)
{{% /notice %}}
  
----
  
## Criar um Elastic IP  
1. No menu esquerdo do painel da VPC, clique em **IP elástico (IP elástico)** 
![gid-network-04](/images/network/gid-network-04.png)
  
1. Clique em **Alocar endereço IP elástico (atribuir novo endereço)**. Isso deve ser criado antes para podermos usa-lo ao criar o gateway NAT que será criado por meio do VPC Wizard
![gid-network-05](/images/network/gid-network-05.png)
  
1. Um IP elástico (IP) é um endereço IPv4 estático projetado para computação em nuvem dinâmica usado para mascarar a falha de uma instância ou software remapeando rapidamente o endereço para outra instância na conta. Por ser um IP público, é um IP acessível externamente. Para criar um IP público fixo para uso com o Gateway NAT, clique em **Alocar**
![gid-network-06](/images/network/gid-network-06.png)
  
4. Você pode ver o novo Elastic IP atribuído à sua conta.  
![gid-network-07](/images/network/gid-network-07.png)
  
----
  
## Criando uma VPC com o Assistente de VPC 
1.No **Painel de controle da VPC** selecione **Launch VPC Wizard** para iniciar o assistente VPC.  
![gid-network-08](/images/network/gid-network-08.png)
  
2.***Etapa 1: selecione uma configuração de VPC***, selecione a segunda opção,**VPC com sub-redes públicas e privadas**. O assistente da VPC cria automaticamente um gateway NAT para que as instâncias do EC2 na sub-rede privada possam acessar a Internet, conforme mostrado na tela. Vamos discutir NAT Gateway com mais detalhes mais tarde.  
![gid-network-09](/images/network/gid-network-09.png)
  
3.***Etapa 2: VPC com sub-redes públicas e privadas***, defina o valores das chaves conforme o exemplo abaixo.

As **sub-redes públicas** são sub-redes que possuem um IP público atribuído às instâncias de EC2 para que possam ter acesso de entrada e saída à Internet através do Internet Gateway, e as **sub-redes privadas** são sub-redes sem IP público atribuído mas possuem acesso de saída à Internet via Gateway NAT.  

Para especificar um Elastic IP e atribui-lo a um gateway NAT selecione **ID de alocação de IP elástico**.Escolha o ID de alocação do Elastic IP criado para o gateway NAT na introdução do laboratório. Quando todas as configurações estiverem concluídas, clique em **Criar VPC**.  
  
    ![gid-network-10](/images/network/gid-network-10.png)
  
| Chaves | Valores |  
|—|—|  
| Bloco CIDR IPv4 | `10.0.0.0/16` |  
| Nome da VPC | `VPC-Lab` |  
| IPv4 CIDR da sub-rede pública | `10.0.10.0/24` |  
| Zona de disponibilidade | `ap-northeast-2a` |  
| Nome da sub-rede pública | `Sub-rede pública A` |  
| IPv4 CIDR IPv4 de sub-rede privada | `10.0.100.0/24` |  
| Zona de disponibilidade | `ap-northeast-2a` |  
| Nome da sub-rede privada | `Subrede privada A` |  
  
1. O assistente de criação de VPC cria automaticamente sub-redes e gateways NAT. (Pode levar alguns minutos para que a criação seja concluída.)  
![gid-network-11](/images/network/gid-network-11.png)
  
5. Quando a criação estiver concluída, clique em **OK**.  
![gid-network-12](/images/network/gid-network-12.png)
  
----
  
## Arquitetura até agora  
Se sua VPC foi concluída por meio do assistente de VPC, o ambiente configurado até o momento é o seguinte:  
![gid-network-13](/images/network/gid-network-13.svg)