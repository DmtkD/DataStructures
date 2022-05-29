from device import Device


class Node:
    def __init__(self, data: Device = None) -> None:
        self.data: Device = data
        self.next: Node = None


class ClosedUnidirectionalLinkedList:
    def __init__(self) -> None:
        self.head: Node = Node(None)
        self.tail: Node = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    # add -> add some element type Device to list
    def add(self, data: Device) -> None:
        new_node: Node = Node(data)
        if self.head.data is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    # print_list -> print all elements of list
    def print_list(self) -> None:
        current: Node = self.head
        if self.head.data is None:
            print("List is empty!")
        else:
            print("Nodes of the circular linked list: ")
            print(current.data, end=''),
            while current.next != self.head:
                current = current.next
                print(current.data, end='')

    # get -> return some element
    def get(self, index: int) -> Device:
        k: int = 0
        current: Node = self.head
        if self.head.data is None:
            raise IndexError("List index out of range")
        else:
            if k == index:
                return current.data
            else:
                while current.next != self.head:
                    k += 1
                    current = current.next
                    if k == index:
                        return current.data
                    elif k > index:
                        raise IndexError("List index out of range")

    # get_information_about_element -> get information about data from element
    def get_information_about_element(self, index: int) -> None:
        k: int = 0
        current: Node = self.head
        if self.head.data is None:
            raise IndexError("List index out of range")
        else:
            if k == index:
                print(current.data, end='')
                return
            else:
                while current.next != self.head:
                    k += 1
                    current = current.next
                    if k == index:
                        print(current.data, end='')
                        return
                    elif k > index:
                        raise IndexError("List index out of range")

    # output_of_devices_with_the_set_limit -> output information about device, which have same limit of measurement
    def output_of_devices_with_the_set_limit(self, limit_of_measurement: int) -> None:
        current: Node = self.head
        if self.head.data is None:
            raise NotImplemented("List is empty!")
        else:
            k: int = self.__length()
            if current.data.get_limit_of_measurement() == limit_of_measurement:
                print(current.data, end='')
                k -= 1
            while current.next != self.head:
                current = current.next
                if current.data.get_limit_of_measurement() == limit_of_measurement:
                    print(current.data, end='')
                    k -= 1
            if k == self.__length():
                print("There are no device with such a measuring range")

    # delete_element -> delete some element by key (index)
    def delete_element(self, index: int) -> None:
        if self.head.data is None:
            raise IndexError("List index out of range")
        else:
            current: Node = self.head
            length: int = self.__length()
            if index == 0:
                self.head = current.next
                self.tail.next = self.head
            elif index == length - 1:
                n: int = 1
                while n < length - 1:
                    current = current.next
                    n += 1
                current.next = self.head
                self.tail = current
            elif index > length - 1:
                raise IndexError("List index out of range")
            elif index < 0:
                raise IndexError("Я ще не настілький крутий, щоб добавляти від'ємний індекс")
            else:
                n = 1
                while n < index - 1:
                    current = current.next
                    n += 1
                temporary_node: Node = current.next.next
                current.next = temporary_node

    # length -> find a length of list (number of elements)
    def __length(self) -> int:
        if self.head.data is None:
            return 0
        else:
            current: Node = self.head
            length: int = 1
            while current.next:
                if current.next == self.head:
                    break
                current = current.next
                length += 1
            return length

    # add_head -> add head to list
    def __add_head(self, data: Device) -> None:
        new_node: Node = Node(data)
        if self.head.data is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

    # add_tail -> add tail to list
    def __add_tail(self, data: Device):
        new_node: Node = Node(data)
        if self.head.data is None:
            self.__add_head(data)
        else:
            temporary_node: Node = self.head
            n: int = 1
            length: int = self.__length()
            while n < length:
                n += 1
                temporary_node = temporary_node.next
            temporary_node.next = new_node
            new_node.next = self.head
            self.tail = new_node

    def insert_by_year(self, data: Device) -> None:
        current: Node = self.head
        if self.head.data is None:
            self.__add_head(data)
        else:
            if data.get_year_of_manufacture() > current.data.get_year_of_manufacture():
                self.__add_head(data)
                return
            else:
                index: int = 1
                while current.next != self.head:
                    if data.get_year_of_manufacture() > current.data.get_year_of_manufacture():
                        new_node: Node = Node(data)
                        temporary_node: Node = self.head
                        n: int = 1
                        while n < index - 1:
                            temporary_node = temporary_node.next
                            n += 1
                        a: Node = temporary_node.next
                        temporary_node.next = new_node
                        new_node.next = a
                        return
                    elif self.__length() - 1 == index:
                        self.__add_tail(data)
                        return
                    index += 1
                    current = current.next

    # delete -> must delete the list
    def delete(self) -> None:
        print("LinkedList has deleted")
        del self
