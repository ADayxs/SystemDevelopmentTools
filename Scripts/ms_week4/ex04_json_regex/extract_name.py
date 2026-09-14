"""
对比：用正则表达式 vs 用 JSON 解析器从 JSON 中提取 name 字段。
Missing Semester 代码质量课程练习 6。
"""
import re
import json
import sys


def extract_with_regex(text):
    """贪婪量词问题：第一次尝试会匹配过多内容。"""
    # 错误（贪婪）: "name":\s*"(.*)" 会匹配到最后一个引号
    # 正确（非贪婪）: "name":\s*"(.*?)"
    pattern = r'"name":\s*"(.*?)"'
    match = re.search(pattern, text)
    return match.group(1) if match else None


def extract_with_json(text):
    """推荐方式：使用语言内置的 JSON 解析器。"""
    data = json.loads(text)
    return data.get("name")


def extract_from_stdin_json():
    """一行代码版本：从 stdin 读取 JSON，输出 name。"""
    print(json.load(sys.stdin)["name"])


if __name__ == "__main__":
    with open("data.json", encoding="utf-8") as f:
        text = f.read()

    print("=== 正则表达式方式 ===")
    print(f"name = {extract_with_regex(text)}")

    print("\n=== JSON 解析器方式（推荐）===")
    print(f"name = {extract_with_json(text)}")

    # 测试含转义引号的情况
    tricky = '{"name": "John \\"Johnny\\" Doe", "age": 30}'
    print("\n=== 含转义引号的 JSON ===")
    print(f"regex 结果: {extract_with_regex(tricky)}")
    print(f"json  结果: {extract_with_json(tricky)}")
