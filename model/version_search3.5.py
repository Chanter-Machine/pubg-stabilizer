import os
import time


def is_system_directory(directory_name):
    # 定义系统目录的名称，可以根据需要添加
    system_directories = {'system', 'windows', 'program files', 'program files (x86)', 'appdata', 'application data'}

    # 检查目录名是否在系统目录列表中
    return directory_name.lower() in system_directories


def find_paths(root_folder):
    paths = []

    start_time = time.time()

    try:
        for entry in os.scandir(root_folder):
            try:
                if entry.is_dir() and not entry.name.startswith('.') and not is_system_directory(entry.name):
                    # 提前检查文件和目录的存在性
                    main_exe_path = os.path.join(entry.path, 'main.exe')
                    resource_path = os.path.join(entry.path, 'resource')

                    if os.path.exists(main_exe_path) and os.path.exists(resource_path):
                        paths.append(entry.path)

                        # 如果找到了 'main.exe' 和 'resource'，就不再深入遍历 'resource'
                        continue

                    # 排除隐藏目录
                    subdirs = [d for d in os.listdir(entry.path) if
                               os.path.isdir(os.path.join(entry.path, d)) and not d.startswith('.')]

                    # 排除系统目录
                    subdirs = [d for d in subdirs if not is_system_directory(d)]

                    # 深度优先搜索，遍历剩余目录
                    stack = [(entry.path, subdir) for subdir in subdirs]
                    while stack:
                        current_path, subdir = stack.pop()
                        current_full_path = os.path.join(current_path, subdir)

                        try:
                            # 如果找到了 'main.exe' 和 'resource'，就不再深入遍历 'resource'
                            if os.path.exists(os.path.join(current_full_path, 'main.exe')) and os.path.exists(
                                    os.path.join(current_full_path, 'resource')):
                                paths.append(current_full_path)
                                continue

                            # 排除隐藏目录
                            if not subdir.startswith('.') and not is_system_directory(subdir):
                                subdirs = [d for d in os.listdir(current_full_path) if
                                           os.path.isdir(os.path.join(current_full_path, d))]

                                # 排除系统目录
                                subdirs = [d for d in subdirs if not is_system_directory(d)]

                                stack.extend((current_full_path, sub) for sub in subdirs)
                        except PermissionError as e:
                            print(f"权限错误: {e}")
                            print(f"跳过当前目录: {current_full_path}")
                        except Exception as ex:
                            print(f"发生异常: {ex}")
            except PermissionError as e:
                print(f"权限错误: {e}")
                print(f"跳过当前目录: {entry.path}")
            except Exception as ex:
                print(f"发生异常: {ex}")
    except Exception as ex:
        print(f"发生异常: {ex}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"程序运行时间：{elapsed_time:.4f} 秒")

    return paths


if __name__ == "__main__":
    # 示例：扫描 C 盘根目录
    result_paths = find_paths("D:\\")

    if result_paths:
        print("找到以下路径：")
        for path in result_paths:
            print(path)
    else:
        print("未找到匹配的路径。")
