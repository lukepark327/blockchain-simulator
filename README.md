# blockchain-simulator
a general purpose blockchain simulation tool.

current version: v1.1.0

## ToDo
* 일반적인 블록체인과의 비교
  * ex) geth, etc.
  * 현재 구현체는 http로 하니까? 미들웨어를 구현하는 등의 방법 구상

* propagation delay와 selected neighbors에 대한 topology를 설정해야 함.
  * 현재는 그냥 random.gauss나 random으로 주고 있지만, 이유가 있으면 더 좋음.

## Trouble Shootings

### flake8 convention
```
flake8 --ignore E501, E722
```
