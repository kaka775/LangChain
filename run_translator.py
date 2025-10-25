#!/usr/bin/env python3
"""
AI 翻譯機器人啟動腳本
提供兩個版本選擇：完整版和簡化版
"""

import sys
import subprocess
import os

def check_dependencies():
    """檢查必要的依賴項"""
    try:
        import gradio
        import langchain_ollama
        print("✅ 所有依賴項已安裝")
        return True
    except ImportError as e:
        print(f"❌ 缺少依賴項：{e}")
        print("請執行：pip install -r requirements.txt")
        return False

def run_full_version():
    """運行完整版翻譯機器人"""
    print("🚀 啟動完整版 AI 翻譯機器人...")
    print("🌐 介面將在 http://127.0.0.1:7860 開啟")
    print("按 Ctrl+C 停止服務")
    print("-" * 50)
    
    try:
        from ai_translator_bot import main
        main()
    except KeyboardInterrupt:
        print("\n👋 翻譯機器人已停止")
    except Exception as e:
        print(f"❌ 啟動失敗：{e}")

def run_simple_version():
    """運行簡化版翻譯機器人"""
    print("🚀 啟動簡化版 AI 翻譯機器人...")
    print("🌐 介面將在 http://127.0.0.1:7861 開啟")
    print("按 Ctrl+C 停止服務")
    print("-" * 50)
    
    try:
        from simple_translator import create_simple_interface
        interface = create_simple_interface()
        interface.launch(server_name="127.0.0.1", server_port=7861)
    except KeyboardInterrupt:
        print("\n👋 翻譯機器人已停止")
    except Exception as e:
        print(f"❌ 啟動失敗：{e}")

def main():
    """主選單"""
    print("=" * 60)
    print("🌍 AI 智能翻譯機器人")
    print("=" * 60)
    
    # 檢查依賴項
    if not check_dependencies():
        return
    
    print("\n請選擇要啟動的版本：")
    print("1. 完整版 (功能豐富，支援多模型)")
    print("2. 簡化版 (輕量快速)")
    print("3. 退出")
    
    while True:
        try:
            choice = input("\n請輸入選項 (1-3): ").strip()
            
            if choice == "1":
                run_full_version()
                break
            elif choice == "2":
                run_simple_version()
                break
            elif choice == "3":
                print("👋 再見！")
                break
            else:
                print("❌ 無效選項，請輸入 1、2 或 3")
                
        except KeyboardInterrupt:
            print("\n👋 再見！")
            break
        except Exception as e:
            print(f"❌ 發生錯誤：{e}")

if __name__ == "__main__":
    main()
