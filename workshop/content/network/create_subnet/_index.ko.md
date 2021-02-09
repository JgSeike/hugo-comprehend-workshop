---
date: 2020-06-30
title: "추가 서브넷 생성"
weight: 120
pre: "<b>1-2. </b>"
---

{{% notice note %}}
고가용성 및 Fault Tolerant한 네트워크 서비스 구성을 위해, VPC의 Availability Zone C를 사용하겠습니다. 여기에 퍼블릭, 프라이빗 서브넷을 하나씩 더 추가하고, 라우팅 테이블을 설정하겠습니다.
{{% /notice %}}

----

## 다른 가용영역(az-northeast-2c)에 **퍼블릭 서브넷** 생성
1. VPC 콘솔 왼쪽 화면의 **Subnet** 을 클릭하고, 상단의 **Create subnet** 버튼을 클릭합니다.  
![gid-network-14](/images/network/gid-network-14.png)

2. **Create Subnet** 란에서 Name tag, VPC, Availability Zone, IPv4 CIDR block을 아래의 값으로 지정하고, 우측 하단의 **Create** 버튼을 누르고 `Puiblic subnet C` 서브넷을 생성합니다.  

    | 키 | 값 |
    |----------|--------------------|
    | VPC | VPC란을 클릭해서 `VPC-Lab` 태그가 설정된 VPC를 선택합니다. |
    | Subnet name | `Public subnet C` |
    | Availability Zone | `ap-northeast-2c` |
    | IPv4 CIDR block | `10.0.20.0/24` |

    ![gid-network-15](/images/network/gid-network-15.png)  
    ![gid-network-15](/images/network/gid-network-15-1.png)  

3. `Puiblic subnet C` **퍼블릭 서브넷**이 생성된 것을 확인할 수 있습니다.
![gid-network-16](/images/network/gid-network-16.png)  

----

## 다른 가용영역(az-northeast-2c)에 **프라이빗 서브넷** 생성
1. 프라이빗 서브넷도 하나 더 생성하기 위하여, **Create Subnet** 버튼을 클릭합니다.  
그리고 아래의 값으로 지정하고, **Create** 버튼을 눌러 `Private subnet C` 도 생성합니다.

    | 키 | 값 |
    |----------|--------------------|
    | VPC | VPC란을 클릭해서 `VPC-Lab` 태그가 설정된 VPC를 선택합니다. |
    | Subnet name | `Private subnet C` |
    | Availability Zone | `ap-northeast-2c` |
    | IPv4 CIDR block | `10.0.200.0/24` |

    ![gid-network-17](/images/network/gid-network-17.png)  

2. `Private subnet C` **프라이빗 서브넷**이 생성된 것을 확인할 수 있습니다.
![gid-network-18](/images/network/gid-network-18.png)  

----

## 생성된 서브넷 확인
1. VPC의  **Subnet** 메뉴를 클릭하고, 서브넷을 확인하면 아래와 같이 4개의 생성된 서브넷을 볼 수 있습니다.
![gid-network-19](/images/network/gid-network-19.png)  

----

## 현재까지의 아키텍처 구성
추가된 서브넷에 대한 현재까지 구성된 환경은 아래와 같습니다.
![gid-network-34](/images/network/gid-network-34.svg)