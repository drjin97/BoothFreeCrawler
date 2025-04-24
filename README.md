# Booth Downloader

부스(Booth)에서 상품을 다운로드하는 GUI 애플리케이션입니다.

## 기능

- 부스 상품 URL에서 이미지와 파일 다운로드
- 하위 폴더 설정 지원
- 일괄 다운로드 지원
- 쿠키 기반 인증
- 다양한 파일 형식 지원 (.zip, .rar, .7z, .pdf, .unitypackage 등)

## 사용 방법

1. 부스 웹사이트에서 "_plaza_session_nktz7u" 쿠키 값을 복사합니다.
2. 애플리케이션에 쿠키 값을 입력합니다.
3. 다운로드할 상품의 URL을 입력합니다.
4. 하위 폴더를 설정합니다 (선택사항).
5. "다운로드 시작" 버튼을 클릭합니다.

## 빌드 방법

Windows용 실행 파일은 GitHub Actions를 통해 자동으로 빌드됩니다.

## 요구사항

- Python 3.10 이상
- requests
- beautifulsoup4
- PySide6 