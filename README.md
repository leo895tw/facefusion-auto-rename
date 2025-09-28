# 🎬 FaceFusion 自動化更名系統 (FaceFusion Auto-Rename System)

這是一套針對 **FaceFusion**（臉部替換工具）的自動化更名流程，  
解決官方輸出影片名稱為亂數檔名的問題。  
This is an **auto-renaming system for FaceFusion**, solving the problem of random hash-like output filenames.

---

## ✨ 功能特色 (Features)
- 自動將輸出影片改名為 / Automatically rename output video as:
  ```
  {target_stem}-{source_stem}_{timestamp}.mp4
  ```
  範例 Example:
  ```
  xxjess_01-dance_01_20250925-221954.mp4
  ```

- JSON 備份機制：所有 `.jobs/completed` 產生的 JSON 會被複製到 `outputs/json_backup`，不怕遺失。  
  JSON backup: all job JSON files will be copied to `outputs/json_backup` for safety.

- 全自動化：FaceFusion 輸出完成後，幾秒內自動完成更名。  
  Fully automated: Renaming happens a few seconds after FaceFusion finishes rendering.

- UI 備援：FaceFusion UI 上有「強制更名 (Force Rename)」按鈕，萬一自動化失效可手動補救。  
  UI fallback: Manual **Force Rename** button inside FaceFusion UI.

- 一鍵啟動：透過 `.bat` 檔同時啟動 FaceFusion + 背景監控。  
  One-click startup: `.bat` launches FaceFusion + background watcher together.

---

## 📂 檔案結構 (Project Structure)
```
facefusion-auto-rename/
├─ README.md
├─ rename_jobs_all.py       # 通用版自動更名程式 / General rename script
├─ json_watcher.py          # JSON 監控程式 / JSON watcher script
├─ 官方版+facefusion 3.4.1.bat  # 啟動批次檔 (同時跑 FF+監控) / Batch file for startup
```

---

## 🚀 使用方式 (How to Use)

### 1. 安裝需求 (Install requirement)
```bash
pip install watchdog
```

### 2. 啟動方式 (Start)
直接雙擊 / Double-click:
```
官方版+facefusion 3.4.1.bat
```
- FaceFusion UI 會開啟 / FaceFusion UI will open  
- 背景同時啟動 JSON 監控程式 / JSON watcher starts in background

### 3. 運作流程 (Workflow)
1. FaceFusion 輸出完成 → `.jobs/completed` 產生 JSON  
   After FaceFusion finishes → JSON file generated in `.jobs/completed`
2. `json_watcher.py` 偵測到新 JSON → 複製到 `outputs/json_backup`  
   JSON watcher detects → copy JSON into `outputs/json_backup`
3. 自動執行 `rename_jobs_all.py` → 將影片亂數檔名更正  
   Auto-run rename script → rename random hash filename

---

## ⚠ 注意事項 (Notes)
- 輸出路徑 (output_path) 可自訂，例如：`I:\WQ-AI\outputs`。  
  Output path is **user-defined**, e.g. `I:\WQ-AI\outputs`.  
- 使用前請依照自己的環境修改路徑。  
  Please modify paths according to your environment.  

---

## 📜 授權與免責 (License & Disclaimer)

- 本專案基於 **FaceFusion**（原始專案：https://github.com/facefusion/facefusion），授權方式為 OpenRAIL-AS 及各資源原始授權。  
- This project is based on **FaceFusion** (original project: https://github.com/facefusion/facefusion), licensed under OpenRAIL-AS and the original licenses of its assets.  

### 使用範圍 | Usage Scope
- 僅限個人學習、研究與實驗用途，不得用於商業行為。  
- For **personal learning, research, and experimental use only**, not for commercial purposes.  

### 修改備註 | Modification Notes
- 本版本資料夾名稱：`FaceFusion3.4.1 (個人版)`    
- 修改範圍：新增自動化更名機制、路徑與批次檔設定；未更改原始專案的核心版權標示。  
- Folder Name: `FaceFusion3.4.1 (Personal Edition)`  
- Scope of Changes: Added auto-rename mechanism, adjusted paths and batch file settings; **no changes to core copyright notices**.  

### 免責聲明 | Disclaimer
- 本修改版非官方發佈，與 FaceFusion 原作者無關。  
- This modified version is **unofficial** and has no relation to the original FaceFusion authors.  
- 本人尊重原作者的智慧財產權與授權條款，如有任何侵權或不當使用疑慮，請透過適當管道通知，我將立即停止使用或移除相關內容。  
- I respect all intellectual property rights and license terms of the original authors. If there are any concerns regarding infringement or improper use, please notify me through proper channels, and I will promptly stop using or remove the content.  
