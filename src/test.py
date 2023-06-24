import re

string = 'https://hoathinh3d.pro/xem-phim-dau-la-dai-luc/tap-1-sv1.html'
match = re.search(r'\/([^\/]+\.html)', string)
if match:
    extracted_part = match.group(1)
    print(extracted_part)
else:
    print("No match found.")