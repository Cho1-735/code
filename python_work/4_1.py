magicians=['alice', 'bob', 'carol', 'dave']
for magician in magicians:#注意冒号
    print(f"{magician.title()},that was a great trick!")#首行缩进的line在循环中
    print(f"I can't wait to see your next trick,{magician.title()}.\n")
print("Thank you everyone,that was a great magic show!")#首行未缩进的line退出循环