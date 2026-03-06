import sys
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = 'Word版 - 複製表格</button>'
new = """Word版 - 複製表格</button><button onclick="window.open('manual.html','_blank')" style="padding:10px 20px;background:#9C27B0;color:white;border:none;border-radius:8px;cursor:pointer;margin-left:10px;">手動輸入</button>"""

content = content.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
