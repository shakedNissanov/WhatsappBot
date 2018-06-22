# Whatsapp Bot

A Whatsapp bot package using Selenium in Python. It allows sending and receiving messages from groups and users.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

What things you need to install the software and how to install them

```
The selenium package for python.
```
```
The chrome driver: http://chromedriver.chromium.org/
```

## Examples
How to use the function provided by the package

### Initialize the connection
* Run the _whatsappWebConnection_ as a threaded function
```
>> import seleniumbot
>> seleniumbot.whatsappWebConnection(PathToChromeDriver) 
```
### Send a message
```
>> seleniumbot.sendMessage(targetName, msg)
```
### Read the last message
```
>> seleniumbot.getLastMessage(targetName, textDirection):
```
### Read all available messages
```
>> seleniumbot.readAllMessages(targetName, textDirection)
```

## Built With

* [Selenium](https://www.seleniumhq.org/) - The main packege used

## Authors

* **Shaked Nissanov** 

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
