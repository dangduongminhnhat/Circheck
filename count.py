import os


def count_files_in_subfolders(root_dir):
    total_files = 0
    # Duyệt qua tất cả các thư mục con của thư mục root_dir
    for root, dirs, files in os.walk(root_dir):
        # Loại bỏ thư mục 'libs' nếu không muốn tính
        if 'libs' in dirs:
            # Điều này giúp loại bỏ thư mục 'libs' khỏi quá trình duyệt
            dirs.remove('libs')
        # Đếm tất cả các tệp trong thư mục hiện tại
        total_files += len(files)
    return total_files


# Thay đổi thành đường dẫn thư mục benchmarks của bạn
benchmark_dir = "./benchmarks"
total_files = count_files_in_subfolders(benchmark_dir)

print(
    f"Total number of files in subfolders of '{benchmark_dir}': {total_files}")
