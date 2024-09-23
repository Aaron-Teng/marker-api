from invoke import convert_pdf_to_markdown_and_save as convert
import os
import time

inputs = [
    'a.pdf',
    # '创业计划书内容要求.pdf',
    # 'P020231011636835574283.pdf',
]

inputs = ['./inputs/' + f for f in inputs]
outputs = 'outputs'
server_url = 'http://127.0.0.1:8000/convert'


def ymdhms(): return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


total = len(inputs)
print(f'【开始】[{ymdhms()}] {total} files.')
start_time = time.time()

for idx, pdf in enumerate(inputs):
    print(f'【{idx + 1}/{total}】 {os.path.basename(pdf)}')
    convert([pdf], outputs, server_url)

print(f'【结束】[{ymdhms()}] {total} files. take {time.time() - start_time:.2f}s.')
