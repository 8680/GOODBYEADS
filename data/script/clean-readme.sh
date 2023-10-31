#!/bin/sh
num_rules=`sed -n 's/^! Total count: //p' rules.txt`
num_allow=`sed -n 's/^! Total count: //p' allow.txt`

time=$(TZ=UTC-8 date +'%Y-%m-%d %H:%M:%S')
sed -i "s/^更新时间:.*/更新时间: $time （北京时间） /g" README.md

sed -i 's/^拦截规则数量.*/拦截规则数量: '$num_rules' /g' README.md
sed -i 's/^白名单规则数量.*/白名单规则数量: '$num_allow' /g' README.md

exit
