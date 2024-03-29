from tkinter import *
from PIL import Image, ImageTk
from random import randint

window = Tk()
window.title("Rock, Paper, Scissor Game")
window.configure(bg="#68228B")

#picture upload and 
image_rockp = ImageTk.PhotoImage(Image.open("images/rock_player.png"))
image_paperp = ImageTk.PhotoImage(Image.open("images/paper_player.png"))
image_scissorp = ImageTk.PhotoImage(Image.open("images/scissor_player.png"))
image_rockc = ImageTk.PhotoImage(Image.open("images/rock_computer.png"))
image_paperc = ImageTk.PhotoImage(Image.open("images/paper_computer.png"))
image_scissorc = ImageTk.PhotoImage(Image.open("images/scissor_computer.png"))

#insert pic
label_player = Label(window, image=image_scissorp,bg="#68228B")
label_computer = Label(window, image=image_scissorc, bg="#68228B")
label_player.grid(row=1, column=4)
label_computer.grid(row=1, column=0)

#score
player_score = Label(window,text=0,font=('arial',60,"bold"),bg="#68228B", fg="black")
computer_score = Label(window,text=0,font=('arial',60,"bold"),bg="#68228B", fg="black")
player_score.grid(row=1,column=3)
computer_score.grid(row=1,column=1)

#indicate the player and computer
player_ind = Label(window,font=('arial',50,"bold"),
                   text="PLAYER",bg="#68228B",fg="#EE7600")
computer_ind = Label(window,font=('arial',45,"bold"),
                   text="COMPUTER",bg="#68228B",fg="#EE7600")
player_ind.grid(row=0,column=3)
computer_ind.grid(row=0,column=1)

#message
final_msg = Label(window,font=('arial',30,"bold"),bg="#68228B",fg="black")
final_msg.grid(row=5,column=2, padx=20, pady=0)

#update msg
def updatemsg(a):
    final_msg['text'] = a

#update player score
def player_update():
    final = int(player_score['text'])
    if final < 5:
        final += 1
        player_score["text"] = str(final)

#update computer score
def computer_update():
    final = int(computer_score['text'])
    if final < 5:
        final += 1
        computer_score["text"] = str(final)

#check for win
def win_check(p,c):
    if p == c:
        updatemsg("IT'S A TIE!!")
    elif p == "rock":
        if c == "paper":
            updatemsg("YOU LOOSE!!")
            computer_update()
        else: 
            updatemsg("YOU WIN!!")
            player_update()

    elif p == "paper":
        if c == "scissor":
            updatemsg("YOU LOOSE!!")
            computer_update()
        else: 
            updatemsg("YOU WIN!!")
            player_update()

    elif p == "scissor":
        if c == "rock":
            updatemsg("YOU LOOSE!!")
            computer_update()
        else: 
            updatemsg("YOU WIN!!")
            player_update()
            
    if int(player_score['text']) == 5 or int(computer_score['text']) == 5:
        winner = "PLAYER" if int(player_score['text']) == 5 else "COMPUTER"
        show_winner_popup(winner)
#popup screen
def show_winner_popup(winner):
    popup = Toplevel()
    popup.title("Game Over")
    popup.geometry("175x60")
    popup.configure(background=	"black")
    Label(popup, text=f"{winner} WINS!", font=('arial', 14, 'bold'), justify='center', bg="black",fg="#68228B").grid(row=0,column=3, padx=1, pady=1)
    popup.geometry(f"175x60+{popup.winfo_screenwidth() // 2 - 100}+{popup.winfo_screenheight() // 2 - 100}")
    Button(popup, text="Close",bg="#68228B",fg="black",justify='center', command=window.quit).grid(row=1,column=3,padx=1, pady=1)


#update choices
to_select=["rock","paper","scissor"]

def choice_update(a):
    #for computer
    choice_computer = to_select[randint(0,2)]
    if choice_computer == "rock":
        label_computer.configure(image = image_rockc)
    elif choice_computer == "paper":
        label_computer.configure(image = image_paperc)
    else:
        label_computer.configure(image = image_scissorc)
    #for player
    if a == "rock":
        label_player.configure(image = image_rockp)
    elif a == "paper":
        label_player.configure(image = image_paperp)
    else:
        label_player.configure(image = image_scissorp)
    
    win_check(a, choice_computer)

#buttons
Player_Rock = Image.open("images/rock_player.png")
resized = Player_Rock.resize((100,100))
rockplayer = ImageTk.PhotoImage(resized)
button_rock = Button(window, width=300, height=150,
                     image=rockplayer, text="ROCK", compound="top", font=('arial',20,"bold"),fg="black", bg="#CD1076",
                     command=lambda:choice_update("rock")).grid(row=3, column=1, padx=10, pady=10)

Player_Paper = Image.open("images/paper_player.png")
resized = Player_Paper.resize((100,100))
paperplayer= ImageTk.PhotoImage(resized)
button_rock = Button(window, width=300, height=150,
                     image=paperplayer, text="PAPER", compound="top", font=('arial',20,"bold"),fg="black", bg="#EEAD0E",
                     command=lambda:choice_update("paper")).grid(row=3, column=2, padx=10, pady=10)

Player_Scissor = Image.open("images/scissor_player.png")
resized = Player_Scissor.resize((100,100))
scissorplayer = ImageTk.PhotoImage(resized)
button_rock = Button(window, width=300, height=150,
                     image=scissorplayer, text="SCISSORS", compound="top", font=('arial',20,"bold"),fg="black", bg="#00CDCD",
                     command=lambda:choice_update("scissor")).grid(row=3, column=3, padx=10, pady=10)


window.mainloop()