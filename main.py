import json
from bitget_api import BitgetAPI  # 导入 BitgetAPI 类

# 读取 JSON 文件中的账户信息
def read_accounts_from_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return []  # 如果读取失败，返回空列表


# 使用 BitgetAPI 查询存款地址
def query_deposit_address(account_info, coin, chain):
    account_name = account_info["account"]
    uuid = account_info["UUID"]
    api_key = account_info["APIKey"]
    api_secret_key = account_info["SecretKey"]
    passphrase = account_info["password"]
    
    # 初始化 BitgetAPI 对象
    bitget = BitgetAPI(api_key, api_secret_key, passphrase)

    # 获取存款地址
    response = bitget.get_address(coin, chain)
    data = response.get('data', {})
    coin = data.get('coin', 'N/A')  # 默认值为 'N/A'，如果没有找到 'coin'
    address = data.get('address', 'N/A')  # 默认值为 'N/A'，如果没有找到 'address'


    # 打印账户信息和响应
    print(f'用户信息: {account_name}; 用户UUID: {uuid}; 提币网络: {coin}; 提币地址： {address}')

# 主程序
def main():
    # 读取账户信息
    accounts = read_accounts_from_json('bitget_accounts.json')

    # 填入币种
    coin = "SOL" 
    # 网络   
    chain = "SOL" 

    # 循环查询每个账户
    for account_info in accounts:
        query_deposit_address(account_info, coin, chain)

if __name__ == '__main__':
    main()
