def check_folder(data):
    new_data = []
    word_list = ['.github','_test_',"requirements.txt"]
    for n in data:
        if sum([n.startswith(word) for word in word_list])==0:
            new_data.append(n.split('/')[0])
    return new_data


with open('files.txt') as f:
    data = f.readlines()

print(data)
new_data = check_folder(data)
print(new_data)

with open("files_flag.txt", 'w') as f:
    for row in new_data:
        f.write(f"{row},")