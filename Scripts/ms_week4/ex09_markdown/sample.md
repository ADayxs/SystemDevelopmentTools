# Markdown 语法实践

> Missing Semester 大杂烩课程 - Markdown 主题

## 1. 文本格式

这是 **粗体文本**，这是 *斜体文本*，这是 ~~删除线~~。

行内代码使用反引号：`print("Hello, World!")`

## 2. 列表

### 无序列表
- 第一项
- 第二项
  - 嵌套项 A
  - 嵌套项 B
- 第三项

### 有序列表
1. 第一步：创建文件
2. 第二步：编写内容
3. 第三步：保存并提交

## 3. 代码块

```python
def greet(name: str) -> str:
    """返回问候语。"""
    return f"Hello, {name}!"

print(greet("Missing Semester"))
```

```bash
# 查看文件状态
git status
git add .
git commit -m "feat: add markdown demo"
```

## 4. 引用

> 这是一段引用文本。
> 可以跨越多行。
>
> —— 某位智者

## 5. 链接与图片

- [Missing Semester 官网](https://missing-semester-cn.github.io/)
- [GitHub](https://github.com "代码托管平台")

## 6. 表格

| 主题 | 课程周次 | 关键工具 |
|------|---------|---------|
| Shell 入门 | 第1周 | bash, grep, find |
| 版本控制 | 第1周 | git, GitHub |
| 代码质量 | 第4周 | ruff, pytest, CI |
| 元编程 | 第4周 | make, semver |

## 7. 分割线与任务列表

---

- [x] 学习 Markdown 基础语法
- [x] 编写示例文档
- [ ] 在项目中实际使用
