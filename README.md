This project is my work sample towards the tasks outlined below.  

The project files have been committed to match the file structure of the sample project which is different than what PyCharm loaded on my behalf.  I have adjusted the reference in azure-pipelines.yaml to match my project name and file name but have not tested this as a Linux Python app within an Azure App Service and as such have not confirmed it will work there.  As I do not have access to Bookbyte's Azure, the referenced pipeline isn't available for me to test with, however, the application does run locally in PyCharm.

The following was pulled from the task's source repository which is linked below as the Example Repository.



***Make sure to base your solution off of the sample Selenium script.***
  
***When you submit please ensure that you are using chrome web driver and python3***
  
***Example Repository: https://github.com/bborncamp-bookbyte/qatesting***

Write unit test script in python3 using the Selenium and Chrome WebDriver to do the following:


1. Check that our street address is correct on amazon seller profile - [https://www.amazon.com/sp?seller=A2N51X1QYGFUPK](https://www.amazon.com/sp?seller=A2N51X1QYGFUPK) 

2800 Pringle Rd SE Suite 100


2. Verify our search bar works by searching for 'college' books [https://www.bookbyte.com/advancedsearch.aspx](https://www.bookbyte.com/advancedsearch.aspx)


3. Using the Google Books API Verify "Brian W. Kernighan", and "Dennis M. Ritchie" are the authors of The C Programming Language (Hint: the isbn for this book is 0131103628) 

  [https://developers.google.com/books/docs/v1/using](https://developers.google.com/books/docs/v1/using)


4. Push code to any public git repository.  Enure your script filename is bookbyte_testing.py. 


5. During the interview we will run your solution through this Azure DevOps CI/CD pipeline. 

[https://bookbyte.visualstudio.com/DevOps/_build?definitionId=458&_a=summary](https://bookbyte.visualstudio.com/DevOps/_build?definitionId=458&_a=summary)

***Make sure to base your solution off of the sample Selenium script. When you submit please ensure that you are using chrome web driver and python3)***
