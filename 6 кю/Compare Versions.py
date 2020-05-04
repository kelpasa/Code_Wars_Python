'''
Karan's company makes software that provides different features based on the version of operating system of the user.

For finding which version is more recent, Karan uses the following method:

While this function worked for OS versions 10.6, 10.7, 10.8 and 10.9, the Operating system company just released OS version 10.10.

Karan's function fails for the new version:

compare_versions ("10.9", "10.10");       # returns True, while it should return False
Karan now wants to spend some time to right a more robust version comparison function that works for any future version/sub-version updates.
'''


from distutils.version import LooseVersion

def compare_versions(version1,version2):
    return LooseVersion(version1) >= LooseVersion(version2)
    
'''
   try:
        ver_1 = float(version1)
        ver_2 = float(version2)
        print(ver_1), print(ver_2)
        return ver_1 >= ver_2
    except:
        ver_1 = version1.replace('.','')
        ver_2 = version2.replace('.','')
        if len(ver_1) == len(ver_2):
            return int(ver_1) >= int(ver_2)
        else:
            if len(ver_1) < len(ver_2):
                    ver_1 = ver_1 + ('0'*(len(ver_2)-len(ver_1)))
                    print(ver_1),print(ver_2)
                    return int(ver_1) >= int(ver_2)

            if len(ver_1) > len(ver_2):
                    ver_2 = ver_2 + ('0'*(len(ver_1)-len(ver_2)))
                    print(ver_1), print(ver_2)
                    return int(ver_1) >= int(ver_2)
                    '''
