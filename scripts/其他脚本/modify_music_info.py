# 去除歌曲的注释信息（三方下载的盗版音乐有广告会写在注释里）
import os
from mutagen.flac import FLAC
from concurrent.futures import ThreadPoolExecutor
 
def update_metadata(file_path, comment):
    """
    更新FLAC文件的元数据注释。
    :param file_path: FLAC文件的路径。
    :param comment: 要设置的注释。
    """
    audio = FLAC(file_path)
    audio['COMMENT'] = comment
    audio.save()
 
def main():
    # 示例路径和注释
    base_dir = 'E:\迅雷下载\周杰伦音乐迷必备歌单\周杰伦-无损单曲合集'
    comment = ''
    
    # 查找所有的flac文件
    for dirpath, _, filenames in os.walk(base_dir):
        for filename in filenames:
            if filename.lower().endswith('.flac'):
                file_path = os.path.join(dirpath, filename)
                # 使用ThreadPoolExecutor来并发执行更新操作
                with ThreadPoolExecutor(max_workers=4) as executor:
                    executor.submit(update_metadata, file_path, comment)
 
if __name__ == '__main__':
    main()



# 删除非flac格式的文件
# import os
# def update_metadata(filename, comment):
#     if os.path.exists(filename):
#         os.remove(filename)
#         print(f"文件 {filename} 删除成功！")
#     else:
#         print(f"文件 {filename} 不存在。")
 
# def main():
#     # 示例路径和注释
#     base_dir = 'E:\迅雷下载\周杰伦音乐迷必备歌单\周杰伦-无损单曲合集'
#     comment = ''
    
#     # 查找所有的flac文件
#     for dirpath, _, filenames in os.walk(base_dir):
#         for filename in filenames:
#             file_path = os.path.join(dirpath, filename)
#             if filename.lower().endswith('.flac'):
#                 print("")
#             else:
#                 # 使用ThreadPoolExecutor来并发执行更新操作
#                 with ThreadPoolExecutor(max_workers=4) as executor:
#                     executor.submit(update_metadata, file_path, comment)
 
# if __name__ == '__main__':
#     main()