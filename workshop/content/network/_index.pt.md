---
date: 2020-06-01
title: "Rede - Amazon VPC"  
weight: 100
pre: "<b>1. </b>"
---
  
{{% notice note %}}
Neste laboratório, criaremos uma sub-rede pública e uma sub-rede privada em duas zonas de disponibilidades diferentes (AZ-A, AZ-C) e configuraremos um gateway NAT em uma sub-rede pública.  
Estabeleceremos então uma tabela de rotas para definir o fluxo do tráfego. Isso conclui a configuração básica de rede para criar um ambiente de serviços Web altamente disponível e escalável no futuro.  
{{% /notice %}}
  
{{% notice info %}}
As imagens inseridas nos documentos do laboratório são criadas para ajudar com o laboratório. O  ***Identificador (ID)*** de cadaelemento criado durante o laboratório (como VPC, NAT Gateway e EIP)podem aparecer de forma diferente para contas de usuário diferentes.   
{{% /notice %}}
  
----
  
## Diagrama  
O diagrama final que gostaríamos de construir através deste laboratório é o seguinte.  
![GID-Network-DG](/images/network/gid-network-01.svg)
  
----
  
## Ordem do laboratório  
Este laboratório está na seguinte ordem:  
  
[1. Criando uma VPC](./create_vpc)  
[2. Criar sub-redes adicionais](./create_subnet)  
[3. Modificando tabelas de rota](./modify_route)
  
  
  
  
  
