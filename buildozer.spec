[app]

title = BULUT AutoClicker
package.name = bulutautoclicker
package.domain = com.bulut

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,java,xml

version = 1.0.0

requirements = python3==3.10.12,kivy==2.2.1,pyjnius,android

android.permissions = android.permission.WRITE_EXTERNAL_STORAGE,android.permission.READ_EXTERNAL_STORAGE,android.permission.SYSTEM_ALERT_WINDOW,android.permission.INTERNET,android.permission.BIND_ACCESSIBILITY_SERVICE

android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

orientation = portrait

android.service = True
android.archs = arm64-v8a,armeabi-v7a
android.bootstrap = sdl2

android.add_src = service
android.manifest.template = templates/AndroidManifest.xml
android.add_resources = templates/accessibility_service_config.xml:xml/accessibility_service_config.xml,templates/strings.xml:values/strings.xml

android.wakelock = True
android.uses_library = org.apache.http.legacy

[buildozer]
log_level = 2
warn_on_root = 1