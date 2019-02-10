#!/usr/bin/env bash

# nohup python3 main.py --nodes=24
python3 main.py --nodes=120 --neighbors=8 --prop_delay_avg=5000 --prop_delay_std=2000 --sleep=10
