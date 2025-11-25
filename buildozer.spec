[app][app]

title = BULUT AutoClicker# Uygulama bilgileri

package.name = bulutautoclickertitle = BULUT Macro

package.domain = com.bulutpackage.name = bulutmacro

package.domain = com.bulut

source.dir = .

source.include_exts = py,png,jpg,kv,atlas,json,java,xml# Kaynak dosyası

source.dir = .

# Java kaynaksource.include_exts = py,png,jpg,kv,atlas,json,java,xml

android.add_src = service

# Java kaynak dosyaları

# Android templatesandroid.add_src = service

android.manifest.template = templates/AndroidManifest.xml

android.add_resources = templates/accessibility_service_config.xml:xml/accessibility_service_config.xml,templates/strings.xml:values/strings.xml# Android Manifest ve Resource dosyaları

android.manifest.intent_filters = 

version = 1.0.0

# Android Manifest template

requirements = python3==3.10.12,kivy==2.2.1,pyjnius,androidandroid.manifest.template = templates/AndroidManifest.xml



# İzinler# Android resources

android.permissions = android.permission.WRITE_EXTERNAL_STORAGE,android.permission.READ_EXTERNAL_STORAGE,android.permission.SYSTEM_ALERT_WINDOW,android.permission.INTERNET,android.permission.BIND_ACCESSIBILITY_SERVICEandroid.add_resources = templates/accessibility_service_config.xml:xml/accessibility_service_config.xml,templates/strings.xml:values/strings.xml



android.api = 31# Versiyon

android.minapi = 21version = 1.0.0

android.ndk = 25b

android.accept_sdk_license = True# Gereksinimler

requirements = python3==3.10.12,kivy==2.2.1,pyjnius,android

orientation = portrait

# Android izinleri

# Serviceandroid.permissions = android.permission.WRITE_EXTERNAL_STORAGE,android.permission.READ_EXTERNAL_STORAGE,android.permission.SYSTEM_ALERT_WINDOW,android.permission.INTERNET,android.permission.BIND_ACCESSIBILITY_SERVICE

android.service = True

# Android API

android.archs = arm64-v8a,armeabi-v7aandroid.api = 31

android.bootstrap = sdl2android.minapi = 21

android.ndk = 25b

[buildozer]android.accept_sdk_license = True

log_level = 2

warn_on_root = 1# Orientasyon

orientation = portrait

# İkon ve splash (opsiyonel)
#icon.filename = %(source.dir)s/icon.png
#presplash.filename = %(source.dir)s/presplash.png

# Arkaplan çalışma
android.wakelock = True
android.service = True

# Kullanılan izinler
android.uses_library = org.apache.http.legacy

# APK formatı
android.archs = arm64-v8a,armeabi-v7a

# Bootstrap
android.bootstrap = sdl2

# Android meta - sadeleştirildi
# android.meta_data = com.google.android.gms.version=@integer/google_play_services_version

# SDK path sadece WSL için
# android.sdk_path = /home/bulut/Android

[buildozer]
# Build dizini
log_level = 2
warn_on_root = 1
