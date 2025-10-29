import requests
import os


def upload_single_file(file_path, upload_url, api_key, api_secret):
    """
    上传单个文件到京东云OSS
    """
    headers = {
        'X-API-KEY': api_key,
        'X-API-SECRET': api_secret
    }

    try:
        with open(file_path, 'rb') as file:
            files = {'file': file}  # 'file需替换为服务器期望的字段名[citation:4]
            response = requests.post(upload_url, files=files, headers=headers)

        if response.status_code == 200:
            print("文件上传成功！")
            return True
        else:
            print(f"上传失败，状态码：{response.status_code}")
            return False
    except Exception as e:
        print(f"上传过程中发生错误：{e}")
        return False
def test_upload_file():
    file_path = r'D:\python_devData\PythonProject\Conf\test_data.txt'
    upload_url = 'https://www.baidu.com/'
    upload_single_file(file_path, upload_url)
    assert upload_single_file(file_path, upload_url) is None
