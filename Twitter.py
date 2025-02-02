import requests
import requests
import json
import requests


token = '  '  # 你的api token

# 将基础URL设置为全局变量
base_url = 'https://api.tikhub.io'


# 创建一个字典来映射API功能到它们的具体路径
api_endpoints = {
    'get_single_tweet_data': '/api/v1/twitter/web/fetch_tweet_detail',
    'get_user_profile': '/api/v1/twitter/web/fetch_user_profile',
    'get_user_post': '/api/v1/twitter/web/fetch_user_post_tweet',
    'search': '/api/v1/twitter/web/fetch_search_timeline',
    'get_comments': '/api/v1/twitter/web/fetch_post_comments',
    'get_the_latest_tweet_comments': '/api/v1/twitter/web/fetch_latest_post_comments',
    'get_user_tweet_replies': '/api/v1/twitter/web/fetch_user_tweet_replies',
    'retweet_user_list': '/api/v1/twitter/web/fetch_retweet_user_list',
    'trending': '/api/v1/twitter/web/fetch_trending',
    'user_followings': '/api/v1/twitter/web/fetch_user_followings',
    'user_followers': '/api/v1/twitter/web/fetch_user_followers'
}

def call_X_api(api_function, params=None):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    url = f'{base_url}{api_endpoints[api_function]}'
    response = requests.get(url, headers=headers, params=params)    # 发送 HTTP GET 请求
    return response

# print(call_X_api('get_single_tweet_data', {'tweet_id':'1820452924805230697'}))


def get_influencer(influencer_name, cursor=None):
    response = call_X_api(api_function='get_user_post', params={'screen_name':{influencer_name},'cursor':{cursor}})
    if response.status_code == 200:            # 请求成功
        data = json.loads(response.text)  # 服务器返回的响应体内容。response.text 将是一个 JSON 格式的字符串
    else:                                 # json.loads() 是 Python 标准库 json 模块中的一个函数，用于将 JSON 格式的字符串解析为 Python 的字典或列表。
        print(f"Error: {response}")            # 请求失败
        data =  []
    return data                                # 若请求成功，data是 {"code": 200,"router": "","params": {},"data": "string"}


def write_to_jsonl(file_path, data={}):
    with open(file_path, 'a') as jsonl_file:  # 以追加模式打开文件
        jsonl_file.write(json.dumps(data) + '\n')  # json.dumps 将 Python 的数据结构（如字典或列表）转换为 JSON 格式的字符串。



# AI方面的大V的名单列表 list
name_list=['sama']
name_list0=[
    "sama", "ylecun", "AndrewYNg", "fchollet", "_KarenHao", "karpathy", 
    "SchmidhuberAI", "sarahookr", "demishassabis", "saranormous", "hardmaru", 
    "lilianweng", "OriolVinyalsML", "Michael_J_Black", "JeffDean", "goodfellow_ian", 
    "achowdhery", "PeterDiamandis", "GaryMarcus", "giffmana", "rasbt", "quaesita", 
    "KateKayeReports", "EMostaque", "drfeifei", "DrJimFan", "omarsar0", "conniechan", 
    "hugo_larochelle", "benjedwards", "rebecca_szkutak", "svlevine", "ericschmidt", 
    "ilyasut", "patrickmineault", "natashajaques", "pabbeel", "ESYudkowsky", 
    "geoffreyhinton", "wintonARK", "jeffclune", "RamaswmySridhar", "bentossell", 
    "johnschulman2", "_akhaliq", "quocleix", "jackclarkSF", "mervenoyann", 
    "DavidSHolz", "natolambert", "RichardSocher", "mustafasuleymn", "ZoubinGhahrama1", 
    "nathanbenaich", "johnvmcdonnell", "tunguz", "bengoertzel", "ch402", "Kseniase_", 
    "paulg", "rsalakhu", "gdb", "vivnat", "bxchen", "AnimaAnandkumar", "JeffreyTowson", 
    "Thom_Wolf", "johnplattml", "SamanyouGarg", "KirkDBorne", "Alber_RomGar", 
    "SilverJacket", "ecsquendor", "jordnb", "jluan", "NPCollapse", "NaveenGRao", 
    "azeem", "Suhail", "maxjaderberg", "Kyle_L_Wiggers", "cocoweixu", "aidangomezzz", 
    "alexandr_wang", "CaimingXiong", "YiMaTweets", "notmisha", "peteratmsr", "shivon", 
    "jackyliang42", "v_vashishta", "xdh", "FryRsquared", "ravi_lsvp", "ClementDelangue", 
    "oh_that_hat", "sapna", "VRLalchand", "svpino", "ceobillionaire", "ykilcher", 
    "BornsteinMatt", "lachygroom", "goodside", "amasad", "polynoamial", "sytelus"
]
data_output={}



for name in name_list:
    cursor = None  # 初始化 cursor
    while True:
        try:
            data = get_influencer(name, cursor)  # 注意data['data']长这个样子dict_keys(['pinned', 'timeline', 'next_cursor', 'prev_cursor', 'status', 'user'])
            if name not in data_output:
                data_output[name] = []     
            data_output[name].append(data['data']['timeline'])
            cursor = data['data'].get('next_cursor')  # 获取下一页的 cursor
            if cursor is None:  # 如果没有更多数据，退出循环
                break
        except KeyError as e:
            print(f"Caught an exception: {e}")
            break  # 如果出现 KeyError，退出循环
    # 这里的data_output是一个很大的字典，键是大V的名字name，值是列表list（列表的每一项是字典，该字典蕴含推文的信息）
    # print(type(data_output))
    # 将最终结果写入到 JSON Lines 文件
    file_path = f"X_{name}.jsonl"
    for name, timelines in data_output.items():  # timelines是列表list
        for timeline in timelines:               # timeline是列表list，每个元素是蕴含推文信息的字典
            write_to_jsonl(file_path, timeline)


