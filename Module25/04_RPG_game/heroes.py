
class Hero:
    # Базовый класс, который не подлежит изменению
    # У каждого наследника будут атрибуты:
    # - Имя
    # - Здоровье
    # - Сила
    # - Жив ли объект
    # Каждый наследник будет уметь:
    # - Атаковать
    # - Получать урон
    # - Выбирать действие для выполнения
    # - Описывать своё состояние

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    # Все наследники должны будут переопределять каждый метод базового класса (кроме геттеров/сеттеров)
    # Переопределенные методы должны вызывать методы базового класса (при помощи super).
    # Методы attack и __str__ базового класса можно не вызывать (т.к. в них нет кода).
    # Они нужны исключительно для наглядности.
    # Метод make_a_move базового класса могут вызывать только герои, не монстры.
    def attack(self, target):
        # Каждый наследник будет наносить урон согласно правилам своего класса
        raise NotImplementedError("Вы забыли переопределить метод Attack!")

    def take_damage(self, damage):
        # Каждый наследник будет получать урон согласно правилам своего класса
        # При этом у всех наследников есть общая логика, которая определяет жив ли объект.
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ", round(self.get_hp()))
        # Дополнительные принты помогут вам внимательнее следить за боем и изменять стратегию, чтобы улучшить выживаемость героев
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        # С каждым днём герои становятся всё сильнее.
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        # Каждый наследник должен выводить информацию о своём состоянии, чтобы вы могли отслеживать ход сражения
        raise NotImplementedError("Вы забыли переопределить метод __str__!")


class Healer(Hero):
    # Целитель:
    # Атрибуты:
    # - магическая сила - равна значению НАЧАЛЬНОГО показателя силы умноженному на 3 (self.__power * 3)
    # Методы:
    # - атака - может атаковать врага, но атакует только в половину силы self.__power
    # - получение урона - т.к. защита целителя слаба - он получает на 20% больше урона (1.2 * damage)
    # - исцеление - увеличивает здоровье цели на величину равную своей магической силе
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # исцеление) на выбранную им цель
    def __init__(self, name):
        super().__init__(name)
        self.magical_power = (self.get_power() * 3)


    def attack(self, target):
        damage_for_target = self.get_power() / 2
        target.take_damage(damage_for_target)


    def take_damage(self, damage):
        get_damage = 1.2 * damage
        self.set_hp(self.get_hp() - get_damage)
        super().take_damage(get_damage)

    def give_health(self, target):
        print('Найден больной', self.name, 'начинает лечить-', target.name, '\nУвеличено здоровье на -', self.magical_power)
        target.set_hp(target.get_hp() + self.magical_power)

    def make_a_move(self, friends, enemies):
        super().make_a_move(friends, enemies)
        for_health = None
        for hero in friends:
            if hero.get_hp() < 100:
                for_health = hero
        if for_health:
            self.give_health(for_health)
        else:
            for_attack = sorted(enemies, key=lambda x: x.get_hp() != 0)
            if not for_attack:
                return
            print(f'{self.name}  атакует {for_attack[0].name} ')
            self.attack(for_attack[0])



    def __str__(self):
        return f'Герой - {self.name}, здоровье - {round(self.get_hp())}'



class Tank(Hero):
    # Танк:
    # Атрибуты:
    # - показатель защиты - изначально равен 1, может увеличиваться и уменьшаться
    # - поднят ли щит - танк может поднимать щит, этот атрибут должен показывать поднят ли щит в данный момент
    # Методы:
    # - атака - атакует, но т.к. доспехи очень тяжелые - наносит половину урона (self.__power)
    # - получение урона - весь входящий урон делится на показатель защиты (damage/self.defense) и только потом отнимается от здоровья
    # - поднять щит - если щит не поднят - поднимает щит. Это увеличивает показатель брони в 2 раза, но уменьшает показатель силы в 2 раза.
    # - опустить щит - если щит поднят - опускает щит. Это уменьшает показатель брони в 2 раза, но увеличивает показатель силы в 2 раза.
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # поднять щит/опустить щит) на выбранную им цель
    def __init__(self, name):
        super().__init__(name)
        self.protection = 1
        self.have_protection = 'off'

    def attack(self, target):
        damage_for_target = self.get_power() / 2
        target.take_damage(damage_for_target)

    def take_damage(self, damage):
        get_damage = damage/self.protection
        self.set_hp(self.get_hp() - get_damage)
        super().take_damage(get_damage)

    def on_protection(self):
        print(f'{self.name} - Поднимаю защиту!!!')
        self.protection = 2
        self.have_protection = 'on'
        self.set_power((self.get_power() / 2))


    def of_protection(self):
        print(f'{self.name} - Опускаю защиту!!!')
        self.protection = 1
        self.have_protection = 'off_protection'
        self.set_power((self.get_power() * 2))

    def make_a_move(self, friends, enemies):
        super().make_a_move(friends, enemies)

        if self.have_protection == 'off_protection' and self.name == friends[0].name or self.get_hp() < 50:
            self.on_protection()

        elif self.have_protection == 'on_protection' and self.name != friends[0].name and self.get_hp() > 50:
            self.of_protection()

        else:
            sort_enemies = sorted(enemies, key=lambda x:  x.get_hp() != 0)
            if not sort_enemies:
                return
            print(len(sort_enemies))
            result_for_attack = sort_enemies[0]
            print('{} атакует {}'.format(self.name, result_for_attack.name))
            self.attack(result_for_attack)

    def __str__(self):
        return f'Герой - {self.name}, здоровье - {round(self.get_hp())}'




class Attacker(Hero):

    # Убийца:
    # Атрибуты:
    # - коэффициент усиления урона (входящего и исходящего)
    # Методы:
    # - атака - наносит урон равный показателю силы (self.__power) умноженному на коэффициент усиления урона (self.power_multiply)
    # после нанесения урона - вызывается метод ослабления power_down.
    # - получение урона - получает урон равный входящему урона умноженному на половину коэффициента усиления урона - damage * (
    # self.power_multiply / 2)
    # - усиление (power_up) - увеличивает коэффициента усиления урона в 2 раза
    # - ослабление (power_down) - уменьшает коэффициента усиления урона в 2 раза
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # усиление, ослабление) на выбранную им цель
    def __init__(self, name):
        super().__init__(name)
        self.power_multiply = 1

    def attack(self, target):
        damage_for_target = (self.get_power() * self.power_multiply)
        target.take_damage(damage_for_target)
        if self.power_multiply > 1:
            self.power_down()

    def power_up(self):
        print(f'{self.name} Накапливаю сила для следующего удара')
        self.power_multiply *= 2


    def power_down(self):
        self.power_multiply = self.power_multiply // 2



    def take_damage(self, damage):
        print(damage, (self.power_multiply / 2))
        get_damage = damage * (self.power_multiply // 2)
        self.set_hp(self.get_hp() - get_damage)
        super().take_damage(get_damage)


    def make_a_move(self, friends, enemies):
        super().make_a_move(friends, enemies)
        sort_enemies = sorted(enemies, key=lambda x: x.get_hp() != 0)
        if not sort_enemies:
            return
        elif self.power_multiply == 1 and self.get_hp() > 50:
            self.power_up()
        else:
            result_for_attack = sort_enemies[0]
            print('{} атакует {}'.format(self.name, result_for_attack.name))
            self.attack(result_for_attack)



    def __str__(self):
        return f'Герой - {self.name}, здоровье - {round(self.get_hp())}'
