# 1. 나눔고딕 폰트 설치
```
!sudo apt-get update -qq
!sudo apt-get install -y fonts-nanum-extra -qq
```

# 2. 시스템 폰트 캐시 업데이트
```
!sudo fc-cache -fv
```

# 3. Matplotlib 폰트 캐시 삭제
```
!rm -rf ~/.cache/matplotlib
```