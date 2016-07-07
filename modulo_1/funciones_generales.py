def convert_fetchall(cursor):
	dict_cursor={}
	list_aux=[]
	for item in cursor:
		list_aux.append(list(item))
	dict_cursor['recordsTotal']=len(list_aux)
	dict_cursor['recordsFiltered']=len(list_aux)
	dict_cursor['draw']= len(list_aux)//10
	dict_cursor['data']=list_aux
	return dict_cursor

def time_in_range(start, end, x):
	"""Return true if x is in the range [start, end]"""
	if start <= end:
		return start < x < end
	else:
		return start < x or x < end

def merge_two_dicts(x, y):
	'''Given two dicts, merge them into a new dict as a shallow copy.'''
	z = x.copy()
	z.update(y)
	return z
