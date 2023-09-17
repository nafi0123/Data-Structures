from math import floor
N = 100000
tree = [0] * (2 * N)
def create_tree(node,b,e):
    if b==e:
        tree[node]=arr[b]
        return
    Left = node*2
    Right = node*2+1
    Mid= floor((b+e) /2)
    create_tree(Left,b,Mid)
    create_tree(Right,Mid+1,e)
    tree[node]=tree[Left]+tree[Right]

def quairy_sum(node,b,e,i,j):
    if i>e or j<b:
        return 0
    if b>=i and e<=j:
        return tree[node]
    left=node*2
    right=node*2+1
    mid=floor((b+e)/2)
    p1=quairy_sum(left,b,mid,i,j)
    p2=quairy_sum(right,mid+1,e,i,j)
    return p1+p2
def update(node,b,e,i,newvalue):
    if i>e or i<b:
        return
    if b>=i and e<=i:
        tree[node]=newvalue
        return
    left=2*node
    right=2*node+1
    mid=floor((b+e)/2)
    update(left,b,mid,i,newvalue)
    update(right,mid+1,e,i,newvalue)
    tree[node]=tree[left]+tree[right]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = len(arr)
    create_tree(1,0,n-1)    
    print(quairy_sum(1,0,n-1,1,10))
    update(1,0,n-1,2,1)
    print(quairy_sum(1,0,n-1,1,10))
