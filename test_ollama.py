#!/usr/bin/env python3
"""
測試 langchain_ollama 模組導入
"""

try:
    from langchain.prompts import ChatPromptTemplate
    from langchain.schema.output_parser import StrOutputParser
    from langchain_ollama.llms import OllamaLLM
    
    print("✅ 所有模組導入成功！")
    
    # 測試模型創建
    model = OllamaLLM(model="gemma3:1b")
    print("✅ OllamaLLM 模型創建成功！")
    print(f"✅ 模型名稱: {model.model}")
    
except ImportError as e:
    print(f"❌ 導入錯誤: {e}")
    print("請確保在正確的 Python 環境中運行此腳本")
except Exception as e:
    print(f"❌ 其他錯誤: {e}")

print("\n🎉 測試完成！")
