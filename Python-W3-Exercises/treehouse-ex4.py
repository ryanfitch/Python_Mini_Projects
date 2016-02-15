# Create a function named most_classes that takes a dictinoary of teachers.  Each key is a teacher's name and their value is a list of classes they've taught.  most-classes should return the teacher with the most classes

dict = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'], 'Kenneth Love': ['Python Basics', 'Python Collections']}

def most_classes(dict):
  teachers_list = {}
  for teacher in dict:
    teachers_list[teacher] = len(dict[teacher])
  busy_teacher = max(teachers_list, key=teachers_list.get)
  return busy_teacher

most_classes(dict)

