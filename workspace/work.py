from invoke import convert_pdf_to_markdown_and_save as convert
import os
import time
import glob
import logging

inputs = [
    'a.pdf',
    # '创业计划书内容要求.pdf',
    # 'P020231011636835574283.pdf',
]

inputs = ['./inputs/' + f for f in inputs]
outputs = 'outputs'
server_url = 'http://127.0.0.1:8000/convert'

# 确保logs目录存在
os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    filename=f'logs/app_{time.strftime("%Y%m%d%H%M%S", time.localtime())}.log',  # 日志文件名
    level=logging.DEBUG,  # 日志级别
    format='%(asctime)s - %(levelname)s - %(message)s'  # 日志格式
)


def ymdhms(): return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def get_inputs_all_pdf():
    pdf_files = glob.glob(os.path.join('./inputs', '*.pdf'))
    return pdf_files


# 取inputs目录下所有pdf文件
inputs = get_inputs_all_pdf()
# print(inputs)


total = len(inputs)
print(f'【开始】[{ymdhms()}] {total} files.')
logging.info(f'【开始】[{ymdhms()}] {total} files.')
start_time = time.time()

for idx, pdf in enumerate(inputs):
    print(f'【{idx + 1}/{total}】 {os.path.basename(pdf)}')
    logging.info(f'【{idx + 1}/{total}】 {os.path.basename(pdf)}')
    convert([pdf], outputs, server_url)

print(f'【结束】[{ymdhms()}] {total} files. take {time.time() - start_time:.2f}s.')
logging.info(f'【结束】[{ymdhms()}] {total} files. take {time.time() - start_time:.2f}s.')
