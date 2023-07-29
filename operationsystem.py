name = 'BottleOS'
version = 1.0
un = 'b-User'

class funcs:
    def changeSelect():
        print('Select Changer <BottleOS> (WINDOWS ONLY!)                              .')
        print('Guide: on project wiki                                                 .\n')
        
        print('Enter RGB code: 1 (0 0 0)')
        rgb1 = input('rgb1: ')
        print('Enter RGB code: 2 (0 0 0)')
        rgb2 = input('rgb2: ')

        select = open('selectColor.reg', 'w')

        if rgb1 == 'default' or 'rgb2' == 'default':
            selectCode = "Windows Registry Editor Version 5.00\n"
            selectCode += "\n[HKEY_CURRENT_USER\Control Panel\Colors]\n"
            selectCode += f'"Hilight"="0 120 215"\n'
            selectCode += "\n[HKEY_CURRENT_USER\Control Panel\Colors]\n"
            selectCode += f'"HotTrackingColor"="0 102 204"'
        else:
            selectCode = "Windows Registry Editor Version 5.00\n"
            selectCode += "\n[HKEY_CURRENT_USER\Control Panel\Colors]\n"
            selectCode += f'"Hilight"="{rgb1}"\n'
            selectCode += "\n[HKEY_CURRENT_USER\Control Panel\Colors]\n"
            selectCode += f'"HotTrackingColor"="{rgb2}"'

        print(selectCode + '\n')

        select.write(selectCode)
        select.close()

