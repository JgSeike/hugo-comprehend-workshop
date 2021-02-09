---
date: 2020-06-01
title: "Ativar versionamento de bucket"  
weight: 460
pre: "<b>4-6. </b>"
---
  
{{% notice note %}}
Se você quiser atualizar um arquivo existente para a versão mais recente dentro do mesmo intervalo, mas quiser manter a versão existente também***Versionamento do bucket***pode ser usado.  
{{% /notice %}}
  
----
  
## Ativar versionamento  
  
1. No console do Amazon S3, selecione o bucket para o qual você deseja habilitar o controle de versão e clique em**Propriedades**Por favor, selecione o menu.**Versionamento do bucket**Clique no botão Editar.  
![gid-s3-31](/images/s3/gid-s3-31.png)
**Versionamento do bucket**Clique sobre o botão de rádio da função da possibilidade,**salvar alterações**Clique em.  
![gid-s3-31](/images/s3/gid-s3-32.png)  
  
2. Selecione um arquivo editável e clique em***Salve algumas modificações no arquivo original com o controle de versão ativado***e carregue os arquivos modificados de volta para o seu bucket. Neste laboratório, você irá modificar o arquivo `index.html`` e re-carregá-lo com o mesmo nome.  
  
3. Quando terminar de carregar o arquivo alterado, clique no objeto no console do S3. Clique na guia **Versões** na página que contém os detalhes do objeto,***versão atual***Você pode verificar as informações.  
![gid-s3-33](/images/s3/gid-s3-33.png) 