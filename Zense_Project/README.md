# Zense_Project
ZENSE PROJECT
by->R Sowmith Nandan(IMT2018074)


IDEA:
My idea was to create a game using python ,i used pygame to build my game.In my game, marbles(rectangular blocks )fall randomly from the sky and we control a player,we should ensure that the marbles dont fall on earth(reach the end of screen) ,the hero of the game(the character we control)can hurl projectiles upwards,we have to use this power of his to destroy the marbles ,but when he hits the marbles the force is not enough to destroy them,they divide into two,that too they go in opposite directions to make things harder.we have to destroy these fragments too before they reach earth.I have made a additional file which makes the hero act on his own my idea is to have a computer player to make things interesting.
Technology usedand and implementation:
I have used pygame to develop this game.


TECHNOLOGY AND IMPLEMENTATION:
I used pygame to make this game.when it comes to implementation i think these are the major parts of the code where i had think on my own to get to the objective.First step was division of balls on colliding.I created a class called rectangles and appended a instance of the calls  into a list and when the conditions which define collsions are met i called a function called createclass which creates and appends another two instances of the rectangle class into list to draw all these appended and delted lists i wrote a for loop in the while loop which draws all the elements in the lsit. To make the original marble disappear i used a flag variable.I put a condition that the flag variable should be true,then and only then the marbles should be drawn.this flag variable is a  attribute of the rectangle class.So each marble has its own flag variable defined.
The next step i found to be interesting that i made a new marble appear only one  all the fragments of the original marble are destroyed.The problem here is that while implementing the interpretor doesn't check which fragment or which marble is destroyed .So ,in the list where i appended instances , i appended lists where each list stores all the marbles and its fragments,using ths i can check whether all the fragments of a particular marble are destroyed or not.So in this way even if the fragments divide further i can ensure that a new marble appears only when all the fraagments are destroyed.
 
I made a computer player(player controlled by the computer)by make the imterpretor check the position of the fragment which is nearer to earth (end of the screen).So this will move the player and and when he in the range of the marble he shoots the projectile on his own.So in this way the player is controlled by the computer.


FUTURE SCOPE OF THE PROJECT:
The next step in this project is to make a main menu which will have the following mode:
1)classic:
the first one is classic in which we have the hero and we control him,as we have destroyed certain marables ,we go to next level ,i plan to make things harder by increasing speed.In the level after that i will increase the fragmentaion of the marbles that means that the hero has to destory the original marble then when he hits the fragments even the fragments divide into two , so he has to get 7 clear shot to destroy a particular marble.
2)player and computer mode:
In the classic mode the number of marbles you have to face is 1,but here we have 2 balls!!! we have two heroes one controlled by you and one by the computer.And even these will have levels.
3)Player vs computer mode-1:
This mode according to me is the most interesting among all,in this mode i will make the player and computer face each other.In this mode the marbles falling on earth wont end the game ,in this mode each correct hit gives player(or the compter points) so the player has to compete with the computer to win.Notice that the player and computer will be in the same screen in this mode
4)Player and computer mode-2
In  this mode player and computer are in two different screens ,but to make it harder if the player fails to stop the marble from falling on earth ,he loses.
  
REFERENCES:
Tech with tim-pygame tutorial(in youtube)

link:-https://www.youtube.com/watch?v=i6xMBig-pP4

OVERALL EXPERIENCE:
I thoroughly enjoyed myslef during this project.The satisfaction when we get the logic to get to the objective was whatcreated enthusiasm in me and made me try for other improvizations.
The interesting thing is that what ever alteration that are made by you can be seen visually when you run the code.This also helps you in debugging as bu observing what is happening you cantell which part of the code is faulty.Also i understood how using OOP(object oriented programming )makes things easier ,before this i thought i actually wont make a difference but due to this project i understood how it logically divides the  code and also helps us in decreasing the number of lines we have to write .I liked the idea to make the computer player as it is something which have alwasy seen in miniclip games in pur childhood.Also i think that game will be interesting if i use the computer player as competitor to the original player.

   
