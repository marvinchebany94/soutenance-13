#!"e:\desktop\openclassroom\soutenance 13\soutenance-13\env\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'restructuredtext-lint==1.4.0','console_scripts','rst-lint'
__requires__ = 'restructuredtext-lint==1.4.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('restructuredtext-lint==1.4.0', 'console_scripts', 'rst-lint')()
    )
