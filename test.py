

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, position):
        self.entries.pop(position)

    def __str__(self):
        return '\n'.join(self.entries)

    # def save(self, filename):
    #     with open(filename, 'w') as file:
    #         file.write(str(input('данныу')))
    #
    # def load(self):
    #     pass
    #
    # def load_from_url(self, url):
    #     pass


class PersistenseManager:
    @staticmethod
    def save_to_file(journal,filename):
        with open(filename, 'w') as file:
            file.write(str(journal))


j = Journal()
j.add_entry("I'm always come back")
j.add_entry('yes, of course')
PersistenseManager.save_to_file(j, 'popa1.txt')

# while True:
#     Messege = input('Сообщния')
#     j.add_entry(Messege)
#     test = input('1/0')
#     match test:
#         case '1':
#             dele = input('indeks:')
#             j.remove_entry(int(dele))
#         case '0':
#             pass
#         case '10':
#             print(f'entry:\n{j}')
#         case 'save':
#             j.save(input('name'))
#         case _:
#             print('default')
#             break
