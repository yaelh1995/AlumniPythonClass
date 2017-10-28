from sys import exit
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("Welcome!")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('end')

        while current_scene != last_scene:
            next_scene_name =current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class GameOver(Scene):

    def enter(self):
        print(dedent("""
            You have failed as an instructor!! Now your poor student will be forced
            to write python code... forever!!
            """))

class FrontDoor(Scene):

    def enter(self):
        print(dedent("""
            It is Halloween night, and you are a programming instructor
            hanging out with one of your students. You both decide to
            check out the Haunted House... but little do you know...
            IT'S HAUUUNTEEED! Like it's actually haunted.

            The door opens, and your student is immediately taken away
            by a floating demon who says, 'Your student is now our prisoner!
            In order to save this student, you must look through each room
            and answer python related questions! However, if you answer any
            of them incorrectly... your student will be forced to write
            code... FOREVER!! MUAHAHAH! Let's see if you're worthy of being
            a Python instructor!'
            So yeah, you better be up to date on your Python skills

            type 'enter' to continue
            """))

        action = input("> ")

        if action == ('enter'):
            print('-' * 10)
            print(dedent("""
            Before you can look through the house, you must answer your
            first Python question.

            What does MRO stand for?
            """))

            answer = input("> ")
            if answer == 'method resolution order':
                print('-' * 10)
                print(dedent("""
                    You got the question right!
                    choose which room to look for your student:

                    kitchen
                    bedroom
                    backyard
                    living room
                    """))

                choice = input("> ")
                if choice == 'kitchen' or choice == 'Kitchen':
                        return 'the_kitchen'
                elif choice == 'bedroom' or choice == 'Bedroom':
                        return 'the_bedroom'
                elif choice == 'backyard' or choice == 'Backyard':
                        return 'the_backyard'
                elif choice == 'living room' or choice == 'Living Room':
                        return 'the_living_room'

            else:
                return 'gameover'
        else:
            print('-' * 10)
            print("Excuse me, I believe I just told you to TYPE 'ENTER'")
            print("Would you like to start the game over?")

            start_over = input("> ")
            if start_over == 'yes':
                return 'frontdoor'
            else:
                return 'gameover'

class Kitchen(Scene):

    def enter(self):
        print('-' * 10)
        print(dedent("""
        The student is not here! However, you still must answer a Python
        question! Hope you're ready.

        What is the simplest form of cryptography?
        """))

        answer = input("> ")
        if answer == 'caesar cipher':
            print('-' * 10)
            print(dedent("""
                You got the question right!
                choose which room to look for your student:

                bedroom
                backyard
                living room
                """))

            choice = input("> ")
            if choice == 'bedroom' or choice == 'Bedroom':
                    return 'the_bedroom'
            elif choice == 'backyard' or choice == 'Backyard':
                    return 'the_backyard'
            elif choice == 'living room' or choice == 'Living Room':
                    return 'the_living_room'

        else:
            return 'gameover'

class Bedroom(Scene):

    def enter(self):
        print('-' * 10)
        print(dedent("""
        The student is not here! However, you still must answer a Python
        question! Hope you're ready.

        When using Flask and HTML forms to make a 'submit' button for a Credit
        Card payment, which form method is most necessary?
        """))

        answer = input("> ")
        if answer == 'POST' or 'post':
            print('-' * 10)
            print(dedent("""
                You got the question right!
                choose which room to look for your student:

                kitchen
                backyard
                living room
                """))

            choice = input("> ")
            if choice == 'kitchen' or choice == 'Kitchen':
                    return 'the_kitchen'
            elif choice == 'backyard' or choice == 'Backyard':
                    return 'the_backyard'
            elif choice == 'living room' or choice == 'Living Room':
                    return 'the_living_room'

        else:
            return 'gameover'

class Backyard(Scene):

    def enter(self):
        print('-' * 10)
        print(dedent("""
        The student is not here! Oh no! In this room, there are THREE floating
        Demons! That means you must answer 3 Python
        questions! I hope you know your stuff!

        What is it called when one class inherits traits from another class?
        """))

        answer = input("> ")
        if answer == 'inheritance':
            print('-' * 10)
            print(dedent("""
            Okay one down.

            what is it called when a class is composed of other classes
            as parts?
            """))

            answer = input("> ")
            if answer == 'composition':
                print('-' * 10)
                print(dedent("""
                Okay, last one.

                What does it mean when a class can inherit traits from more
                than one class?
                """))

                answer = input("> ")
                if answer == 'multiple inheritance':
                    print('-' * 10)
                    print(dedent("""
                        You got the questions right!
                        choose which room to look for your student:

                        kitchen
                        bedroom
                        living room
                        """))

                    choice = input("> ")
                    if choice == 'kitchen' or choice == 'Kitchen':
                            return 'the_kitchen'
                    elif choice == 'bedroom' or choice == 'Bedroom':
                            return 'the_bedroom'
                    elif choice == 'living room' or choice == 'Living Room':
                            return 'the_living_room'

                else:
                    return 'gameover'
            else:
                return 'gameover'
        else:
            return 'gameover'

class LivingRoom(Scene):

    def enter(self):
        print('-' * 10)
        print(dedent("""
        OMG!! The student is here! All you have to do is answer this Python
        question! THIS IS THE MOMENT OF TRUTH!

        Who invented the Python programming language?
        """))

        answer = input("> ")
        if answer == 'Guido van Rossum' or answer == 'guido van rossum':
            return 'frontdoorexit'

        else:
            return 'gameover'

class FrontDoorExit(Scene):

    def enter(self):

        print('-' * 10)
        print(dedent("""
            You got the student out of the Haunted House safe and sound!
            Good job!
            """))

class Map(object):

    scenes = {
        'frontdoor': FrontDoor(),
        'the_kitchen': Kitchen(),
        'the_bedroom': Bedroom(),
        'the_backyard': Backyard(),
        'the_living_room': LivingRoom(),
        'gameover': GameOver(),
        'frontdoorexit': FrontDoorExit(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('frontdoor')
a_game = Engine(a_map)
a_game.play()
