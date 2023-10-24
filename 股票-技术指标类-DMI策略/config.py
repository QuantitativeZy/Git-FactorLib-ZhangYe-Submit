# -*- coding: utf-8 -*-
# 主要功能：本地config设置


from itertools import product

"""
全部可用config配置
config_all = {
    # 配置标号
    "config_index": [],
    # 因子名称
    "name": ["RSJ"],
    # 数据存放路径
    "data_dir": ["data/"],
    # 结果输出路径
    "output_dir": ["result/"],
    # 回测开始日期
    "start_date": ['2018-11-23'],
    # 回测结束日期
    "end_date": ['2021-05-25'],
    # 回测频率
    "frequency": ["minutely", "five_minute", "daily", "weekly", "monthly"],
    # 回测基准，字典
    "benchmark": [{"000300": 1}, {"000300": 0.7, "110044": 0.3}],
    # 择时策略中的股票
    "security": ['000300', '002267', '002268'],
    # 股票池
    "universe": ["hs300", "stock20"],
    # 初始现金
    "cash": [300000000],
    # 子账户数
    "subportfolio": [3],
    # 窗长
    "window": [10],
    # 买入手续费率
    "open_commission": [0, 0.0001, 0.0003],
    # 卖出手续费率
    "close_commission": [0, 0.0001, 0.0003],
    # 卖出印花税率
    "close_tax": [0, 0.001, 0.002],
    # 最小手续费
    "min_commission": [0, 5],
    # 固定值滑点
    "fixed_slippage": [0, 0.01, 0.02],
    # 百分比滑点
    "price_related_slippage": [0, 0.002],
    # 是否允许小数下单
    "decimal_order": [True],
    # 是否允许交易中出现停牌
    "suspension": [True],
    # 生成的辅助表格
    "result_df": [["value", "price", "trade", "capacity"]],
    # 衍生表是否开启
    "time_df": [True],
    "security_df": [True]
}
"""

# 本地总CONFIG
CONFIG = {
    # 因子路径，因子所在文件夹名称
    "factor_path": ["股票-技术指标类-DMI"],
    # 因子名称
    "factor_name": ["DMI"],
    # 配置标号
    "config_index": [],
    # all_factor层是否并行
    "multiProcess_all_factor": [False],
    # multi_run层是否并行
    "multiProcess_multiRun": [False],
    # 是否进行性能分析：
    "enable_profiler": [False],
    # 数据存放路径
    "data_dir": ["data/"],
    # 结果输出路径
    "output_dir": ["result/"],
    # 回测开始日期
    "start_date": ['2023-01-01'],
    # 回测结束日期
    "end_date": ['2023-09-30'],
    # 回测频率
    "frequency": [],  # "daily"
    # 调仓周期（每多少个交易日更新一次股票池）；这个跟daily等交易频率互斥；
    "SELECT_INTERVAL": [1],  # 5
    # 买入周期（每多少个交易日执行一次买入操作）；
    "BUY_INTERVAL": [1],  # 2
    # 卖出周期（每多少个交易日执行一次卖出操作）；默认与买入周期相同
    "SELL_INTERVAL": [1],  # 2
    # 账户类型
    "account_type": ["stock"],
    # 回测基准，字典
    "benchmark": [{"000300.XSHG": 1}],  # {"000300.XSHG": 0.7, "110044.XSHG": 0.3}
    # 择时策略中的股票
    "security": ['000300.XSHG', '601088.XSHG'],  # '002267.XSHE', '002268.XSHE'
    # 股票池
    "universe": ["hs300"],
    # 初始现金
    "cash": [300000000],
    # 子账户数（即分组测试的分组数量）
    "subportfolio_num": [3],
    # 是否设置多空，如果不为None，则为所在的subportfolio_index
    "long": [1],
    "short": [2],
    # 买入手续费率
    "open_commission": [0],  # , 0.0001, 0.0003
    # 卖出手续费率
    "close_commission": [0],  # , 0.0001, 0.0003
    # 卖出印花税率
    "close_tax": [0],  # , 0.001, 0.002
    # 最小手续费
    "min_commission": [0],  # , 5
    # 固定值滑点
    "fixed_slippage": [0],  # , 0.01, 0.02
    # 百分比滑点
    "price_related_slippage": [0],  # , 0.002
    # 是否允许小数下单
    "decimal_order": [True],
    # 是否允许交易中出现停牌
    "suspension": [True],
    # 冻结期
    "locked_period": [{"stock": 0}],  # {"stock": 1}
    # 是否启用强行平仓
    "forced_liquidation": [False],
    # 是否在run()层输出结果
    "output_run": [True],
    # 生成的辅助表格
    "result_df": [["value", "price", "trade"]],  # , "capacity"
    # 衍生表是否开启
    "time_df": [True],
    "security_df": [True],
    # 是否计算时间序列相关性
    "time_series_corr": [True],
    # 是否输出运行时间表
    "timing": [True],
    # 以下为筛选项
    "filter_market_value": [],
    "filter_suspension": [],
    # 基金筛选
    "filter_fund_xxx": [],
    # 一年包含的数据条数（一个为一个周期，一个周期内含有的日期数量）
    "period": [252],  # 自然日365，工作日252，周度52，月度12，季度4，半年度2；
    # 基金前端费率
    "fee_ratio": [0],  # 0.015
    # 基金申购份额到账天数
    "subscription_receiving_days": [1],
    # 基金赎回款到账天数
    "redemption_receiving_days": [3],
    # 系统日志级别，用于控制策略框架输出日志的详细程度（策略打印的日志不受该选项控制），设置为某一级别则框架会输出该级别及更"严重"的日志
    # 可选值："debug"|"info"|"warning"|"error"，通常推荐设置为 info 或 warning
    # error 日志一般为不可逆的错误，如策略抛出异常、加载 Mod 失败等
    # warning 日志一般为告警信息，如 API 废弃、订单创建失败等
    # info 日志一般为说明性的信息，如 Mod 在某种设置下被动关闭等
    # debug 日志一般为开发者关注的调试信息，如策略状态变更、事件触发等，用户通常不需要关注
    "log_level": ["info"],
    # 融资利率/年
    "financing_rate": [0.00],
    # Todo: 超过了不能再买入，如果是0或空就不判断，不限制总账户、多空账户和基准账户
    # 最大持仓股票数（策略最多持有的标的数量）
    "MAX_HOLDING_NUM": [],
    # {1: 10, 2: 20, 3: 1}    # 账户根据自己代码对应修改；分账户指定，账户数量与之前的"subportfolio_num"一致；账户0默认不限制，也不出现在这里。其它账户如果没有出现，就表示不限制；
    # 个股最大持仓比重（策略每个标的的最大比例）
    "MAX_WEIGHT": [],
    # {1: 0.2, 2: 0.3, 3: 1} # 账户根据自己代码对应修改；分账户指定，账户数量与之前的"subportfolio_num"一致；账户0默认不限制，也不出现在这里。其它账户如果没有出现，就表示不限制；
}

# 因子config，因子自有配置项，只能在因子空间使用，不进backtest，不一定出现在远端config中。
config_custom = {
    "name": ["张晔"],
    "ID": ["320201199909183017"],
    "Tel": ["13915263537"],
    "mail": ["863347961@qq.com"],
    "organazation": ["中南财经政法大学"],
    "window1": [14],
    "window2": [6]
}

CONFIG_factor = {**CONFIG, **config_custom}
'''
默认CONFIG
default_config = {
    # 配置标号
    "config_index": [],
    # 因子名称
    "name": ["RSJ"],
    # 数据存放路径
    "data_dir": ["data/"],
    # 结果输出路径
    "output_dir": ["result/"],
    # 回测开始日期
    "start_date": ['2018-11-23'],
    # 回测结束日期
    "end_date": ['2021-05-25'],
    # 回测频率
    "frequency": ["daily"],
    # 回测基准，可设置为单个指数或组合
    "benchmark": [{"000300": 0.7, "bond": 0.3}],
    # 择时策略中的股票
    "security": ['000300', '002267', '002268'],
    # 股票池
    "universe": ["hs300"],
    # 初始现金
    "cash": [300000000],
    # 子账户数
    "subportfolio": [3],
    # 窗长
    "window": [10],
    # 买入手续费率
    "open_commission": [0, 0.0001, 0.0003],
    # 卖出手续费率
    "close_commission": [0, 0.0001, 0.0003],
    # 卖出印花税率
    "close_tax": [0, 0.001, 0.002],
    # 最小手续费
    "min_commission": [0, 5],
    # 固定值滑点
    "fixed_slippage": [0, 0.01, 0.02],
    # 百分比滑点
    "price_related_slippage": [0, 0.002],
    # 是否允许小数下单
    "decimal_order": [True],
    # 是否允许交易中出现停牌
    "suspension": [True],
    # 生成的辅助表格
    "result_df": [["value", "price", "trade", "capacity"]],
    # 衍生表是否开启
    "time_df": [True],
    "security_df": [True]
}
'''


def generate_config_combinations(CONF):
    """
    根据多选的config字典生成单个config字典的列表
    :param CONFIG: dict, 多选的CONFIG，每个键的值为列表，例如"security": ['002266', '002267', '002268']
    :return: config_list: list, 每项为一个config字典，每个键的值为单个的值。
    """
    # 对于配置中的空列表，将其替换为 [None]
    for key in CONF:
        if not CONF[key]:
            CONF[key] = [None]
    # 获取配置项的键和值
    keys = CONF.keys()
    values = CONF.values()
    # 生成配置组合
    config_combinations = list(product(*values))
    # 将配置组合转换为字典列表
    config_list = [{k: v for k, v in zip(keys, config_combination)} for config_combination in config_combinations]
    return config_list


# 生成本地CONFIG的configs列表
configs = generate_config_combinations(CONFIG_factor)


def update_config(super_config, local_config=CONFIG, overwrite=True):
    """
    更新配置信息
    :param super_config: dict, 远端CONFIG或config
    :param local_config: dict, 本地CONFIG或config，默认为本地CONFIG
    :param overwrite: 是否覆盖本地配置，默认为 True
    :return: new_config: dict, 更新后的配置信息
    """
    # 本地配置浅拷贝避免被修改
    new_config = local_config.copy()

    # 如果选择覆盖本地配置
    if overwrite:
        # 遍历远端配置的键，将非空的配置项更新到新配置中
        for key in super_config:
            if super_config[key] != [] and super_config[key] != [None] and super_config[key] is not None:
                new_config[key] = super_config[key]
    # 如果选择不覆盖本地配置
    else:
        # 遍历远端配置
        for key in super_config:
            # 如果远端配置项值为 [] 或 [None] 或 None，则跳过当前配置项，仍使用本地配置
            if super_config[key] == [] or super_config[key] == [None] or super_config[key] is None:
                continue
            # 如果配置项在本地配置中已存在，则将远端配置项的值与本地配置项值的并集更新到新配置中
            if key in new_config:
                new_config[key] = list(set(new_config[key] + super_config[key]))
            # 如果配置项在本地配置中不存在，则将当前远端配置项添加到新配置中
            else:
                new_config[key] = super_config[key]

    return new_config
