# 🚀 GitHub'a Yükle ve APK Derle

## 📋 Adım 1: GitHub Hesabı

1. https://github.com/ git
2. Hesap aç (varsa giriş yap)

---

## 📦 Adım 2: Yeni Repository Oluştur

1. GitHub'da sağ üstte **"+"** → **"New repository"**
2. İsim: `bulut-autoclicker`
3. **Public** seç
4. **✅ Add a README file** - KAPATMA (boş bırak)
5. **Create repository**

---

## 📤 Adım 3: Dosyaları Yükle

### Yöntem A: Web Üzerinden (KOLAY)

1. GitHub repo sayfasında **"uploading an existing file"** linkine tıkla
2. Tüm dosyaları sürükle-bırak:
   ```
   - main.py
   - buildozer.spec
   - README.md
   - service/AutoClickService.java
   - templates/AndroidManifest.xml
   - templates/accessibility_service_config.xml
   - templates/strings.xml
   - .github/workflows/build-apk.yml
   ```
3. **"Commit changes"** butonuna bas

### Yöntem B: GitHub Desktop (ÖNERİLEN)

1. **GitHub Desktop** indir ve kur: https://desktop.github.com/
2. GitHub Desktop'ı aç
3. **File** → **Add local repository**
4. `C:\Users\BULUT\Desktop\KO_MOBILE_APK` klasörünü seç
5. **"Create a repository"** tıkla
6. **"Publish repository"** tıkla
7. Repository adı: `bulut-autoclicker`
8. **Publish**

### Yöntem C: Git Command Line

```bash
cd C:\Users\BULUT\Desktop\KO_MOBILE_APK
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/KULLANICI_ADIN/bulut-autoclicker.git
git push -u origin main
```

---

## 🤖 Adım 4: GitHub Actions ile APK Derle

1. GitHub repo sayfasında **"Actions"** sekmesine git
2. **"I understand my workflows, go ahead and enable them"** tıkla
3. **"Build Android APK"** workflow'unu bul
4. **"Run workflow"** → **"Run workflow"** (yeşil buton)
5. ⏳ **20-30 dakika bekle**

---

## 📥 Adım 5: APK'yı İndir

1. Actions sayfasında en son çalışan workflow'a tıkla
2. Aşağıda **"Artifacts"** bölümünü bul
3. **"bulutautoclicker-apk"** dosyasını indir (ZIP)
4. ZIP'i aç
5. APK dosyasını bul: `bulutautoclicker-1.0.0-arm64-v8a_armeabi-v7a-debug.apk`

---

## 📱 Adım 6: Telefona Kur

1. APK'yı telefona gönder (USB, WhatsApp, Email...)
2. Telefonda APK'ya dokun
3. **"Bilinmeyen kaynaklardan yükleme"** iznini ver
4. **Kur**
5. Uygulamayı aç
6. **⚙️ İzinler** → **Erişilebilirlik** → **BULUT AutoClicker** → **AÇ**

---

## 🎮 Kullan!

1. Oyunu aç (örn: Knight Online Mobile)
2. Sağ altta **⚙️** butonuna tıkla
3. **🔴** → Kayıt başlat
4. Oyunda tıklamalarını yap
5. **⏹** → Kayıt durdur
6. **▶** → Otomatik oynat!

---

## 🐛 Sorun mu var?

### APK indirilmiyor:
- Actions'da **"Artifacts"** bölümünü kontrol et
- Workflow başarılı mı? (✅ yeşil işaret)
- Hata varsa log'ları kontrol et

### Build hatası:
- Log'ları oku (genelde NDK/SDK sorunu)
- Workflow'u tekrar çalıştır

### Telefonda çalışmıyor:
- Erişilebilirlik izni verdin mi?
- Android 5.0+ gerekli
- Logcat'e bak: `adb logcat | grep BULUT`

---

## ✅ BAŞARILI!

Tebrikler! Artık kendi macro uygulamana sahipsin! 🎉

---

**Not:** İlk derleme 25-30 dakika sürer. Sonrakiler 15-20 dakika.
