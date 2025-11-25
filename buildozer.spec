[app][app]



title = BULUT AutoClickertitle = BULUT AutoClicker

package.name = bulutautoclickerpackage.name = bulutautoclicker

package.domain = com.bulutpackage.domain = com.bulut



source.dir = .source.dir = .

source.include_exts = py,png,jpg,kv,atlas,json,java,xmlsource.include_exts = py,png,jpg,kv,atlas,json,java,xml



version = 1.0.0android.add_src = service

android.manifest.template = templates/AndroidManifest.xml

requirements = python3==3.10.12,kivy==2.2.1,pyjnius,androidandroid.add_resources = templates/accessibility_service_config.xml:xml/accessibility_service_config.xml,templates/strings.xml:values/strings.xml

android.manifest.intent_filters = 

android.permissions = android.permission.WRITE_EXTERNAL_STORAGE,android.permission.READ_EXTERNAL_STORAGE,android.permission.SYSTEM_ALERT_WINDOW,android.permission.INTERNET,android.permission.BIND_ACCESSIBILITY_SERVICE

version = 1.0.0

android.api = 31

android.minapi = 21# Android Manifest template

android.ndk = 25b

android.accept_sdk_license = Truerequirements = python3==3.10.12,kivy==2.2.1,pyjnius,androidandroid.manifest.template = templates/AndroidManifest.xml



orientation = portrait



android.service = True# İzinler# Android resources

android.archs = arm64-v8a,armeabi-v7a

android.bootstrap = sdl2android.permissions = android.permission.WRITE_EXTERNAL_STORAGE,android.permission.READ_EXTERNAL_STORAGE,android.permission.SYSTEM_ALERT_WINDOW,android.permission.INTERNET,android.permission.BIND_ACCESSIBILITY_SERVICEandroid.add_resources = templates/accessibility_service_config.xml:xml/accessibility_service_config.xml,templates/strings.xml:values/strings.xml



android.add_src = service

android.manifest.template = templates/AndroidManifest.xml

android.add_resources = templates/accessibility_service_config.xml:xml/accessibility_service_config.xml,templates/strings.xml:values/strings.xmlandroid.api = 31# Versiyon



android.wakelock = Trueandroid.minapi = 21version = 1.0.0

android.uses_library = org.apache.http.legacy

android.ndk = 25b

[buildozer]

log_level = 2android.accept_sdk_license = True# Gereksinimler

warn_on_root = 1

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
