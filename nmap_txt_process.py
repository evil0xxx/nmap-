import re
import sys
import time

#脚本用于nmap tcp和udp端口扫描oN参数输出结果整理，use：python3 namptxt.py nmapresult.txt

ippattern = re.compile(r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
pt = []
rz = []
file = open (sys.argv[1],'r')
te = str(int(time.time())) #获取系统时间
ne = 'result_' + te
refile = open (ne +'.txt','w')

for line in file:
	if 'Nmap scan report for ' in line:
		ip = ippattern.search(line)
		ipre = ip.group()
	if ('/tcp ' or '/upd ') in line:
		pt.append(ipre + ' ' + line.strip()) #拼接IP和端口信息

for i in range(len(pt)):
	ir = pt[i].split()[0:4]
	vr = pt[i].split()[4:]
	ir = '|'.join(ir) #分割IP、端口、端口状态、协议并组合
	rz = ''.join(vr)  #拼接版本信息
	refile.write(ir + '|' + rz + '\n') #写入文本

print('处理结果已保存到' + ne + '.txt 文件')

file.close()
refile.close()