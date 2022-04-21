#!/bin/sh
num_adg=`sed -n 's/^! Total count: //p' rules.txt`

time=$(TZ=UTC-8 date +'%Y-%m-%d %H:%M:%S')
sed -i "s/^更新时间:.*/更新时间: $time （北京时间） /g" README.md

sed -i 's/^规则数量.*/规则数量: '$num_adg' /g' README.md

exit
