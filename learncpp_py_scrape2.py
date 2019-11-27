file = open("learncpp_source_urls.txt")
final_file = open("learncpp_final_urls.txt", "w")

url_list = []
filtered_list = []
final_list = []

string = 'None'
https = 'https'

for f in enumerate(file):
	url_list.append(f)

for e, f in url_list:
	if string not in f:
		filtered_list.append(f)
	if https not in f:
		filtered_list.append('https://www.learncpp.com' + f)

for e, f in enumerate(filtered_list):
	if string not in f and https in f:
		final_list.append(f)

for f in final_list:
	print(f)
	final_file.write(f)

file.close()
final_file.close()