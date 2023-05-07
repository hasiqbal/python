# filenames = ['document', 'report', 'presentation']

# Take the list above so it prints out the output below:

# 0-Document.txt
# 1-Report.txt
# 2-Presentation.txt

filenames = ['document', 'report', 'presentation']

for i, j in enumerate(filenames):
    print(f'{i}-{j.capitalize()}.txt')

