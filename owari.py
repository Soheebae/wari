

def GetWhoMovesFirst():
    print("Would you like to go first? (y/n)")
    answer= input().upper()
    if answer =='Y':
        return 'NORTH'
    elif answer =='N':
        return 'SOUTH'


def displayinitialboard(board):
    print(' '+board[12]+' '+board[11]+' '+board[10]+' '+board[9]+' '+board[8]+' '+board[7]+' ')
    print(board[13]+'           '+board[6])
    print(' '+board[0]+' '+board[1]+' '+board[2]+' '+board[3]+' '+board[4]+' '+board[5]+' ')


print("Welcome to Owari game!\n")
board=['3','3','3','3','3','3','0','3','3','3','3','3','3','0']
displayinitialboard(board)
turn = GetWhoMovesFirst()
print("The " +turn+" will go first")
if turn =='NORTH':
    print(turn+ ", choose your pit (7-12)")
    pitchosen=input()
    pitint = int(pitchosen)
    if pitint < 7 or pitint > 12:
        print("Your pit should be among 7 to 12!")
    pit=board[int(pitchosen)]
    ans = int(pit)
    print(ans)

   

    



