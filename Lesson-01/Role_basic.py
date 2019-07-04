import random

simple_grammar = """
    sentence => noun_phrase verb_phrase
    noun_phrase => Article Adj* noun
    Adj* => null | Adj Adj*
    verb_phrase => verb noun_phrase
    Article =>  一个 | 这个
    noun =>   女人 |  篮球 | 桌子 | 小猫
    verb =>  看着  |  坐在 |  听着 | 看见
    Adj =>  蓝色的 | 好看的 | 小小的
    """
adj_grammar = """
 Adj* => null | Adj Adj*
 Adj =>  蓝色的 | 好看的 | 小小的
                
"""
#在西部世界里，一个”人类“的语言可以定义为：
human = """
human = 自己 寻找 活动
自己 = 我 | 俺 | 我们 
寻找 = 找找 | 想找点 
活动 = 乐子 | 玩的
"""
#一个“接待员”的语言可以定义为

host = """
host = 寒暄 报数 询问 业务相关 结尾 
报数 = 我是 数字 号 ,
数字 = 单个数字 | 数字 单个数字 
单个数字 = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
寒暄 = 称谓 打招呼 | 打招呼
称谓 = 人称 ,
人称 = 先生 | 女士 | 小朋友
打招呼 = 你好 | 您好 
询问 = 请问你要 | 您需要
业务相关 = 玩玩 具体业务
玩玩 = null
具体业务 = 喝酒 | 打牌 | 打猎 | 赌博
结尾 = 吗？
"""
programming = """
stmt => if_exp | while_exp | assignment 
assignment => var = var
if_exp => if ( var ) { /n .... stmt }
while_exp=> while ( var ) { /n .... stmt }
var => chars number
chars => char | char char
char => student | name | info  | database | course
number => 1 | 2 | 3
"""
waiter= '''
waiter = 寒暄 询问 服务 结尾
寒暄 = 称谓 打招呼 | 打招呼
称谓 = 帅哥 | 美女 | 大爷 | 阿姨 | 小朋友
打招呼 = 你好 | 您好
询问 = 请问需要 | 您想要 | 需要
服务 = 来点儿 商品
商品 = 蔬菜 | 水果 | 面食 | 零食 | 甜点
结尾 = 吗？
'''
customer = '''
customer = 打招呼 自己 动作 东西
打招呼 = 您好 | 你好
自己 = 我 | 俺 | 我们 
动作 = 买点 | 来点 | 来些
东西 = 苹果 | 黄瓜 | 馒头 | 面包 | 蛋糕| 梨 | 香蕉 | 豆角
'''

##建立一一对应的字典
def create_grammar(grammar_str, split='=>'):
    grammar = {}
    for line in grammar_str.split('\n'):
        if not line.strip(): continue

        exp, stmt = line.split(split)
        grammar[exp.strip()] = [t.split() for t in stmt.split('|')]
    return grammar
##随机生成句子
def generate(gram,target):
    if target in gram:
        new_target = [generate(gram,t) for t in random.choice(gram[target])]
        return ''.join([e if e != '/n' else '\n' for e in new_target if e != 'null'])
    else:
        return target

sen = generate(create_grammar(simple_grammar,split='='),target='sentence')
for i  in range(20):
    print(generate(create_grammar(customer,split='='),target='customer'))

#print(generate(create_grammar(programming),target='stmt'))
