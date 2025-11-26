# _*_coding:utf-8_*_
# author: zlg
# create time: 2025/11/11 8:34
# file: study20251111.py
# IDE: PyCharm
# desc: 
# version: v1.0
import numpy as np
import pandas as pd
import json
from matplotlib import rcParams
from matplotlib import pyplot as plt
import seaborn as sns
rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.min_rows', 10)  # 设置显示的最小行数
# pd.reset_option('display.max_rows')  # 重置为默认值
def building_floor_type(x):
    if pd.isna(x):
        return '未知'
    elif '低' in x:
        return '低楼层'
    elif '中' in x:
        return '中楼层'
    elif '高' in x:
        return '高楼层'
    else:
        return '其他'


if __name__ == '__main__':
    # print(pd.get_option('display.max_columns') )
    # 1.导入库
    # 2.导入数据
    df = pd.read_csv(r'D:\BaiduNetdiskDownload\课件及代码\课件及代码\代码\data\house_sales.csv')
    # 3.数据概览
    print('总记录数：', len(df))
    print('字段数量：', len(df.columns))
    # print(df.head(5))
    # print(df.info())
    # 4.数据清洗
    # 删除无用的数据列，比如url就不需要
    df.drop(columns=['origin_url'], inplace=True)
    # 检查是否有缺失值
    # print(df.isna().sum())
    # 删除缺失值
    df.dropna(inplace=True)
    # print(df.isna().sum())
    # 删除重复值
    df.drop_duplicates(inplace=True)
    # 检查是否有重复值
    # print(df.duplicated().sum())
    # print('总记录数：', len(df))
    # 数据类型转换
    # 面积数据去掉单位
    df['area'] = df['area'].str.replace('㎡', '').astype(float)
    # 售价数据去掉单位
    df['price'] = df['price'].str.replace('万', '').astype(float)
    # 朝向数据类型转换
    # 查看是否可以转换
    # print(df['toward'].value_counts())
    df['toward'] =df['toward'].astype('category')
    # unit单位总价去掉单位
    df['unit'] = df['unit'].str.replace('元/㎡', '').astype(float)
    # 建筑年代数据类型转换
    df['year'] = df['year'].str.replace('年建', '').astype(int)
    # 异常值的处理
    # 检查房屋面积是否有异常值
    # print(df[(df['area']<20) & (df['area']>600)])
    df = df[(df['area']<600) & (df['area']>20)]
    # 房屋售价的异常处理 IQR（箱线图的处理逻辑）
    Q1 = df['price'].quantile(0.25)
    Q3 = df['price'].quantile(0.75)
    IQR = Q3 - Q1
    low_price = Q1 - 1.5 * IQR
    high_price = Q3 + 1.5 * IQR
    # print(len(df[(df['price'] < low_price)]))
    # print(len(df[(df['price'] > high_price)]))
    df = df[(df['price'] > low_price) & (df['price'] < high_price)]
    # 5.新数据特征构造
    # 地区 district
    # print(df['address'].str.split('-').str[0])
    df['district'] = df['address'].str.split('-').str[0]
    # 楼层 floor_type 两种处理方式都可以
    df['floor_type'] = df['floor'].str.split('（').str[0]
    # apply 就是循环该列的每一个元素
    df['floor_type2'] = df['floor'].apply(building_floor_type).astype('category')
    # 是否是直辖市 zxs
    df['zxs'] = df['city'].apply(lambda x: 1 if x in ['北京', '上海', '天津', '重庆'] else 0)
    # print(df[df['zxs'] == 1])
    # 卧室数量 bedrooms
    df['bedrooms'] = df['rooms'].str.split('室').str[0].astype(int)
    # 客厅数量 livingrooms 太长，用正则表达式更方便
    # df['livingrooms'] = df['rooms'].str.split('室').str[1].str.split('厅').str[0].astype(int)
    df['livingrooms'] = df['rooms'].str.extract(r'(\d+)厅').astype(int)
    # 楼龄 building_age
    df['building_age'] = 2025 - df['year']
    # 价格分段 price_labels
    df['price_labels'] = pd.cut(df['price'], bins=4, labels=['低价', '中价', '高价', '超高价'])
    print(df.head(5))
    print(len(df))
    print('=' * 50)
    # 6.问题分析及可视化
    # 问题1：哪些变量影响房价？面积，楼层，房间数哪个影响最大？
    # 分析主题：相关性分析
    # 分析目标：了解房屋各特征对房价的线性影响
    # 分组字段：无
    # 指标/方法：皮尔逊相关系数
    # 选择数值型特征
    # ['price', 'area', 'unit', 'building_age']
    # 通过 相关系数，就能看出来趋势，
    # 比如 price         1.000000  0.452523  0.742731      0.091520  价格越高建造年限越短
    # print(df[['price', 'area', 'unit', 'building_age']].corr())
    # a = df[['price', 'area', 'unit', 'building_age']].corr()
    # 对房价的影响最大的几个因素排序; 单价>面积>建龄
    # print(a['price'].sort_values(ascending=False)[1:])
    # 相关性的热力图
    # plt.figure(figsize=(10, 10))
    # sns.heatmap(a, annot=True, cmap='coolwarm')
    # plt.title('房屋各特征的相关性热力图')
    # plt.show()

    # 问题2：全国房价总体分布是怎样的？是否存在极端值？
    # 分析主题：描述性统计
    # 分析目标：该来数值型字段的分布特征
    # 分组字段：无
    # 指标/方法：平均数 中位数 四分位数 标准差
    # df.describe()
    # # 房价分布的直方图
    # plt.subplot(111)
    # # plt.hist(df['price'], bins=50, color='blue', alpha=0.5, label='房价')
    # # kde=true 会出一条趋势线
    # sns.histplot(df['price'], bins=50, color='blue', alpha=0.5, label='房价', kde=True)
    # plt.show()

    # 问题3：南北向是否真比单一朝向贵？贵多少？
    # 分析主题：朝向溢价
    # 分析目标：评估不同朝向的价格差异
    # 分组字段：朝向 toward
    # 指标/方法：方差分析 多重比较
    print(df['toward'].value_counts())
    # b = df.groupby('toward').agg({
    #     'price': ['mean', 'median'],
    #     'unit': ['median'],
    #     'building_age': 'mean'
    # })
    # print(b)
    plt.figure(figsize=(14, 5))
    sns.boxplot(x='toward', y='price', data=df)
    # 单从 groupby 看不出南北向房价的溢价，但是从箱线图看，南北向房价的价格差距很大，存在溢价，特别是朝南的均存在溢价。
    plt.show()



