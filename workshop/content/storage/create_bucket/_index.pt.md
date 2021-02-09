---
date: 2020-06-01
title: "Criar um bucket no S3"  
weight: 410
pre: "<b>4-1. </b>"
---
  
{{% notice note %}}
Todos os objetos no Amazon S3 são armazenados em um bucket. Você deve criar um bucket antes de armazenar seus dados no Amazon S3.  
{{% /notice %}}
  
----
  
## Criar Bucket  
  
  
![gid-s3-01](/images/s3/gid-s3-01.png) 
  
2.**Criar bucket**para criar o bucket.  
![gid-s3-02](/images/s3/gid-s3-02.png) 
  
3.***Nome do bucket***, insira um nome de bucket exclusivo. Neste laboratório, insira `immersion-day-labs username` para prosseguir.***O nome do bucket inserido não pode ser duplicado e exclusivo no Amazon S3***Deve. Crie um nome de bucket exclusivo que reflita o nome da sua organização ou nome de usuário, etc.**Região**Na caixa suspensa, especifique a região na qual você deseja criar o bucket. Neste laboratório,**Ásia-Pacífico (Seul)**Selecione. As configurações de bucket para Bloquear Acesso Público usam o valor padrão e**Criar bucket**Por favor selecione  
![gid-s3-03](/images/s3/gid-s3-03.png) 
  
Os nomes de bucket devem estar em conformidade com as seguintes regras:  
> - letras minúsculas, números, pontos (.) E você pode incluir um traço (-).  
> - Deve começar com um número ou letra  
> - Pode ter um mínimo de 3 caracteres e um máximo de 255 caracteres.  
> - Não pode ser especificado no mesmo formato que o endereço IP. (por exemplo, 265.255.5.4)  
  
{{% notice tip %}}
Dependendo da região em que o bucket é criado, pode haver restrições adicionais. O nome do bucket não pode ser alterado depois de criado e é incluído no URL para especificar os objetos armazenados no bucket. Certifique-se de que o intervalo que você deseja criar seja nomeado adequadamente.  
{{% /notice %}}
  
4. Um bucket foi criado no Amazon S3.  
![gid-s3-04](/images/s3/gid-s3-04.png) 
  
{{% notice tip %}}
Criar um bucket sozinho não cobra você. Você só é cobrado pelo armazenamento de um Objeto em um Bucket, transferir um Objeto para um bucket ou enviá-lo para fora da caixa.  
{{% /notice %}}
  
