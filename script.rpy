# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Hikari")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show hikari sad 

    # These display lines of dialogue.

    h "Sigh... {i}when did it become like this {/i}"

    h "{i}I haven\’t felt this way in a long time. So… dull..? It\’s like everything is so dull.{/i}"

    h "{i}I\’m just typing away right now, though.{/i}"

    # This ends the game.

    return
