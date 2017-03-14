import sys;

max_sale=0
old_store=None;
for line in sys.stdin:
	data=line.strip().split("\t");
	new_store=data[0];
	if len(data) != 2 :
		continue;
	if old_store and old_store !=new_store:
		print "{0}\t{1}".format(old_store,max_sale);
		max_sale=0;
	if max_sale < float(data[1]):
		max_sale=float(data[1]);
	old_store=new_store;

print "{0}\t{1}".format(old_store,max_sale);
