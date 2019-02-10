[![license](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![version](https://img.shields.io/badge/version-v1.2.0-orange.svg)](https://github.com/twodude/blockchain-simulator/blob/master/main.py#L2)
[![node](https://img.shields.io/badge/node-%3E%3D4.3.2-yellow.svg)](https://nodejs.org/en/)
[![python](https://img.shields.io/badge/python-3.6.7-blue.svg)](https://www.python.org)  


# blockchain-simulator
a general purpose blockchain simulation tool.

> Based on [one-chain](https://github.com/twodude/onechain)   

## How to Use

### Preconditions
```bash
sh preconditions.sh
```
* ```npm install``` for onechain, master, and mallcious.   

### Run
```bash
sh run.sh
```

또는

```bash
nohup python3 main.py --nodes=400 --neighbors=8 --prop_delay_avg=5000 --prop_delay_std=2000 --sleep=60
```

* nodes: (full) node 수
* neighbors: 한 노드와 연결할 다른 (최소) 노드 수
* prop_delay_avg: propagation delay의 평균
* prop_delay_std: propagation delay의 표준편차
* sleep: 대기 시간이 필요한 코드들(예를들어 connection이 완료되기를 기다리거나) 사이에서 기다릴 시간, 초(sec) 단위.

* log를 출력하고 싶을 시 nohup 제외:

```bash
python3 main.py --nodes=400 --neighbors=8 --prop_delay_avg=5000 --prop_delay_std=2000 --sleep=60
```

### RESTful API

TBA

### Cleanup

TBA

## ToDo
* 일반적인 블록체인과의 비교
  * ex) geth, etc.
  * 현재 구현체는 http로 하니까? 미들웨어를 구현하는 등의 방법 구상

* propagation delay와 selected neighbors에 대한 topology를 설정해야 함.
  * 현재는 그냥 random.gauss나 random으로 주고 있지만, 이유가 있으면 더 좋음.

* mallcious node, light client 추가하기

## Trouble Shootings

### flake8 convention
```
flake8 --ignore E501, E722
```

# License
The blockchain-simulator project is licensed under the [Apache License, Version 2.0](https://opensource.org/licenses/Apache-2.0), also included in our repository in the [LICENSE](https://github.com/twodude/blockchain-simulator/blob/master/LICENSE) file.
