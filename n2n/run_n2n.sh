# 在边缘服务器上运行n2n
# 需先安装
# cd ./n2n_linux
# make && make install


# 没有域名。若云服务器ip变化则需修改下行(-l后)的ip；同时需根据已有的边缘服务器分配(-a后)没有用过的10.0.1.*段ip。必须要同一网段
# -p 80表示暴露80端口，以供客户端连接，可更改
/usr/sbin/edge -a 10.0.1.1 -c ENSS -k BIT_ENSS -l 124.71.236.106:7000 -p 80