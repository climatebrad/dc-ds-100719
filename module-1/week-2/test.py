thor2 = ['Chris Hemsworth', 'Natalie Portman', 'Tom Hiddleston', 'Kat Dennings', 'Anthony Hopkins', 'Jaimie Alexander', 'Idris Elba']

ragnarok = ['Chris Hemsworth', 'Tessa Thompson', 'Cate Blanchett', 'Tom Hiddleston', 'Mark Ruffalo', 'Jeff Goldblum', 'Karl Urban', 'Idris Elba', 'Anthony Hopkins']

def both_casts(a,b):
   return [x for x in a if x in b]

def both_casts1(a,b):
   return list(set(a).intersection(set(b)))

import time

def timer(exec_string,ct=1000):
	start_time = time.perf_counter()
	for i in range(ct):
		exec(exec_string)
	end_time = time.perf_counter()
	return end_time - start_time

print(both_casts(thor2,ragnarok))
print(both_casts1(thor2,ragnarok))
times = []
for i in range(1000):
    both_casts_time = timer('both_casts(thor2,ragnarok)',5000)
    both_casts2_time = timer('both_casts1(thor2,ragnarok)',5000)
    times.append([i,both_casts_time,both_casts2_time])

import pandas as pd
df = pd.DataFrame(times,columns=['index','list_interp','set_intersection'])
df['diff']=df.list_interp - df.set_intersection
print(df.describe())
