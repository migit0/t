from  datetime import strptime
#класс мероприятия
#список админов
admin = []
class Event():
    # свойства
    def __init__(self, name, info, date, participant = []):
        self.name = str(name) #имя
        self.info = str (info) #описание
        self.date = strptime(date) #дата проведения
        self.participant = list(participant) #участники
    #методы
    def setName(self, name) -> None: #установить имя
        self.name = name
    def setDate(self, date) -> None: #установить дату
        self.date = date
    def save(self) -> None: #сохранить мероприятие
        pass
    def create(self) -> None: #создать мероприятие
        pass