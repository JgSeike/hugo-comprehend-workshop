---
date: 2020-06-01
title: "Exibindo Objetos"  
weight: 430
pre: "<b>4-3. </b>"
---
  
{{% notice note %}}
Depois de adicionar objetos ao seu bucket, vamos vê-los em um navegador da Web.  
{{% /notice %}}
  
----
  
## Exibindo Objetos  
  
1. No console do Amazon S3, consulte***Clique em um objeto***Por favor. Você pode verificar os detalhes do objeto como mostrado abaixo.  
![gid-s3-13](/images/s3/gid-s3-13.png) 
  
{{% notice info %}}
Por padrão, todos os objetos em um bucket do S3 são Somente Proprietário (Privado).  
***https://{Bucket}.s3. {region} .amazonaws.com/ {Objeto}***para resolver o objeto por meio de um URL de um tipo como***lendo***permissão. Como alternativa, você pode criar um URL assinado baseado em assinatura para esse objeto que contém informações de autenticação, permitindo que usuários não autorizados acessem esse objeto temporariamente.  
{{% /notice %}}
  
2. Volte para a página anterior e clique em**Permissões**guia.**Bloquear acesso público (configurações de bucket)**, pressione o botão Editar no lado direito.  
![gid-s3-14](/images/s3/gid-s3-14.png) 
  
3. Topo**Desmarque a caixa**e**Salvar alterações**botão.  
![gid-s3-15](/images/s3/gid-s3-15.png) 
  
4. Na janela pop-up Editar Bloco de Acesso Público do Bucket, digite `confirm` e**Confirmar**botão.  
![gid-s3-16](/images/s3/gid-s3-16.png) 
  
5.**Objetos**, clique no botão**Selecionar arquivos**depois**Ação**botão suspenso, clique em**Tornar público**botão para configurá-lo público.  
![gid-s3-17](/images/s3/gid-s3-17.png) 
  
6. Quando a janela de confirmação aparecer, clique em**Tornar público**botão para confirmar.  
![gid-s3-18](/images/s3/gid-s3-18.png) 
  
7. Volte para a página do bucket, selecione index.html e selecione***URL do objeto***Clique no link.  
![gid-s3-19](/images/s3/gid-s3-19.png) 
  
8. Quando você acessa a URL do objeto de arquivo de objeto HTML, a tela a seguir será exibida.  
![gid-s3-20](/images/s3/gid-s3-20.png) 
  
9. Quando você clica na imagem, você será redirecionado para a página da instância criada.  
![gid-s3-21](/images/s3/gid-s3-21.png) 
