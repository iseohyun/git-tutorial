import os

def find_largest_files(directory, top_n=10):
    # 모든 파일 경로와 크기를 저장
    files_with_size = []

    # 하위 폴더 포함 모든 파일 탐색
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                filesize = os.path.getsize(filepath)
                files_with_size.append((filepath, filesize))
            except OSError:
                # 파일 크기 확인 실패 시 무시
                pass

    # 크기 기준으로 정렬
    files_with_size.sort(key=lambda x: x[1], reverse=True)

    # 상위 N개 출력
    for i, (filepath, filesize) in enumerate(files_with_size[:top_n], 1):
        print(f"{i}. {filepath} ({filesize / (1024 ** 2):.2f} MB)")

# 현재 디렉토리에서 실행
find_largest_files(os.getcwd())
# find_largest_files('C:\\Users\\iseoh\\Downloads\\myProject')
# find_largest_files('C:\\Users\\iseoh\\OneDrive\\Document\\git\\html')
