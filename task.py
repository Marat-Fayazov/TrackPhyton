# TODO Напишите функцию find_common_participants

def find_common_participants(participants1, participants2, separator='|'):
    participants_first_group = participants1.split(separator)
    participants_second_group= participants2.split(separator)

    common_participants = set(participants_first_group) & set(participants_second_group)
    return sorted(list(common_participants))

# TODO Провеьте работу функции с разделителем отличным от запятой

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))