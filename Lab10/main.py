from closedunidirectionallinkedlist import ClosedUnidirectionalLinkedList as LinkedList
from device import Device


def main():
    linked_list = LinkedList()
    obj1 = Device("Voltmeter", "Ka-51", 2013, 100)
    obj2 = Device("Voltmeter", "Ka-52", 2015, 150)
    obj3 = Device("Voltmeter", "Ka-15", 2018, 200)
    obj4 = Device("Voltmeter", "Ka-17", 2020, 100)
    obj5 = Device("Voltmeter", "Ka-13", 2019, 200)
    obj6 = Device("Voltmeter", "Ka-33", 2012, 150)
    linked_list.add(obj1)
    linked_list.add(obj2)
    linked_list.add(obj3)
    linked_list.print_list()
    linked_list.output_of_devices_with_the_set_limit(100)
    linked_list.output_of_devices_with_the_set_limit(150)
    linked_list.output_of_devices_with_the_set_limit(200)
    linked_list.output_of_devices_with_the_set_limit(0)
    print(linked_list.get(0), end='')
    print(linked_list.get(1), end='')
    print(linked_list.get(2), end='')
    linked_list.get_information_about_element(0)
    linked_list.get_information_about_element(1)
    linked_list.get_information_about_element(2)
    linked_list.delete_element(2)
    linked_list.print_list()
    linked_list.delete_element(0)
    linked_list.print_list()
    linked_list.insert_by_year(obj5)
    linked_list.insert_by_year(obj4)
    linked_list.insert_by_year(obj6)
    linked_list.print_list()
    linked_list.delete()


if __name__ == '__main__':
    main()
