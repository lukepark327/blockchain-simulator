# blockchain-simulator
a general purpose blockchain simulation tool.

## ToDo
- [ ] 일반적인 블록체인과의 비교를 위해
* ex) geth, etc.
  * http로 하니까?
* 확장 가능하도록

## ToDo
* propagation delay와 selected neighbors에 대한 topology를 설정해야 함.
  * 현재는 그냥 random.gauss나 random으로 주고 있지만, 이유가 있으면 더 좋음.

* research: Solidity
  * mapping값을 zero로 하면 실제 0으로 되는건지, 저장소(storage)에서 날라가는건지?
  * geth에서 어떻게 구현했는가?

## flake8 convention
```
flake8 --ignore E501, E722
```
