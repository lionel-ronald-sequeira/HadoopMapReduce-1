import sys;

total_sales=0
old_category=None;
for line in sys.stdin:
	data=line.strip().split("\t");
	new_category=data[0];
	if len(data) != 2 :
		continue;
	if old_category and old_category !=new_category:
		print "{0}\t{1}".format(old_category,total_sales);
		total_sales=0;
	total_sales+=float(data[1]);
	old_category=new_category;
print "{0}\t{1}".format(old_category,total_sales);

