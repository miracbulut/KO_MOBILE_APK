# 🚀 HEMEN APK DERLE!

## En Hızlı Yöntem: Colab (10 dakika)

1. **Google Colab'ı Aç:**
   https://colab.research.google.com/

2. **Yeni Notebook Oluştur** ve bu kodu çalıştır:

```python
# 1. Sistemi hazırla
!apt-get update -qq
!apt-get install -y -qq zip unzip openjdk-17-jdk
!pip install -q buildozer cython==0.29.33

# 2. Android SDK kur
!wget -q https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip
!mkdir -p /root/android-sdk/cmdline-tools
!unzip -q commandlinetools-linux-9477386_latest.zip -d /root/android-sdk/cmdline-tools
!mv /root/android-sdk/cmdline-tools/cmdline-tools /root/android-sdk/cmdline-tools/latest

# 3. SDK bileşenlerini kur
import os
os.environ['ANDROID_SDK_ROOT'] = '/root/android-sdk'
os.environ['PATH'] = f"{os.environ['PATH']}:/root/android-sdk/cmdline-tools/latest/bin"

!yes | /root/android-sdk/cmdline-tools/latest/bin/sdkmanager --licenses
!/root/android-sdk/cmdline-tools/latest/bin/sdkmanager "platform-tools" "platforms;android-31" "build-tools;30.0.3" "ndk;25.2.9519653"

# 4. Proje dosyalarını yükle (sol panelden)
# - main.py
# - buildozer.spec
# - service/AutoClickService.java
# - templates/AndroidManifest.xml
# - templates/accessibility_service_config.xml
# - templates/strings.xml

# 5. buildozer.spec'i güncelle
!sed -i 's|# android.sdk_path|android.sdk_path = /root/android-sdk|g' buildozer.spec

# 6. APK derle
!buildozer -v android debug

# 7. APK'yı indir
from google.colab import files
!ls -lh bin/
files.download('bin/bulutautoclicker-1.0.0-arm64-v8a_armeabi-v7a-debug.apk')
```

## Alternatif: GitHub Actions (Otomatik)

1. Bu klasörü GitHub'a yükle
2. Actions sekmesine git
3. "Build Android APK" workflow'unu çalıştır
4. 20-30 dakika bekle
5. APK'yı Artifacts'ten indir

---

**Not:** main.py dosyasını henüz oluşturmadım çünkü dosya yazma hatası var.
Yukarıdaki Colab kodunu çalıştır, ben sana çalışan bir main.py göndereyim!
