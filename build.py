import os
import platform
import subprocess
import sys

def install_requirements():
    """필요한 패키지를 설치합니다."""
    print("필요한 패키지 설치 중...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

def build_executable():
    """PyInstaller를 사용하여 실행 파일을 생성합니다."""
    print("실행 파일 생성 중...")
    # Windows용 .exe 파일 생성
    subprocess.check_call([
        "pyinstaller",
        "--onefile",  # 단일 실행 파일로 생성
        "--windowed",  # 콘솔 창 없이 실행
        "--name=BoothDownloader",  # 실행 파일 이름
        "booth_downloader.py"  # 메인 스크립트
    ])

def main():
    """메인 함수"""
    if platform.system() != "Windows":
        print("이 스크립트는 Windows에서만 실행할 수 있습니다.")
        return

    install_requirements()
    build_executable()
    print("빌드가 완료되었습니다.")
    print("생성된 파일:", os.path.join("dist", "BoothDownloader.exe"))

if __name__ == "__main__":
    main() 