#A program that will simulate the process of the CPU getting a memory hit or miss from the cache
#And then searching the memory bus and rewriting the cache if needed



class CPU:
    def __init__ (self, name):
        self.name = name
    
    def data_search(self):
        data_to_find = input('What are you looking for? ')
        return data_to_find


class Cache:
    def __init__ (self, storage_size):
        self.storage_size = storage_size
        self.storage = [None for x in range(storage_size)]
        #self.storage_index = 0
        self.storage_history_indices = []
    
    def current_storage(self):
        return self.storage
    
    def available_space(self):
        space = 0
        for item in self.storage:
            if item == None:
                space += 1
        print('There are {0} available spaces left in the cache.'.format(space))
        return space
    
    def find_data(self, memory_bus, data_to_find):
        memory_location = 0
        for item in self.storage:
            if item == data_to_find:
                print('Cache Memory HIT. Found {0} at cache storage index {1}.'.format(data_to_find, memory_location))
                return
            else:
                print('Cache Memory MISS.')
            memory_location += 1
        print()
        print('Searching memory bus.')
        print()
        memory_bus.find_data(data_to_find)
        self.write_data(data_to_find)

    def write_data(self, data_to_write):
        memory_location = 0
        current_space = self.available_space()
        if current_space != 0:
            for item in self.storage:
                if item == None:
                    print('Found empty space at cache storage index {0}. Writing {1}.'.format(memory_location, data_to_write))
                    self.storage[memory_location] = data_to_write
                    self.storage_history_indices.append(memory_location)
                    return
                memory_location += 1
        else:
            print('Now using first in first out replacement policy.')
            self.fifo_replacement_policy(data_to_write)
    
    def write_history_indices(self):
        return self.storage_history_indices

    def fifo_replacement_policy(self, data_to_write):
        storage_history = self.write_history_indices()
        #print(storage_history) #debug line
        self.storage[storage_history[0]] = data_to_write
        self.storage_history_indices = self.storage_history_indices[1:]
        self.storage_history_indices.append(storage_history[0])


class MemoryBus:
    def __init__(self, storage_size):
        self.storage_size = storage_size
        self.storage = [None for x in range(storage_size)]
        #self.storage_index = 0
        self.storage_history_indices = []

    def current_storage(self):
        return self.storage
    
    def available_space(self):
        space = 0
        for item in self.storage:
            if item == None:
                space += 1
        print('There are {0} available spaces left in the memory bus.'.format(space))
        return space
    
    def find_data(self, data_to_find):
        memory_location = 0
        data_hit = False
        for item in self.storage:
            if item == data_to_find:
                print('Memory Bus HIT. Found {0} at memory bus index {1}.'.format(data_to_find, memory_location))
                data_hit = True
                return data_hit
            else:
                print('Memory Bus MISS.')
            memory_location += 1
        print('Data not found in memory bus.')
        self.write_data(data_to_find)


    def write_data(self, data_to_write):
        memory_location = 0
        current_space = self.available_space()
        if current_space != 0:
            for item in self.storage:
                if item == None:
                    print('Found empty space at memory bus index {0}. Writing {1}.'.format(memory_location, data_to_write))
                    self.storage[memory_location] = data_to_write
                    self.storage_history_indices.append(memory_location)
                    return
                memory_location += 1
        else:
            print('Now using first in first out replacement policy.')
            self.fifo_replacement_policy(data_to_write)
    
    def write_history_indices(self):
        return self.storage_history_indices

    def fifo_replacement_policy(self, data_to_write):
        storage_history = self.write_history_indices()
        self.storage[storage_history[0]] = data_to_write
        self.storage_history_indices = self.storage_history_indices[1:]
        self.storage_history_indices.append(storage_history[0])

nvidia = CPU('NVIDIA')
my_cache = Cache(8)
my_memory_bus = MemoryBus(16)
#print(my_cache.current_storage())
#my_cache.available_space()
#my_cache.find_data('Hi')
#my_cache.write_data('Hi')
#my_cache.find_data('Hi')
for x in range(20):
    data = nvidia.data_search()
    my_cache.find_data(my_memory_bus, data)
    print()
    #my_memory_bus.find_data(data)
    #print()
    print(my_cache.current_storage())
    print(my_memory_bus.current_storage())
    print('********************************')

