import time
import shutil
import subprocess
import sys
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 路徑設定
BASE_DIR = Path(r"G:\AI\FaceFusion3.4.1")
COMPLETED_DIR = BASE_DIR / ".jobs" / "completed"
JSON_BACKUP_DIR = Path(r"I:\WQ-AI\outputs\json_backup")
RENAME_SCRIPT = BASE_DIR / "rename_jobs_all.py"

# 確保備份資料夾存在
JSON_BACKUP_DIR.mkdir(parents=True, exist_ok=True)

class JsonHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        file_path = Path(event.src_path)
        if file_path.suffix.lower() == ".json":
            print(f"[監控] 偵測到新 JSON: {file_path.name}")

            # 複製 JSON 到備份資料夾
            backup_path = JSON_BACKUP_DIR / file_path.name
            try:
                shutil.copy2(file_path, backup_path)
                print(f"[動作] 備份 JSON 到: {backup_path}")
            except Exception as e:
                print(f"[錯誤] 複製 JSON 失敗: {e}")
                return

            # 執行 rename_jobs_all.py
            try:
                subprocess.run([sys.executable, str(RENAME_SCRIPT)], check=True)
                print("[完成] 已執行 rename_jobs_all.py")
            except Exception as e:
                print(f"[錯誤] 執行 rename_jobs_all.py 失敗: {e}")

def main():
    event_handler = JsonHandler()
    observer = Observer()
    observer.schedule(event_handler, str(COMPLETED_DIR), recursive=False)
    observer.start()
    print("[監控] 開始監控 JSON ... (Ctrl+C 結束)")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n[監控] 停止監控")

    observer.join()

if __name__ == "__main__":
    main()
