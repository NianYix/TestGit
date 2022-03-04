from collections import OrderedDict
import json
import codecs
import xlrd


path=r'F:\Work\JerryStudy\Python\ZiLiao\Code\folderCode\duoduoduo.xlsx'
wb=xlrd.open_workbook(path);
convert_list=[];
sh=wb.sheet_by_index(0);
title=sh.row_values(0);
for rownum in range(1,sh.nrows):
	rowvalue=sh.row_values(rownum);
	single=OrderedDict();
	for colnum in range(0,len(rowvalue)):
		print(title[colnum],rowvalue[colnum]);
		single[title[colnum]]=rowvalue[colnum];
	convert_list.append(single);

j=json.dumps(convert_list,separators=(',',':'),ensure_ascii=False);

newPath=r'F:\Work\JerryStudy\Python\ZiLiao\Code\folderCode\zhuanJson.json'
with codecs.open(newPath,"w","utf-8") as f:
 f.write(j);


