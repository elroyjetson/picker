# Random Student Name Picker

The school I work at has divided the students into "houses" as a way of fostering mentorship and competition.  We hold contests between the houses occasionally and need to randomly select names of the students that will compete.  The catch is that once a student has competed, they do not get to compete again until all students have had a chance.

Making sure that the students are not in the list to get selected again was becoming tedious so I wrote this to deal with the random selection and remember who had been picked so that they are not selected again.

To reset the list: remove the exclusions.dat file.

To make a selection:

```$python3 picker.py <number of students to pick> <name of house to pick from>```

