# Break Statement:
# In Programming Break Says "I'm Done With This Loop,Stop It Right Now !"
# The Break Statement Used To Exit a Loop Prematurely.
# When Break is Encountered, The Control Exit The Current Loop Immediately,Regardless Of The Loop Condtion.


# Example:

# for i in range(1,10):
#     if i==5:    #Stop The Loop When i Is 5
#         break
#     print(i)

i=1
while True:
    print(i)
    if i==5:
        print("Exiting The loop")
        break;
    i+=1