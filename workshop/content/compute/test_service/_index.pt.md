---
date: 2020-06-01
title: "Verificar e testar serviços da Web"  
weight: 230
pre: "<b>2-3. </b>"
---
  
{{% notice note %}}
Agora, vamos testar se o serviço que você configurou está funcionando corretamente. Primeiro, vamos certificar-se de que o site é acessível normalmente e que o balanceador de carga está funcionando e, em seguida, carregar o servidor web para ver se Auto Scaling funciona.  
{{% /notice %}}
  
----
  
## Verificar o comportamento do serviço Web e do balanceador de carga  
1. Para se conectar por meio do Application Load Balancer configurado para o seu serviço Web, clique no menu 'Load Balancers** no console do EC2 e selecione o `Web-Albs' que você criou anteriormente. Está aqui a configuração padrão de***Nome DNS***Copie o arquivo.  
![gid-ec2-67](/images/compute/gid-ec2-67.png) 
  
2. Abra uma nova guia no seu navegador e***Nome DNS copiado***Cole o. Você pode ver este serviço web trabalhando no laboratório do EC2 como mostrado abaixo. Para a imagem abaixo***ap-northeast-2a***que você está atendendo a página da web.  
![gid-ec2-68](/images/compute/gid-ec2-68.png) 
  
3. Se você pressionar o botão de atualização aqui, o host que serve a página da Web como mostrado abaixo***Instâncias em outras zonas de disponibilidade***(ap-northeast-2c). Isto significa que o algoritmo de roteamento do grupo-alvo ALB é à revelia*Rodada Robin*porque ele se comporta no caminho.  
![gid-ec2-69](/images/compute/gid-ec2-69.png) 
  
4. Atualmente, o grupo Auto Scaling tem 30% de utilização da CPU para cada instância definida como um destino de escalabilidade.  
- a média das instâncias***A utilização da CPU é inferior a 30%***Se**Reduza o número de instâncias e**,  
- a média das instâncias***A utilização da CPU é de pelo menos 30%***,**Distribuir a carga, colocando uma instância**de**instâncias para ter uma utilização média de CPU de 30%**A política de reconciliação funciona.  
  
5. Agora vamos realmente dar uma carga para ver se Auto Scaling funciona bem. Na página da web acima,**TESTE DE CARGA**Clique no menu. A tela muda e a carga exercida é visível. Você pode ver que cada instância está sob carga clicando no logotipo no canto superior esquerdo da página.  
- Antes que a carga ocorra,  
   ![gid-ec2-70](/images/compute/gid-ec2-70.png)
- Após a carga ocorrer,  
   ![gid-ec2-70-1](/images/compute/gid-ec2-70-1.png)
  
{{% notice tip %}}
O princípio da criação de carga da CPU é que, se o valor da CPU Idle estiver acima de 50, o código PHP se comportará em um ciclo de cinco segundos para criar, comprimir e descomprimir arquivos arbitrários. Como o tráfego é distribuído pelos ALBs, a carga continuará sob carga em outras instâncias.  
{{% /notice %}}
  
6. No console do EC2, selecione**Grupos de Auto Scaling**entrar em,**Monitoramento**ab. por baixo**Métricas habilitadas**em**EC2**e pressione o prazo certo**1 hora**Defina para. Se você esperar por um tempo**Utilização da CPU (Percentual)**Você pode ver que o gráfico está mudando.  
![gid-ec2-71](/images/compute/gid-ec2-71.png)
  
7. Aguarde cerca de 5 minutos (300 segundos)**Atividade**, você verá o posicionamento de instâncias do EC2 adicionais com base na política de escalabilidade.  
![gid-ec2-72](/images/compute/gid-ec2-72.png)
  
8.**Gerenciamento de instâncias**, você pode ver que há duas instâncias adicionais e um total de quatro instâncias estão em execução.  
![gid-ec2-73](/images/compute/gid-ec2-73.png)
  
9. Se você acessar e atualizar uma página da Web usando o DNS ALB que copiou anteriormente, verá que está hospedando uma página da Web em duas instâncias que você não tinha. Como esta é uma instância recém-criada, a carga atual da CPU é 0%. Você também pode ver que cada um foi criado em uma zona de disponibilidade diferente. Se não for 0%, pode parecer ser mais do que 100% porque a carga ainda está ocorrendo.  
![gid-ec2-74](/images/compute/gid-ec2-74.png)
  
Até este ponto, o teste de carga do serviço Web confirma que o grupo Auto Scaling está funcionando. Se a página que causa a carga da CPU estiver em execução, feche a tela para evitar carga adicional.  
  
----
  
## Dimensionamento manualmente  
  
{{% notice note %}}
Agora, ajustaremos manualmente as opções de escala para que apenas uma instância permaneça no Grupo Auto Scaling.  
{{% /notice %}}
  
1. No lado esquerdo da consola EC2**Grupos de Auto Scaling**Clique em. Depois disso, acabamos de criar o nome dos Grupos de Auto Scaling, clique em `WEB-ASG`.  
![gid-ec2-75](/images/compute/gid-ec2-75.png)
  
2. Em Detalhes do grupo, o direito**Editar**botão.  
![gid-ec2-76](/images/compute/gid-ec2-76.png)
  
3. Na janela Editar WEB-ASG**Capacidade desejada**com**Capacidade mínima**,**Capacidade máxima**para `1`,**Atualizar**botão.  
![gid-ec2-77](/images/compute/gid-ec2-77.png)
  
4. As configurações atualizadas foram aplicadas.  
![gid-ec2-78](/images/compute/gid-ec2-78.png)
  
5.**Atividade**, você pode ver que as instâncias estão Drenando de ALBs para corresponder à capacidade desejada. Levará alguns minutos para que a drenagem real seja concluída.  
![gid-ec2-79](/images/compute/gid-ec2-79.png)
  
6. Depois que a operação de drenagem da instância for concluída no ALB, você pode usar**Atividade**foi alterada.  
![gid-ec2-82](/images/compute/gid-ec2-82.png)
  
7.**Gerenciamento de instâncias**e você verá que há apenas uma instância restante.  
![gid-ec2-83](/images/compute/gid-ec2-83.png)
  
8. Você também pode verificá-lo no menu **Instâncias**.***encerrado***Você pode ver quais instâncias foram e 1 instâncias restantes.  
![gid-ec2-80](/images/compute/gid-ec2-80.png)
  
{{% notice info %}}
Mais tarde, no laboratório de banco de dados, se você criar uma AMI com a configuração que concluiu a conexão do aplicativo Web e o banco de dados, alteraremos a contagem de instâncias de volta para ser escalável para mais de dois.  
Mais tarde, no laboratório de banco de dados, se você criar uma AMI com a configuração que concluiu a conexão do aplicativo Web e o banco de dados, alteraremos a contagem de instâncias de volta para ser escalável para mais de dois.  
{{% /notice %}}
  
