---
date: 2020-06-30
title: "라우트 테이블 수정"
weight: 130
pre: "<b>1-3. </b>"
---

{{% notice note %}}
**Routing Table** 을 선택하면 생성된 모든 라우트 테이블을 확인할 수 있으며, 라우트 테이블을 변경하거나 해당 라우트 테이블에 Subnet을 연결(Association)하는 작업을 할 수 있습니다. 여기서는 새로 생성한 두 개의 서브넷에 적합한 라우트 테이블을 연결해 주겠습니다.
{{% /notice %}}

----

## **퍼블릭 서브넷** 라우트 테이블 수정

1. VPC 메뉴 좌측의 **Route Tables** 을 클릭합니다. 가운데 검색 창을 클릭 후 리소스 속성에서 **VPC** 를 선택하여, 방금 생성한 `VPC-Lab`의 ***VPC ID*** 를 찾아 필터를 설정합니다.
![gid-network-20](/images/network/gid-network-20.png)
  
2. 필터링이 되고 나면 두 개의 라우트 테이블이 보입니다. 일단 **Explicit subnet associations** 에 서브넷이 연결되어 있는 라우트 테이블부터 살펴보겠습니다. 해당 라우트 테이블을 클릭하면, 아래에 세부 사항이 표시됩니다. `VPC-Lab` 에 속한게 맞는지 한 번 더 확인합니다.
![gid-network-21](/images/network/gid-network-21.png)

3. 하단의 **Routes** 탭을 눌러, 이 라우트 테이블의 설정을 확인합니다.  
![gid-network-22](/images/network/gid-network-22.png)
   - 목적지가 ***10.0.0.0/16(VPC 내부)*** 인 경우 **로컬 게이트웨이(local)** 로 트래픽을 라우팅 합니다.  
   - 목적지가 ***그 외*** 일 경우, 모든 목적지(0.0.0.0/0)의 트래픽을 **인터넷 게이트웨이(igw-xxx)** 로 라우팅 합니다.  
   - **인터넷과 바로 통신** 이 가능한 라우팅 구성이므로, **퍼블릭 서브넷** 들에 적용되어야 하는 라우트 테이블입니다.  

4. 해당 라우트 테이블 조건이 연결되어 있는 서브넷을 확인하기 위하여 **Subnet Association** 탭을 선택합니다.
![gid-network-23](/images/network/gid-network-23.png)
    - **10.0.10.0/24** 의 주소 공간을 갖는 `Public subnet A` 만 해당 라우트 테이블에 연결되어 있는 것을 볼 수 있습니다.
    - 우리가 새로 만든 `Public subnet C` 역시 해당 라우트 테이블의 규칙에 따라 **0.0.0.0/0** 으로의 트래픽을 인터넷 게이트웨이로 보내야 합니다.
    - **Edit subnet associations** 을 눌러 `Public Subnet C` 도 해당 라우트 테이블에 연결해 보겠습니다.

5. ***Edit subnet associations*** 창의 가운데 서브넷 ID란을 보면, `Public subnet C` 가 선택되지 않은 것을 보실 수 있습니다. `Public subnet C` 의 **좌측 체크박스** 를 눌러 연결 설정을 해 준 뒤, 우측 하단의 **Save** 버튼을 누릅니다.
![gid-network-24](/images/network/gid-network-24.png)
 
6. 이제 해당 라우트 테이블에 `Public subnet A`(10.0.10.0/24), `Public subnet C`(10.0.20.0/24) 가 연결된 것을 확인할 수 있습니다.
![gid-network-25](/images/network/gid-network-25.png)

7. 추후 혼선을 방지하기 위해, 라우트 테이블의 **Name** 필드를 눌러 `Public route` 라고 라우트 테이블에 이름을 붙여 주겠습니다.
![gid-network-26](/images/network/gid-network-26.png)

8. 퍼블릭 서브넷을 위한 라우트 테이블인 `Public route` 설정이 완료되었습니다.
![gid-network-27](/images/network/gid-network-27.png)

----

## **프라이빗 서브넷** 라우트 테이블 수정

1. 프라이빗 서브넷들을 위한 라우트 테이블을 수정해 보겠습니다.  
현재 보이는 두 개의 라우트 테이블 중, **이름이 없는 라우트 테이블** 을 클릭하고 **라우트(Routes)** 탭을 선택합니다.
![gid-network-28](/images/network/gid-network-28.png)

2. 하단의 **Routes** 탭을 눌러, 이 라우트 테이블의 설정을 확인합니다.
![gid-network-29](/images/network/gid-network-29.png)
   - 목적지가 ***10.0.0.0/16(VPC 내부)*** 인 경우 **로컬 게이트웨이(local)** 로 트래픽을 라우팅 합니다.
   - 목적지가 ***그 외*** 일 경우, 모든 목적지(0.0.0.0/0)의 트래픽을 **NAT 게이트웨이(nat-xxx)** 로 라우팅 합니다.
   - **NAT 게이트웨이** 를 사용하도록 한 서브넷이므로 **프라이빗 서브넷** 들에 적용되어야 하는 라우트 테이블입니다.

3. 프라이빗 서브넷을 라우트 테이블에 연결시키기 위하여, **Subnet Associations** 탭을 눌러 보겠습니다.
![gid-network-30](/images/network/gid-network-30.png)
   - 서브넷 연결을 확인해 보니 아무 서브넷도 연결되어 있지 않습니다.
   - 연결되지 않은 `Private subnet A`(10.0.100.0/24), `Private subnet C`(10.0.200.0/24) 서브넷들이 하단에 보입니다.
    - **Edit subnet associations** 을 눌러 `Private Subnet A`와 `Private Subnet C` 를 해당 라우트 테이블에 연결해 보겠습니다.

4. ***Edit subnet associations*** 창의 가운데 서브넷 ID에 `Private subnet A`(10.0.100.0/24), `Private subnet C`(10.0.200.0/24) 의 **좌측 체크박스** 를 눌러 연결 설정을 해 준 뒤, 우측 하단의 **Save** 버튼을 누릅니다.
![gid-network-31](/images/network/gid-network-31.png)

5. 프라이빗 서브넷 2개가 해당 라우트 테이블에 잘 연결되었는지 확인 후, **Name** 필드를 눌러 `Private route` 라고 라우트 테이블의 이름을 지정해 줍니다.
![gid-network-32](/images/network/gid-network-32.png)

6. 프라이빗 서브넷을 위한 라우트 테이블인 `Private route` 설정이 완료되었습니다.
![gid-network-33](/images/network/gid-network-33.png)

{{% notice info %}}
자, 이제 기본적인 네트워크 구성이 완료되었습니다.
{{% /notice %}}

----

## 현재까지의 아키텍처 구성
현재까지 구성한 자원들을 개념적으로 도면에 표시해 보면 아래 그림과 같습니다.
![gid-network-01](/images/network/gid-network-01.svg)
