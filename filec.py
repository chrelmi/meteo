#!/usr/bin/env python3
import csv
with open('list.csv') as csvfile:
	r=csv.DictReader(csvfile)
	for row in r:
		name=row['nome']
		img=row['img']
		print(name+" "+img)
