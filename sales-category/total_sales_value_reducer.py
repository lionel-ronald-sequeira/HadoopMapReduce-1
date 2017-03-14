import sys;

total_sales_value=0;
total_sales=0;
for line in sys.stdin:
	data=line.strip().split("\t");
	if len(data) != 2 :
		continue;
	total_sales+=1;
	total_sales_value+=float(data[1]);
print "{0}\t{1}".format(total_sales,total_sales_value);
