---
date: 2020-06-30
title: "Modificando tabelas de rota"  
weight: 130
pre: "<b>1-3. </b>"
---
  
{{% notice note %}}
vá em **Tabela de roteamento** para exibir todas as tabelas de roteamento criadas, você pode alterar a tabela de roteamento ou associar uma sub-rede a essa tabela. Nesse caso, associaremos a tabela de roteamento apropriada para as duas sub-redes recém-criadas.  
{{% /notice %}}
  
----
  
##  Modificando tabelas de rota na **Sub-redes públicas** 
  
1. Clique em **tabelas de roteamento** no lado esquerdo do menu. Depois Clique na barra de pesquisa e selecione **VPC**  em seguida selecione o ***ID DO VPC*** e pressione ENTER.  
![gid-network-20](/images/network/gid-network-20.png)
  
1. Após a filtragem, você verá duas tabelas de roteamento. Vamos começar com a tabela de roteament que tem sub-redes anexadas a ela. Quando você clica na tabela de roteamento correspondente, os detalhes serão exibidos abaixo. Verifique se ele pertence a `VPC-Lab`.  
![gid-network-21](/images/network/gid-network-21.png)
  
3. Na parte inferior, vá em **Rotas** para exibir as configurações desta tabela de roteamento.  
![gid-network-22](/images/network/gid-network-22.png)
- Se o destino for **10.0.0.0/16 (dentro do VPC)**, ele roteia o tráfego para o gateway local (local).
- Se o destino for qualquer outra coisa, ele roteia o tráfego de todos os destinos (0.0.0.0/0) para o gateway da Internet (igw-xxx).
- Esta é uma tabela de rotas que deve ser aplicada a **sub-redes públicas**, pois é uma configuração de roteamento que pode se comunicar diretamente com a Internet.
  
1.Selecione a guia **Subnet Association** para verificar a sub-rede à qual a condição da tabela de rotas está conectada. 
![gid-network-23](/images/network/gid-network-23.png)
-Você pode ver que apenas a `sub-rede pública A` com um espaço de endereço de 10.0.10.0/24 está conectada a essa tabela de rota. 
- Nossa recém-criada `sub-rede C pública` também precisa enviar tráfego de **0.0.0.0/0** para o gateway de Internet de acordo com as regras da tabela de rotas.
-Clique em **Editar associações de sub-rede** para associar a `Sub-rede pública C` também à sua tabela de rotas. 
  
5.Se você observar o campo **ID** da sub-rede no meio da janela **Editar associações de sub-rede**, verá que a `sub-rede pública C` não está selecionada. Clique na caixa de seleção à esquerda da `sub-rede pública C` para configurar a conexão e, em seguida, clique no botão Salvar na parte inferior direita.
![gid-network-24](/images/network/gid-network-24.png)
  
1. Agora você pode ver que a `sub-rede pública A` (10.0.10.0/24) e a `sub-rede pública C` (10.0.20.0/24) estão conectadas à tabela de rotas.
![gid-network-25](/images/network/gid-network-25.png)
  
7. Para evitar confusão no futuro, nomeie a tabela de rotas como `Rota pública` clicando no campo **Nome** na tabela de rotas.  
![gid-network-26](/images/network/gid-network-26.png)
  
8. A `rota pública` e a tabela de rotas para a sub-rede pública, foram configurada.  
![gid-network-27](/images/network/gid-network-27.png)
  
----
  
## Modificando a tabela de rota das **sub-redes privadas**
  
1. Vamos modificar a tabela de rotas para sub-redes privadas.
Entre as duas tabelas de rotas atualmente visíveis, clique na tabela de rotas sem nome e selecione a guia **Rotas**. 
![gid-network-28](/images/network/gid-network-28.png)
  
2. Clique na guia **Rotas** na parte inferior para ver as configurações para esta tabela de rota.  
![gid-network-29](/images/network/gid-network-29.png)
- Se o destino for **10.0.0.0/16 (dentro do VPC)**, ele roteia o tráfego para o **gateway local (local).**
- Se o destino for qualquer outra coisa, ele roteia o tráfego de todos os destinos (0.0.0.0/0) para o **gateway NAT (nat-xxx)**.  
- Esta é a tabela de rotas que deve ser aplicada às **sub-redes privadas**, pois esta é a sub-rede em que estamos usando um **gateway NAT**. 
  
3. Para associar uma sub-rede privada à tabela de rotas, clique na guia **Subnet Associations**.  
![gid-network-30](/images/network/gid-network-30.png)
- Verifiquei a conexão de sub-rede e não há nenhuma sub-rede conectada.
- `Sub-rede privada A` (10.0.100.0/24) e `sub-rede privada C` (10.0.200.0/24) que não estão conectadas são mostradas abaixo. 
- Clique em **Editar associações** de sub-rede para associar a `Sub-rede privada A` e a `Sub-rede privada C` às suas tabelas de rotas.
  
4.Clique na caixa de seleção à esquerda de `Sub-rede privada A` (10.0.100.0/24) e de `Sub-rede privada C (10.0.200.0/24)`,veja a ID de sub-rede no meio da janela Editar associações de sub-rede e clique no botão Salvar no canto inferior direito.
![gid-network-31](/images/network/gid-network-31.png)
  
1. Depois de confirmar que as duas sub-redes privadas estão conectadas à tabela de rotas apropriada, clique no campo **Nome** para nomear a tabela de rotas como `Rota privada`. 
![gid-network-32](/images/network/gid-network-32.png)
  
6. A `rota privada`, a tabela de rotas para a sub-rede privada, agora está configurada. 
![gid-network-33](/images/network/gid-network-33.png)
  
{{% notice info %}}
Agora, a configuração de rede básica está completa.  
{{% /notice %}}
  
----
  
## Arquiteturas até agora
Conceitualmente, os recursos que você configurou até o momento são exibidos no desenho como mostrado abaixo.  
![gid-network-01](/images/network/gid-network-01.svg)
