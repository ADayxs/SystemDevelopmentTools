"""
命令行常用标志（CLI flags）演示。
Missing Semester 大杂烩课程 - Common command-line flags/patterns

演示以下常用模式：
  --help / -h      显示帮助信息
  --version / -V   显示版本号
  --verbose / -v   详细输出（可叠加 -vvv）
  --quiet / -q     静默模式（只输出错误）
  --dry-run        试运行（只打印将执行的操作，不实际执行）
  --interactive    交互模式（每个破坏性操作前确认）
  --               结束选项解析，后续参数视为位置参数
"""
import argparse
import sys
import shutil
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        prog="filetool",
        description="一个演示常用 CLI 标志的文件处理工具",
        epilog="示例: filetool --dry-run --verbose file1.txt file2.txt",
    )

    # --version
    parser.add_argument(
        "--version", "-V",
        action="version",
        version="%(prog)s 1.0.0",
    )

    # --verbose (可叠加: -v, -vv, -vvv)
    parser.add_argument(
        "--verbose", "-v",
        action="count",
        default=0,
        help="增加输出详细程度 (可叠加: -v, -vv, -vvv)",
    )

    # --quiet
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="静默模式，只输出错误",
    )

    # --dry-run
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="试运行，只打印将执行的操作而不实际执行",
    )

    # --interactive
    parser.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="交互模式，每个破坏性操作前请求确认",
    )

    # 操作类型
    parser.add_argument(
        "--action",
        choices=["copy", "delete", "move"],
        default="copy",
        help="要执行的操作 (默认: copy)",
    )

    # 目标目录
    parser.add_argument(
        "--dest",
        default="/tmp/output",
        help="目标目录 (默认: /tmp/output)",
    )

    # 位置参数（文件列表）
    parser.add_argument(
        "files",
        nargs="+",
        help="要处理的文件列表（使用 -- 后可传入以 - 开头的文件名）",
    )

    args = parser.parse_args()

    # 日志级别控制
    def log(level, msg):
        if args.quiet and level > 0:
            return
        if level <= args.verbose or level == 0:
            prefix = ["", "[INFO] ", "[DEBUG] ", "[TRACE] "][min(level, 3)]
            print(f"{prefix}{msg}", file=sys.stderr if level > 0 else sys.stdout)

    log(0, f"filetool v1.0.0 — action={args.action}, dest={args.dest}")
    log(1, f"处理 {len(args.files)} 个文件")
    log(2, f"verbose level: {args.verbose}, dry_run: {args.dry_run}")

    dest = Path(args.dest)

    for filepath in args.files:
        src = Path(filepath)
        target = dest / src.name

        if args.dry_run:
            log(0, f"[DRY-RUN] 将{args.action} {src} -> {target}")
            continue

        if args.interactive:
            answer = input(f"确认{args.action} {src} -> {target}? [y/N] ")
            if answer.lower() != "y":
                log(1, f"跳过 {src}")
                continue

        if not src.exists():
            print(f"错误: 文件不存在 - {src}", file=sys.stderr)
            sys.exit(1)

        if args.action == "copy":
            dest.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, target)
            log(0, f"已复制 {src} -> {target}")
        elif args.action == "delete":
            src.unlink()
            log(0, f"已删除 {src}")
        elif args.action == "move":
            dest.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(target))
            log(0, f"已移动 {src} -> {target}")

    log(1, "操作完成")


if __name__ == "__main__":
    main()
