#/usr/bin/python2.7
##usage: pnmap.py (nmap -sn result file) (nmap -Pn result file) (ip range to scan)
import subprocess
import sys
netscan = sys.argv[1]
out = sys.argv[2]
net = sys.argv[3]
subprocess.check_output(["nmap", "-sn", net])
f = open(netscan, "r")
o = open(out, "w")
o.close()
iseven = 1
s = f.readline()
while(s!=""):
	o = open(out, "r")
	ot = o.read()
	o.close()
	if iseven:
		o = open(out, "w")
		o.write(ot + s)
		o.close()
		iseven = 0
	else:
		iseven = 1
	s = f.readline()
f.close()
o = open(out, "r")
ot = o.read()
o.close()
ot = ot.split("\n")
outstring = ""
ot = ot[:-2]
for item in ot:
	outstring = outstring + "\n" +  item[21:]
f = open(out, "w")
f.write(outstring[2:])
f.close()

##part 2
s = open(out,"r")
text = s.read()
s.close()
s = open(out,"w")
s.write("")
s.close()
text = text.split("\n")
for ip in text:
	result = subprocess.check_output(["nmap","-Pn", ip])
	s = open(out,"r")
	text2 = s.read()
	s.close()
	s = open(out,"w")
	s.write(text2 + "\n" + result)
	s.close()
	print result
print "Results have been logged in " + out + "."
