def testPrint(a):
 print('testImport testPrint:',a);

 
 
 
def string_to_float(str):
 grop=str.split('/');
 if len(grop)>1:
  if float(grop[1])==0:
   return 0;
  return float(float(grop[0])/float(grop[1]))
 return float(grop[0])
 
str='0/0';
res = string_to_float(str);
print(res);



