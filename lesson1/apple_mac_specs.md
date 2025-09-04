### Apple Mac 系列機型規格與比較（含 Python 範例）

> 檔案用途：以結構化方式整理 Apple Mac 全系列（MacBook Air / MacBook Pro / iMac / Mac mini / Mac Studio / Mac Pro）的常見規格欄位，並提供 Python 程式碼生成比較表與彙總。可於本倉庫的 Jupyter Notebook 執行，或直接在本機 `python` 環境執行。

---

### 內容說明

- 本文件包含：
  - 規格欄位設計與示例資料（可自行增修）
  - 以 `pandas` 建立表格、排序與彙總比較的 Python 程式碼
  - 產生各系列精簡對照表與依需求篩選的範例

- 注意：實際規格會隨官方更新而變動，請依需求持續補充或修訂下方 `DATA`。本示例以「代表性、保守」資訊為主，僅供快速比較與教學用途。

---

### 快速開始（Jupyter / Python）

```python
# 建議先安裝套件（如尚未安裝）：
# pip install pandas tabulate

from dataclasses import dataclass, asdict
from typing import List, Optional
import pandas as pd


@dataclass
class MacSpec:
    series: str                 # 系列：MacBook Air / MacBook Pro / iMac / Mac mini / Mac Studio / Mac Pro
    model: str                  # 機型名稱或尺寸：如 "13-inch", "14-inch", "24-inch"
    chip: str                   # 晶片：如 M2 / M3 / M3 Pro / M3 Max / M2 Ultra 等
    year: Optional[int]         # 發表年份（可留空）
    cpu_cores: Optional[int]    # CPU 核心數（可留空）
    gpu_cores: Optional[int]    # GPU 核心數（可留空）
    memory_options: str         # 記憶體選項：如 "8/16/24 GB" 或 "32~192 GB"
    storage_options: str        # 儲存選項：如 "256 GB ~ 2 TB"
    display: Optional[str]      # 螢幕：尺寸、面板與解析度，桌機可填機身支援（或留空）
    battery_hours: Optional[int]# 續航（筆電適用，單位：小時）
    weight_kg: Optional[float]  # 重量（公斤）
    ports: str                  # 連接埠摘要
    wireless: str               # 無線規格摘要
    notes: Optional[str]        # 備註


def to_dataframe(specs: List[MacSpec]) -> pd.DataFrame:
    df = pd.DataFrame([asdict(s) for s in specs])
    # 欄位順序（可依喜好調整）
    columns = [
        "series", "model", "chip", "year", "cpu_cores", "gpu_cores",
        "memory_options", "storage_options", "display", "battery_hours",
        "weight_kg", "ports", "wireless", "notes",
    ]
    return df.reindex(columns=columns)


# ---------------------------------------------
# 示例資料（請依實際需求持續更新/擴充）
# ---------------------------------------------
DATA: List[MacSpec] = [
    # MacBook Air（代表性示例）
    MacSpec(
        series="MacBook Air",
        model="13-inch",
        chip="M2",
        year=2022,
        cpu_cores=8,
        gpu_cores=8,
        memory_options="8/16/24 GB",
        storage_options="256 GB ~ 2 TB",
        display='13.6" Liquid Retina',
        battery_hours=18,
        weight_kg=1.24,
        ports="2x Thunderbolt / USB 4, 3.5mm",
        wireless="Wi‑Fi 6, Bluetooth 5.x",
        notes="風扇less、輕薄攜帶",
    ),
    MacSpec(
        series="MacBook Air",
        model="15-inch",
        chip="M2",
        year=2023,
        cpu_cores=8,
        gpu_cores=10,
        memory_options="8/16/24 GB",
        storage_options="256 GB ~ 2 TB",
        display='15.3" Liquid Retina',
        battery_hours=18,
        weight_kg=1.51,
        ports="2x Thunderbolt / USB 4, 3.5mm",
        wireless="Wi‑Fi 6, Bluetooth 5.x",
        notes="較大螢幕、仍主打輕薄",
    ),

    # MacBook Pro（代表性示例）
    MacSpec(
        series="MacBook Pro",
        model="14-inch",
        chip="M3",
        year=2023,
        cpu_cores=None,  # 因不同款式差異，可留空
        gpu_cores=None,
        memory_options="8/16/24/36+ GB（依晶片等級）",
        storage_options="512 GB ~ 8 TB",
        display='14.2" Liquid Retina XDR',
        battery_hours=18,
        weight_kg=1.6,
        ports="3x Thunderbolt, HDMI, SDXC, MagSafe 3",
        wireless="Wi‑Fi 6E（或以上）, Bluetooth 5.x",
        notes="XDR 顯示器、較多連接埠",
    ),
    MacSpec(
        series="MacBook Pro",
        model="16-inch",
        chip="M3 Pro / M3 Max",
        year=2023,
        cpu_cores=None,
        gpu_cores=None,
        memory_options="18/36/48/64+ GB（依晶片等級）",
        storage_options="512 GB ~ 8 TB",
        display='16.2" Liquid Retina XDR',
        battery_hours=22,
        weight_kg=2.1,
        ports="3x Thunderbolt, HDMI, SDXC, MagSafe 3",
        wireless="Wi‑Fi 6E（或以上）, Bluetooth 5.x",
        notes="效能取向、較長續航（影片播放）",
    ),

    # iMac（代表性示例）
    MacSpec(
        series="iMac",
        model="24-inch",
        chip="Apple Silicon（例：M3）",
        year=2023,
        cpu_cores=None,
        gpu_cores=None,
        memory_options="8/16/24 GB",
        storage_options="256 GB ~ 2 TB",
        display='24" 4.5K Retina',
        battery_hours=None,
        weight_kg=4.5,
        ports="Thunderbolt / USB 4（依機型數量不同）、USB-A（部分）、乙太網（選配）",
        wireless="Wi‑Fi 6E（或以上）, Bluetooth 5.x",
        notes="一體機、彩色外觀",
    ),

    # Mac mini（代表性示例）
    MacSpec(
        series="Mac mini",
        model="—",
        chip="M2 / M2 Pro（或更新）",
        year=2023,
        cpu_cores=None,
        gpu_cores=None,
        memory_options="8/16/32+ GB（依晶片等級）",
        storage_options="256 GB ~ 8 TB（依配置）",
        display=None,
        battery_hours=None,
        weight_kg=1.2,
        ports="Thunderbolt / USB 4、USB-A、HDMI、乙太網、3.5mm",
        wireless="Wi‑Fi 6E（或以上）, Bluetooth 5.x",
        notes="小型桌機，外接螢幕",
    ),

    # Mac Studio（代表性示例）
    MacSpec(
        series="Mac Studio",
        model="—",
        chip="M2 Max / M2 Ultra（或更新）",
        year=2023,
        cpu_cores=None,
        gpu_cores=None,
        memory_options="32/64/128/192 GB（依 Ultra 等級）",
        storage_options="512 GB ~ 8 TB",
        display=None,
        battery_hours=None,
        weight_kg=2.7,
        ports="Thunderbolt（前後多組）、USB-A、HDMI、SD、乙太網、3.5mm",
        wireless="Wi‑Fi 6E（或以上）, Bluetooth 5.x",
        notes="高效能創作與開發工作站",
    ),

    # Mac Pro（代表性示例）
    MacSpec(
        series="Mac Pro",
        model="塔式 / 機架",
        chip="Apple Silicon（例：M2 Ultra / M3 Ultra）",
        year=2023,
        cpu_cores=None,
        gpu_cores=None,
        memory_options="64~192+ GB（依 Ultra 等級）",
        storage_options="1 TB ~ 8+ TB",
        display=None,
        battery_hours=None,
        weight_kg=None,
        ports="多組 Thunderbolt、PCIe 擴充（Apple Silicon 限制）、HDMI、乙太網",
        wireless="Wi‑Fi 6E（或以上）, Bluetooth 5.x",
        notes="極致擴充與 I/O（相對於 Studio）",
    ),
]


df = to_dataframe(DATA)

# 依系列與尺寸/型號排序，方便瀏覽
df_sorted = df.sort_values(by=["series", "model", "chip"], na_position="last")
print("\n=== 全部規格列表（節錄） ===")
print(df_sorted.to_string(index=False))


# 範例一：各系列「重量中位數」與「最大續航（筆電適用）」
summary = (
    df_sorted
    .groupby("series")
    .agg(
        weight_median_kg=("weight_kg", "median"),
        max_battery_hours=("battery_hours", "max"),
        models=("model", "nunique"),
    )
    .reset_index()
    .sort_values(by=["series"]) 
)

print("\n=== 各系列摘要（重量中位數 / 最大續航 / 機型數） ===")
print(summary.to_string(index=False))


# 範例二：只看筆電（MacBook Air / MacBook Pro），依續航由高到低
laptops = df_sorted[df_sorted["series"].isin(["MacBook Air", "MacBook Pro"])].copy()
laptops = laptops.sort_values(by=["battery_hours", "weight_kg"], ascending=[False, True])

print("\n=== 筆電續航與重量（高續航優先） ===")
print(laptops[["series", "model", "chip", "battery_hours", "weight_kg"]].to_string(index=False))


# 範例三：欄位過濾與輸出 CSV（可選）
# df_sorted.to_csv("mac_specs_export.csv", index=False)
```

---

### 建議欄位與維護指南

- 規格欄位建議持續維護與擴充（例如新增：顯示器亮度、解析度、外接螢幕上限、Thunderbolt 版本、HDMI 規格、乙太網速度、Touch ID / FaceTime 鏡頭規格等）。
- 每逢 Apple 發佈會或官網更新，調整 `DATA` 中對應機型的：
  - **chip**：晶片等級與世代（M2/M3/M4… 及 Pro/Max/Ultra）
  - **memory_options**：最大記憶體容量與組態
  - **storage_options**：最大 SSD 容量
  - **ports**：連接埠數量與版本（如 Thunderbolt 4/5、HDMI 2.1 等）
  - **wireless**：Wi‑Fi 版本（6 / 6E / 7）、藍牙版本
  - **display / battery_hours / weight_kg**：面板、續航與重量

---

### 常見比較需求（可用上述 DataFrame 快速達成）

- 筆電續航力排序與重量權衡
- 桌機 I/O 密度與擴充能力（Mac Studio vs Mac Pro）
- 同系列不同尺寸（如 13/14/15/16 吋）之顯示、重量與 I/O 差異
- 不同晶片等級（標準/Pro/Max/Ultra）之記憶體上限與 GPU 核心差異

---

### 來源建議

- 請以 Apple 官網技術規格頁為準（各機型 Technical Specifications）。
- 若需歷代機型，可參考 Apple 新品發表與媒體測試報告，並清楚標注年份與晶片世代。


