# 0x14. JavaScript - Web scraping
## Details
      By Guillaume, CTO at Holberton School          Weight: 1                Ongoing project - started 02-01-2022, must end by 02-02-2022 (in about 23 hours)          - you're done with 0% of tasks.              Checker will be released at 02-01-2022 12:00 PM              QA review fully automated.      ## Resources
Read or watch :
* [Working with JSON data](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON) 

* [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319) 

* [request module](https://github.com/request/request) 

* [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet) 

## Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/KGl7tkF5ZHilz24aw3uk_g) 
 ,  without the help of Google :
### General
* Why JavaScript programming is amazing
* How to manipulate JSON data
* How to use  ` request `  and fetch API
* How to read and write a file using  ` fs `  module
## Requirements
### General
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files will be interpreted on Ubuntu 14.04 LTS using  ` node `  (version 10.14.x)
* All your files should end with a new line
* The first line of all your files should be exactly  ` #!/usr/bin/node ` 
* A  ` README.md `  file, at the root of the folder of the project, is mandatory
* Your code should be  ` semistandard `  compliant. [Rules of Standard](https://intranet.hbtn.io/rltoken/c82PxNOgt77URzBvKDVcqg) 
 + [semicolons on top](https://intranet.hbtn.io/rltoken/GEBmmrmMUnGd20y4k6_4OA) 
. Also as reference: [AirBnB style](https://intranet.hbtn.io/rltoken/B5xrtt_3vxQFbcCpW5rVsw) 

* All your files must be executable
* The length of your files will be tested using  ` wc ` 
* You are not allowed to use  ` var ` 
## More Info
### Install Node 10
 ` $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
 ` ### Install semi-standard
[Documentation](https://intranet.hbtn.io/rltoken/GEBmmrmMUnGd20y4k6_4OA) 

 ` $ sudo npm install semistandard --global
 ` ### Install request module and use it
[Documentation](https://intranet.hbtn.io/rltoken/9L4UYvlIwDVDoObD7zpJZQ) 

 ` $ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
 ` Notes:  Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).
## Tasks
### 0. Readme
          mandatory         Progress vs Score  Task Body Write a script that reads and prints the content of a file.
* The first argument is the file path
* The content of the file must be read in  ` utf-8 ` 
* If an error occurred during the reading, print the error object
```bash
guillaume@ubuntu:~/0x14$ cat cisfun
C is super fun!
guillaume@ubuntu:~/0x14$ ./0-readme.js cisfun
C is super fun!

guillaume@ubuntu:~/0x14$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
guillaume@ubuntu:~/0x14$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x14-javascript-web_scraping ` 
* File:  ` 0-readme.js ` 
 Self-paced manual review  Panel footer - Controls 
### 1. Write me
          mandatory         Progress vs Score  Task Body Write a script that writes a string to a file.
* The first argument is the file path
* The second argument is the string to write
* The content of the file must be written in  ` utf-8 ` 
* If an error occurred during while writing, print the error object
```bash
guillaume@ubuntu:~/0x14$ ./1-writeme.js my_file.txt "Python is cool"
guillaume@ubuntu:~/0x14$ cat my_file.txt ; echo ""
Python is cool
guillaume@ubuntu:~/0x14$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x14-javascript-web_scraping ` 
* File:  ` 1-writeme.js ` 
 Self-paced manual review  Panel footer - Controls 
### 2. Status code
          mandatory         Progress vs Score  Task Body Write a script that display the status code of a   ` GET `   request.
* The first argument is the URL to request ( ` GET ` )
* The status code must be printed like this:  ` code: <status code> ` 
* You must use the module  ` request ` 
```bash
guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://intranet.hbtn.io/status
code: 200
guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://intranet.hbtn.io/doesnt_exist
code: 404
guillaume@ubuntu:~/0x14$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x14-javascript-web_scraping ` 
* File:  ` 2-statuscode.js ` 
 Self-paced manual review  Panel footer - Controls 
### 3. Star wars movie title
          mandatory         Progress vs Score  Task Body Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
* The first argument is the movie ID
* You must use the [Star wars API](https://intranet.hbtn.io/rltoken/2sAQZ5ZAsYKRYccrnNAK2Q) 
 with the endpoint  ` https://swapi-api.hbtn.io/api/films/:id ` 
* You must use the module  ` request ` 
```bash
guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 1
A New Hope
guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 5
Attack of the Clones
guillaume@ubuntu:~/0x14$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x14-javascript-web_scraping ` 
* File:  ` 3-starwars_title.js ` 
 Self-paced manual review  Panel footer - Controls 
### 4. Star wars Wedge Antilles
          mandatory         Progress vs Score  Task Body Write a script that prints the number of movies where the character “Wedge Antilles” is present.
* The first argument is the API URL of the [Star wars API](https://intranet.hbtn.io/rltoken/2sAQZ5ZAsYKRYccrnNAK2Q) 
:  ` https://swapi-api.hbtn.io/api/films/ ` 
* Wedge Antilles is character ID  ` 18 `  - your script must use this ID for filtering the result of the API
* You must use the module  ` request ` 
```bash
guillaume@ubuntu:~/0x14$ ./4-starwars_count.js https://swapi-api.hbtn.io/api/films
3
guillaume@ubuntu:~/0x14$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x14-javascript-web_scraping ` 
* File:  ` 4-starwars_count.js ` 
 Self-paced manual review  Panel footer - Controls 
### 5. Loripsum
          mandatory         Progress vs Score  Task Body Write a script that gets the contents of a webpage and stores it in a file.
* The first argument is the URL to request
* The second argument the file path to store the body response
* The file must be UTF-8 encoded
* You must use the module  ` request ` 
```bash
guillaume@ubuntu:~/0x14$ ./5-request_store.js http://loripsum.net/api loripsum
guillaume@ubuntu:~/0x14$ cat loripsum
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Haec quo modo conveniant, non sane intellego. Nam memini etiam quae nolo, oblivisci non possum quae volo. Te enim iudicem aequum puto, modo quae dicat ille bene noris. Terram, mihi crede, ea lanx et maria deprimet. Deinde prima illa, quae in congressu solemus: Quid tu, inquit, huc? Hoc etsi multimodis reprehendi potest, tamen accipio, quod dant. </p>

<p>Ad eos igitur converte te, quaeso. Pudebit te, inquam, illius tabulae, quam Cleanthes sane commode verbis depingere solebat. Sic enim censent, oportunitatis esse beate vivere. Quo studio Aristophanem putamus aetatem in litteris duxisse? Aeque enim contingit omnibus fidibus, ut incontentae sint. Ut aliquid scire se gaudeant? Qui enim existimabit posse se miserum esse beatus non erit. Putabam equidem satis, inquit, me dixisse. </p>

<p>Duo Reges: constructio interrete. Quid ei reliquisti, nisi te, quoquo modo loqueretur, intellegere, quid diceret? Quis animo aequo videt eum, quem inpure ac flagitiose putet vivere? Illud non continuo, ut aeque incontentae. Illa videamus, quae a te de amicitia dicta sunt. At ille pellit, qui permulcet sensum voluptate. Tamen aberramus a proposito, et, ne longius, prorsus, inquam, Piso, si ista mala sunt, placet. </p>

<p>Non enim, si omnia non sequebatur, idcirco non erat ortus illinc. Nos cum te, M. Quem si tenueris, non modo meum Ciceronem, sed etiam me ipsum abducas licebit. Apparet statim, quae sint officia, quae actiones. Ergo instituto veterum, quo etiam Stoici utuntur, hinc capiamus exordium. Eadem nunc mea adversum te oratio est. Quid, si etiam iucunda memoria est praeteritorum malorum? Hoc enim constituto in philosophia constituta sunt omnia. </p>

guillaume@ubuntu:~/0x14$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x14-javascript-web_scraping ` 
* File:  ` 5-request_store.js ` 
 Self-paced manual review  Panel footer - Controls 
### 6. How many completed?
          mandatory         Progress vs Score  Task Body Write a script that computes the number of tasks completed by user id.
* The first argument is the API URL:  ` https://jsonplaceholder.typicode.com/todos ` 
* Only print users with completed task
* You must use the module  ` request ` 
```bash
guillaume@ubuntu:~/0x14$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{ '1': 11,
  '2': 8,
  '3': 7,
  '4': 6,
  '5': 12,
  '6': 6,
  '7': 9,
  '8': 11,
  '9': 8,
  '10': 12 }
guillaume@ubuntu:~/0x14$

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x14-javascript-web_scraping ` 
* File:  ` 6-completed_tasks.js ` 
 Self-paced manual review  Panel footer - Controls 
[Done with the mandatory tasks? Unlock 2 advanced tasks now!](https://intranet.hbtn.io/projects/333/unlock_optionals) 

×#### Recommended Sandbox
[Running only]() 
### 1 image(0/5 Sandboxes spawned)
### Ubuntu 14.04 - NodeJS 10
Ubuntu 14.04 with NodeJS 10
[Run]() 
