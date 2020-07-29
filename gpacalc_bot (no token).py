from discord.ext.commands import Bot
import random

BOT_PREFIX = ("?", "!")
TOKEN = "XXXXXX" # REPLACE W/ YOUR BOT TOKEN


client = Bot(command_prefix=BOT_PREFIX)

@client.command(pass_context=True,
                description = "Returns GPA and Grade.")

async def grade(ctx, mark):

    try:
        if (type(mark) != int):
            mark = float(mark)

        grade = int(mark)
        
        if (grade >= 90 and grade <=100):
            letter = "A+"
            gpa = "4.33"

        elif (grade >= 85 and grade <=89):
            letter = "A"
            gpa = "4.00"
        elif (grade >= 80 and grade <=84):
            letter = "A-"
            gpa = "3.67"
        elif (grade >= 77 and grade <=79):
            letter = "B+"
            gpa = "3.33"
        elif (grade >= 73 and grade <=76):
            letter = "B"
            gpa = "3.0"
        elif (grade >= 70 and grade <=72):
            letter = "B-"
            gpa = "2.67"
        elif (grade >= 67 and grade <=69):
            letter = "C+"
            gpa = "2.33"
        elif (grade >= 63 and grade <=66):
            letter = "C"
            gpa = "2.00"
        elif (grade >= 60 and grade <=62):
            letter = "C-"
            gpa = "1.67"
        elif (grade >= 57 and grade <=59):
            letter = "D+"
            gpa = "1.33"
        elif (grade >= 53 and grade <=56):
            letter = "D"
            gpa = "1.00"
        elif (grade >= 50 and grade <=52):
            letter = "D-"
            gpa = "0.67"
        elif (grade >= 0 and grade <=49):
            letter = "F"
            gpa = "0"

        await ctx.send("Letter grade = " + letter + "\n" + "GPA = " + gpa )

    except ValueError:
        await ctx.send("Not a int or float. Please try again. ")
        print("Value Error. Please Try Again")



client.run(TOKEN)
