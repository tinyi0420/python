course1={'id':'POOP','duration':'30','point':5.5,
         'schedual':['Saturday','Sunday'],'date':'1-Dec-2019',
         'instructor':'何孟翰'}
print('language'in course1,'何孟翰' in course1,
      'id' in course1)
for k in course1:
    print(f'key={k},value={course1[k]}')
print(['key={k},value={course1[k]' for k in course1.keys()])
#for v in course1.values():
    #print(v)
for i in course1.items():
    print(i)
print(course1.get('price'))
