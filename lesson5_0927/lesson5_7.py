from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate

model = OllamaLLM(model="geamm3:1b")



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

formatted_prompt = chat_prompt_template.format(
    target_language="繁體中文",
    source_language="英文",
    domain="商業",
    text="The quarterly revenue increased by 15% compared to last year."
    )

print("=== 多變數複雜模板範例 ===")
print(formatted_prompt)
print("\n" + "="*50)
print("Ollama gpt-oss:20b模型回應:")

response = model.invoke(formatted_prompt)
print(response)