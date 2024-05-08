import streamlit as st
from cb_oop import answer_oop
from PIL import Image
st.set_page_config(
    page_title = "Object-Oriented Programming",
    page_icon = "💻",
)
st.title(':rainbow[Object Oriented Programming]')
st.caption("OOPs... How can we save the world with OOP?")

col1, col2, col3 = st.columns(3)

# In Column 1 (Definition)
with col1:
    oop_definitions = st.button("Intro & Definitions")
with col2:
    oop_applications = st.button("Applications of OOP")
with col3:
    oop_diagram = st.button("UML Diagram")

if oop_definitions:
    st.markdown("""
    ## Object-Oriented Programming (OOP)
    Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data and code: data in the form of fields (often known as attributes or properties), and code, in the form of procedures (often known as methods).

    ### Key Concepts of OOP
    OOP revolves around four main concepts which are essential for understanding and applying this paradigm effectively:

    1. **Encapsulation**: This involves bundling the data (attributes) and the methods that operate on the data into a single unit or class. It also involves restricting access to some of the object's components, which is a means of preventing external interference and misuse of the state.

    2. **Abstraction**: This principle involves hiding the complex reality while exposing only the necessary parts. It helps in reducing programming complexity and effort.

    3. **Inheritance**: This is a way to form new classes using classes that have already been defined. It helps in creating a new class from an existing class code.

    4. **Polymorphism**: It allows methods to do different things based on the object it is acting upon. This means that the same function name can be used for different types.

    ### Benefits of OOP
    - **Modularity**: The source code for an object can be written and maintained independently of the source code for other objects.
    - **Reusability**: Objects can be reused in different programs.
    - **Pluggability and Debugging Ease**: If a particular object turns out to be problematic, it can simply be removed from the application and plugged in a different object as a replacement.
    """)
    st.markdown("### Defintions")
    st.markdown("**Class:** **:red[blueprint/template]** for creating objects")
    st.markdown("**Object**: **:red[runtime instantiation]** of a class")
    st.markdown("**Encapsulation**: **Bundling of data and methods within a class entity;** **:red[private data]** are accessible via **:red[public methods]**")
    st.markdown("**Inheritance**: **Ability of a :red[subclass]** to **:red[adopt data and methods]** from a **:red[superclass]**; **:red[subclass can define its own data and method]**")
    st.markdown("**Polymorphism**: Ability to **:red[invoke different methods]** in different classes **:red[using the same name]** at **:red[program runtime]**")

if oop_applications:
    st.markdown("""
    ## OOP Concepts and Examples

    ### Encapsulation
    Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It refers to the bundling of data with the methods that operate on that data. It restricts direct access to some of an object's components, which can prevent the accidental modification of data. An encapsulated object is a sort of black box that can be interacted with only through its exposed interfaces.

    #### Example of Encapsulation
    Below is an example of a class in Python that uses encapsulation.
    """)

    st.code('''
    class Account:
        def __init__(self, owner, balance=0):
            self.owner = owner
            self.__balance = balance  # Private attribute

        def deposit(self, amount):
            if amount > 0:
                self.__balance += amount
                print("Deposit successful.")
            else:
                print("Invalid amount.")

        def withdraw(self, amount):
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal successful.")
            else:
                print("Invalid amount or insufficient funds.")

        def get_balance(self):
            return self.__balance

    # Creating and using an Account object
    acc = Account("John")
    acc.deposit(100)
    print(acc.get_balance())
    acc.withdraw(50)
    print(acc.get_balance())
    ''', language='python')

    st.markdown("""
    ### Inheritance
    Inheritance allows programmers to create a new class from an existing class. The new class inherits the attributes and methods of the existing class. This facilitates code reusability and can lead to an efficient way of handling code.

    #### Example of Inheritance
    Below is an example showing how inheritance can be implemented in Python.
    """)

    st.code('''
    class Vehicle:  # Base class
        def __init__(self, brand, model):
            self.brand = brand
            self.model = model

        def display_info(self):
            return f"{self.brand} {self.model}"

    class Car(Vehicle):  # Derived class
        def __init__(self, brand, model, year):
            super().__init__(brand, model)
            self.year = year

        def display_info(self):
            return f"{self.brand} {self.model} ({self.year})"

    # Using the Car class, which inherits from Vehicle
    my_car = Car("Honda", "Civic", 2020)
    print(my_car.display_info())
    ''', language='python')

    st.markdown("""
    ### Polymorphism
    Polymorphism allows methods to do different things based on the object it is acting upon. This concept lets us define methods in the child class with the same name as defined in their parent class.

    #### Example of Polymorphism
    Here is how polymorphism works, illustrated with Python classes.
    """)

    st.code('''
    class Animal:
        def speak(self):
            raise NotImplementedError("Subclasses must implement abstract method")

    class Dog(Animal):
        def speak(self):
            return "Woof!"

    class Cat(Animal):
        def speak(self):
            return "Meow!"

    def animal_sound(animal):
        print(animal.speak())

    # Polymorphism in action
    my_dog = Dog()
    my_cat = Cat()
    animal_sound(my_dog)
    animal_sound(my_cat)
    ''', language='python')


if oop_diagram:
    st.markdown("""
    ## Understanding Class Diagrams in OOP

    Class diagrams are a type of static structure diagram that describe the structure of a system by showing the system's classes, their attributes, methods, and the relationships among objects. The most basic elements of a class diagram are classes and the relationships that exist among them.

    ### Key Components of Class Diagrams
    - **Class**: Represented by a rectangle divided into three parts: the top part contains the class's name; the middle part contains the class's attributes; the bottom part contains the methods.
    - **Relationships**: Various types of relationships can be depicted, including:
    - **Inheritance (Generalization)**: Illustrated with a hollow arrowhead pointing from the subclass to the superclass.
    - **Association**: A relationship between two classes that indicates instances of one class connect to instances of another.
    - **Aggregation and Composition**: Both are stronger forms of association used to indicate ownership between classes. Composition has a stronger relationship than aggregation.

    ### Example of a Class Diagram
    Let's consider a simple class diagram involving `Vehicle`, `Car`, and `Truck` where `Car` and `Truck` inherit from `Vehicle`.

    #### Diagram Description
    - The `Vehicle` class has attributes like `brand` and `model`.
    - The `Car` class inherits `Vehicle` and adds an attribute `year`.
    - The `Truck` class inherits `Vehicle` and adds an attribute `capacity`.

    You can use tools like Lucidchart, Draw.io, or even simple drawing tools in office software to create class diagrams.

    Below is a textual representation of what a simple class diagram might look like:
    """)

    st.markdown("""
    ```plaintext
            +-------------------+
            |      Vehicle      |
            +-------------------+
            | - brand: string   |
            | - model: string   |
            +-------------------+
            | + display_info()  |
            +--------^----------+
                    | Inheritance
            +--------+----------+
            |                  |
    +--------+-------+  +-------+--------+
    |       Car       |  |      Truck     |
    +-----------------+  +----------------+
    | - year: int     |  | - capacity: int|
    +-----------------+  +----------------+
    | + display_info()|  | + display_info()|
    +-----------------+  +----------------+
    """)

st.divider()

# Initialise a state to keep track of person response"
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

chat_box = st.chat_input("Enter your question")
if chat_box:
    with st.chat_message("user"):
        st.markdown(chat_box)
    st.session_state.messages.append({"role": "user", "content": chat_box})
    response = answer_oop(chat_box)
    with st.chat_message("assistant"):
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
