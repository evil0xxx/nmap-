import re
import sys
import time

#脚本用于nmap 存活扫描结果整理，use：python3 namptxt.py nmapresult.txt

ippattern = re.compile(r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
pt = []
rz = []
file = open (sys.argv[1],'r')
te = str(int(time.time())) #获取系统时间
dne = te +'_down'
drefile = open (dne +'.txt','w')
une = te + '_up'
urefile = open (une +'.txt','w')

for line in file:
	if '[host down]' in line:
		dip = ippattern.search(line)
		dipre = dip.group()
		drefile.write(dipre + '\n')
	if (('Nmap scan report for ' in line) and '[host down]' not in line):
		uip = ippattern.search(line)
		uipre = uip.group()
		urefile.write(uipre + '\n')

print('处理结果已保存到文件')

file.close()
drefile.close()
urefile.close()