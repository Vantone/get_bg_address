# 使用环境
python3.10

#  1 通过bitget交易所创建api信息，填入到bitget_accounts.json文件中，样例如下
```
[
    {
        "account": "account_1",
        "UUID": "uuid_1",
        "APIKey": "api_key_1",
        "SecretKey": "secret_key_1",
        "password": "password_1"
    },
    {
        "account": "account_2",
        "UUID": "uuid_2",
        "APIKey": "api_key_2",
        "SecretKey": "secret_key_2",
        "password": "password_2"
    }
]

```

# 2 在main.py中填入所需要参数，提币地址和提币网络，修改如下信息

```
    # 填入币种
    coin = "SOL" 
    # 网络   
    chain = "SOL" 

```

# 3 启动
```
python mian.py 
```


