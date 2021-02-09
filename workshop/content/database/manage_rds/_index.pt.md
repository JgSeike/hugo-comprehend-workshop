---
date: 2020-06-01
title: "Recursos de gerenciamento do RDS"  
weight: 350
pre: "<b>3-5. </b>"
---
  
{{% notice note %}}
Em implantações Multi-AZ, o Amazon RDS provisiona e mantém automaticamente uma réplica em espera síncrona em diferentes zonas de disponibilidade. A instância de banco de dados principal é sincronizada com a espera na zona de disponibilidade para fornecer redundância de dados  
{{% /notice %}}
  
----
  
## Teste de failover de RDS  
{{% notice info %}}
Quando o Multi-AZ estiver habilitado, se uma instância de banco de dados encontrar uma interrupção planejada ou não planejada, o Amazon RDS alterna automaticamente para uma espera em uma zona de disponibilidade diferente. O tempo necessário para que um failover seja concluído depende da atividade do banco de dados e de outras condições quando a instância de banco de dados principal fica indisponível. O failover normalmente leva 60-120 segundos. No entanto, se a transação for grande ou o processo de recuperação for complexo, o tempo de failover pode aumentar. Após a conclusão do failover, a interface do usuário do console do RDS levará mais tempo para refletir na nova Zona de Disponibilidade.  
{{% /notice %}}
  
1. A partir do Console de Gerenciamento do RDS**bancos de dados**, selecione a instância para a qual você deseja fazer failover e clique em**Failover**Clique em.  
![gid-rds-50](/images/rds/gid-rds-50.png) 
  
2. Surge a pergunta se você deseja fazer failover do cluster?**Failover**botão.  
![gid-rds-51](/images/rds/gid-rds-51.png) 
  
3.**Atualizar**botão, o identificador de banco de dados**rdscluster**tem um status de**Failing-over**vai mudar para.  
![gid-rds-51-1](/images/rds/gid-rds-51-1.png) 
  
4. Depois de um tempo**Atualizar**botão, o**As funções do leitor e as funções do Writer foram alteradas**, que você pode ver. Failover concluído.  
![gid-rds-51-2](/images/rds/gid-rds-51-2.png) 
  
----
  
## Criando Snapshots do RDS  
  
{{% notice info %}}
Vou criar um Snapshot para um RDS em execução. Os snapshots podem ser criados a qualquer momento de sua escolha para fazer backup de uma instância de banco de dados e você pode restaurar um banco de dados com base no Snapshot criado a qualquer momento.  
{{% /notice %}}
  
1. A partir do Console de Gerenciamento do RDS**bancos de dados**para executar a operação de snapshot e selecionar**Selecionar uma instância**. Cima Direita**Ações**->**Tirar instantâneo**Selecione.  
![gid-rds-51-3](/images/rds/gid-rds-51-3.png) 
  
2. Digite o nome `immersionday-snapshot` para o instantâneo.**Tirar Snapshot**botão para concluir a criação.  
![gid-rds-52](/images/rds/gid-rds-52.png) 
  
3. Selecione Snapshots no menu RDS esquerdo e verifique o status de criação dos Snapshots. O estado do snapshot é o primeiro***criando***estado, e***disponível***, você pode usar esse snapshot para restaurar o banco de dados.  
![gid-rds-53](/images/rds/gid-rds-53.png) 
  
4. Para restaurar, selecione o snapshot desejado e selecione **Ações** para ver o que você pode fazer com esse snapshot. **Restaurar Snapshot** permite que você crie uma instância do RDS com os mesmos dados com base no snapshot obtido.***Neste laboratório, você não executará uma restauração.***  
![gid-rds-54](/images/rds/gid-rds-54.png) 
  
----
  
## Alterações na especificação da instância do RDS  
{{% notice info %}}
Aumentar e diminuir a capacidade de uma instância do RDS ativa (Scale-Up/Scale-Down) pode ser feito de forma muito simples através do Console de Gerenciamento do RDS.  
{{% /notice %}}
  
1. mudança**Selecionar uma instância**e**Modificar**para alterar as dimensões da instância do RDS.  
![gid-rds-55](/images/rds/gid-rds-55.png) 
  
3. A primeira entrada,***Especificações da instância***em**Classes de**Você pode selecionar a especificação da instância que deseja alterar marcando a caixa de listagem. Aqui.**db.t3.medium**Vamos selecionar  
![gid-rds-56](/images/rds/gid-rds-56.png) 
  
1. Role para baixo até a parte inferior e selecione**Continuar**, você pode escolher o tamanho da instância e quando aplicar antes e depois da alteração, conforme mostrado abaixo.  
![gid-rds-57](/images/rds/gid-rds-57.png) 
  
1.**Aplicar imediatamente**Selecione. Nesse caso, você altera imediatamente a instância do RDS depois de executar um backup para o RDS. E**Modificar instância de banco**botão. Dependendo do tipo de instância e da quantidade de dados para fazer backup, pode levar vários minutos. Consequentemente, você deve esperar uma interrupção do serviço RDS por algum tempo. (A configuração de redundância minimiza o tempo de inatividade.)  
![gid-rds-58](/images/rds/gid-rds-58.png) 
**Aplicar durante a próxima janela de manutenção programada**, a alteração é feita na Janela de Manutenção do usuário especificado semanalmente.  
  
1. Se o status da instância for***Modificando***e você pode ver que ele mudou para  
![gid-rds-59](/images/rds/gid-rds-59.png) 
  
1. Se você clicar em Atualizar novamente, você verá que a instância do Writer foi alterada. Isso ocorre porque a instância selecionada para redimensionamento era uma instância do Writer. O RDS garante que o tempo de inatividade seja minimizado por meio de failover antes de uma operação de redimensionamento.  
![gid-rds-60](/images/rds/gid-rds-60.png) 
  
2. Se você esperar por um tempo,***Disponível***Você pode ver que a mudança para o estado está completa.  
![gid-rds-61](/images/rds/gid-rds-61.png) 
  
{{% notice warning %}}
O RDS pode alterar o tamanho de uma instância a qualquer momento. No entanto, o tamanho do banco de dados não oferece suporte ao encolhimento após o dimensionamento.  
{{% /notice %}}
  
