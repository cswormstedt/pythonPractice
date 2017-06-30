import os
import time

# 1. the files and the directories to be backed up
# are specified in a list.
source = ['/Users/swormtrooper/notes']

# 2. the backup must be stored in a main backup
# directory
target_dir = '/Users/swormtrooper/backup'

# 3. The files are backed up into a zip file.
# 4. the name of the zip archive is the current date and time

target = target_dir + os.sep + \
		 time.strftime('%Y%m%d%H%M%S') + '.zip'

# Create target directory if it is not persent
if not os.path.exists(target_dir):
	os.mkdir(target_dir) 

# 5. use zip command to put the files in a zip archive
zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))

#run the backup
print('Zip command is:')
print(zip_command)
print('running:')
if os.system(zip_command) == 0:
	print('successful backup to', target)
else:
	print('backup FAILED')