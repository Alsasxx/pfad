import pandas as pd
import matplotlib.pyplot as plt

# 读取 CSV 文件
file1_path = '/Users/yezigongzhu/Desktop/Russia/file1.csv'  # 替换为文件 1 的路径
file2_path = '/Users/yezigongzhu/Desktop/Russia/file2.csv'  # 替换为文件 2 的路径
file3_path = '/Users/yezigongzhu/Desktop/Russia/file3.csv'  # 替换为文件 3 的路径
file4_path = '/Users/yezigongzhu/Desktop/Russia/file4.csv'  # 替换为文件 4 的路径

# 读取数据
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)
df3 = pd.read_csv(file3_path)
df4 = pd.read_csv(file4_path)

# 打印列名以确认
print("文件 1 列名:", df1.columns)
print("文件 2 列名:", df2.columns)
print("文件 3 列名:", df3.columns)
print("文件 4 列名:", df4.columns)

# 选择需要的列
# 假设我们只需要文件 2 的 'gfw_net_flux_co2e__Mg' 列进行可视化
data_col2 = 'gfw_net_flux_co2e__Mg'  # 文件 2 的数据列

# 可视化文件 2 数据
plt.figure(figsize=(15, 5))

# 绘制文件 2 数据
if data_col2 in df2.columns:
    plt.subplot(1, 4, 1)
    plt.plot(df2[data_col2], marker='o', linestyle='-')
    plt.title('File 2: Net CO2 Flux')
    plt.xlabel('Index')
    plt.ylabel('Net CO2 Flux (Mg)')
else:
    print(f"列 '{data_col2}' 不在文件 2 中，请检查列名。")

# 绘制其他文件的数据（示例）
# 文件 1 数据
plt.subplot(1, 4, 2)
plt.plot(df1['name'], marker='o', linestyle='-')
plt.title('File 1: Name')
plt.xlabel('Index')
plt.ylabel('Name')

# 文件 3 数据
plt.subplot(1, 4, 3)
plt.plot(df3['iso'], marker='o', linestyle='-')
plt.title('File 3: ISO')
plt.xlabel('Index')
plt.ylabel('ISO')

# 文件 4 数据
plt.subplot(1, 4, 4)
plt.plot(df4['title'], marker='o', linestyle='-')
plt.title('File 4: Title')
plt.xlabel('Index')
plt.ylabel('Title')

plt.tight_layout()
plt.show()
