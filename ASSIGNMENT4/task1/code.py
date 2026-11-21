def os_layers():
    return {
        'Android':['Linux/GKI','HAL','bionic/native libs','ART','Android framework','APK'],
        'iOS':['XNU','IOKit/Core OS','Core Services','ObjC/Swift runtime','Cocoa Touch','.app'],
        'Windows':['NT kernel','HAL/drivers','system libraries','WinRT/.NET','WinUI/framework','package']
    }
for os,layers in os_layers().items():
    print(os,'->',' -> '.join(layers))
print('Boundary repair: SavedStateHandle + rememberSaveable + lifecycle-scoped coroutine.')
