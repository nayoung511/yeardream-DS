import glob
output = glob.glob("afolder/**", recursive = True)
print(output)

import glob
output = glob.glob('afolder/**/*.txt', recursive = True)
print(output)