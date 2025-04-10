

def upload_to_geoportal(
    url: str,
    zip_path: str,
    username: str,
    password: str,
    field_name: str = 'base_file'
):
    """
    Gửi file zip qua API có xác thực Basic Auth

    Args:
        url (str): URL endpoint của API
        zip_path (str): Đường dẫn đến file zip
        username (str): Tên người dùng
        password (str): Mật khẩu
        field_name (str): Tên trường file trong form-data (mặc định: base_file)

    Returns:
        response (requests.Response): Đối tượng response từ server
    """
    import requests
    import base64
    import os
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"❌ File không tồn tại: {zip_path}")

    credentials = f"{username}:{password}"
    token = base64.b64encode(credentials.encode()).decode()
    headers = {
        "Authorization": f"Basic {token}"
    }

    with open(zip_path, 'rb') as f:
        files = [(field_name, (os.path.basename(zip_path), f, 'application/zip'))]
        response = requests.post(url, headers=headers, files=files)

    return response
