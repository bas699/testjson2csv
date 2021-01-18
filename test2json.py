import os,tkinter,tkinter.filedialog,pathlib,shutil,json,csv,codecs

def flatten_json(json):
    def process_value(keys,value,flattened):
        if isinstance(value,dict):
            for key in value.keys():
                process_value(keys+[key],value[key],flattend)
        elif isinstance(value,list):
            for idx,v in enumerate(value):
                process_value(keys+[str(idx)],v,flattend)
        else:
            flattened['__'.join(keys)]=value
    flattend={}
    for key in json.keys():
        process_value([key],json[key],flattend)
    return flattend

def change_suffix(file_name,to_suffix):
    st=pathlib.PurePath(file_name).stem
    to_name=st+to_suffix
    return to_name

root = tkinter.Tk()
root.withdraw()
fTyp =[("","*")]
iDir=os.path.abspath(os.path.dirname(__file__))
print("jsonをscvに変更します")
print("対象ファイルを選んでください")
file0=tkinter.filedialog.askopenfilename(filetypes=fTyp,initialdir = iDir)
file = codecs.open(file0,'r',"utf_8")
data=json.load(file)
file.close()
if isinstance(data,list):
	pt_data1=codecs.open(change_suffix(file0,'.csv'),'w','utf_8')
	for data1 in data:
		csvwriter=csv.writer(pt_data1,lineterminator='\n')
		#print(data1)
		#print(flatten_json(data1))
		for row in flatten_json(data1).items():
		    print(row)
		    csvwriter.writerow(row)
	pt_data1.close()	
else:
	pt_data1=codecs.open(change_suffix(file0,'.csv'),'w','utf_8')
	csvwriter=csv.writer(pt_data1,lineterminator='\n')
	#print(data)
	#print(flatten_json(data))
	for row in flatten_json(data).items():
	    print(row)
	    csvwriter.writerow(row)
	pt_data1.close()
