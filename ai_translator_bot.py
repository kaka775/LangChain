import gradio as gr
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# 載入環境變數
load_dotenv()

class AITranslatorBot:
    def __init__(self):
        self.models = {
            "Ollama (Gemma3:1b)": ChatOllama(model="gemma3:1b", base_url="http://localhost:11434"),
            "Google Gemini": ChatGoogleGenerativeAI(model="gemini-2.5-flash"),
            "OpenAI GPT": ChatOpenAI(model="gpt-3.5-turbo")
        }
        
        # 支援的語言選項
        self.languages = {
            "繁體中文": "繁體中文",
            "簡體中文": "簡體中文", 
            "English": "英文",
            "日本語": "日文",
            "한국어": "韓文",
            "Français": "法文",
            "Deutsch": "德文",
            "Español": "西班牙文",
            "Italiano": "義大利文",
            "Português": "葡萄牙文",
            "Русский": "俄文",
            "العربية": "阿拉伯文"
        }
        
        # 建立翻譯提示模板
        self.translation_template = """
你是一位專業的{target_language}翻譯家，具有豐富的語言學背景和多語言翻譯經驗。

請將以下{source_language}文本翻譯成{target_language}，並確保：
1. 保持原文的語氣、風格和語調
2. 使用自然流暢的{target_language}表達
3. 保持專業術語的準確性
4. 符合{target_language}的語言習慣和文化背景
5. 如果原文包含特殊格式（如標點符號、換行等），請保持相同的格式

{source_language}文本：
{text}

{target_language}翻譯：
"""

    def translate_text(self, text, source_lang, target_lang, model_name, temperature=0.7):
        """執行翻譯功能"""
        if not text.strip():
            return "請輸入要翻譯的文本。"
        
        try:
            # 選擇模型
            model = self.models.get(model_name)
            if not model:
                return f"錯誤：找不到模型 {model_name}"
            
            # 建立提示模板
            prompt_template = ChatPromptTemplate.from_template(self.translation_template)
            
            # 格式化提示
            formatted_prompt = prompt_template.format_messages(
                source_language=source_lang,
                target_language=target_lang,
                text=text
            )
            
            # 設定模型參數（如果支援）
            if hasattr(model, 'temperature'):
                model.temperature = temperature
            
            # 執行翻譯
            response = model.invoke(formatted_prompt)
            
            # 提取翻譯結果
            if hasattr(response, 'content'):
                return response.content
            else:
                return str(response)
                
        except Exception as e:
            return f"翻譯過程中發生錯誤：{str(e)}"

    def create_interface(self):
        """創建 Gradio 介面"""
        
        # 自定義 CSS 樣式
        css = """
        .gradio-container {
            font-family: 'Microsoft JhengHei', 'PingFang TC', 'Helvetica Neue', Arial, sans-serif;
        }
        .main-header {
            text-align: center;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .translation-box {
            border: 2px solid #e1e5e9;
            border-radius: 8px;
            padding: 15px;
            background-color: #f8f9fa;
        }
        .output-box {
            border: 2px solid #28a745;
            border-radius: 8px;
            padding: 15px;
            background-color: #d4edda;
        }
        """
        
        with gr.Blocks(css=css, title="AI 智能翻譯機器人") as interface:
            
            # 標題區域
            gr.HTML("""
            <div class="main-header">
                <h1>🌍 AI 智能翻譯機器人</h1>
                <p>支援多種語言互譯，提供專業級翻譯服務</p>
            </div>
            """)
            
            with gr.Row():
                with gr.Column(scale=1):
                    # 模型選擇
                    model_dropdown = gr.Dropdown(
                        choices=list(self.models.keys()),
                        value="Ollama (Gemma3:1b)",
                        label="🤖 選擇 AI 模型",
                        info="選擇您偏好的翻譯模型"
                    )
                    
                    # 溫度設定
                    temperature_slider = gr.Slider(
                        minimum=0.1,
                        maximum=1.0,
                        value=0.7,
                        step=0.1,
                        label="🎯 創意度 (Temperature)",
                        info="較高值 = 更有創意，較低值 = 更保守"
                    )
                
                with gr.Column(scale=2):
                    # 語言選擇
                    with gr.Row():
                        source_lang = gr.Dropdown(
                            choices=list(self.languages.keys()),
                            value="English",
                            label="📝 來源語言"
                        )
                        
                        target_lang = gr.Dropdown(
                            choices=list(self.languages.keys()),
                            value="繁體中文",
                            label="🎯 目標語言"
                        )
                    
                    # 語言交換按鈕
                    swap_btn = gr.Button("🔄 交換語言", size="sm")
            
            # 翻譯區域
            with gr.Row():
                with gr.Column():
                    gr.HTML('<div class="translation-box">')
                    input_text = gr.Textbox(
                        lines=8,
                        placeholder="請在此輸入要翻譯的文本...",
                        label="📝 輸入文本",
                        show_label=True
                    )
                    gr.HTML('</div>')
                
                with gr.Column():
                    gr.HTML('<div class="output-box">')
                    output_text = gr.Textbox(
                        lines=8,
                        label="🎯 翻譯結果",
                        show_label=True,
                        interactive=False
                    )
                    gr.HTML('</div>')
            
            # 控制按鈕
            with gr.Row():
                translate_btn = gr.Button("🚀 開始翻譯", variant="primary", size="lg")
                clear_btn = gr.Button("🗑️ 清除內容", variant="secondary")
            
            # 範例文本
            with gr.Accordion("💡 範例文本", open=False):
                gr.Examples(
                    examples=[
                        ["Hello, how are you today? I hope you're having a wonderful day!"],
                        ["The quick brown fox jumps over the lazy dog."],
                        ["人工智慧正在改變我們的世界，帶來無限的可能性。"],
                        ["La vie est belle et pleine de surprises."],
                        ["こんにちは、元気ですか？"]
                    ],
                    inputs=input_text,
                    label="點擊範例快速開始"
                )
            
            # 功能說明
            with gr.Accordion("ℹ️ 使用說明", open=False):
                gr.Markdown("""
                ### 🎯 功能特色
                - **多模型支援**：整合 Ollama、Google Gemini、OpenAI 等頂級 AI 模型
                - **多語言翻譯**：支援 12+ 種主要語言互譯
                - **智能調節**：可調整創意度參數，獲得不同風格的翻譯
                - **即時翻譯**：快速準確的翻譯結果
                - **用戶友好**：直觀的現代化介面設計
                
                ### 🚀 使用步驟
                1. 選擇您偏好的 AI 模型
                2. 設定來源語言和目標語言
                3. 輸入要翻譯的文本
                4. 點擊「開始翻譯」按鈕
                5. 查看翻譯結果
                
                ### 💡 小貼士
                - 較高的創意度設定會產生更有創意的翻譯
                - 較低的創意度設定會產生更保守、準確的翻譯
                - 可以點擊「交換語言」快速切換翻譯方向
                """)
            
            # 事件處理
            def swap_languages():
                return target_lang.value, source_lang.value
            
            def clear_all():
                return "", ""
            
            # 綁定事件
            swap_btn.click(
                fn=swap_languages,
                outputs=[source_lang, target_lang]
            )
            
            clear_btn.click(
                fn=clear_all,
                outputs=[input_text, output_text]
            )
            
            translate_btn.click(
                fn=self.translate_text,
                inputs=[input_text, source_lang, target_lang, model_dropdown, temperature_slider],
                outputs=output_text
            )
        
        return interface

def main():
    """主程式入口"""
    print("🚀 正在啟動 AI 翻譯機器人...")
    
    # 創建翻譯機器人實例
    translator = AITranslatorBot()
    
    # 創建並啟動介面
    interface = translator.create_interface()
    
    print("✅ AI 翻譯機器人已準備就緒！")
    print("🌐 介面將在 http://127.0.0.1:7860 開啟")
    
    # 啟動介面
    interface.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=False,
        show_error=True
    )

if __name__ == "__main__":
    main()
