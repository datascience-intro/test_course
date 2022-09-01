# Test_course
This is a test course for the [genJSONnotebookGrader](https://github.com/datascience-intro/GenJSONnotebookGrader).

## Prerequisites
One needs to install:-
1. Python (Python3 is recommended.)
2. Docker and Docker Compose

# (1) Master Notebook Preparation

In `test_course` repository, you will find all related files and directories needed for the notebook extraction. If you already have a repository for a course you can copy the contents from ´test_course´ to it.  

### Master Notebook Creation
To create a master notebook, please see examples of master notebooks (stored in `master` directory in `test_course` repository) and read the description in the section below:

- See `Example_databricks_1.dbc` and `Example_databricks_2.dbc` in `master/db` directory for examples of databricks master notebooks
- See `Example_Jupyter_1.ipynb` and `Example_Jupyter_2.ipynb` in `master/jp` directory for examples of Jupyter master notebooks

> **NOTE !**
> The construction of a master notebook for both databricks and Jupyter is the same. The difference is just the file format.

> For databricks notebooks, one may use magic line (`%python` or `%scala`) as desired to switch between languages in a single notebook. **However, for Jupyter notebook, do not put `%python` in any cells of Jupyter notebook; otherwise, the master notebook cannot be extracted.**

As seen in the examples of the master notebooks, there are different cell types with different cell tags one needs to strictly specify:

1. **Lecture Part**
This part includes lecture notes, pictures, VDO, websites, etc. in markdown cells. It can also include code cells for students to play along with the lecture. Hence, there can be more than one lecture cell and they can be put in any place in the notebook. These lecture cells do not need any tags, and cab be extracted into a lecture notebook.

2. **Assignment Part**
The assignment part is where an instructor creates problems for students as homework. One assignment can include several problems and for each problem there are four cell types:

	- **Problem Cell**
		A problem can consist of several PROBLEM cells. For example, one can specify a problem statement in a markdown cell and follow it with a cell where students fill in code to answer the problem. These cells must be tagged with the following comment in the first line: 

		For scala,

		// ASSIGNMENT 1, PROBLEM 1, Points 3

		val x = 0 // REPLACE '0' WITH THE RIGHT VALUE
		val y = 0 // REPLACE '0' WITH THE RIGHT VALUE
		val z = 0 // REPLACE '0' WITH THE RIGHT VALUE

		sc.parallelize(Seq.range(x, y)).takeOrdered(z)(Ordering[Int].reverse)`

		For Python,

	    # ASSIGNMENT 1, PROBLEM 1, Points 2
		
	> For more elaborate examples of PROBLEM cell see the example master notebooks

	- **Test Cell**
    Test cells represents local tests that the student run to make sure that their answers are in a correct format. Each problem must have one, and only one, Test cell. These cells must be tagged with the following comment in the first line:

		For scala,

	    // ASSIGNMENT 1, Test 1, Points 3
		// This is a local Test cell. Students must run Test cell to check if their answers are in a correct format or not.

		// Here we can tell student to not change anything in local Test cells

		val regex = "\\d+" //Match digit, no decimal allowed (must have at least one digit)

		try {
		assert((x.toString).matches(regex))
		print("Your answer x is in a valid format. Hopefully, it is correct.\n")
		} catch {
		case _: Throwable => print("Try again for x! Please make sure you input a valid format.\n")
		}

	> For more elaborate examples of Test cell see the example master notebooks

	- **TEST Cell**
		The (capital) TEST cells are used by the autograder to compare the students answer with the correct solution. Each problem must have one, and only one, TEST cell. These cells must be tagged with the following comment in the first line:

		For scala,

		// ASSIGNMENT 1, TEST 1, POINTS 3
		// This is a TEST cell which the autograder uses to check whether student answers or codes are correct or not, and adjust points accordingly.

		var local_points = 0

		try {
		assert(x == 669966)
		local_points = local_points + 1
		
		print("x is correct.\n")
		} catch {
		case _: Throwable => print("x is incorrect.\n")
		}




    > **NOTE !**
    In every TEST cell, it is necessary to initialize a `local_points` variable to 0. For each correct answer increase this variable with the corresponding points for getting that answer right. 
	
    > For more elaborate examples of TEST cell see the example master notebooks


	- **SOLUTION Cell**
		The SOLUTION cells are used to store references to correct answers or code snippets. Each problem must have one, and only one, SOLUTION cell. These cells must be tagged with the following comment in the first line:

		For scala,

	    // ASSIGNMENT 1, SOLUTION 1, Points 3
		// This is a Test cell to keep the solution for a reference.

		val x = 669966
		val y = 969697
		val z = 20
    > For more elaborate examples of SOLUTION cell see the example master notebooks

For python, just replace *//* with *#*


### Directories for Storing Master Notebooks
Export databricks master notebooks as *.dbc* and jupyter as *.ipynb* and store them in `master/db` and `master/jp` respectively.  

# (2) Notebook Extraction


### Pre-configured file
For the extraction of lecture and assignment notebooks out of a master notebook, one has to pre-configure `configNotebooks.json` stored inside the top directory of the GenJSONnotebookGrader. 

Note the symbolic link inside `GenerateMaterial` called `NotebookGrader` which is linked to the NotebookGrader directory inside the GenJSONnotebookGrader repository. See an example of the configuration file below.

For Jupyter notebooks,

    {
	    "master_notebooks":["Example_Jupyter_1", "Example_Jupyter_2"],
	    "notebook_file_extension":"jp",
	    "notebook_folder":"master/jp",
	    "target_notebook_folder":"lectures",
	    "target_notebook_book_folder":"Notebooks",
	    "assignments":[1,2],
	    "CourseID":"54514",
	    "CourseName":"Scalable Data Science and Distributed Machine Learning",
	    "CourseInstance":"2022"
    }

For databricks notebooks,

    {
	    "master_notebooks":["Example_databricks_1", "Example_databricks_2"],
	    "notebook_file_extension":"db",
	    "notebook_folder":"master/db",
	    "target_notebook_folder":"lectures",
	    "target_notebook_book_folder":"Notebooks",
	    "assignments":[1,2],
	    "CourseID":"54514",
	    "CourseName":"Scalable Data Science and Distributed Machine Learning",
	    "CourseInstance":"2022"
    }


> One must make sure all directories specified in `configNotebook.json` exist !

The description of each key in `configNotebook.json` is in the table below:-

| Key | Description |
|--|--|
| master_notebooks | A list of names of master notebooks **WITHOUT** any file extension|
| notebook_file_extension | A file extension of master notebooks. This key accepts only two values, namely `db` for databricks notebooks, and `jp` for Jupyter notebooks. |
| notebook_folder | A path to a directory that stores master notebooks. For databricks notebooks, they are stored in `master/db`, and for Jupyter notebooks, they are stored in `master/jp`. Different directory names or paths are also possible, if necessary. |
| target_notebook_folder | A directory where extracted notebooks (both lecture and assignment notebooks) are stored |
| target_notebook_book_folder | A directory where extracted notebooks in a form of e-book are stored (Support only Jupyter notebook)|
| assignments | A list of assignment numbers, which will be extracted into assignment notebooks from the master notebooks |
| CourseID | A course ID on Studium |
| CourseName | A course name on Studium |
| CourseInstance | This is usually a year in which the course is conducted.  |

### Make Lecture Notebook
Go into your course directory, and then into `GenerateMaterial` directory, and run the following command:-

    python3 generate.py

The extracted lecture notebooks are stored in `lectures` directory as specified in `configNotebook.json`.

### Make Assignment Notebook

Go into the course directory, and then into `GenerateMaterial` directory. One needs to open and edit  `generate_assignment.py` and specify in the function `makeAssignmentNotebook` what assignment number and cell types one needs the system to extract from master notebooks.
For Databricks, instantiate a `DBCourse` for Databricks and `IDSCourse`for Jupyter. See an example below:

    course = IDSCourse()

    course.makeAssignmentNotebook(assignment_number = 1,notebook_type='problem')
    course.makeAssignmentNotebook(assignment_number = 1,notebook_type='problem_TEST')

	#For more specific types of notebooks you can generate the following. These are not necessary for the purpose of providing assignments and autograding them.
    course.makeAssignmentNotebook(assignment_number = 1,notebook_type='problem_solution')
    course.makeAssignmentNotebook(assignment_number = 1,notebook_type='problem_solution_TEST')
    course.makeAssignmentNotebook(assignment_number = 1,notebook_type='solution')
    course.makeAssignmentNotebook(assignment_number = 1,notebook_type='solution_TEST')
    course.makeAssignmentNotebook(assignment_number = 1,notebook_type='TEST')

In the example above, it creates an object of `IDSCourse()` and calls `makeAssignmentNotebook()` function from the object. It call this function 7 times to generate 7 separate notebooks. For example, the first one generates a notebook with only problem cells (along with their corresponding Test cells). The second one generates a notebook with problem cells (along with their corresponding Test cells) and TEST cells. The third one generates a notebook with problem cells (along with their corresponding Test cells) and solution cells.  

> **Note !**
> Problem cells are always extracted together with their corresponding Test cells.
> This means the first line where 'problem' is specified shall generate a notebook with both problem and Test cells.

> For the argument `notebook_type`, if more than one cell types are needed to be extracted into another notebook, use `underscore` (`_`) to concatenate cell types.

Then, run the following command:-

    python3 generate_assignment.py

The extracted notebooks are stored in `lectures` directory as specified in `configNotebooks.json`. Change the config files and symbolic links for if you need a more specific setup.
