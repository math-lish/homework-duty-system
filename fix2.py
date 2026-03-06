import sys
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add button - simpler version without onclick
old = 'Word版 - 複製表格</button>'
new = 'Word版 - 複製表格</button><a href="manual.html" target="_blank"><button style="padding:10px 20px;background:#9C27B0;color:white;border:none;border-radius:8px;cursor:pointer;margin-left:10px;">手動輸入</button></a>'

content = content.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
