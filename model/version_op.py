import os
import time
import string
import shutil

EXCLUDED_DIRS = {
    'system32', 'windows', 'program files', 'program files (x86)',
    'appdata', 'application data'
}


def is_hidden(filepath):
    # Windows-specific method to check if a file is hidden
    try:
        # Get the file attributes
        attrs = os.stat(filepath).st_file_attributes
        # Check if 'hidden' attribute is set
        if attrs & 0x02:
            return True
    except Exception as e:
        print(f"Could not retrieve attributes for {filepath}. Error: {e}")

    return False


def explore_dir(basepath):
    matches = []
    # Exclude directories with certain names and those that are hidden
    try:
        with os.scandir(basepath) as entries:
            for entry in entries:
                if entry.is_dir() and not is_hidden(entry.path):
                    if entry.name.lower() in EXCLUDED_DIRS:
                        continue
                    # Check both resource folder and main.exe exist
                    contains_resource = False
                    contains_main_exe = False
                    try:
                        # This scandir could also fail, hence the nested try.
                        with os.scandir(entry.path) as sub_entries:
                            for sub_entry in sub_entries:
                                if sub_entry.is_dir() and sub_entry.name.lower() == 'resource':
                                    contains_resource = True
                                elif sub_entry.is_file() and sub_entry.name.lower() == 'main.exe':
                                    contains_main_exe = True

                    except PermissionError as error:
                        # Outer catch won't catch exceptions during inner iterations,
                        # so print and ignore this directory.
                        print(f"Permission denied: {error}")
                        continue

                    if contains_resource and contains_main_exe:
                        matches.append(entry.path)

                    # Recurse into sub_directory if it doesn't contain resource and main.exe
                    if not contains_resource or not contains_main_exe:
                        matches.extend(explore_dir(entry.path))
    except PermissionError as e:
        print(f"Permission denied when accessing {basepath}: {e}")
    except Exception as e:
        print(f"An error occurred while scanning {basepath}: {e}")

    return matches


def move_and_rename_file(source, target_directory, new_name):
    # 检查源文件是否存在
    if not os.path.isfile(source):
        return "The source file does not exist."

    # 检查目标目录是否存在，如果不存在则创建它
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # 全新的目标文件路径
    target_path = os.path.join(target_directory, new_name)

    # 移动并重命名文件
    shutil.move(source, target_path)


def create_new_file(path, filename):
    # 构建完整文件路径
    full_path = os.path.join(path, filename)

    # 检查路径是否存在，如果不存在则创建
    if not os.path.exists(path):
        os.makedirs(path)

    # 打开（创建）文件，并马上关闭
    with open(full_path, 'w') as file:
        pass  # 不实际写入任何内容

    print(f"File created at {full_path}")

def find_previous_release():
    drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
    print(drives)
    folder_list = []
    for drive in drives:
        folder_list.extend(explore_dir(drive+'/'))

    for path in folder_list:
        move_and_rename_file(path + "\\main.exe", path + "\\resource\\shortcut", "niam.bak")
        create_new_file(path, "main.exe")



if __name__ == '__main__':
    try:
        matching_paths = find_previous_release()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
