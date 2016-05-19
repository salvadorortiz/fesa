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