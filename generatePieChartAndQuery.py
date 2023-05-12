import matplotlib.pyplot as plt

# 从 txt 文件中读取域名和贡献值的数据
data = {}
with open('data.txt', 'r') as f:
    for line in f:
        domain, contribution = line.strip().split(", ")
        data[domain] = int(contribution)

# 计算总贡献值
total = sum(data.values())

# 定义饼图的标签和占比
labels = []
sizes = []
for key, value in data.items():
    labels.append(key + ": {:.2f}%".format(value/total*100))
    sizes.append(value)

# 生成饼图
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')

# 添加标题和显示图像
plt.title('Contributions to AOSP by Domain')
plt.show()

# 域名和 changeset 的查询函数
def query_contribution(domain, changeset=None):
    if domain in data:
        percentage = data[domain]/total*100
        print("The contribution percentage of {} in AOSP is {:.2f}%".format(domain, percentage))
        if changeset:
            print("The contribution of {} in changeset {} is {:.2f}%".format(domain, changeset, percentage*changeset/total))
    else:
        print("Sorry, the domain {} is not found in the data.".format(domain))

# 在控制台中查询域名
domain = input("Enter a domain to query its contribution rate: ")
query_contribution(domain)
