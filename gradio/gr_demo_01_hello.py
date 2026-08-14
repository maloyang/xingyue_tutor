import gradio as gr

# 1. 定義核心邏輯函數
def my_function(name):
    return f"Hello~ {name}"

# 2. 建立 Gradio 介面
demo = gr.Interface(
    fn=my_function,                   # 要呼叫的 Python 函數
    inputs=gr.Textbox(label="請輸入您的名字", placeholder="例如：小明"), # 輸入元件
    outputs=gr.Textbox(label="打招呼結果"),                          # 輸出元件
    title="Demo 01: 我的第一個 Gradio 網頁程式"
)

# 3. 啟動服務
if __name__ == "__main__":
    demo.launch()