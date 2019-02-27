from py2neo import Node,Relationship,order ,size,walk, authenticate
from  py2neo import Graph

#节点和关系
# a = Node('Person',name='Alice')
# b = Node('Person',name='Bob')
# r = Relationship(a,'know',b)
# print(a,b,r)
# # 设置其他属性
# # 1.1 直接设置
# a['age'] = 20
# b['age'] = 19
# r['time'] = '2017/10/2'
# print(a,b,r)
# # 1.2通过 setdefault 方法设置
# a.setdefault('sex','woman')
# print(a)
# # 1.3  update 方法批量更新
# data = {'name':'Amy','age':21}
# a.update(data)
# print(a)

# 子图 Subgraph
# a = Node('Person',name='Alice')
# b = Node('Person',name='Bob')
# r = Relationship(a,'know',b)
# s = a | b | r
# print(s) #打印子图
# print(s.keys()) #打印节点属性
# print(s.labels()) #打印节点标签
# print(s.nodes())  #打印节点
# print(s.relationships()) #打印关系
# print(s.types())
# print(order(s)) #打印节点数量
# print(size(s))  #打印关系数量

# 子图遍历 walkable
# a = Node('Person',name='Alice')
# b = Node('Person',name='Bob')
# c= Node('Person',name='coe')
# ac = Relationship(a,'know',b)
# bc = Relationship(b,'love',c)
# sw = bc +Relationship(a,'hate',c)
# print(sw)
# print("===============================")
# # 调用 walk()方法遍历
# for item in walk(sw):
#     print(item)
# print("===============================")
# print(sw.start_node())
# print(sw.end_node())
# print(sw.nodes())
# print(sw.relationships())

# 图 graph
graph = Graph('http://127.0.0.1:7474',user='neo4j',password='147369')
# graph = Graph('http://127.0.0.1:7474')
# graph = Graph()


# 1 创建节点和关系
a = Node('Person',name='samma')
b = Node('Person',name='kkkkkkkk')
r = Relationship(a,'meet',b)
r['time'] = '2017/10/4'
s = a|b|r
graph.create(s)
# c = Node('cat',name='kitte')
# r1 = Relationship(b,'have',c)
# graph.create(r1)
# r2 = Relationship(c,'bite',a)
# graph.create(r2)
# 2 查询
# 2.1 graph.data()查询
# data = graph.data('MATCH(p:Person) return p')
# print(data)
# 2.2 graph.find()/find_one() 方法查找节点，match()/match_one()方法查找关系
node = graph.find_one(label='Person',property_key='name',property_value='456')
print(node)
# re = graph.match(rel_type='kown',limit=2)
# print(re)
# 2.3 删除
# re = graph.match_one(rel_type='know')
# graph.delete(re)