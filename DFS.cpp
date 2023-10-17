#include<stdio.h>
#define WHITE 1
#define GRAY 2
#define BLACK 3
int adj[100][100],stime[100],ftimr[100],time=1,node,edge,color[100];
void dfs();
void dfsvisit();
void display()
{
    for(int i=0; i<node; i++)
    {
        for(int j=0; j<edge; ++j)
        {
            printf("%d ",adj[i][j]);
        }
        printf("\n");
    }

}
int main()
{

    int n1,n2;
    scanf("%d %d",&node, &edge);
    for(int i=0; i<edge; i++)
    {
        scanf("%d %d",&n1,&n2);
        adj[n1][n2]=1;
        adj[n2][n1]=1;
    }
    printf("\n");
    display();
    dfs();
    for(int i=0; i<node; ++i)
    {
        printf("Node : %d %d\n",stime[i],ftimr[i]);
    }
    return 0;
}
void dfs()
{
    for(int i=0; i<node; ++i)
    {
        color[i]=WHITE;
    }
    for(int i=0; i<node; ++i)
    {
        if(color[i]==WHITE)
        {
            dfsvisit(i);
        } 
    }
}
void dfsvisit(int x)
{
    color[x]=GRAY;
    stime[x]=time;
    ++time;
    for(int i=0; i<node; ++i)
    {
        if(adj[x][i]==1)
        {
            if(color[i]==WHITE)
            {
                dfsvisit(i);
            }
        }
    }
    color[x]=BLACK;
    ftimr[x]=time;
    ++time;
}
