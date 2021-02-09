---
date: 2020-06-30
title: "Criando sub-redes adicionais"  
weight: 120
pre: "<b>1-2. </b>"
---
  
{{% notice note %}}
Para configurar serviços de rede com alta disponibilidade e tolerantes a falhas, usaremos a **zona de disponibilidade C (AZ C)** em uma VPC. Vamos adicionar mais uma sub-rede pública e privada, e configurar uma tabela de rotas.  
{{% /notice %}}
  
----
  
## Gerar uma sub-rede pública em uma outra Zona de Disponibilidade
1. No lado esquerdo do console da VPC em **Sub-rede**, clique em **Criar sub-rede**.  
![gid-network-14](/images/network/gid-network-14.png)
  
2.**Criar sub-rede**, especifique a tag de nome, VPC, zona de disponibilidade e bloco CIDR IPv4 como os valores abaixo e clique no botão **Criar** e crie a ` sub-rede Publica C`.  
  
| Chaves | Valores |  
|—|—|  
 VPC ID | `VPC-Lab`. |  
| Nome da sub-rede | `Sub-rede publica C` |  
| Zona de disponibilidade | `sa-east-1c` |  
| Bloco CIDR IPv4 | `10.0.20.0/24` |  
  
    ![gid-network-15](/images/network/gid-network-15.png)  
    ![gid-network-15](/images/network/gid-network-15-1.png)  
  
1. `Sub-rede publica C` foi criado.  
![gid-network-16](/images/network/gid-network-16.png)  
  
----
  
#### Gerar uma sub-rede privada em uma outra Zona de Disponibilidade 
1. Para criar mais uma sub-rede privada,vá em **Criar sub-rede**.  
e especifique o valores abaixo,clique em **Criar** para a`sub-net Privada C`.  
  
| Chaves | Valores |  
|—|—|  
 VPC ID |  `VPC-Lab`. |  
| Nome da sub-rede | `Subrede privada C` |  
| Zona de disponibilidade | `sa-east-1c` |  
| Bloco CIDR IPv4 | `10.0.200.0/24` |  
  
    ![gid-network-17](/images/network/gid-network-17.png)  
  
1. `Subrede privada C` foi criada.  
![gid-network-18](/images/network/gid-network-18.png)  
  
----
  
## Verificar sub-redes geradas  
1. 
![gid-network-19](/images/network/gid-network-19.png)  
  
----
  
## Arquiteturas até agora 
O ambiente configurado atualmente para as sub-redes adicionadas é o seguinte:  
![gid-network-34](/images/network/gid-network-34.svg)