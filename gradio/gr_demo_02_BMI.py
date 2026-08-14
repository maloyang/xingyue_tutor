# https://gradio.app/docs --> 官方說明文件

import gradio as gr

# 1. 定義 BMI 計算邏輯
def calculate_bmi(height_cm, weight_kg):
    # 檢查輸入數值是否合法
    if height_cm <= 0 or weight_kg <= 0:
        return "身高與體重必須大於 0！"
    
    # 單位轉換：公分轉公尺
    height_m = height_cm / 100
    # 計算 BMI
    bmi = weight_kg / (height_m ** 2)
    
    # 判斷體重狀態
    if bmi < 18.5:
        status = "體重過輕"
    elif 18.5 <= bmi < 24:
        status = "正常範圍"
    elif 24 <= bmi < 27:
        status = "過重"
    else:
        status = "肥胖"
        
    return f"您的 BMI 指數為：{bmi:.2f} （狀態：{status}）"

# 2. 建立 Gradio 介面
demo = gr.Interface(
    fn=calculate_bmi,
    # 當有多個輸入時，使用 Python list 依序傳入
    inputs=[
        gr.Number(label="身高 (公分)", value=170),
        gr.Number(label="體重 (公斤)", value=65)
    ],
    outputs=gr.Textbox(label="計算結果"),
    title="Demo 02: BMI 健康指數計算器",
    description="請輸入身高與體重，系統將為您計算 BMI 指數。"
)

# 3. 啟動服務
if __name__ == "__main__":
    demo.launch()