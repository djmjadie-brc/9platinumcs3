# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation groups variables and methods to form one object. Using this, we can add properties for different product objects such as product name, price, and quantity/stock, and can even add methods like add_stock(). This helps keep the system organized and makes things easier to fix.

### 2. Abstraction
Abstraction means hiding irrelevant details to simplify the program. An example is when we use the method add_stock() to update the "quantity" property of the product object, We don't have to know how it adds stock, we just have to know what calling the method does. Which simplifies the inventory system more.

### 3. Inheritance
Inheritance allows objects to get properties and methods from an existing parent object. We can use this concept to organize the products by having the same parent object and properties (product name, price, quanttiy) without repeating code and makes the program more efficient to run.

### 4. Polymorphism
Poymorphism makes objects have different forms and behave differently. An example for this is when we use the method add_stock() again, it would behave differently depending on the product object you use it on, such as stocking in bulk or just one. This makes the inventory system more flexible by allowing the same method to have a different effect on certain product objects.

## Reflection
I think in improving the sari-sari store inventory system, the most useful from the four pillars of Object-Oriented Programming would be EncapsulaI tion. This is because it creates an object that has its own properties and variables, which keeps the system organized. Additionally, this is basically the most important part of the inventory system due to the other OOP pillars being dependent on encapsulation as it needs an object with properties and sometimes methods.