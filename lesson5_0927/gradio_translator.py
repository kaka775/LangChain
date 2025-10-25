import gradio as gr
from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate
import time

# 初始化模型
model = OllamaLLM(model="gpt-oss:20b")

# 建立多變數的翻譯模板
complex_template = """
你是一位專業的{target_language}翻譯家，專精於{domain}領域。
請將以下{source_language}文本翻譯成{target_language}，並確保：
1. 保持原文的語氣和風格
2. 使用專業術語
3. 符合{target_language}的語言習慣

{source_language}文本：{text}
{target_language}翻譯：
"""

chat_prompt_template = ChatPromptTemplate.from_template(complex_template)

def translate_text(source_text, source_language, target_language, domain):
    """
    翻譯文本的主要函數
    """
    if not source_text.strip():
        return "請輸入要翻譯的文本。"
    
    try:
        # 格式化提示詞
        formatted_prompt = chat_prompt_template.format(
            target_language=target_language,
            source_language=source_language,
            domain=domain,
            text=source_text
        )
        
        # 調用模型進行翻譯
        response = model.invoke(formatted_prompt)
        
        # 清理回應文本，移除模板中的提示部分
        if target_language in response:
            # 提取翻譯結果
            lines = response.split('\n')
            for i, line in enumerate(lines):
                if target_language in line and "翻譯" in line:
                    # 返回翻譯結果部分
                    if i + 1 < len(lines):
                        return '\n'.join(lines[i+1:]).strip()
                    break
        
        return response.strip()
        
    except Exception as e:
        return f"翻譯過程中發生錯誤：{str(e)}"

def create_interface():
    """
    創建 Gradio 介面
    """
    
    # 語言選項
    languages = [
        "繁體中文", "簡體中文", "英文", "日文", "韓文", 
        "法文", "德文", "西班牙文", "義大利文", "俄文"
    ]
    
    # 專業領域選項
    domains = [
        "一般", "商業", "科技", "醫療", "法律", 
        "文學", "新聞", "學術", "技術文件", "行銷"
    ]
    
    with gr.Blocks(
        title="AI 專業翻譯助手",
        theme=gr.themes.Soft(),
        css="""
        .gradio-container {
            max-width: 1200px !important;
            margin: 0 auto !important;
        }
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        .header h1 {
            background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.5rem;
            font-weight: bold;
            margin: 0;
        }
        .header p {
            color: #666;
            font-size: 1.1rem;
            margin: 10px 0 0 0;
        }
        .translation-box {
            border-radius: 10px !important;
            border: 2px solid #e1e5e9 !important;
        }
        .result-box {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%) !important;
            border-radius: 10px !important;
        }
        """
    ) as interface:
        
        # 標題區域
        with gr.Row():
            with gr.Column():
                gr.HTML("""
                <div class="header">
                    <h1>🤖 AI 專業翻譯助手</h1>
                    <p>基於 Ollama GPT-OSS 模型的智能翻譯工具，支援多語言專業領域翻譯</p>
                </div>
                """)
        
        # 主要翻譯區域
        with gr.Row(equal_height=True):
            # 輸入區域
            with gr.Column(scale=1):
                gr.Markdown("### 📝 輸入設定")
                
                source_language = gr.Dropdown(
                    choices=languages,
                    value="英文",
                    label="源語言",
                    info="選擇要翻譯的原始語言"
                )
                
                target_language = gr.Dropdown(
                    choices=languages,
                    value="繁體中文",
                    label="目標語言",
                    info="選擇要翻譯成的目標語言"
                )
                
                domain = gr.Dropdown(
                    choices=domains,
                    value="一般",
                    label="專業領域",
                    info="選擇文本所屬的專業領域"
                )
                
                source_text = gr.Textbox(
                    label="要翻譯的文本",
                    placeholder="請輸入要翻譯的文本...",
                    lines=8,
                    elem_classes=["translation-box"],
                    info="支援長文本翻譯，建議一次輸入完整段落"
                )
                
                translate_btn = gr.Button(
                    "🚀 開始翻譯",
                    variant="primary",
                    size="lg",
                    elem_classes=["gradio-button"]
                )
            
            # 輸出區域
            with gr.Column(scale=1):
                gr.Markdown("### 📄 翻譯結果")
                
                result_text = gr.Textbox(
                    label="翻譯結果",
                    lines=8,
                    interactive=False,
                    elem_classes=["result-box"],
                    info="AI 翻譯結果將顯示在這裡"
                )
                
                # 操作按鈕
                with gr.Row():
                    clear_btn = gr.Button("🗑️ 清除", variant="secondary")
                    copy_btn = gr.Button("📋 複製結果", variant="secondary")
        
        # 範例區域
        with gr.Row():
            with gr.Column():
                gr.Markdown("### 💡 使用範例")
                
                examples = gr.Examples(
                    examples=[
                        ["The quarterly revenue increased by 15% compared to last year.", "英文", "繁體中文", "商業"],
                        ["Hello, how are you today?", "英文", "日文", "一般"],
                        ["La inteligencia artificial está revolucionando la medicina.", "西班牙文", "繁體中文", "科技"],
                        ["Le taux de chômage a diminué de 2% ce mois.", "法文", "繁體中文", "新聞"],
                        ["Die Maschine verwendet künstliche Intelligenz.", "德文", "繁體中文", "科技"]
                    ],
                    inputs=[source_text, source_language, target_language, domain],
                    label="點擊範例快速填入"
                )
        
        # 狀態顯示
        status = gr.Markdown("✅ 準備就緒，請輸入文本開始翻譯")
        
        # 事件處理
        def update_status(message):
            return f"🔄 {message}"
        
        def translate_with_status(*args):
            status_msg = update_status("正在翻譯中，請稍候...")
            yield status_msg, ""
            
            result = translate_text(*args)
            final_status = "✅ 翻譯完成！"
            
            yield final_status, result
        
        # 綁定事件
        translate_btn.click(
            fn=translate_with_status,
            inputs=[source_text, source_language, target_language, domain],
            outputs=[status, result_text]
        )
        
        clear_btn.click(
            fn=lambda: ("", "", "", "", "✅ 已清除，請輸入新文本"),
            outputs=[source_text, result_text, source_language, target_language, status]
        )
        
        copy_btn.click(
            fn=lambda text: "📋 結果已複製到剪貼板！" if text else "❌ 沒有可複製的內容",
            inputs=[result_text],
            outputs=[status]
        )
        
        # 鍵盤快捷鍵說明
        gr.Markdown("""
        ### ⌨️ 快捷操作
        - **Enter**: 在文本框中按 Enter 可以開始翻譯
        - **Ctrl/Cmd + Enter**: 快速翻譯
        """)
    
    return interface

if __name__ == "__main__":
    # 創建並啟動介面
    interface = create_interface()
    
    print("🚀 正在啟動 AI 翻譯助手...")
    print("📱 介面將在瀏覽器中自動開啟")
    print("🔗 本地訪問地址：http://127.0.0.1:7860")
    print("🌐 公開訪問地址將在啟動後顯示")
    
    interface.launch(
        server_name="0.0.0.0",  # 允許外部訪問
        server_port=7860,       # 端口號
        share=True,             # 創建公開連結
        show_error=True,        # 顯示錯誤信息
        show_tips=True,         # 顯示使用提示
        enable_queue=True       # 啟用隊列處理
    )

