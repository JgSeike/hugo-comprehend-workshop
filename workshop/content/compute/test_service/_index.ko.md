---
date: 2020-06-01
title: "웹 서비스 확인 및 테스트"
weight: 230
pre: "<b>2-3. </b>"
---

{{% notice note %}}
이제 구성한 서비스가 정상적으로 동작하는지 테스트해 보겠습니다. 먼저 정상적으로 웹 사이트에 접속 가능한지, 로드 밸런서가 동작하는지 확인한 후, 웹 서버에 부하를 주어 Auto Scaling이 동작하는지 확인해 보겠습니다.
{{% /notice %}}

----

## 웹 서비스 및 로드 밸런서 동작 확인
1. 해당 웹 서비스에 구성한 Application Load Balancer를 통해 접속하기 위해, EC2 콘솔에서 **Load Balancers** 메뉴를 클릭하고, 아까 생성한 `Web-ALB`를 선택해 줍니다. 여기서 기본 구성의 ***DNS 이름*** 을 복사해 줍니다. 
![gid-ec2-67](/images/compute/gid-ec2-67.png) 

2. 브라우저에서 새 탭을 열고 ***복사한 DNS 이름*** 을 붙여 넣습니다. 아래와 같이 EC2 Lab에서 본 웹 서비스가 동작하는 것을 확인할 수 있습니다. 아래 그림의 경우 ***ap-northeast-2a*** 의 웹 인스턴스에서 해당 웹 페이지를 서비스하고 있다는 것을 확인할 수 있습니다.
![gid-ec2-68](/images/compute/gid-ec2-68.png) 

3. 여기서 새로 고침 버튼을 눌러 보면, 아래와 같이 웹 페이지를 서비스하는 호스트가 ***다른 가용 영역의 인스턴스*** (ap-northeast-2c) 로 바뀐 것을 볼 수 있습니다. 이는 ALB 타겟 그룹의 라우팅 알고리즘이 기본적으로 *Round Robin* 방식으로 동작하기 때문입니다. 
![gid-ec2-69](/images/compute/gid-ec2-69.png) 

4. 현재 Auto Scaling 그룹에는 각 인스턴스의 CPU 사용률 30%가 조정 목표로 설정되어 있습니다.  
   - 인스턴스들의 평균 ***CPU 사용률이 30% 미만*** 인 경우 **인스턴스 숫자를 줄이고**,  
   - 인스턴스들의 평균 ***CPU 사용률이 30%를 이상*** 이면 **인스턴스를 추가 배치, 부하를 분산** 하여 **인스턴스들의 평균 CPU 사용률이 30%가 되도록** 조정 정책이 동작합니다. 

5. 이제 실제로 부하를 주어 Auto Scaling이 잘 동작하는지 확인해 보겠습니다. 상기 웹 페이지에서 **LOAD TEST** 메뉴를 클릭합니다. 화면이 바뀌고 가해진 부하가 보입니다. 페이지 좌측 상단의 로고를 클릭해 보면 각 인스턴스에 부하가 걸린 것을 확인할 수 있습니다.
   - 부하 발생 전,
   ![gid-ec2-70](/images/compute/gid-ec2-70.png)
   - 부하 발생 후,
   ![gid-ec2-70-1](/images/compute/gid-ec2-70-1.png)

{{% notice tip %}}
CPU 부하를 발생시키는 원리는 CPU Idle 값이 50이 넘어가면, 임의의 파일을 만들고 압축하고 압축을 해제하는 작업을 하도록 PHP 코드가 5초 주기로 동작합니다. ALB에 의해서 트래픽이 분산되어 동작되기 때문에 부하를 걸어주고 나면 계속적으로 다른 인스턴스에도 부하가 발생하게 됩니다.
{{% /notice %}}

6. EC2 콘솔의 좌측 메뉴에서 **Auto Scaling Groups**에 들어가, **Monitoring** 탭을 누릅니다. 아래 **Enabled metrics**에서 **EC2**를 누르고, 우측 타임프레임을 **1시간**으로 설정해 줍니다. 이후 잠시 기다리면 **CPU Utilization (Percent)** 그래프가 변화하는 것을 보실 수 있습니다. 
![gid-ec2-71](/images/compute/gid-ec2-71.png)

7. 5분(300초) 정도 기다린 후 **Activity** 탭을 눌러 보면, 조정 정책에 따라 EC2 인스턴스를 추가 배치하는 것을 보실 수 있습니다.
![gid-ec2-72](/images/compute/gid-ec2-72.png)

8. **Instance management** 탭을 클릭해 보니, 두 개의 인스턴스가 추가적으로 생겨나 총 4개의 인스턴스가 동작중인 것을 볼 수 있습니다.
![gid-ec2-73](/images/compute/gid-ec2-73.png)

9. 아까 복사해 둔 ALB DNS를 이용하여 웹 페이지에 접속, 새로 고침을 해 보면 없었던 두 개의 인스턴스에서 웹 페이지를 호스팅하는 것을 확인할 수 있습니다. 새로 생겨난 인스턴스이기 때문에 현재 CPU Load는 0% 입니다. 각각 다른 가용 영역에 생성된 것도 확인 가능합니다. 만약 0%가 아니라면, 부하가 계속 걸리는 상황이기 때문에 100% 이상으로 보일 수 있습니다.
![gid-ec2-74](/images/compute/gid-ec2-74.png)

여기까지 웹 서비스에 대한 부하 테스트를 통해 Auto Scaling 그룹이 동작하는 것을 확인하였습니다. 만약 CPU 부하를 발생시키는 페이지가 동작중이면 화면을 닫아서 추가적으로 부하가 발생하지 않도록 합니다.

----

## 수동으로 스케일 조정

{{% notice note %}}
이제 수동으로 스케일 옵션을 조정하여 한 개의 인스턴스만 Auto Scaling Group에 남겨 두도록 하겠습니다.
{{% /notice %}}

1. EC2 콘솔 좌측의 **Auto Scaling Groups**를 클릭합니다. 이후 우리가 방금 생성한 Auto Scaling Groups의 Name이 `Web-ASG`을 클릭합니다.
![gid-ec2-75](/images/compute/gid-ec2-75.png)

2. Group details에서 우측 **Edit** 버튼을 누릅니다.
![gid-ec2-76](/images/compute/gid-ec2-76.png)

3. Edit Web-ASG 창에서 **Desired capacity**와 **Minimum capacity**, **Maximum capacity**를 모두 `1`로 변경하고, **Update** 버튼을 누릅니다.
![gid-ec2-77](/images/compute/gid-ec2-77.png)

4. 업데이트된 설정이 적용되었습니다.
![gid-ec2-78](/images/compute/gid-ec2-78.png)

5. **Activity** 탭을 들어가 보면, Desired capacity에 맞게 인스턴스들을 ALB에서 Draining하는 것을 볼 수 있습니다. 실제 Draining이 완료되기까지는 수 분이 소요됩니다.
![gid-ec2-79](/images/compute/gid-ec2-79.png)

6. ALB에서 인스턴스 Draining 작업이 완료되면 아래와 같이 **Activity** 탭의 로그가 변경된 것을 볼 수 있습니다.
![gid-ec2-82](/images/compute/gid-ec2-82.png)

7. **Instance management** 탭에 들어가 보면 인스턴스가 하나만 남아 있는 것을 볼 수 있습니다.
![gid-ec2-83](/images/compute/gid-ec2-83.png)

8. **Instances** 메뉴에서도 확인 가능합니다. ***terminated*** 된 인스턴스와 남아 있는 1개의 인스턴스를 확인할 수 있습니다.
![gid-ec2-80](/images/compute/gid-ec2-80.png)

{{% notice info %}}
이후 Database 실습에서 Web Application과 DB를 연결 완료한 설정이 수록된 AMI를 만들면, 인스턴스 개수를 다시 2개 이상으로 확장 가능하도록 변경할 예정입니다.   
[3-4. 오토 스케일링 그룹 업데이트](../../database/update_asg) 참조
{{% /notice %}}

