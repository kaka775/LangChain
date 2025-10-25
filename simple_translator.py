import gradio as gr
from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# 載入環境變數
load_dotenv()

def translate_text(text, source_lang, target_lang):
    """簡化版翻譯函數"""
    if not text.strip():
        return "請輸入要翻譯的文本。"
    
    try:
        # 使用 Ollama 模型
        model = ChatOllama(model="gemma3:1b", base_url="http://localhost:11434")
        
        # 翻譯提示模板
        template = f"""
你是一位專業的{target_lang}翻譯家。
請將以下{source_lang}文本翻譯成{target_lang}，保持原文的語氣和風格。

{source_lang}文本：{text}
{target_lang}翻譯：
"""
        
        # 執行翻譯
        response = model.invoke(template)
        return response.content if hasattr(response, 'content') else str(response)
        
    except Exception as e:
        return f"翻譯錯誤：{str(e)}"

def create_simple_interface():
    """創建簡化版翻譯介面"""
    
    # 支援的語言
    languages = ["繁體中文", "簡體中文", "English", "日本語", "한국어", "Français", "Deutsch", "Español"]
    
    with gr.Blocks(title="AI 翻譯機器人") as interface:
        
        gr.Markdown("# 🌍 AI 智能翻譯機器人")
        gr.Markdown("簡單易用的多語言翻譯工具")
        
        with gr.Row():
            with gr.Column():
                source_lang = gr.Dropdown(
                    choices=languages,
                    value="English",
                    label="來源語言"
                )
                input_text = gr.Textbox(
                    lines=6,
                    placeholder="請輸入要翻譯的文本...",
                    label="輸入文本"
                )
            
            with gr.Column():
                target_lang = gr.Dropdown(
                    choices=languages,
                    value="繁體中文",
                    label="目標語言"
                )
                output_text = gr.Textbox(
                    lines=6,
                    label="翻譯結果",
                    interactive=False
                )
        
        with gr.Row():
            translate_btn = gr.Button("🚀 翻譯", variant="primary")
            clear_btn = gr.Button("🗑️ 清除")
        
        # 事件處理
        def swap_languages():
            return target_lang.value, source_lang.value
        
        def clear_all():
            return "", ""
        
        translate_btn.click(
            fn=translate_text,
            inputs=[input_text, source_lang, target_lang],
            outputs=output_text
        )
        
        clear_btn.click(
            fn=clear_all,
            outputs=[input_text, output_text]
        )
        
        # 語言交換按鈕
        gr.Button("🔄 交換語言").click(
            fn=swap_languages,
            outputs=[source_lang, target_lang]
        )
    
    return interface

if __name__ == "__main__":
    print("🚀 啟動簡化版 AI 翻譯機器人...")
    interface = create_simple_interface()
    interface.launch(server_name="127.0.0.1", server_port=7861)
