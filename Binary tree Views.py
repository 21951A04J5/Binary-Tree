#Top VIew
'''
class node:
    def __init__(self,data):
        self.lc=None
        self.rc=None
        self.data=data
        self.hd=0

def topview(root):
    m={}
    q=[root]
    while q:
        node=q.pop(0)
        if node.hd not in m:
            m[node.hd]=node.data
        if node.lc:
            node.lc.hd=node.hd-1
            q.append(node.lc)
        if node.rc:
            node.rc.hd=node.hd+1
            q.append(node.rc)
    print("Topview")
    for hd in sorted(m):
        print(m[hd],end=" ")

root=node(1)
root.lc=node(2)
root.rc=node(3)
root.lc.lc=node(4)
root.lc.rc=node(5)
root.rc.lc=node(6)
root.rc.rc=node(7)
root.lc.rc.lc=node(8)
root.rc.lc.rc=node(9)
topview(root)

'''
#Bottom View
'''
class node:
    def __init__(self,data):
        self.lc=None
        self.rc=None
        self.data=data
        self.hd=0

def bottomview(root):
    m={}
    q=[root]
    while q:
        node=q.pop(0)
        m[node.hd]=node.data
        if node.lc:
            node.lc.hd=node.hd-1
            q.append(node.lc)
        if node.rc:
            node.rc.hd=node.hd+1
            q.append(node.rc)
    print("Bottomview")
    for hd in sorted(m):
        print(m[hd],end=" ")

root=node(1)
root.lc=node(2)
root.rc=node(3)
root.lc.lc=node(4)
root.lc.rc=node(5)
root.rc.lc=node(6)
root.rc.rc=node(7)
root.lc.rc.lc=node(8)
root.rc.lc.rc=node(9)
bottomview(root)

'''
#Left View #Right View

class node:
    def __init__(self,data):
        self.lc=None
        self.rc=None
        self.data=data
        self.hd=0

def level_order(root):
    level_map={}
    q=[(root,0)]
    while q:
        node,level=q.pop(0)
        if level not in level_map:
            level_map[level]=[]
        level_map[level].append(node.data)
        if node.lc:
            q.append((node.lc,level+1))
        if node.rc:
            q.append((node.rc,level+1))
    print("\nLevel orderL:")
    for level in level_map:
        print(level,":",level_map[level])
    print("\n Left View:")
    for level in level_map:
        print(level_map[level][0],end=",")
    print("\n Right vIEW")
    for level in level_map:
        print(level_map[level][-1],end=",")

root=node(1)
root.lc=node(2)
root.rc=node(3)
root.lc.lc=node(4)
root.lc.rc=node(5)
root.rc.lc=node(6)
root.rc.rc=node(7)
root.lc.rc.lc=node(8)
root.rc.lc.rc=node(9)
level_order(root) 
        


























    



