import os, time

source = ['/Users/sheawinkler/Documents/ByteOfPython']

target_dir = '/Users/sheawinkler/Documents/ByteOfPython/backup'

#error checking, build directory if not exists
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

#current day is the name of subdirectory in main directory
today = target_dir + os.sep + time.strftime('%Y%m%d')

#current time for name of zip archive
now = time.strftime('%H%M%S')

#zip file
target = today + os.sep + now + '.zip'

#create subdirectory if not exists
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

zip_command = 'zip -r {0} {1}'.format(target, ''.join(source))

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')


