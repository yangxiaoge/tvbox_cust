# -*- coding: utf-8 -*-
# @Time : 2024/06/17 16:20
# @Author : Bruce
# @File : 
# @Software : VS CODE
# @Description : pdf转图片

from pdf2image import convert_from_path  
import os  
  
def pdf_to_images(pdf_path, pic_name):  
    # 使用convert_from_path将PDF转换为PIL图片对象列表  
    images = convert_from_path(pdf_path, poppler_path=r"D:\Programs\poppler-24.02.0\Library\bin")  
  
    # 遍历图片列表并保存为文件  
    for i, image in enumerate(images):  
        if i == 0:
            # 设置文件名（例如：page_0.png, page_1.png等）  
            filename = pic_name + ".png"  
            output_path = os.path.join(output_folder, filename)  
            # 保存图片  
            image.save(output_path, "PNG")  
  
# 批量处理PDF文件  
def batch_convert_pdfs(pdf_folder, output_folder):  
    # 遍历PDF文件夹中的所有文件  
    for filename in os.listdir(pdf_folder):  
        if filename.endswith(".pdf"):  
            # 构建完整的PDF路径和输出文件夹路径  
            pdf_path = os.path.join(pdf_folder, filename)  
            # 调用函数进行转换  
            pdf_to_images(pdf_path, os.path.splitext(filename)[0])  
  
# 使用示例  
pdf_folder = r"C:\Users\yang\Downloads\发票pdf"  # 你的PDF文件所在的文件夹路径  
output_folder = r"C:\Users\yang\Downloads\发票图片"  # 你想要保存图片的文件夹路径  
batch_convert_pdfs(pdf_folder, output_folder)