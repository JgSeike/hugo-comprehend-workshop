---
date: 2020-06-01
title: "오토 스케일링 그룹 업데이트"
weight: 340
pre: "<b>3-4. </b>"
---

{{% notice note %}}
Aurora를 사용하도록 구성된 웹 인스턴스를 이용하여 새로운 커스텀 AMI를 생성합니다. 이 새로 만든 커스텀 AMI로 Launch Template 을 업데이트하고, Auto Scaling Group을 이용하여 RDS 연결 정보를 보유한 새 버전의 인스턴스들을 배포합니다.
{{% /notice %}}

----

## 신규 커스텀 AMI 생성
1. ***EC2 콘솔*** 로 들어가 좌측 메뉴에서 **Instances** 를 누르고, `ASG-Web-Instance` 인스턴스 체크 박스를 선택합니다. 이후 Actions -> Image and templates -> Create Image를 순차적으로 선택합니다.
![gid-rds-23](/images/rds/gid-rds-23.png) 

2. ***Image name*** 에 `Web Server v2`를 입력하고, ***Image description*** 에 `LAMP web server AMI with RDS connection config` 를 입력합니다. 그리고 **Create Image** 버튼을 클릭합니다.
![gid-rds-24](/images/rds/gid-rds-24.png) 

3. EC2 콘솔 좌측 메뉴에서 AMIs를 찾아 클릭합니다. 잠시 기다리면 새로운 커스텀 AMI가 ***pending*** 상태에서 ***available*** 상태로 업데이트 됩니다.
![gid-rds-26](/images/rds/gid-rds-26.png) 
![gid-rds-27](/images/rds/gid-rds-27.png)

4. 현재까지의 아키텍처는 아래와 같습니다.
![gid-rds-102](/images/rds/gid-rds-102.svg)

----

## Launch Template 업데이트
1. EC2 콘솔 좌측 메뉴에서 **Launch Templates** 를 선택하고, 우측 화면에서 ***Launch template name*** 이 `Web` 인 것을 체크 박스 선택 후, **Actions** 버튼을 클릭하고, **Modify template(Create new verison)** 를 클릭합니다.
![gid-rds-28](/images/rds/gid-rds-28.png)

2. Modify Template 에서 ***Template version description*** 을 아래와 같이 입력하고, Auto Scaling guidance의 ***Provide…*** 에 **체크박스를 선택** 합니다.
![gid-rds-29](/images/rds/gid-rds-29.png)
- Template version description: `Immersion Day Web Instances Template - with RDS connection String`
 
3. 스크롤을 내려 ***Launch template contents*** 의 Amazon machine image (AMI) 란에서 새로 만든 커스텀 AMI를 선택합니다. 검색 창에 ***Web Server v2*** 를 입력하면 쉽게 찾을 수 있습니다.
![gid-rds-30](/images/rds/gid-rds-30.png) 

4. 이후 다른 설정들은 그대로 두고, 스크롤을 맨 아래로 내려 **Create template version** 을 클릭합니다. 
![gid-rds-31](/images/rds/gid-rds-31.png) 

5. **View launch template** 을 누릅니다.
![gid-rds-32](/images/rds/gid-rds-32.png) 

6. 가운데 Versions 탭을 선택합니다. 아래와 같은 화면이 나올 겁니다.
![gid-rds-33](/images/rds/gid-rds-33.png) 

7. 두 개의 버전 중, 방금 생성한 Version 2를 선택하고 Actions -> Set default version을 누릅니다.
![gid-rds-34](/images/rds/gid-rds-34.png) 
 
8. 템플릿 버전이 2인지 확인한 이후, 우측 하단의 **Set as default version** 버튼을 누릅니다.
![gid-rds-35](/images/rds/gid-rds-35.png) 

9. 이제 Launch template의 Default version이 변경된 것이 보입니다.
![gid-rds-36](/images/rds/gid-rds-36.png) 
 
----
 
## Auto Scaling Group 업데이트
이제 Auto Scaling Group을 업데이트할 차례입니다.

1. EC2 콘솔 좌측 메뉴에서 맨 아래 **Auto Scaling Groups**을 선택합니다. 생성해 둔 `Web-ASG`를 선택한 후, **Edit** 버튼을 클릭합니다.
![gid-rds-37](/images/rds/gid-rds-37.png) 

2. Edit Web-ASG 화면에서 ***Desired capacity*** 와 ***Minimum capacity*** 는 `2`, ***Maximum capacity*** `4`를 넣고 **Update** 버튼을 클릭합니다.
![gid-rds-38](/images/rds/gid-rds-38.png) 

3. 아래 Launch template 버전을 확인해 줍니다. `Default (2)` 로 설정되어 있는지 확인하고, **Update** 버튼을 클릭합니다.
![gid-rds-39](/images/rds/gid-rds-39.png) 
![gid-rds-40](/images/rds/gid-rds-40.png) 


4. 아래로 스크롤을 내려 ***Advanced configurations*** 란으로 이동하고, **Edit** 버튼을 클릭합니다.
![gid-rds-41](/images/rds/gid-rds-41.png) 

5. ***Default cooldown*** 을 `30 seconds` 로 변경하고 우측 하단의 **Update** 버튼을 누릅니다. 잠시 기다리면, Auto Scaling Group이 새 Launch Template을 이용하여 새로운 인스턴스를 생성하는 걸 볼 수 있습니다.
![gid-rds-42](/images/rds/gid-rds-42.png) 

6. 두 개의 인스턴스가 InService인 것을 확인할 수 있습니다. 그런데 버전을 살펴보니 하나는 예전 Launch template ***버전(Version 1)*** 으로 만들어진 인스턴스입니다. 이 예전 버전 인스턴스를 수동으로 종료해 보겠습니다. **인스턴스의 ID(i-xxxxx)** 를 클릭합니다.
    ![gid-rds-44](/images/rds/gid-rds-44.png) 

    현재까지 구성한 아키텍처는 아래와 같습니다.
    ![gid-rds-103](/images/rds/gid-rds-103.svg)
 
7. 종료할 인스턴스의 명세를 확인할 수 있습니다. **Instance State** -> **Terminate instance** 를 눌러 줍니다. 
![gid-rds-45](/images/rds/gid-rds-45.png) 

8. 정말 종료하겠냐는 경고 팝업이 뜨면, **Terminate** 를 누릅니다.
![gid-rds-46](/images/rds/gid-rds-46.png) 

9. 다시 **Auto Scaling Group** 메뉴로 들어옵니다. **Web-ASG를 선택**하고, 가운데 **Instance management 탭을 눌러** 보면 현재 ***3개의 인스턴스가 보입니다.*** 이를 살펴보면, 수동으로 종료시킨 ***Version 1 인스턴스가 Terminating*** 상태이고, 새로이 ***Version 2 인스턴스가 올라오는 것*** 을 볼 수 있습니다. 
![gid-rds-47](/images/rds/gid-rds-47.png) 
    인스턴스가 종료된 직후의 다이어그램입니다.
    ![gid-rds-104](/images/rds/gid-rds-104.svg)

10. 변경이 발생하는 동안 ALB의 DNS를 이용하여 웹 서비스에 접근해 보면, 정상적으로 접근이 되는 것을 볼 수 있습니다. 
![gid-rds-47-1](/images/compute/gid-ec2-68.png) 

11. 인스턴스 추가가 완료되면, 앞서 [컴퓨트 – Amazon EC2](../../compute) 실습에서 본 것과 같이 두 개의 인스턴스에 번갈아 접근하게 됩니다. 데모 페이지에서 Instance Id가 변경된다면, Auto Scaling Group 콘솔로 들어가 봅니다. 두 개의 Launch Template Version 2 인스턴스가 정상적으로 동작 중인 것을 확인할 수 있습니다.
데모 웹 페이지로 돌아와, 데이터베이스 접속을 위해서 **RDS** 버튼을 눌러 보겠습니다. 
![gid-rds-48](/images/rds/gid-rds-48.png) 

12. 바로 아래와 같이 접근되며, 아까 수정한 내용 역시 반영된 것을 확인할 수 있습니다.
![gid-rds-49](/images/rds/gid-rds-49.png) 

----

## 현재까지의 아키텍처 구성
자, 여기까지의 작업을 통해 여러분은 고가용성이 보장된 웹 서비스를 구축하였습니다. 지금까지 구성한 인프라 아키텍처는 아래와 같습니다.
![gid-rds-105](/images/rds/gid-rds-105.svg)

