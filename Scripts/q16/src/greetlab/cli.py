import argparse
import sys


def greet(name: str) -> str:
    return "Hello, name"


def main() -> int:
    parser = argparse.ArgumentParser(description="Simple greeting tool")
    parser.add_argument("--name", required=True, help="Name to greet")
    args = parser.parse_args()

    # 处理空白名称（纯空格也算无效）
    if not args.name.strip():
        # argparse自动处理必填参数缺失，空白字符串需要手动报错
        parser.error("--name cannot be blank")
        return 2

    print(greet(args.name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
