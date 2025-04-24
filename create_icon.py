from PIL import Image, ImageDraw

def create_icon():
    """아이콘 이미지를 생성합니다."""
    # 1024x1024 크기의 이미지 생성
    size = 1024
    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # 원 그리기
    margin = 100
    draw.ellipse([margin, margin, size-margin, size-margin], 
                 fill=(255, 255, 255), outline=(0, 0, 0, 255))
    
    # 'B' 문자 그리기
    font_size = 600
    # 여기서는 간단한 원으로 대체
    draw.ellipse([size//2-200, size//2-200, size//2+200, size//2+200], 
                 fill=(0, 0, 0, 255))
    
    # PNG로 저장
    image.save('icon.png')
    
    # macOS용 .icns 파일 생성
    if platform.system() == "Darwin":
        os.system('iconutil -c icns icon.iconset')
    
    # Windows용 .ico 파일 생성
    else:
        image.save('icon.ico')

if __name__ == "__main__":
    import platform
    import os
    
    create_icon() 