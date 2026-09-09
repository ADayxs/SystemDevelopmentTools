import subprocess
import sys


def test_normal_name():
    result = subprocess.run(
        [sys.executable, "-m", "greetlab.cli", "--name", "Alice"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "Hello, Alice!" in result.stdout


def test_blank_name():
    result = subprocess.run(
        [sys.executable, "-m", "greetlab.cli", "--name", "   "],
        capture_output=True,
        text=True,
        check=False,
    )
    # 空白参数触发parser错误，返回码固定为2
    assert result.returncode == 2


def test_no_name_raises_error():
    """测试不传--name的情况"""
    result = subprocess.run(
        [sys.executable, "-m", "greetlab.cli"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 2
