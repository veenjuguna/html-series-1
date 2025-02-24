# Define a class named `Person`
class Person
    attr_accessor :name, :age

    # Constructor method to initialize the object
    def initialize(name, age)
        @name = name
        @age = age
    end

    # Method to display person's details
    def display_details
        puts "Name: #{@name}"
        puts "Age: #{@age}"
    end

    # Method to check if the person is an adult
    def adult?
        @age >= 18
    end
end

# Create an array to store person objects
people = []

# Add some person objects to the array
people << Person.new("Alice", 30)
people << Person.new("Bob", 17)
people << Person.new("Charlie", 22)

# Iterate over each person and display their details
people.each do |person|
    person.display_details
    if person.adult?
        puts "#{person.name} is an adult."
    else
        puts "#{person.name} is not an adult."
    end
    puts "-------------------------"
end

# Define a class named `Car`
class Car
    attr_accessor :make, :model, :year

    # Constructor method to initialize the object
    def initialize(make, model, year)
        @make = make
        @model = model
        @year = year
    end

    # Method to display car details
    def display_details
        puts "Make: #{@make}"
        puts "Model: #{@model}"
        puts "Year: #{@year}"
    end

    # Method to check if the car is vintage
    def vintage?
        current_year = Time.now.year
        current_year - @year > 25
    end
end

# Create an array to store car objects
cars = []

# Add some car objects to the array
cars << Car.new("Toyota", "Corolla", 1995)
cars << Car.new("Ford", "Mustang", 2005)
cars << Car.new("Chevrolet", "Impala", 1967)

# Iterate over each car and display their details
cars.each do |car|
    car.display_details
    if car.vintage?
        puts "#{car.make} #{car.model} is a vintage car."
    else
        puts "#{car.make} #{car.model} is not a vintage car."
    end
    puts "-------------------------"
end