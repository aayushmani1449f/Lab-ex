class Coach:
    def __init__(self, coach_number):
        self.coach_number = coach_number
        self.next = None


class Train:
    def __init__(self):
        self.head = None

    def add_coach(self, coach_number):
        new_coach = Coach(coach_number)
        if not self.head:
            self.head = new_coach
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_coach

    def remove_coach(self, coach_number):
        temp = self.head
        prev = None

        if temp and temp.coach_number == coach_number:
            self.head = temp.next
            return

        while temp and temp.coach_number != coach_number:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.coach_number, end=" -> ")
            temp = temp.next