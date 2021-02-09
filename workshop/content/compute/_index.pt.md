---
date: 2020-06-01
title: "Computação — Amazon EC2"  
weight: 200
pre: "<b>2. </b>"
---
  
{{% notice note %}}
Amazon Elastic Compute Cloud (Amazon EC2) é um serviço da web que fornece poder de computação escalável e seguro na nuvem. A interface de serviço da web simples do Amazon EC2 torna mais fácil obter e configurar a capacidade de que você precisa. Fornece controle abrangente sobre seus recursos de computação e pode ser executado no ambiente de computação comprovado da Amazon.
{{% /notice %}}
  
----
  
## Diagrama
Este laboratório de computação implanta instâncias de serviço da Web usando o grupo Auto Scaling nas sub-redes privadas dentro do VPC criado no laboratório de rede acima. Por meio disso, um serviço da web que garante alta disponibilidade é configurado para que usuários externos possam acessar a página da web de amostra por meio de um navegador da web.  
![gid-ec2-01](/images/compute/gid-ec2-01.svg)
  
  
Este laboratório contém o seguinte conteúdo:  
- Lançamento de instâncias de um servidor web e execução de dados do usuário
- Configurações do Grupo de Segurança  
- Criar uma imagem de máquina da Amazon (AMI) personalizada  
- Criar Application Load Balancer (ALB)  
- Configuração da configuração de configuração do lançamento  
- Configurar o grupo de Auto Scaling  
- Teste o Auto Scaling e altere as configurações manuais  
  
----
  
## Ordem do laboratório  
[2-1. Início da instância do servidor web](./launching)  
[2-2. Implantar serviço Web de escalonamento automático ](./auto_scaling)  
[2-3. Verificação e teste do serviço Web](./test_service)  
[2-4. Apêndice - Conceitos adicionais do EC2](./appendix)  
  
{{% notice tip %}}
Este Guia de Laboratório foi escrito com base no AWS Management Console em inglês. Certifique-se de que a guia **Nova experiência EC2** no canto superior esquerdo do painel EC2 esteja habilitada.  
{{% /notice %}}
![gid-ec2-02](/images/compute/gid-ec2-02.png)
  
  
  
  
  
