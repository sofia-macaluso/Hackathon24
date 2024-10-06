from tkinter import *
import webbrowser
from turtle import *

class american_flag:

    def __init__(self, turtle, x, y, width):
        self.turtle = turtle
        self.turtle.speed(0)
        self.x = x
        self.y = y
        self.width = width
        length = self.width*1.9
        self.length = length

        self.draw_stripes()
        self.blue_corner()
        self.draw_stars()


    def start_position(self):
        self.turtle.goto(self.x-self.length/2, self.y+self.width/2)

    def rectangle(self, length, width):
        self.turtle.forward(length)
        self.turtle.right(90)
        self.turtle.forward(width)
        self.turtle.right(90)
        self.turtle.forward(length)
        self.turtle.right(90)
        self.turtle.forward(width)

    def blue_corner(self):
        self.turtle.penup()
        self.start_position()
        self.turtle.setheading(0)
        self.turtle.color("blue")
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.rectangle(self.width*0.76, self.width*0.5385)
        self.turtle.end_fill()

    def stripe(self):
        self.turtle.setheading(0)
        self.turtle.color("red")
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.rectangle(self.width*1.9, self.width*0.0769)
        self.turtle.end_fill()

    def draw_stripes(self):
        self.turtle.penup()
        self.start_position()
        self.turtle.setheading(0)
        for i in range(7):
            self.stripe()
            self.turtle.penup()
            self.turtle.goto(self.turtle.xcor(), self.turtle.ycor()-((self.width*0.0769)*2))
            self.turtle.pendown()

    def star(self):
        chord = self.width*0.0616
        side = self.width*0.02353
        self.turtle.setheading(90)
        self.turtle.forward(chord/2)
        self.turtle.right(162)
        self.turtle.color("white")
        self.turtle.pendown()
        self.turtle.begin_fill()
        for i in range(5):
            self.turtle.forward(side)
            self.turtle.left(72)
            self.turtle.forward(side)
            self.turtle.right(144)
        self.turtle.end_fill()

    def draw_stars(self):
        self.turtle.penup()
        self.start_position()
        self.turtle.setheading(0)
        self.turtle.forward(self.width*0.063)
        self.turtle.right(90)
        self.turtle.forward(self.width*0.054)
        start_x = self.turtle.xcor()
        start_y = self.turtle.ycor()
        def star_row(row):
            for i in range(row):
                x = self.turtle.xcor()
                y = self.turtle.ycor()
                self.turtle.pendown()
                self.star()
                self.turtle.penup()
                self.turtle.goto(x, y)
                self.turtle.setheading(0)
                self.turtle.forward(self.width*0.063*2)
        row = 1
        for i in range(4):
            star_row(6)
            self.turtle.penup()
            self.turtle.goto(start_x+self.width*0.063, start_y-self.width*0.054*row)
            row += 1
            star_row(5)
            self.turtle.penup()
            self.turtle.goto(start_x, start_y - self.width * 0.054*row)
            row += 1
        self.turtle.penup()
        self.turtle.goto(start_x, start_y - self.width*0.054*8)
        star_row(6)




class MyGUI:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1200x800")
        self.canvas = Canvas(self.root, bg="white", width="190", height="100")
        self.canvas.pack()
        draw = RawTurtle(self.canvas)
        draw.hideturtle()
        american_flag(draw,0, 0, 100)
        self.label = Label(self.root, text="2024 Election Survey", font=('Fredoka', 26))
        self.label.pack()
        self.label = Label(self.root, text="Have you ever voted before?", font=('Fredoka', 18))
        self.label.pack()
        b1 = Button(self.root, text="Yes!", command=self.first_prompt_yes)
        b1.pack()
        b2 = Button(self.root, text="Not yet", command=self.first_prompt_no)
        b2.pack()
        self.root.mainloop()

    vote_info = {
        'alabama':'https://www.sos.alabama.gov/alabama-votes/voter/register-to-vote',
        'alaska':'https://www.elections.alaska.gov/Core/voterregistration.php',
        'arizona':'https://azsos.gov/elections/voters/registering-vote#:~:text=To%20see%20all%20voter%20registration%20deadlines,',
        'arkansas':'https://www.sos.arkansas.gov/elections/voter-information',
        'california':'https://registertovote.ca.gov/',
        'colorado':'https://www.sos.state.co.us/voter/pages/pub/olvr/findVoterReg.xhtml#:~:text=Enter%20your%20information%20as%20it%20is',
        'connecticut':'https://portal.ct.gov/sots/election-services/voter-information/voter-registration-information',
        'delaware':'https://elections.delaware.gov/voter/votereg.shtml#:~:text=You%20may%20complete%20and%20submit%20a',
        'florida':'https://www.registertovoteflorida.gov/home',
        'georgia':'https://georgia.gov/register-vote',
        'hawaii':'https://elections.hawaii.gov/register-to-vote/registration/#:~:text=You%20can%20apply%20to%20register%20to',
        'idaho':'https://voteidaho.gov/voter-registration/#:~:text=Learn%20how%20to%20register%20to%20vote',
        'illinois':'https://www.elections.il.gov/votingandregistrationsystems/register.aspx#:~:text=Illinois',
        'indiana':'https://www.in.gov/idr/hoosiers-vote/update-or-confirm-registration/#:~:text=All%20voter%20registrations%20must%20be%20submitted',
        'iowa':'https://sos.iowa.gov/elections/voterinformation/voterregistration.html',
        'kansas':'https://sos.ks.gov/elections/voter-registration.html#:~:text=Voter%20Registration.%20In%20Kansas,%20registering%20to',
        'kentucky':'https://vrsws.sos.ky.gov/vic/#:~:text=Welcome%20to%20the%20Commonwealth%20of%20Kentucky',
        'louisiana':'https://www.sos.la.gov/ElectionsAndVoting/Pages/OnlineVoterRegistration.aspx#:~:text=Registering%20to%20vote%20or%20changing%20your',
        'maine':'https://registertovote.sos.maine.gov/Home#:~:text=Register%20as%20a%20Maine%20Voter.%20Use',
        'maryland':'https://elections.maryland.gov/voter_registration/index.html',
        'massachusetts':'https://www.mass.gov/topics/voting#:~:text=Register%20to%20vote.%20Check%20your%20registration',
        'michigan':'https://www.michigan.gov/sos/elections/voting/register-to-vote#:~:text=If%20there%20are%2015+%20days%20before#:~:text=If%20there%20are%2015+%20days%20before',
        'minnesota':'https://www.sos.state.mn.us/elections-voting/register-to-vote/#:~:text=Download%20a%20voter%20registration%20form%20to',
        'mississippi':'https://vote.gov/register/mississippi#:~:text=Find%20out%20ways%20to%20register%20to',
        'missouri':'https://www.sos.mo.gov/elections/goVoteMissouri/register',
        'montana':'https://votemt.gov/voter-registration/#:~:text=Covered%20topics%20include:%20Voter%20Registration,%20Registration',
        'nebraska':'https://www.nebraska.gov/apps-sos-voter-registration/#:~:text=You%20may%20use%20the%20voter%20registration',
        'nevada':'https://www.nvsos.gov/sos/elections/voters/registering-to-vote#:~:text=Online%20voter%20registration%20is%20now%20available',
        'new hampshire':'https://www.sos.nh.gov/elections/register-vote#:~:text=Registering%20to%20Vote%20in%20New%20Hampshire',
        'new jersey':'https://voter.svrs.nj.gov/register?os=app&ref=app',
        'new mexico':'https://www.sos.nm.gov/voting-and-elections/voter-information-portal-nmvote-org/#:~:text=You%20can%20use%20this%20site%20to',
        'new york':'https://elections.ny.gov/register-vote#:~:text=Ways%20to%20Register.%20Use%20the%20Board',
        'north carolina':'https://vote.gov/register/north-carolina#:~:text=Start%20or%20update%20your%20registration%20online',
        'north dakota':'https://www.sos.nd.gov/elections/voter/voting-north-dakota#:~:text=North%20Dakota%20does%20not%20require%20voter',
        'ohio':'https://www.ohiosos.gov/elections/voters/register/#:~:text=Access%20Ohio%E2%80%99s%20Voter%20Registration%20form%20by#:~:text=Access%20Ohio%E2%80%99s%20Voter%20Registration%20form%20by',
        'oklahoma':'https://oklahoma.gov/elections/ovp.html#:~:text=Use%20the%20OK%20Voter%20Portal%20to:',
        'oregon':'https://sos.oregon.gov/voting/Pages/registration.aspx?lang=en',
        'pennsylvania':'https://www.pa.gov/en/agencies/vote/voter-registration.html#:~:text=You%20ca',
        'rhode island':'https://vote.sos.ri.gov/#:~:text=Be%20a%20Voter.%20Register%20to%20Vote;',
        'south carolina':'https://scvotes.gov/voters/register-to-vote/#:~:text=Visit%20your%20county%20board%20of%20voter',
        'south dakota':'https://sdsos.gov/elections-voting/voting/register-to-vote/default.aspx#:~:text=Registration%20&%20Voting.%20How%20to%20register:',
        'tennessee':'https://sos.tn.gov/elections/guides/how-to-register-to-vote#:~:text=Use%20one%20of%20the%20following%20methods:',
        'texas':'https://www.texas.gov/living-in-texas/texas-voter-registration/#:~:text=Fill%20out%20your%20voter%20registration%20application',
        'utah':'https://secure.utah.gov/voterreg/index.html',
        'vermont':'https://sos.vermont.gov/elections/voters/registration/#:~:text=You%20login%20to%20the%20page%20using',
        'virginia':'https://www.elections.virginia.gov/registration/',
        'washington':'https://www.sos.wa.gov/elections/voters/voter-registration/register-vote-washington-state#:~:text=Before%20you%20register%20to%20vote,%20view',
        'west virginia':'https://ovr.sos.wv.gov/register/Landing#:~:text=Register%20to%20Vote.%20You%20may%20apply',
        'wyoming':'https://sos.wyo.gov/Elections/State/RegisteringToVote.aspx',
        'wisconsin':'https://myvote.wi.gov/en-us/Voter-Registration#:~:text=Voter%20Registration.%20Search%20by%20name%20to',
    }

    def first_prompt_yes(self):
        self.vote_func()

    def first_prompt_no(self):
        b2_label = Label(self.root, text="How old are you?", font=('Fredoka', 18))
        b2_label.pack()
        b2_response = Entry(self.root)
        b2_response.pack()
        def click() -> str:
            a_label = Label(self.root, text="You're not yet old enough to vote, make sure to register once you turn 18!", font=('Fredoka', 18))
            age = int(b2_response.get())
            if age < 18:
                a_label.pack()
            else:
                self.vote_func()
        b2_button2 = Button(self.root, text="enter", font=('Fredoka', 16), command=click)
        b2_button2.pack()

    def vote_func(self):
        z_label = Label(self.root, text="What state are you currently living in?", font=('Fredoka', 18))
        z_label.pack()
        state = Entry(self.root)
        state.pack()
        def click2():
            stute = state.get()
            if stute.lower() in self.vote_info:
                q_label = Label(self.root, text="Link to vote!")
                q_label.pack()
                q_label.bind("<Button-1>", webbrowser.open_new(str(self.vote_info[stute])) )


        b4_button = Button(self.root, text="enter", font=('Fredoka', 16), command=click2)
        b4_button.pack()



MyGUI()


