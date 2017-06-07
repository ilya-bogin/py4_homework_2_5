from subprocess import call
from os import listdir, makedirs
from os.path import isfile, join, exists, dirname
from shutil import copyfile

def copy_files_to_new_folder(source_folder_path, destination_folder_path, files):
  if not exists(dirname(destination_folder_path)):
    try:
        makedirs(dirname(destination_folder_path))
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
  for image_file_name in files:
    if image_file_name.startswith('.'):
      continue
    copyfile('{0}/{1}'.format(source_folder_path, image_file_name),
             '{0}/{1}'.format(destination_folder_path, image_file_name))


def convert_files(folder_path, files):
  for image_file_name in files:
    if image_file_name.startswith('.'):
      continue
    print('Convert ' + image_file_name)
    call(['sips', '--resampleWidth', '200', '{0}{1}'.format(folder_path, image_file_name)])


def main():
  source_image_files_path = './Source/'
  dest_image_files_path = './Converted/'

  image_files = [f for f in listdir(source_image_files_path) if isfile(join(source_image_files_path, f))]
  copy_files_to_new_folder(source_image_files_path, dest_image_files_path, image_files)
  print('Source images list:')
  print(image_files)
  print('Start conversion...')
  convert_files(dest_image_files_path, image_files)
  return

main()
