import subprocess
import os

print(f"{'Hash':<40} {'Type':<10} {'File Name':<30}")
print("-" * 80)

# 파일 위치를 기준
script_dir = os.path.dirname(os.path.abspath(__file__))
# 현재 명령 프롬프트를 기준
script_dir = os.getcwd()

result = subprocess.run(
    ["git", "rev-list", "--all", "--objects"],
    capture_output=True,
    text=True,
    cwd=script_dir
)
for line in result.stdout.strip().split("\n"):
    parts = line.split(" ", 1)
    obj_hash = parts[0]
    file_name = parts[1] if len(parts) > 1 else "(no file)"

    obj_type = subprocess.run(
        ["git", "cat-file", "-t", obj_hash], capture_output=True, text=True
    ).stdout.strip()
    print(f"{obj_hash:<40} {obj_type:<10} {file_name:<30}")
