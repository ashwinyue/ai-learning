from dotenv import load_dotenv
import os
from openai import OpenAI

# 加载环境变量
load_dotenv()

# 获取API密钥
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    print("错误：未找到OPENAI_API_KEY环境变量")
    exit(1)

# 创建OpenAI客户端，配置为使用Kimi的API地址
client = OpenAI(
    api_key=api_key,
    base_url="https://api.moonshot.cn/v1"  # Kimi的API地址
)

print("正在连接到Kimi API...")

try:
    # 发送一个简单的聊天请求
    response = client.chat.completions.create(
        model="moonshot-v1-8k",  # Kimi的模型名称
        messages=[
            {"role": "system", "content": "你是一个友好的AI助手。"},
            {"role": "user", "content": "你好！请简单介绍一下你自己。"}
        ],
        temperature=0.7,
        max_tokens=500
    )
    
    # 打印响应
    print("\n=== Kimi API 响应 ===")
    print(f"模型: {response.model}")
    print(f"使用token: {response.usage.total_tokens}")
    print(f"回复内容: {response.choices[0].message.content}")
    
except Exception as e:
    print(f"错误: {e}")
    print("请检查：")
    print("1. API密钥是否正确")
    print("2. 网络连接是否正常")
    print("3. Kimi API服务是否可用")

print("\n演示完成！")