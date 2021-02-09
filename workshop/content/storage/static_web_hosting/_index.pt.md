---
date: 2020-06-01
title: "Usando hospedagem de sites estáticos"  
weight: 440
pre: "<b>4-4. </b>"
---
  
{{% notice note %}}
Você pode usar o Amazon S3 para hospedar sites estáticos.  
{{% /notice %}}
  
----
  
## Configurando um site estático  
{{% notice info %}}
Um site estático refere-se a um site que contém apenas conteúdo estático (HTML, imagens, vídeos) ou scripts do lado do cliente (Javascript) em uma página web.  
Em contraste, sites dinâmicos exigem processamento no lado do servidor, incluindo scripts do lado do servidor, como PHP, JSP ou ASP.NET. O Amazon S3 não oferece suporte a scripts no lado do servidor. Se você quiser hospedar um site dinâmico, você pode usar outros serviços, como o EC2 na AWS.  
{{% /notice %}}
  
1. No console do S3, selecione o bucket que você acabou de criar, clique em**Propriedades**guia. Role para baixo**Hospedagem de site estática**Clique no botão Editar.  
![gid-s3-22](/images/s3/gid-s3-22.png)
![gid-s3-22](/images/s3/gid-s3-22-1.png) 
  
2. Ativar hospedagem de sites estáticos, selecione um tipo de hospedagem, insira o valor ``index.html`` no valor do documento de índice e clique em**salvar alterações**botão.  
![gid-s3-22](/images/s3/gid-s3-23.png) 
  
3.**Hospedagem de site estática**criado no item**Ponto de extremidade do site do bucket**para acessar o site estático.  
![gid-s3-22](/images/s3/gid-s3-23-1.png) 
  
4. A conexão é boa. Você pode usar o Amazon S3 para hospedar seu site estático.  
![gid-s3-22](/images/s3/gid-s3-24.png) 
  
