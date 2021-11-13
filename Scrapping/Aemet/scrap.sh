python3 scrapping.py
find . -iname "*.rar" -execdir unrar x -r '{}' \;
find . -iname "*.rar" -execdir rm '{}' \;
python3 joiner.py
rm -rf 20*
