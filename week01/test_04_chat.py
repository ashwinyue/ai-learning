"""
04-chat.py 的测试用例
测试 query 函数的各种使用场景
"""

import sys
import os

# 添加当前目录到 Python 路径，以便导入 04-chat 模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 导入要测试的模块 (04-chat.py 重命名为 chat_04 以便导入)
import importlib.util
spec = importlib.util.spec_from_file_location("chat_04", "04-chat.py")
chat_04 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chat_04)
query = chat_04.query

def test_basic_query():
    """测试基本的查询功能"""
    print("=== 测试基本查询 ===")
    
    test_prompts = [
        "你好，请介绍一下自己",
        "帮我写一个简单的 Python 函数"
    ]
    
    for i, prompt in enumerate(test_prompts, 1):
        print(f"\n测试 {i}: {prompt}")
        print("-" * 50)
        try:
            response = query(prompt)
            print(f"响应: {response}")
            print(f"响应长度: {len(response)} 字符")
        except Exception as e:
            print(f"测试失败: {e}")
        print("-" * 50)

def test_empty_and_special_inputs():
    """测试空输入和特殊输入"""
    print("\n=== 测试特殊输入 ===")
    
    special_inputs = [
        "",  # 空字符串
        " ",  # 空格
        "你好" * 100,  # 长文本
        "Hello, how are you?",  # 英文
        "1 + 1 = ?",  # 数学问题
    ]
    
    for i, prompt in enumerate(special_inputs, 1):
        print(f"\n特殊测试 {i}: '{prompt[:50]}{'...' if len(prompt) > 50 else ''}'")
        print("-" * 50)
        try:
            response = query(prompt)
            print(f"响应: {response[:100]}{'...' if len(response) > 100 else ''}")
        except Exception as e:
            print(f"测试失败: {e}")
        print("-" * 50)

def test_conversation_flow():
    """测试对话流程"""
    print("\n=== 测试对话流程 ===")
    
    conversation = [
        "我想学习 Python 编程",
        "请推荐一些适合初学者的资源",
        "谢谢你的建议"
    ]
    
    for i, prompt in enumerate(conversation, 1):
        print(f"\n对话 {i}: {prompt}")
        print("-" * 50)
        try:
            response = query(prompt)
            print(f"响应: {response}")
        except Exception as e:
            print(f"对话测试失败: {e}")
        print("-" * 50)

def main():
    """运行所有测试"""
    print("开始测试 04-chat.py 的 query 函数")
    print("=" * 60)
    
    try:
        # 运行各种测试
        test_basic_query()
        test_empty_and_special_inputs()
        test_conversation_flow()
        
        print("\n" + "=" * 60)
        print("所有测试完成！")
        
    except Exception as e:
        print(f"测试过程中发生错误: {e}")

if __name__ == "__main__":
    main()