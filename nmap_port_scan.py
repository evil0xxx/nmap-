# -*- coding: utf-8 -*-
import subprocess
import os
import sys
import time
import tempfile
import re

refile = open ('portResut.txt', 'w', encoding='utf-8')
ippattern = re.compile(r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')

for line in open(sys.argv[1]):
    try:
        ipre = ippattern.search(line)
        ip = ipre.group()
        port = line.split()[1]
        print('正在扫描' + ip + '的' + port + '端口')
        cmd = ['nmap -n -Pn -sV -p' + port + ' ' + ip]
        out_temp = tempfile.TemporaryFile()
        fileno = out_temp.fileno()
        re = subprocess.Popen(cmd, shell = True, stdout=fileno,stderr=fileno)
        re.wait()
        out_temp.seek(0)
        lines = out_temp.read().decode('utf-8', 'ignore')
        refile.write(lines)
    except:
        continue

refile.close