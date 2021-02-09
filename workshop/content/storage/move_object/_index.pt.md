---
date: 2020-06-01
title: "Mover objetos"  
weight: 450
pre: "<b>4-5. </b>"
---
  
{{% notice note %}}
No processo até agora, identificamos a capacidade de adicionar objetos a um bucket e verificá-los. Agora, vamos ver a capacidade de mover um objeto para outro bucket ou pasta.  
{{% /notice %}}
  
----
  
## Mover objetos  
  
1. Crie um bucket temporário para mover objetos entre intervalos. (Nome do bucket: `Nome do bucket existente-TEMP`)  
Para configuração rápida**Bloquear todo o acesso público*****Desativar a caixa de seleção***Por favor.  
![gid-s3-25](/images/s3/gid-s3-25.png) 
  
2. abaixo**Painel de notificação de check-in**,**Criar bucket**Por favor selecione  
![gid-s3-26](/images/s3/gid-s3-26.png) 
  
3. No console do Amazon S3, selecione o bucket no qual o objeto reside (o bucket criado pela primeira vez) e clique na caixa de seleção do objeto que você deseja mover. início**Ações**menu para ver as várias funções que podem ser executadas nesse objeto. Entre os recursos listados**Mover**Selecione.  
![gid-s3-27](/images/s3/gid-s3-27.png) 
  
4. Selecione o destino como o bucket como mostrado abaixo e clique no botão Procurar S3.  
![gid-s3-28](/images/s3/gid-s3-28.png) 
  
5. Na janela pop-up, clique no nome do bucket e selecione o intervalo de destino (chegada).**Escolha o destino**botão.  
![gid-s3-29](/images/s3/gid-s3-29.png) 
![gid-s3-29](/images/s3/gid-s3-29-1.png) 
  
6. Observe que o objeto foi movido no bucket de destino.  
![gid-s3-30](/images/s3/gid-s3-30.png) 
  
{{% notice tip %}}
Quando você move um objeto, as permissões existentes são mantidas.  
{{% /notice %}}
