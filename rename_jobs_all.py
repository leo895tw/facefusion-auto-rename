import os
import json
from pathlib import Path
from datetime import datetime

# FaceFusion 主資料夾
BASE_DIR = Path(r"G:\AI\FaceFusion3.4.1")
# JSON 優先路徑（備份 JSON）
JSON_BACKUP_DIR = Path(r"I:\WQ-AI\outputs\json_backup")
# 已完成任務的 JSON 路徑
JOBS_COMPLETED_DIR = BASE_DIR / ".jobs" / "completed"

def extract_timestamp(json_file, data):
    """優先從檔名取 timestamp，如果不符合規則就用 date_created"""
    stem = Path(json_file).stem
    if stem.startswith("ui-"):
        # ui-2025-09-26-00-33-46 → 20250926-003346
        timestamp_raw = stem.split("ui-")[-1]
        timestamp = timestamp_raw.replace("-", "")
        return f"{timestamp[:8]}-{timestamp[8:]}"
    else:
        # 從 date_created 抽
        created = data.get("date_created", "")
        try:
            dt = datetime.fromisoformat(created.replace("Z", "+00:00"))
            return dt.strftime("%Y%m%d-%H%M%S")
        except Exception:
            return "unknown"

def rename_from_json(json_file):
    """讀取 JSON 檔，逐一處理裡面的每個 step 輸出檔"""
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    timestamp = extract_timestamp(json_file, data)
    steps = data.get("steps", [])

    for idx, step in enumerate(steps, start=1):
        args = step["args"]

        # 抽取來源與目標檔案名稱（stem = 去掉副檔名）
        source_stem = Path(args["source_paths"][0]).stem
        target_stem = Path(args["target_path"]).stem

        # 找到輸出檔案
        output_path = Path(args["output_path"])
        output_dir = output_path.parent

        # 新檔名格式
        new_name = f"{target_stem}-{source_stem}_{timestamp}.mp4"
        new_path = output_dir / new_name

        if output_path.exists():
            try:
                os.rename(output_path, new_path)
                print(f"[✓] 已重新命名：{output_path.name} → {new_name}")
            except Exception as e:
                print(f"[!] 改名失敗 {output_path.name} → {new_name}, 錯誤：{e}")
        else:
            print(f"[⚠] 找不到輸出檔：{output_path}")

def main():
    """掃描 JSON，優先從 json_backup，其次是 .jobs/completed"""
    search_dirs = []
    if JSON_BACKUP_DIR.exists():
        search_dirs.append(JSON_BACKUP_DIR)
    search_dirs.append(JOBS_COMPLETED_DIR)

    for folder in search_dirs:
        for json_file in folder.glob("*.json"):
            rename_from_json(json_file)

if __name__ == "__main__":
    main()
