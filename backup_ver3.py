import os, time, zipfile

#for using os.path
#source = ['/Users/sheawinkler/Documents/ByteOfPython']

#for using zipfile
os.chdir('/Users/sheawinkler/Documents/ByteOfPython')

source = '/Users/sheawinkler/Documents/ByteOfPython'

target_dir = '/Users/sheawinkler/Documents/ByteOfPython/backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = input('Enter a comment --> ')

#check if comment was entered
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

#create directory if not exists --> os.path solution
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

'''
#zip command
zip_command = 'zip -r {0} {1}'.format(target, ''.join(source))

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
'''

# Python's built-in ZipFile method
with zipfile.ZipFile(target, 'w') as myzip:
    myzip.write('backup_ver2.py')
    myzip.write('backup_ver1.py')
