import turtle
import pandas

US_STATES = 50

screen = turtle.Screen()
screen.title("U.S State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

# To write the states in the map
write_state = turtle.Turtle()
write_state.hideturtle()
write_state.penup()

correct_answers = []
while len(correct_answers) < US_STATES:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/{len(data.state.values)} States Correct",
                                    prompt="What's another State's name?").title()
    if answer_state in data["state"].values:
        correct_answers.append(answer_state)
        state_data = data[data["state"] == answer_state]
        x,y = int(state_data.x.iloc[0]), int(state_data.y.iloc[0]) # extracts coordinates
        #write the state name at a given coordinate
        write_state.goto(x, y)
        write_state.write(answer_state)

#screen.exitonclick()