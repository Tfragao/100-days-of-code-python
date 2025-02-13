import turtle
import pandas

US_STATES = 50

screen = turtle.Screen()
screen.title("U.S State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# To write the states in the map
write_state = turtle.Turtle()
write_state.hideturtle()
write_state.penup()

while len(guessed_states) < US_STATES:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(data.state.values)} States Correct",
                                    prompt="What's another State's name (Enter exit to finish)?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in data["state"].values:
        guessed_states.append(answer_state)
        state_data = data[data["state"] == answer_state]
        x,y = int(state_data.x.iloc[0]), int(state_data.y.iloc[0]) # extracts coordinates
        #write the state name at a given coordinate
        write_state.goto(x, y)
        write_state.write(answer_state)

