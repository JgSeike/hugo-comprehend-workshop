---
date: 2020-06-01
title: "네트워크 – Amazon VPC"
weight: 100
pre: "<b>1. </b>"
---

{{% notice note %}}
본 실습에서는 **VPC Wizard**를 통하여 Public Subnet 및 Private Subnet을 2개의 가용영역(AZ-a, AZ-c)에 각각 하나씩 생성하고, 하나의 Public Subnet에 NAT 게이트웨이를 구성합니다.  
이후 라우팅 테이블을 설정하여 트래픽 흐름을 정의하게 됩니다. 이와 같은 작업을 통해 추후 고가용성과 확장성을 가진 웹 서비스 환경을 만들기 위한 기본 네트워킹 구성을 완료합니다.
{{% /notice %}}

{{% notice info %}}
실습 문서에 삽입된 이미지들은 실습을 돕기 위하여 작성되었습니다. 실습 수행 중 생성하는 각각의 요소들의(VPC, NAT Gateway 및 EIP 등) ***식별자(ID)*** 는 사용자 계정마다 다르게 표시될 수 있습니다.
{{% /notice %}}

----

## 목표 구성도
이번 실습을 통하여 구축하고자 하는 최종 구성도는 아래와 같습니다.
![GID-Network-DG](/images/network/gid-network-01.svg)

----

## 실습 순서
이번 실습의 순서는 다음과 같습니다.

[1. VPC 생성](./create_vpc)  
[2. 추가 서브넷 생성](./create_subnet)  
[3. 라우트 테이블 수정](./modify_route)





