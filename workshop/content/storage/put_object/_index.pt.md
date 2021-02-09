---
date: 2020-06-01
title: "Adicionando objetos a um bucket"  
weight: 420
pre: "<b>4-2. </b>"
---
  
{{% notice note %}}
Se o bucket foi criado com sucesso, você estará pronto para adicionar os objetos. Um objeto pode ser qualquer tipo de arquivo, incluindo arquivos de texto, arquivos de imagem e arquivos de vídeo. Ao adicionar arquivos ao Amazon S3, você pode incluir informações sobre permissões e configurações de acesso para esses arquivos nos metadados.  
{{% /notice %}}
  
----
  
## Adicionando objetos para hospedagem na Web estática  
Neste laboratório, você hospedará um site estático via S3. O site estático atua como redirecionamento para uma instância criada no laboratório da VPC quando você clica em uma imagem específica. Então, prepare um arquivo de imagem, um arquivo HTML e um nome DNS ALB.  
  
  
  
2. Escreva `index.html` usando o código-fonte abaixo.  
```html  
<html>  
<head>  
<meta charset="utf-8">  
<title> Feriados AWS General Immersion Day S3 </title>  
</head>  
<body>  
<center>  
<br>  
<h2> Clique na imagem a ser redirecionada para a instância do EC2 que você criou </h2>  
<img src="S3에 업로드될 이미지 접근 URL" onclick="window.location='DNS 이름'"/>  
</center>  
</body>  
</html>  
```  
  
3. Carregue o arquivo `aws.png` para o S3. Eu acabei de criar***Balde S3***para**clicando**.  
![gid-s3-05](/images/s3/gid-s3-05.png) 
  
4.**Upload**botão e clique**Adicionar arquivos**botão. Selecione o arquivo `aws.png` que você baixou antecipadamente através do File Explorer. Alternativamente, arraste e solte o arquivo na tela.  
![gid-s3-06](/images/s3/gid-s3-06.png) 
  
5.**Upload**botão e clique**Adicionar arquivos**botão.  
![gid-s3-07](/images/s3/gid-s3-07.png) 
  
6. informações de arquivo para carregar `aws.png`**Verificar arquivo**no canto inferior esquerdo e, em seguida, clique em**Upload**Clique no botão para carregá-lo.  
![gid-s3-08](/images/s3/gid-s3-08.png) 
![gid-s3-08](/images/s3/gid-s3-08-1.png)
  
7. Verifique as informações de URL para preencher o URL da imagem em `index.html`. Selecione o arquivo `aws.png` carregado e clique em***URL do objeto***Copie as informações.  
![gid-s3-09](/images/s3/gid-s3-09.png) 
  
  
![gid-s3-10](/images/s3/gid-s3-10.png) 
  
9. Carregue o arquivo `index.html` para o S3 assim como você carregou a imagem.  
![gid-s3-11](/images/s3/gid-s3-11.png) 
  
10. Quando você vê a imagem carregada, ela se parece com isto:  
![gid-s3-12](/images/s3/gid-s3-12.png) 
