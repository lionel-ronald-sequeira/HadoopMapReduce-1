import sys;
no_of_lines=0;
url="/assets/js/the-associates.js";
for line in sys.stdin:
	data=line.strip().split("\t");
	
	if data[0]==url:
		no_of_lines+=1;
print "{0}\t{1}".format(url,no_of_lines);		
