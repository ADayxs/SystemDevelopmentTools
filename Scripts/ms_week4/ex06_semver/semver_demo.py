"""
语义版本号（Semantic Versioning）演示。
Missing Semester 元编程课程练习 2。

版本格式：主版本号.次版本号.补丁号 (MAJOR.MINOR.PATCH)
- PATCH: 不改变 API 的 bug 修复
- MINOR: 向后兼容的新增功能
- MAJOR: 不向后兼容的 API 变更
"""


class Version:
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"

    def compatible_with(self, other):
        """判断当前版本是否与 other 兼容（同主版本，次版本 >=）。"""
        return (
            self.major == other.major
            and self.minor >= other.minor
        )


def scenario_patch_bump():
    """场景1：安全修复，PATCH 递增，API 不变。"""
    v1 = Version(1, 3, 0)
    v2 = Version(1, 3, 1)  # 修复了安全漏洞
    print(f"[PATCH] {v1} -> {v2}: 安全修复，完全兼容，应立即升级")


def scenario_minor_bump():
    """场景2：新增功能，MINOR 递增，向后兼容。"""
    v1 = Version(1, 3, 7)
    v2 = Version(1, 4, 0)  # 新增了可选参数
    print(f"[MINOR] {v1} -> {v2}: 新增功能，向后兼容，旧代码无需修改")


def scenario_major_bump():
    """场景3：API 变更，MAJOR 递增，不向后兼容。"""
    v1 = Version(1, 9, 2)
    v2 = Version(2, 0, 0)  # 重命名了核心函数
    print(f"[MAJOR] {v1} -> {v2}: 破坏性变更，依赖方需要修改代码")


def scenario_caret_requirement():
    """场景4：Cargo (Rust) 中 ^1.3.0 的含义。"""
    required = Version(1, 3, 0)
    candidates = [
        Version(1, 3, 0),   # 满足
        Version(1, 3, 5),   # 满足（patch 更高）
        Version(1, 5, 0),   # 满足（minor 更高，同 major）
        Version(1, 2, 9),   # 不满足（minor 更低）
        Version(2, 0, 0),   # 不满足（major 不同）
    ]
    print(f"\n依赖要求: ^{required} (>= {required}, < 2.0.0)")
    for c in candidates:
        ok = c.compatible_with(required) and c.major == required.major
        print(f"  {c}: {'满足' if ok else '不满足'}")


if __name__ == "__main__":
    scenario_patch_bump()
    scenario_minor_bump()
    scenario_major_bump()
    scenario_caret_requirement()
