## [Get this title for $10 on Packt's Spring Sale](https://www.packt.com/B09656?utm_source=github&utm_medium=packt-github-repo&utm_campaign=spring_10_dollar_2022)
-----
For a limited period, all eBooks and Videos are only $10. All the practical content you need \- by developers, for developers

# Jupyter Cookbook
This is the code repository for [Jupyter Cookbook](https://www.packtpub.com/big-data-and-business-intelligence/jupyter-cookbook?utm_source=github&utm_medium=repository&utm_campaign=9781788839440), published by [Packt](https://www.packtpub.com/?utm_source=github). It contains all the supporting project files necessary to work through the book from start to finish.
## About the Book
This book will start with you learning about environment design and preparing containers for your application. You will then start using systemd-nspawn, configure it for private networks, and create your own virtual network with it. Next, you will have a set of powerful recipes to work with LXC such as configuring networks, accessing LXC with programming languages, troubleshooting and installing virtual machines. Moving on, you will work with next most used Linux container which is LXD where you will learn to work with nested containers, Unbuntu cloud images and running docker in LXD. Finally, you learn to use Docker inside an LXC container and also explore the Ansible modules for LXC.


## Instructions and Navigation
All of the code is organized into folders. Each folder starts with a number followed by the application name. For example, Chapter02.



The code will look like the following:
```
import pyspark
if not 'sc' in globals():
sc = pyspark.SparkContext()
lines = sc.textFile("B09656_02 Spark Sample.ipynb")
lineLengths = lines.map(lambda s: len(s))
totalLengths = lineLengths.reduce(lambda a, b: a + b)
print(totalLengths)
```

This cookbook is for data science professionals, developers, technical data analysts, and programmers who want to execute technical coding, visualize output, and do scientific computing with one tool. Prior understanding of data science concepts will be helpful for using this book, but it's not mandatory.

## Related Products
* [Microsoft System Center Data Protection Manager Cookbook](https://www.packtpub.com/virtualization-and-cloud/microsoft-system-center-data-protection-manager-cookbook-0?utm_source=github&utm_medium=repository&utm_campaign=9781787289284)

* [Go Network Programming Cookbook](https://www.packtpub.com/application-development/go-network-programming-cookbook?utm_source=github&utm_medium=repository&utm_campaign=9781788392860)

* [Linux Containers Cookbook ](https://www.packtpub.com/virtualization-and-cloud/linux-containers-cookbook?utm_source=github&utm_medium=repository&utm_campaign=9781785285219)
