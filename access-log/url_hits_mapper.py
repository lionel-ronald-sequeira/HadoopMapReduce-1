import sys;

for line in sys.stdin:
	data=line.strip().split(" ");
	if len(data)==10:
		print "{0}\t{1}".format(data[6],1);
		
