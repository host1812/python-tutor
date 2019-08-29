class User:
    active_users=0
    def __init__(self, name):
        self.name = name
        User.active_users += 1

    def __len__(self):
        return len(self.name)

    # def __len__():
    #     return active_users    

u1 = User("Alex")

print(len(u1))
# print(len(User.__len__()))