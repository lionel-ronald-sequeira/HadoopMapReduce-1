import sys;
no_of_lines=0;
ip="10.99.99.186";
for line in sys.stdin:
	data=line.strip().split("\t");
	if data[0]==ip:
		no_of_lines+=1;
print "{0}\t{1}".format(ip,no_of_lines);		
