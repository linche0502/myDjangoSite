
'''

#include<stdio.h>
void roll_forward(int j, int **dice);
void roll_back(int j, int **dice);
void roll_left(int j, int **dice);
void roll_right(int j, int **dice);
void bubble_sort(int *arr, int n);

int main(void)
{
    int N=0, n[4], arr[4], i=0, j=0, Bool[3], bb=0, score=18, k = 0;
    int D[4][6]={{1,6,5,2,3,4}, //上下左右前後
                 {1,6,5,2,3,4},
                 {1,6,5,2,3,4},
                 {1,6,5,2,3,4}};

    int *dice[4] = {D[0], D[1], D[2], D[3]};  // == {&dice[0][0], &dice[1][0]...}

    scanf("%d", &N);
    for(i=0; i<N; i++) //操作次數
    {
        //計算得分
        scanf("%d %d %d %d", &n[0], &n[1], &n[2], &n[3]);
        for(j=0; j<4; j++) //4個骰子輪調整
        {

            switch(n[j])
            {
                case 1:
                    roll_forward(j, dice);
                    break;
                case 2:
                    roll_back(j, dice);
                    break;
                case 3:
                    roll_right(j, dice);
                    break;
                case 4:
                    roll_left(j, dice);
                    break;
            }
        }

        for(k=0; k<4; k++)
        {
            arr[k]=D[k][0];
        }
        //arr[0]<=arr[1]<=arr[2]<=arr[3]
        bubble_sort(arr, 4); //排序可使邏輯判斷只需考慮8種情況

        for(k=0; k<3; k++)
        {
            if(arr[k]==arr[k+1])
            {
                Bool[k]=1;
            }
            else{
                Bool[k]=0;
            }
        }
        //Bool[0]=(arr[0]==arr[1]) Bool[1]=(arr[1]==arr[2]) //Bool[2]=(arr[2]==arr[3])
        bb=Bool[0]+2*Bool[1]+4*Bool[2]; //8種情況
        switch(bb)
        {
            case 0: //4個不同點數
                score = 0;
                break;
            case 1: //arr[0]==arr[1] score=arr[2]+arr[3]兩顆不同點數相加
                score = arr[2] + arr[3];
                break;
            case 2: //arr[1]==arr[2] score=arr[0]+arr[3]兩顆不同點數相加
                score = arr[0] + arr[3];
                break;
            case 3: //三同一異 arr[0]==arr[1]==arr[2]
                score = 0;
                break;
            case 4: //arr[2]==arr[3] score=arr[0]+arr[1]兩顆不同點數相加
                score = arr[0] + arr[1];
                break;
            case 5: //兩對得點數(取較大那對)
                score = 2 * arr[2];
                break;
            case 6: //三同一異 arr1]==arr[2]==arr[3]
                score = 0;
                break;
            case 7:
                score = 18;
                break;
        }

    }
    printf("%d", score);
    return 0;
}


void roll_forward(int j, int **dice)
{
    int tmp=0;
    tmp=dice[j][0];
    dice[j][0]=dice[j][5];
    dice[j][5]=dice[j][1];
    dice[j][1]=dice[j][4];
    dice[j][4]=tmp;
}
void roll_back(int j, int **dice)
{
    int tmp=0;
    tmp=dice[j][0];
    dice[j][0]=dice[j][4];
    dice[j][4]=dice[j][1];
    dice[j][1]=dice[j][5];
    dice[j][5]=tmp;
}

void roll_right(int j, int **dice)
{
    int tmp=0;
    tmp=dice[j][0];
    dice[j][0]=dice[j][2];
    dice[j][2]=dice[j][1];
    dice[j][1]=dice[j][3];
    dice[j][3]=tmp;
}

void roll_left(int j, int **dice)
{
    int tmp=0;
    tmp=dice[j][0];
    dice[j][0]=dice[j][3];
    dice[j][3]=dice[j][1];
    dice[j][1]=dice[j][2];
    dice[j][2]=tmp;
}

void bubble_sort(int *arr, int n) { //小到大
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < i; ++j) {
      if (arr[j] > arr[i]) {
        int temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
      }
    }
  }
}
'''

'''
020 擲骰子遊戲

十八骰子是一種常見的擲骰子遊戲，用四顆骰子計點。
四顆一開始都是點數 1 朝上，點數 4 朝向玩家，點數 2 朝右，
骰子擺放示意圖如連結所示 (https://imgur.com/Ntds1Ri)，
骰子展開如連結所示 (https://imgur.com/xEVHA5h)。
=================
接下來 N 次修改操作，每次操作包含四個整數代表依序針對四個骰子操作。
輸入整數之操作意義如下：
1表示向前滾一次。(往玩家視角的前方滾動)
2表示向後滾一次。(往玩家視角的後方滾動)
3表示向右滾一次。
4表示向左滾一次。
註：以上修改操作，皆只針對骰子做操作，並不會改變玩家的視角方向

操作完成後輸出得分，計點方式如下：
1. 若四顆點數均相同，稱一色，計18分，例如6, 6, 6, 6 或 3, 3, 3, 3。if(
2. 若四顆點數均不同；或有三顆點數相同，一顆不同，計 0分，例如 1, 2, 3, 4 或 2, 2, 2, 6。
3. 若兩顆點數相同，另兩顆點數也相同，但兩組兩顆點數不同，則得分計算為：加總兩顆較大點數，例如 2, 2, 5, 5，加總兩顆較大點數為 5+5=10分。
4. 若兩顆點數相同，另兩顆點數不同，則得分計算為加總兩顆不同點數，例如 2, 2, 4, 5，加總兩顆不同點數為 4+5=9分。
註：骰子點數以操作後最終朝上的那面點數為準
=================
輸入說明：
先輸入一個自然數N代表接下來有N次修改操作，
接著輸入N行修改操作，每行皆由4個1~4的數字組成，數字間以空格區隔

輸出說明：
輸出骰子最終的得分
=================
範例輸入說明：
2
1 4 3 2
4 2 1 3
'''

class Dice():
    def __init__(self) -> None:
        self.face= 1
        self.up= 3
        self.down= 4
        self.right= 2
        self.left= 5
        self.back= 6
    

def turn(dice:Dice, direction:str):
    # 防止左右有多餘的空白干擾
    direction= direction.strip()
    
    # 向前滾時
    if direction == '1':
        dice.face, dice.up, dice.down, dice.back= [dice.up, dice.back, dice.face, dice.down]
    # 向後滾時
    elif direction == '2':
        dice.face, dice.up, dice.down, dice.back= [dice.down, dice.face, dice.back, dice.up]
    # 向右滾時
    elif direction == '3':
        dice.face, dice.left, dice.right, dice.back= [dice.left, dice.back, dice.face, dice.right]
    # 向左滾時
    elif direction == '4':
        dice.face, dice.left, dice.right, dice.back= [dice.right, dice.face, dice.back, dice.left]
    return dice
    



dice1= Dice()
dice2= Dice()
dice3= Dice()
dice4= Dice()


# 輸入4次指令
for diceOrders in range(4):
    inputNums= input()
    # ex: inputNums='1 3 2 4', inputNum= '1'
    for inputNum in inputNums.split():
        dice1= turn(dice1, inputNum)


# 計算分數
result= [dice1.face,dice2.face,dice3.face,dice4.face]
# 四顆一樣時，18分
if len(set(result)) == 1:
    print(18)
elif len(set([dice1.face,dice2.face,dice3.face,dice4.face]))==4 or '':
    print()


# 1. 若四顆點數均相同，稱一色，計18分，例如6, 6, 6, 6 或 3, 3, 3, 3。if(
# 2. 若四顆點數均不同；或有三顆點數相同，一顆不同，計 0分，例如 1, 2, 3, 4 或 2, 2, 2, 6。
# 3. 若兩顆點數相同，另兩顆點數也相同，但兩組兩顆點數不同，則得分計算為：加總兩顆較大點數，例如 2, 2, 5, 5，加總兩顆較大點數為 5+5=10分。
# 4. 若兩顆點數相同，另兩顆點數不同，則得分計算為加總兩顆不同點數，例如 2, 2, 4, 5，加總兩顆不同點數為 4+5=9分。


'''
範例輸出說明：
第一次操作後4顆骰子朝上的那面分別是4253
第二次操作後4顆骰子朝上的那面分別是2345
由於最終點數皆不同，因此得分為0並輸出
=================
Sample Input 1：
0

Sample Output 1：
18
=================
Sample Input 2：
1
4 3 1 2

Sample Output 2：
0
=================
Sample Input 3：
1
3 3 3 3

Sample Output 3：
18
=================
Sample Input 4：
2
1 3 4 2
2 4 3 1

Sample Output 4：
18
=================
Sample Input 5：
2
3 2 4 1
1 4 1 4

Sample Output 5：
8
=================
Sample Input 6：
2
1 1 2 3
3 1 2 4

Sample Output 6：
6
=================
Sample Input 7：
2
4 1 2 4
3 1 2 4

Sample Output 7：
0
=================
Sample Input 8：
3
2 3 3 1
4 3 1 2
1 3 2 4

Sample Output 8：
6
=================
Sample Input 9：
3
1 4 2 3
1 3 1 3
2 2 4 1

Sample Output 9：
5
=================
Sample Input 10：
5
1 2 3 4
2 3 4 1
3 4 1 2
4 1 2 3
1 2 3 4

Sample Output 10：
0
=================
Sample Input 11：
10
4 2 2 1
4 2 2 4
1 2 3 4
2 2 3 2
3 2 1 2
3 4 4 2
3 3 1 3
1 4 1 1
4 1 4 2
1 1 4 4

Sample Output 11：
8
*/
'''