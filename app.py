
import random
import streamlit as st

st.title("Dino Battle")

tRex = {
    "health": 20,
    "attackA": random.randint(6, 10),
    "attackD": random.randint(4, 8),
    "defenseA": random.randint(0, 2),
    "defenseD": random.randint(3, 5),
}

Stego = {
    "health": 40,
    "attackA": random.randint(3, 6),
    "attackD": random.randint(1, 4),
    "defenseA": random.randint(1, 3),
    "defenseD": random.randint(4, 8),
}

Triceratops = {
    "health": 30,
    "attackA": random.randint(4, 8),
    "attackD": random.randint(2, 6),
    "defenseA": random.randint(1, 4),
    "defenseD": random.randint(2, 6),
}

if "started" not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:
    userChoice = st.selectbox(
        "Choose your dinosaur",
        ["T-Rex", "Stego", "Triceratops"]
    )

    if st.button("Start Battle"):
        st.session_state.userDino_name = userChoice

        if userChoice == "T-Rex":
            st.session_state.userDino_stats = tRex.copy()
        elif userChoice == "Stego":
            st.session_state.userDino_stats = Stego.copy()
        else:
            st.session_state.userDino_stats = Triceratops.copy()

        compChoice = random.randint(1, 3)

        if compChoice == 1:
            st.session_state.compDino_name = "T-Rex"
            st.session_state.compDino_stats = tRex.copy()
        elif compChoice == 2:
            st.session_state.compDino_name = "Stego"
            st.session_state.compDino_stats = Stego.copy()
        else:
            st.session_state.compDino_name = "Triceratops"
            st.session_state.compDino_stats = Triceratops.copy()

        st.session_state.started = True
        st.session_state.gameOver = False
        st.session_state.battleLog = []
        st.rerun()

else:
    userDino_name = st.session_state.userDino_name
    userDino_stats = st.session_state.userDino_stats
    compDino_name = st.session_state.compDino_name
    compDino_stats = st.session_state.compDino_stats

    st.subheader("Your Dinosaur: " + userDino_name)
    st.write("Your HP:", max(0, userDino_stats["health"]))
    st.progress(
        max(0, userDino_stats["health"]) /
        {"T-Rex": 20, "Stego": 40, "Triceratops": 30}[userDino_name]
    )

    st.subheader("Computer Dinosaur: " + compDino_name)
    st.write("Computer HP:", max(0, compDino_stats["health"]))
    st.progress(
        max(0, compDino_stats["health"]) /
        {"T-Rex": 20, "Stego": 40, "Triceratops": 30}[compDino_name]
    )

    if not st.session_state.gameOver:
        userStance = st.radio(
            "Choose your move",
            ["Aggressive", "Defensive"],
            horizontal=True
        )

        if st.button("Fight!"):
            compStance = random.randint(1, 2)

            if userStance == "Aggressive":
                userAttack = userDino_stats["attackA"]
                userDefense = userDino_stats["defenseA"]
            else:
                userAttack = userDino_stats["attackD"]
                userDefense = userDino_stats["defenseD"]

            if compStance == 1:
                compAttack = compDino_stats["attackA"]
                compDefense = compDino_stats["defenseA"]
            else:
                compAttack = compDino_stats["attackD"]
                compDefense = compDino_stats["defenseD"]

            compHPChange = max(0, userAttack - compDefense)
            userHPChange = max(0, compAttack - userDefense)

            compDino_stats["health"] -= compHPChange
            st.session_state.battleLog.append(
                f"You dealt {compHPChange} damage!"
            )

            if compDino_stats["health"] <= 0:
                st.session_state.gameOver = True
                st.session_state.battleLog.append("YOU WIN!!")
            else:
                userDino_stats["health"] -= userHPChange
                st.session_state.battleLog.append(
                    f"The computer dealt {userHPChange} damage!"
                )

                if userDino_stats["health"] <= 0:
                    st.session_state.gameOver = True
                    st.session_state.battleLog.append("YOU LOSE!")

            st.rerun()

    st.subheader("Battle Log")

    for message in st.session_state.battleLog:
        st.write(message)

    if st.session_state.gameOver:
        if st.button("Play Again"):
            st.session_state.started = False
            st.rerun()
